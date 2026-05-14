#!/usr/bin/python3
"""
etconfig.py
Author: Taylor Schmidt, WaveLynx Technologies

Operations for manipulating and signing configurations for the ethos reader main
mcu.
"""

import secrets
import binascii
from aes import AES
import byteutils as byteutils


NULL_IV: bytes = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

# TLV constants
ENVELOPE_HEADER: bytes = bytes([0x0E, 0x82])
CRC_HEADER: bytes = bytes([0xEF, 0x02])
CONFIG_HEADER: bytes = bytes([0x0B, 0x82])
FACTORY_RESET_HEADER: bytes = bytes([0xF1, 0x82])

CRC_TLV_LEN: int = 4

def sign_factory_config(config: bytes, key: bytes) -> bytes:
    """
    Encrypts an ethos config. Ethos configs are encrypted using AES128-CBC
    with a null (all 0s) starting IV. The configuration block and keys are
    wrapped in a full factory config tlv before encryption.

    Params:
      - config: plaintext config bytes
      - key: signing AES128 key

    Returns:
      - (config: bytes) encrypted config
    """
    outconf: bytes = config

    # wrap the block in a TLV
    outconf: bytes = CONFIG_HEADER + byteutils.big_endian16(len(outconf)) + outconf
    # print("final block w hdr len :", hex(len(outconf)), outconf)
    # encrypt with null iv
    return AES(key).encrypt_cbc(outconf, NULL_IV)


def wrap_config(config: bytes) -> bytes:
    """
    Wrap the configuration in the correct TLV structure.


    [ENVELOPE HEADER][CONFIG HEADER][ENCRYPTED CONFIG][ENVELOPE CRC]

    Params:
      - config: encrypted configuration block

    Returns:
      - (wrapped config: bytes) fully wrapped config with correct TLV structure.
    """
    outconf: bytes = config
    # print("len inner", hex(len(outconf)), outconf.hex() )
    # wrap in various header TLVs

    outconf = CONFIG_HEADER + byteutils.big_endian16(len(outconf)) + outconf
    outconf = ENVELOPE_HEADER + byteutils.big_endian16(len(outconf) + CRC_TLV_LEN) + outconf

    # append CRC TLV
    crc = byteutils.crc16(outconf[4:])
    outconf = outconf + CRC_HEADER + crc

    return outconf
