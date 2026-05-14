"""
This module is a special fork of the script to create the unified config files
targeted at creating Brivo specific versions for their use.

This allows Brivo to independently distribute wallet configurations to their
customers without involving Wavelynx at each stage.

The purpose of this file is to perform a single shot "batch" creation of files
for all assigned Brivo TCI values.

Below is an example Brivo Wallet config that this file needs to setup:

################################################################################
# HF Settings
################################################################################

# 13.56 MHz High Frequency RF Front End
OPT_AUG,OPERATION_INDEX , ENABLE_HF_RF

#  Add all RF protocols

RF,0 , CP_ISO_14443A
# RF,1, CP_ISO_15693
# RF,2 , CP_PICO_15693

#
#  Smart card application support
#

APP,CT_MF_DESFIRE_EV1_2,0, CA_LEAF_IP
APP,CT_MF_DESFIRE_EV1_2,1,CA_NEXPACS
APP,CT_MF_DESFIRE_EV1_2,2, CA_FEATURES_KEYS

# enable apple wallet
APP,CT_ECP_NFC,0,CA_MERIDIAN_NFC

# uncomment these lines for MF2GO support
APP,CT_MF_DESFIRE_EV1_2,3,CA_M2GO_GENERIC_ACD
APP,CT_ISO_14443A_4,0,CA_M2GO_GENERIC_ACD
APP,CT_GENERIC_CL2,0,CA_M2GO_GENERIC_ACD

# comment this line for MF2GO support, EVX CSNs need to be disabled
# APP,CT_MF_DESFIRE_EV1_2,3, CA_CSN

USER_APP_OCPSK_KEYSET,Lk50010:OCPSK
USER_APP_READ_KEYSET,Lk50010:APPVK
USER_APP_CARD_MASTER_KEYSET , Lk50010:APPVK
USER_APP_CARD_WRITE_KEYSET , BRIVO:USER_APP_CARD_WRITE

MFC_KEYSET , BRIVO:MFC

USER_APP2_K1_KEYSET , ETHOS:USER_APP2_K1
USER_APP2_K2_KEYSET , ETHOS:USER_APP2_K2

OPT_AUG, NEXPACS_OPTIONS_INDEX, SKIP_SIGNATURE_CHECK
OPT_AUG,NEXPACS_OPTIONS_INDEX, SKIP_CIO

#
# LEAF settings
#

OPT,LEAF_IP_DEF_INDEX , 40
OPT,LEAF_IP_KS1_INDEX , 1
OPT,LEAF_IP_KS2_INDEX , LEAF_IP_IGNORE_KEYSET_MASK
OPT,LEAF_IP_KS3_INDEX , LEAF_IP_IGNORE_KEYSET_MASK

# leaf cc read key
LEAF_IP_OCPSK_KEYSET , Lk50010:Kc1
LEAF_IP_READ_KEYSET ,  Lk50010:Kc1

# leaf si read key
LEAF_IP_KS1_OCPSK_KEYSET, Lk00001:Ksi
LEAF_IP_KS1_READ_KEYSET, Lk00001:Kv1

# apple meridian keys
NFC_MP0_KEYS,Lk50010:Kr0
NFC_MC0_KEYS,Lk50010:Kr1

# apple ecp settings
MOBILE,ecpFormat,ECP_FORMAT_2
MOBILE,ecpTerminalInfoMode,ECP_WL_TERMINAL_INFO
MOBILE,ecpTerminalType,ECP_TERMINAL_TYPE
MOBILE,ecpTerminalSubType,ECP_TERMINAL_SUBTYPE_CORPORATE
MOBILE,ecpTCI_1,ECP_TCI_1
MOBILE,ecpTCI_2,0x30
MOBILE,ecpTCI_3,0x00

# meridian credential application num bits
MOBILE,ecpBitCount,128

# Config card keys
FEATURE_MANAGEMENT_READ_KEYSET, ETHOS:FEATURE_READ
FEATURE_MANAGEMENT_WRITE_KEYSET, ETHOS:FEATURE_WRITE

################################################################################
# CapTouch Settings
################################################################################

# uncomment to enable captouch
# captouch is disabled by default for wallet configss
# OPT,CAPTOUCH_FEATURES_INDEX , 0x5400
# OPT_AUG,CAPTOUCH_FEATURES_INDEX, CAPTOUCH_ENABLED_MASK
# OPT,CAPTOUCH_EVENT_TRIGGER_LEVEL,30
"""
import base64
import json
import sys
from typing import Tuple

import requests

import features as wl
import standardTypes


SEQUOIA_IP: str = "10.1.10.14"
SEQUOIA_PORT: int = 443
BASE_URL: str = "https://" + SEQUOIA_IP + ":" + str(SEQUOIA_PORT) + "/"
ENCODE_KEY: str = "ETHOS:EXT_MEM"


def _verify_success(rsp: requests.Response) -> bool:
    """
    Checks a sequoia response json body for success code and status.

    Params:
        rsp: Response object returned from requests lib.

    Returns:
        T/F rsp was success.
    """
    content = rsp.json()
    return (rsp.status_code == 200) and ("status" in content) and (content["status"] == "ok")


def load_blob(
    blob_id: str,
    name: str,
    desc: str,
    data: bytes,
    signing: str,
    signingkey: str,
    operations: list,
    keyset: list,
) -> Tuple[bool, bytes]:
    """
    Load a blob into sequoia to allow for an operation to be performed on it.

    Params:
        id: Unique id for blob. (Uses the filepath)
        name: Extended name of blob. (Uses the filepath)
        desc: Extended description of blob. (Uses the filepath)
        signing: Type of signing to be performed on blob.
        operations: Operation to be performed on blob.
        keyset: Key ids to be used in blob.

    Returns:
        (T/F success, returned blob with op performed)
        If success is False, None is returned for the blob.
    """
    body = {
        "id": blob_id,
        "name": name,
        "description": desc,
        "data": base64.b64encode(data).decode("utf-8"),
        "signing": signing,
        "signingkey": signingkey,
        "operations": operations,
        "keyset": keyset,
    }
    print("attempting to connect to sequoia")
    rsp = requests.post(BASE_URL + "load_blob", json=body, verify=False)
    print("finished connection attempt")
    if _verify_success(rsp):
        return True, base64.b64decode(rsp.json()["result"].encode("utf-8"))
    else:
        return False, bytes([])


def load_input_file(filepath: str) -> dict:
    """
    Read in an input json file for processing.

    Params:
        - filepath: path to json file.

    Returns:
        - dict containing deserialized json contents.
    """
    data: dict = {}
    with open(filepath) as f:
        data = json.load(f)

    return data


def make_keyset_list(lk_number: str) -> list:
    """
    Creates the specific keyset list based on the provided Lk number. This is
    used by the Sequoia "load blob" endpoint to populate the config.

    Params:
        - lk_number: Lk number string for keyset.

    Returns:
        Formatted list for Sequoia keyset field.
    """
    Lk_Kr0 = lk_number + ":Kr0"
    Lk_Kr1 = lk_number + ":Kr1"
    Lk_Kr4 = lk_number + ":Kr4"
    Lk_Kr5 = lk_number + ":Kr5"

    return [
        (wl.NFC_MP0_MC0_KEYS, Lk_Kr0, Lk_Kr1),
        (wl.M2G_ACD_LEAF_GENERIC_KEYS, Lk_Kr4, Lk_Kr5),
    ]


def make_unified_blob(entry: dict, tra_enabled: bool) -> bytes:
    """
    creates the config file/card blob for a Brivo unified config.

    Params:
        entry: dict containing specific values to populate config with.
        tra_enabled: T/F whether to enable Apple dual auth.

    Returns:
        config file/card payload blob.
    """

    # Set ISO14443A as the only supported HF protocol
    rf_protocol_config = standardTypes.RfProtocolsConfig()
    rf_protocol_config.append_protocol(wl.CP_ISO_14443A)

    # Enable Apple ECP Meridian
    card_apps_ecp = standardTypes.CardAppsConfig()
    card_apps_ecp.set_card_type(wl.CT_ECP_NFC)
    # card_apps_ecp.append_card_app(wl.CA_MERIDIAN_NFC)

    # Add mf2go for EV2/3
    # Note this must be added in addition to LEAF, NEXPACS, and config cards
    card_apps_ev1_ev2 = standardTypes.CardAppsConfig()
    card_apps_ev1_ev2.set_card_type(wl.CT_MF_DESFIRE_EV1_2)
    card_apps_ev1_ev2.append_card_app(wl.CA_LEAF_IP)
    card_apps_ev1_ev2.append_card_app(wl.CA_NEXPACS)
    card_apps_ev1_ev2.append_card_app(wl.CA_FEATURES_KEYS)
    card_apps_ev1_ev2.append_card_app(wl.CA_M2GO_GENERIC_ACD)

    # Add mf2go for base iso14443A-4
    card_apps_iso14443a_4 = standardTypes.CardAppsConfig()
    card_apps_iso14443a_4.set_card_type(wl.CT_ISO_14443A_4)
    card_apps_iso14443a_4.append_card_app(wl.CA_M2GO_GENERIC_ACD)

    # Add mf2go for generic class 2
    card_apps_generic_Cl2 = standardTypes.CardAppsConfig()
    card_apps_generic_Cl2.set_card_type(wl.CT_GENERIC_CL2)
    card_apps_generic_Cl2.append_card_app(wl.CA_M2GO_GENERIC_ACD)

    # turn off captouch
    captouch_options = standardTypes.TAG_OPTION()
    captouch_options.set(wl.BIT_OP_CLEAR, wl.CAPTOUCH_FEATURES_INDEX, wl.CAPTOUCH_ENABLED_MASK)

    # turning on iso wrapping
    iso_options = standardTypes.TAG_OPTION()
    iso_options.set(wl.BIT_OP_SET, wl.NEXPACS_OPTIONS_INDEX, wl.USE_ISO7816_WRAPPER)

    # setting up ecp frame + dfname
    nfc_config = standardTypes.NFC_CONFIG()
    nfc_config.set("ecpTCI_1", int(entry["tci"][0:2], base=16))
    nfc_config.set("ecpTCI_2", int(entry["tci"][2:4], base=16))
    nfc_config.set("ecpTCI_3", int(entry["tci"][4:6], base=16))
    nfc_config.set("features", wl.NFC_LEGACY_CREDENTIALS)
    nfc_config.set("activeKeysets", wl.MOBILE_ACTIVE_KEYSET_SLOT1)
    nfc_config.set("ecpFormat", 0x02)

    if tra_enabled:
        nfc_config.set("ecpTerminalInfoMode", wl.ECP_WL_TERMINAL_INFO_USER_AUTH)
    else:
        nfc_config.set("ecpTerminalInfoMode", wl.ECP_WL_TERMINAL_INFO)

    nfc_config.set("ecpTerminalType", 0x2)
    nfc_config.set("ecpTerminalSubType", 0x02)
    nfc_config.set("ecpBitCount", 40)
    nfc_config.set("ecpAppOptions", wl.DIVERSIFY_MC0_MASK)

    return (
        nfc_config.dumpTlv()
        + iso_options.dumpTlv()
        + captouch_options.dumpTlv()
        + rf_protocol_config.dump_tlv()
        + card_apps_ecp.dump_tlv()
        + card_apps_ev1_ev2.dump_tlv()
        + card_apps_generic_Cl2.dump_tlv()
        + card_apps_iso14443a_4.dump_tlv()
    )


def create_unified_config_bin(filepath: str, entry: dict, tra_enabled: bool) -> bool:
    """
    Creates a Brivo unified .bin config file using Sequoia's "load_blob" endpoint.
    If the call is successful, the file is written to memory.

    Params:
        - filepath: File name/path to write to.
        - entry: dict entry used to construct file.
        - tra_enabled: Bool indicating if TRA is enabled on the reader config.

    Returns:
        T/F whether file was written.
    """
    success: bool
    config: bytes

    success, config = load_blob(
        blob_id=filepath,
        name=filepath,
        desc=filepath,
        signing="config",
        operations=["config"],
        keyset=make_keyset_list(entry["keyset"]),
        signingkey=ENCODE_KEY,
        data=make_unified_blob(entry, tra_enabled),
    )

    if success:
        with open(filepath, mode="w+b") as f:
            f.write(config)

    else:
        print(
            "no Data returned from SEQUOIA check that it is reachable and unlocked and that the file is correct",
        )
    return success


def create_unified_config(config_id: str, entry: dict) -> bool:
    """
    Make both TRA and Express mode unified config bin files for a given entry.

    Param:
        - entry: dict containging file details to load into config. The Lk id and tci fields
                 are used in this case.

    Returns:
        - T/F whether both tra and express mode files were created.
    """
    print("LK ", entry["id"], "tci is ", entry["tci"])

    # tra_file: str = f"{config_id}-{entry['id']}-{entry['tci']}-TRA.bin"
    # res: bool = create_unified_config_bin(tra_file, entry, tra_enabled=True)

    # if not res:
    #     # print(f"failed to create: {tra_file}")
    #     return False

    std_file: str = f"{config_id}-{entry['id']}-{entry['tci']}.bin"
    res = create_unified_config_bin(std_file, entry, tra_enabled=False)

    if not res:
        print(f"failed to create: {std_file}")
        return False

    return True


if __name__ == "__main__":
    #
    # Script entry point
    #
    # 1. Load the input config JSON file from the first argument.
    # 2. Prompt user for Config ID.
    # 3. Iterate through entries in input file and create TRA/Express mode config files for
    #    each entry.
    #
    if ("--help" in sys.argv) or ("help" in sys.argv) or ("-h" in sys.argv):
        print(
            """


-------- Brivo Unified Config Builder -------

Build a batch of Brivo Unified wallet config files based on the given input json file.

Usage: python3 scripts/build_brivo_card.py [PATH TO INPUT JSON FILE]

The input json file should have the following minimum format to be valid for this script. Note
there may be additional utilities used by other scripts present in the json objects, but this
script requires the high level structure be an array containing objects with "id" and "tci" keys.

[
    {
        "id": "Lk60069",
        "tci": "020934"
        "keyset_id": "Lk50010"
    },

    ...
]


              """
        )

        sys.exit(0)

    if len(sys.argv) != 2:
        print("Usage: python3 scripts/build_brivo_card.py [PATH TO INPUT JSON FILE]")
        sys.exit(1)

    input_data: list[dict] = load_input_file(sys.argv[1])
    print("Input file loaded.")

    # Prompt user for Config ID
    config_id: str = input("Config ID (EX: CBVR6): ").strip()

    for item in input_data:
        if not create_unified_config(config_id, item):
            sys.exit(1)

    print("All config files created successfully.")