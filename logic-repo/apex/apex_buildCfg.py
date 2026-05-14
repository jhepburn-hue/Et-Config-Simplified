"""
Script to generate apex configs from a .ini file containing all settings that will be changed from their default value for a custom config

.env file should contain:
    SEQUOIA_IP=[IP address for Sequoia]
    SEQUOIA_PORT=[port for Sequoia]
    BASE_URL=https://${SEQUOIA_IP}:${SEQUOIA_PORT}/
    TOKEN=[token for Sequoia usage]
    ENCRYPT_KEYSET=[name of the keyset in Sequoia that contains the key that will encrypt the config]
    ENCRYPT_KEY=[name of the key in Sequoia that will encrypt the config]
"""

import os
import sys
from dotenv import load_dotenv, find_dotenv
import configparser
import requests
import argparse
import shutil
import tlv
import crc

from colorama import Fore, Style

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from pathlib import Path

FT_TAG_ENVELOPE             = 0x0E
FT_TAG_FIRMWARE             = 0x0F
FT_TAG_ENVELOPE_CRC         = 0xEF
FT_TAG_CONFIG               = 0x0C
FT_TAG_KEYSET               = 0x0D
FT_TAG_LFS_FILE             = 0x20
LFS_FILE_TAG_NAME           = 0x01
LFS_FILE_TAG_DATA           = 0x02
LFS_FILE_TAG_CRC            = 0x03
FT_TAG_FIRMWARE_APP_CORE    = 0x23
FT_TAG_FIRMWARE_NET_CORE    = 0x24
FT_TAG_FIRMWARE_BOOTLOADER  = 0x22
FT_TAG_FIRMWARE_PERSONALITY = 0x21

def _print_colored(color, *args):
    print(color + ' '.join(map(str, args)) + Style.RESET_ALL)

def PRINT_INFO(*args):
    print(' '.join(map(str, args)))

def PRINT_WARN(*args):
    _print_colored(Fore.YELLOW, *args)

def PRINT_ERROR(*args):
    _print_colored(Fore.RED, *args)

def parse_ini(filename: Path) -> configparser.ConfigParser:
    """
    Parse INI file to object
    :param filename: Path to INI file to parse
    :return: INI object
    """
    config = configparser.ConfigParser(inline_comment_prefixes=';')
    config.read(filename)
    return config

def populate_keysets(keyset_ini: configparser.ConfigParser):
    """
    Send request to Sequoia to retrive keys listed in the INI
    :param keyset_ini: Parsed INI configuration containing only the "key" section
    :return: Parsed INI configuration where the values are replaced with the Sequoia keys
    """
    if "keys" not in keyset_ini:
        PRINT_ERROR("keys section is missing")
        return
    
    for key, value in keyset_ini['keys'].items():
        if ":" not in value:
            PRINT_ERROR("Format of keys incorrect. Expected Keyset_Name:Key_Name")
            return
        
        keyset_id = value.split(":")

        body = {
            "token": os.getenv("TOKEN"),
            "keyset_id": keyset_id[0],
            "key_id": keyset_id[1]
        }

        rsp = requests.post(os.getenv("BASE_URL") + "read_key", json=body, verify=False)
        key_json = rsp.json()
        if (key_json['status'] == "ok" and 'key' in key_json):
            key_raw = key_json['key']['key_data']

            keyset_ini['keys'][key] = key_raw
        else:
            PRINT_ERROR("Some or all keys are not in Sequoia. Please check key and keyset names are correct in your .ini file.")
            sys.exit(1)
  
    return keyset_ini

def populate_custom_with_defaults(custom_ini: configparser.ConfigParser, default_ini: configparser.ConfigParser):
    """
    Populate any settings that are not set by the custom config with the default value
    :param custom_ini: Parsed custom INI configuration
    :param default_ini: Parsed default INI configuration
    :return: Merged version of the custom and default INIs where the custom INIs overwrite any of the existing default configurations
    """
    for section in default_ini.sections():
        if not custom_ini.has_section(section):
            custom_ini.add_section(section)
        for name in default_ini[section]:
            if name not in custom_ini[section]:
                custom_ini[section][name] = default_ini[section][name]
            elif custom_ini[section][name] != default_ini[section][name]:
                PRINT_INFO('Value for ' + Fore.GREEN + f'[{section}][{name}]' + Style.RESET_ALL + ' updated from ' + 
                      Fore.GREEN + default_ini[section][name] + Style.RESET_ALL + 
                      " to " + Fore.GREEN + custom_ini[section][name] + Style.RESET_ALL)

    return custom_ini

def validate_custom_against_defaults(custom_ini: configparser.ConfigParser, default_ini: configparser.ConfigParser):
    """
    Compare the dictionary containing custom settings with the default. 
    :param custom_dict: dictionary containing settings specific to a customer config
    :param default_dict: dictionary containing all settings with the default values
    """
    for section in custom_ini.sections():
        if not default_ini.has_section(section):
            PRINT_ERROR(f'"{section}" is not an allowed section')
            sys.exit(1)
        for name in custom_ini[section]:
            if name not in default_ini[section]:
                PRINT_ERROR(f'"{name}" is an invalid configuration within the "{section}" section')
                sys.exit(1)


def encrypt_cbc(plaintext: bytes):
    """
    Encrypt plaintext bytes via Cipher Block Chaining with the key defined in .env
    :param plaintext: unencrypted data containing all settings for a customer config
    :return: encrypted data containing all settings for a customer config
    """
    body = {
        "token": os.getenv("TOKEN"),
        "keyset_id": os.getenv("ENCRYPT_KEYSET"),
        "key_id": os.getenv("ENCRYPT_KEY")
    }
    rsp = requests.post(os.getenv("BASE_URL") + "read_key", json=body, verify=False)
    key_json = rsp.json()
    key_raw = bytes.fromhex(key_json['key']['key_data'])

    plaintext = pad(plaintext)

    iv = bytes(16)

    cipher = Cipher(algorithms.AES(key_raw), modes.CBC(iv), backend=default_backend)
    encryptor = cipher.encryptor()
    if plaintext is not None:
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return ciphertext
    else:
        PRINT_ERROR("plaintext is None")
        return None

def pad(plaintext: bytes):
    """
    Pad plaintext with zeros so that it is a multiple of 16, thus suitable for Cipher Block Chaining
    :param plaintext: plaintext data to add padding to
    :return: plaintext + padding
    """
    padding_len = 16 - (len(plaintext) % 16)
    padding = bytes(padding_len)
    if padding_len != 16:
        return plaintext + padding
    else:
        return plaintext

def full_envelope_wrap(config_ini_path: Path, keyset_ini_path: Path, appcore_image_path: Path, netcore_image_path: Path,  mcuboot_image_path: Path) -> bytes:
    """
    Wrap data in an Envelope TLV for a full configuration
    :param config_ini_path: Path to the config INI
    :param keyset_ini_path: Path to the keysets INI
    :param appcore_image_path: Path to the APP image
    :param netcore_image_path: Path to the NET image
    :param mcuboot_image_path: Path to the MCUBoot image
    :return: Wrapped Envelope data bytes
    """
    # Config LFS File TLV
    lfs_filename = 'config.ini'.encode('utf-8')
    config_tlv = tlv.tlv_encode(LFS_FILE_TAG_NAME, len(lfs_filename), lfs_filename)
    with open(config_ini_path, 'rb') as f:
        config_bytes = f.read()
    config_tlv += tlv.tlv_encode(LFS_FILE_TAG_DATA, len(config_bytes), config_bytes)
    config_tlv += tlv.tlv_encode(LFS_FILE_TAG_CRC, 2, crc.crc_ccitt(config_tlv, iv=0x6363).to_bytes(2, byteorder='big'))
    config_tlv = tlv.tlv_encode(FT_TAG_LFS_FILE, len(config_tlv), config_tlv)

    # Keyset LFS File TLV
    lfs_filename = 'keysets.ini'.encode('utf-8')
    keyset_tlv = tlv.tlv_encode(LFS_FILE_TAG_NAME, len(lfs_filename), lfs_filename)
    with open(keyset_ini_path, 'rb') as f:
        keyset_bytes = f.read()
    keyset_tlv += tlv.tlv_encode(LFS_FILE_TAG_DATA, len(keyset_bytes), keyset_bytes)
    keyset_tlv += tlv.tlv_encode(LFS_FILE_TAG_CRC, 2, crc.crc_ccitt(keyset_tlv, iv=0x6363).to_bytes(2, byteorder='big'))
    keyset_tlv = tlv.tlv_encode(FT_TAG_LFS_FILE, len(keyset_tlv), keyset_tlv)

    # APP core TLV
    with open(appcore_image_path, 'rb') as f:
        appcore_bytes = f.read()
    appcore_tlv = tlv.tlv_encode(FT_TAG_FIRMWARE_APP_CORE, len(appcore_bytes), appcore_bytes)

    # NET core TLV
    with open(netcore_image_path, 'rb') as f:
        netcore_bytes = f.read()
    netcore_tlv = tlv.tlv_encode(FT_TAG_FIRMWARE_NET_CORE, len(netcore_bytes), netcore_bytes)

    # MCUBoot TLV
    with open(mcuboot_image_path, 'rb') as f:
        mcuboot_bytes = f.read()
    mcuboot_tlv = tlv.tlv_encode(FT_TAG_FIRMWARE_BOOTLOADER, len(mcuboot_bytes), mcuboot_bytes)

    # Concatenate and generate Envelope
    envelope_data = config_tlv + keyset_tlv + appcore_tlv + netcore_tlv + mcuboot_tlv
    envelope_data += tlv.tlv_encode(FT_TAG_ENVELOPE_CRC, 2, crc.crc_ccitt(envelope_data, iv=0x6363).to_bytes(2, byteorder='big'))
    return tlv.tlv_encode(FT_TAG_ENVELOPE, len(envelope_data), envelope_data)


def partial_envelope_wrap(config_ini_path: bytes = None, keyset_ini_path: bytes = None) -> bytes:
    """
    Wrap data in an Envelope TLV for a partial configuration
    :param config_ini_path: Path to the config INI
    :param keyset_ini_path: Path to the keysets INI
    :return: Wrapped Envelope data bytes
    """   
    full_tlv = bytearray()

    if config_ini_path:
        with open(config_ini_path, 'rb') as f:
            config_ini = f.read()
        full_tlv.extend(tlv.tlv_encode(FT_TAG_CONFIG, len(config_ini), config_ini))

    if keyset_ini_path:
        with open(keyset_ini_path, 'rb') as f:
            keyset_ini = f.read()
        full_tlv.extend(tlv.tlv_encode(FT_TAG_KEYSET, len(keyset_ini), keyset_ini))

    full_tlv += tlv.tlv_encode(FT_TAG_ENVELOPE_CRC, 2, crc.crc_ccitt(full_tlv, iv=0x6363).to_bytes(2, byteorder='big'))
    return tlv.tlv_encode(FT_TAG_ENVELOPE, len(full_tlv), full_tlv)

def main(args: argparse.Namespace):
    """
    Application entrypoint
    """
    if not os.path.exists("./apex/tmp"):
        os.mkdir("./apex/tmp")

    # Check arguments
    if args.random_byte_images:
        PRINT_INFO("Populating random bytes for images")
        images = []
        if not args.appcore:
            PRINT_INFO("Populating APP image with random bytes")
            args.appcore = Path("./apex/tmp/appcore.bin")
            images.append(args.appcore)
        if not args.netcore:
            PRINT_INFO("Populating NET image with random bytes")
            args.netcore = Path("./apex/tmp/netcore.bin")
            images.append(args.netcore)
        if not args.mcuboot:
            PRINT_INFO("Populating MCUBoot image with random bytes")
            args.mcuboot = Path("./apex/tmp/mcuboot.bin")
            images.append(args.mcuboot)
        for image in images:
            with open(image, 'wb') as f:
                for _ in range(256):
                    f.write(bytes.fromhex("DEADBEEF"))

    if args.type == "full":
        for name, arg in [("APP", args.appcore), ("NET", args.netcore), ("MCUBoot", args.mcuboot)]:
            if arg is None:
                raise argparse.ArgumentError(arg, f"Must provide image path for {name} image")
            elif not arg.exists():
                PRINT_ERROR(name + " image path does not exist!")
                exit(1)
            else:
                PRINT_INFO(f"{name} image path: {arg.absolute()}")
    else:
        if args.appcore:
            PRINT_WARN("WARNING: APP image provided, but unused due to --type partial")
        if args.netcore:
            PRINT_WARN("WARNING: NET image provided, but unused due to --type partial")
        if args.mcuboot:
            PRINT_WARN("WARNING: MCUBoot image provided, but unused due to --type partial")

    # Check environment variables
    if not args.no_sequoia or not args.no_encrypt:
        if not load_dotenv(find_dotenv()):
            PRINT_ERROR("Failed to find .env file")
            sys.exit(1)
    
        for env_name in ["TOKEN", "BASE_URL", "ENCRYPT_KEYSET", "ENCRYPT_KEY"]:
            if os.getenv(env_name) is None:
                PRINT_ERROR(f"{env_name} not found in environment variables")
                sys.exit(1)
    else:
        PRINT_WARN("WARNING: Sequoia not in use due to --no-sequoia and --no-encrypt")

    # Parse INI files
    PRINT_INFO(f"Config INI path: {args.ini.absolute()}")
    default_ini = parse_ini("./apex/settings_default.ini")
    custom_ini = parse_ini(args.ini)
    validate_custom_against_defaults(custom_ini, default_ini)

    # Combine default + custom INIs to single dictionary
    if args.type == "full":
        custom_ini = populate_custom_with_defaults(custom_ini, default_ini)

    if custom_ini.has_section("keys"):
        keyset_ini = configparser.ConfigParser()
        keyset_ini.add_section('keys')
        if 'keys' in custom_ini.sections():
            keyset_ini['keys'].update(custom_ini['keys'])
            custom_ini.remove_section('keys')
        
        # Populate keys from Sequoia
        if not args.no_sequoia:
            keyset_ini = populate_keysets(keyset_ini)
        else:
            for name in keyset_ini['keys']:
                keyset_ini['keys'][name] = '"' + ('00' * 16) + '"'    
        
        # Check if any other sections provided in the custom_ini (were only keys provided?)
        if len(custom_ini.sections()) == 0:
            custom_ini = None
            PRINT_WARN("WARNING: only keys provide")
    else:
        PRINT_WARN("WARNING: no keys found in config file")
        keyset_ini = None

    # Write temporary ini files
    if custom_ini:
        with open('./apex/tmp/config.ini', 'w') as f:
            custom_ini.write(f)
    if keyset_ini:
        with open('./apex/tmp/keyset.ini', 'w') as f:
            keyset_ini.write(f)

    if args.type == "full":
        final_file_data = full_envelope_wrap(
            config_ini_path='./apex/tmp/config.ini', 
            keyset_ini_path='./apex/tmp/keyset.ini', 
            appcore_image_path=args.appcore, 
            netcore_image_path=args.netcore, 
            mcuboot_image_path=args.mcuboot,
        )
    elif args.type == "partial":
        final_file_data = partial_envelope_wrap(
            config_ini_path='./apex/tmp/config.ini' if custom_ini else None,
            keyset_ini_path='./apex/tmp/keyset.ini' if keyset_ini else None
        )

    if not args.no_encrypt:
        final_file_data = encrypt_cbc(final_file_data)
    
    with open("config.bin", 'wb') as file:
        file.write(final_file_data)

    # Cleanup
    if not args.no_cleanup:
        shutil.rmtree('./apex/tmp')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--ini", type=Path, required=True, help="Apex INI configuration path")
    parser.add_argument("-a", "--appcore", type=Path, help="Apex APP core image path")
    parser.add_argument("-n", "--netcore", type=Path, help="Apex NET core image path")
    parser.add_argument("-m", "--mcuboot", type=Path, help="Apex MCUBoot image path")
    parser.add_argument("-t", "--type", type=str, required=True, choices=['full','partial'], help="full or partial")
    parser.add_argument("--no-encrypt", action="store_true", help="Don't encrypt the final binary")
    parser.add_argument("--no-sequoia", action="store_true", help="Don't retrieve keys from Sequoia, populates with random bytes")
    parser.add_argument("--random-byte-images", action="store_true", help="Use random bytes for images (1024 bytes each) not provided")
    parser.add_argument("--no-cleanup", action="store_true", help="Retain temporary files upon completion")
    
    main(parser.parse_args())
