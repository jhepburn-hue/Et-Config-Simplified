# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import binascii
from enum import IntEnum, unique
import binascii
import etconfig as etconfig
import encoding as encoding
import base64

PROD_TEST_CUST_KEY = bytes.fromhex("00000000000000000000000000000000")
KEY1 = "db020101010101010101010101010101"  #kc2 from LK_TEST

KEY_ID = "PROD_TEST_CUST_KEY"


@unique
class ledColorCode(IntEnum):
    Off = 0x00  # Off
    Red = 0x01  # Red
    Green = 0x02  # Green
    Amber = 0x03  # Amber
    Blue = 0x04  # Blue
    Magenta = 0x05  # Magenta
    Cyan = 0x06  # Cyan
    White = 0x07  # White
    NoOp = 0x80  # NoOp


def buildMfgPrefix():
    OSDP_MFG = 0x80
    VENDOR_1 = 0x5C
    VENDOR_2 = 0x26
    VENDOR_3 = 0x23
    WL_DATA_PREFIX = 0x57
    WL_MFG_PREFIX = b'\x80\x5C\x26\x23\x57'
    # return binascii.hexlify(b'\x80\x5C\x26\x23\x57')
    # the following is for coldFusion only
    return binascii.hexlify(b'\x5C\x26\x23\x57')


def buildRtfd():
    return b'\x48\x00'


def __mkU8bytes(value):
    return value.to_bytes(1, byteorder="little", signed=False)


def printOSDP(id, cmd):
    osdp = buildMfgPrefix() + binascii.hexlify(cmd)
    print(id, osdp)


def buildLed(idle, read, intensity):
    cmd = bytearray()
    cmd += b'\x41\x04'
    cmd += __mkU8bytes(idle.value)
    cmd += __mkU8bytes(read.value)
    cmd += binascii.unhexlify(hex(intensity)[2:].zfill(4))
    # print("LEDCMD", cmd.hex(), binascii.hexlify(cmd).hex())
    return cmd


def getLed():
    return b'\x41\x00'


def buildBuzzer(gBeep, rbeep):
    cmd = bytearray()
    cmd += b'\x42\x01'
    cmd += __mkU8bytes(((gBeep & 0x01) << 1) | (rbeep & 0x01))
    return cmd


def getBuzzer():
    cmd = b'\x42\x00'
    return cmd


TECH_LOW_FREQUENCY = 0x01
TECH_HIGH_FREQUENCY = 0x02
TECH_BLE = 0x04


def buildTech(techVal):
    cmd = bytearray()
    cmd += b'\x43\x01'
    cmd += __mkU8bytes(techVal)
    return cmd


def getTech():
    return b'\x43\x00'


CUSTOMER_CREDENTIALS_EV1_EV2_CSN_ENABLE = 0x01
CUSTOMER_CREDENTIALS_MFC_CSN_ENABLE = 0x02
CUSTOMER_CREDENTIALS_ICLASS_CSN_ENABLE = 0x04
CUSTOMER_CREDENTIALS_SMARTMAX_ENABLE = 0x08
CUSTOMER_CREDENTIALS_BLE_ENABLE = 0x10
CUSTOMER_CREDENTIALS_NFC_ENABLE = 0x20
CUSTOMER_CREDENTIALS_LEAF_ENABLE = 0x40
CUSTOMER_CREDENTIALS_ECP_ENABLE = 0x80

CSN_AS_IS = 0x00
CSN_4001 = 0x01
CSN_4002 = 0x02
CSN_5002 = 0x03
CSN_6400 = 0x04
CSN_26_BIT = 0x05
CSN_32_BIT_LSB_XOR = 0x06
CSN_32_BIT_MSB_XOR = 0x07
CSN_40_BIT_MSB_LRC = 0x08
CSN_34_BIT_MSB_PARITY = 0x09
CSN_32_BIT_LSB = 0x0A
CSN_32_BIT_MSB = 0x0B
CSN_32_BIT_PLUS = 0x0C
CSN_56_BIT = 0x0D
CSN_40_BIT_PCSC = 0x0E
CSN_75_BIT_PCSC = 0x0F
CSN_5002_CL2 = 0x10
TLV_TAG_CUST_CONFIG = 0x0B


def buildCred(credVal, iso1443, pico):
    cmd = bytearray()
    cmd += b'\x44\x04'
    cmd += credVal.to_bytes(2, byteorder="little", signed=False)
    cmd += __mkU8bytes(iso1443 & 0xFF)
    cmd += __mkU8bytes(pico & 0x0FF)

    return cmd


def getCred():
    return b'\x44\x00'


NFC_FEA_TRANSPORT = 0x01  # disable key rolling after ~1 minute
NFC_FEA_MFG = 0x02  # allow wl specific credentials
NFC_LEGACY_CREDENTIALS = 0x04

MOBILE_ACTIVE_KEYSET_SLOT1 = 0x01  # use the key in mobile slot 1
MOBILE_ACTIVE_KEYSET_SLOT2 = 0x02  # use the key in mobile slot2


def buildMobile(features, keySlot, metaData):
    cmd = bytearray()
    cmd += b'\x45\x06'
    cmd += __mkU8bytes(features)
    cmd += __mkU8bytes(keySlot)

    cmd += bytes(4)
    if len(cmd) != 8:
        raise RuntimeError("invalid message length")

    return cmd


def getMobile():
    return b'\x45\x00'


CUST_KEY_LEAF_IP_OCPSK_KEYSET = 6
CUST_KEY_LEAF_IP_READ_KEYSET = 7
CUST_KEY_MASTER = 24
CUST_KEY_NFC_KM1_KEYS = 26
CUST_KEY_NFC_KC1_KEYS = 27
CUST_KEY_NFC_KM2_KC2_KEYS = 28
CUST_KEY_NFC_KC2_KEYS = 29


def buildKeys(slot, key):
    cmd = bytearray()
    cmd += b'\x47\x11'
    cmd += __mkU8bytes(slot)
    cmd += bytes.fromhex(key)
    # print("key", bytes.fromhex(key).hex())
    # print("KEYLEN ", len(bytes.fromhex(key)))
    # print("cmdlen ", len(cmd))

    if len(cmd) != 19:
        raise RuntimeError("invalid key length of ", len(cmd))
    return cmd


def writeBinFile(id, tlv):
    # print("-------------------->writeBinFile :: id : ", id, " <--------------------------")
    # print("writeBinFile :: tlv : ", binascii.hexlify(tlv))
    commandConfig = etconfig.sign_factory_config(tlv, PROD_TEST_CUST_KEY)
    # print("writeBinFile ::  (after 'sign_factory_config') commandConfig : ", binascii.hexlify(commandConfig))
    commandConfig = bytes(etconfig.wrap_config(commandConfig))
    # print("writeBinFile :: (after 'wrap_config') commandConfig : ", binascii.hexlify(commandConfig))
    printOSDP(id, tlv)
    f = open("Gen-PT/"+id + "_" + KEY_ID + ".bin", "wb")
    f.write(commandConfig)
    f.close()
    # print("")


# Address must be between 0x00 and 0x7E
# baud rates are:
def baudRateToStr(x):
    return {
        0: "9600_DEFAULT",
        1: "19200",
        2: "38400",
        3: "57600",
        4: "115200",
        5: "230400",
        6: "460800",
    }[x]


def buildOsdp(address, baud):
    cmd = bytearray()
    cmd += b'\x49\x02'
    cmd += __mkU8bytes(address)
    cmd += __mkU8bytes(baud)

    return cmd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # list(ledColorCode)
    writeBinFile("rtfd", buildRtfd())
    writeBinFile("get_led", getLed())
    writeBinFile("setLed_white_blue_defaultPwm", buildLed(ledColorCode.White, ledColorCode.Blue, 0xFFFF))
    writeBinFile("setLed_off_blue_defaultPwm", buildLed(ledColorCode.Off, ledColorCode.Blue, 0xFFFF))
    writeBinFile("setLed_RED_BLUE_defaultPwm", buildLed(ledColorCode.Red, ledColorCode.Green, 0xFFFF))
    writeBinFile("setLed_GREEN_RED_defaultPwm", buildLed(ledColorCode.Green, ledColorCode.Red, 0xFFFF))
    writeBinFile("setLed_blue_amber_defaultPwm", buildLed(ledColorCode.Blue, ledColorCode.Amber, 0xFFFF))
    writeBinFile("setLed_white_blue_maxPwm_invalid", buildLed(ledColorCode.White, ledColorCode.Blue, 0x0AAA))
    writeBinFile("setLed_white_blue_maxPwm", buildLed(ledColorCode.White, ledColorCode.Blue, 0x0556))
    writeBinFile("setLed_white_blue_minPwm", buildLed(ledColorCode.White, ledColorCode.Blue, 0x0111))

    # buzzer
    writeBinFile("setBuzz_gON_cardON", buildBuzzer(1, 1))
    writeBinFile("setBuzz_gOFF_cardON", buildBuzzer(0, 1))
    writeBinFile("setBuzz_gON_cardOFF", buildBuzzer(1, 0))
    writeBinFile("setBuzz_gOFF_cardOFF", buildBuzzer(0, 0))
    writeBinFile("get_buzzer", getBuzzer())

    # tech
    writeBinFile("get_tech", getTech())
    writeBinFile("setTech-0", buildTech(0))
    writeBinFile("setTech-1", buildTech(TECH_LOW_FREQUENCY))
    writeBinFile("setTech-2", buildTech(TECH_HIGH_FREQUENCY))
    writeBinFile("setTech-3", buildTech(TECH_HIGH_FREQUENCY | TECH_LOW_FREQUENCY))
    writeBinFile("setTech-4", buildTech(TECH_BLE))
    writeBinFile("setTech-5", buildTech(TECH_BLE | TECH_LOW_FREQUENCY))
    writeBinFile("setTech-6", buildTech(TECH_BLE | TECH_HIGH_FREQUENCY))
    writeBinFile("setTech-7", buildTech(TECH_BLE | TECH_HIGH_FREQUENCY | TECH_LOW_FREQUENCY))
    writeBinFile("setTech-15", buildTech(0xF))

    # Credentials
    writeBinFile("get_credentials", getCred())
    writeBinFile("setCred_EV1_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_EV1_EV2_CSN_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_MFC_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_MFC_CSN_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_ICLASS_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_ICLASS_CSN_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_SMARTMAX_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_SMARTMAX_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_BLE_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_BLE_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_NFC_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_NFC_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_LEAF_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_LEAF_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_ECP_1443CSN_AS_IS_15693CSN_AS_IS  ",
                 buildCred(CUSTOMER_CREDENTIALS_ECP_ENABLE, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_NONE_1443CSN_AS_IS_15693CSN_AS_IS  ", buildCred(0, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_ALL-Current_1443CSN_AS_IS_15693CSN_AS_IS  ", buildCred(0x00FF, CSN_AS_IS, CSN_AS_IS))
    writeBinFile("setCred_ALL-FUTURE_1443CSN_56_BIT_15693CSN_56_BIT  ",
                 buildCred(0xFFFF, CSN_56_BIT, CSN_56_BIT))
    writeBinFile("setCred_ALL-Current_1443CSN_5002_15693CSN_5002  ", buildCred(0x00FF, CSN_5002, CSN_5002))
    writeBinFile("setCred_ALL-Current_1443CSN_40_BIT_MSB_LRC_15693CSN_40_BIT_PCSC  ",
                 buildCred(0x00FF, CSN_40_BIT_MSB_LRC, CSN_40_BIT_PCSC))
    writeBinFile("setCred_ALL-Current_1443CSN_26_BIT_15693CSN_26_BIT  ",
                 buildCred(0x00FF, CSN_26_BIT, CSN_26_BIT))
    writeBinFile("setCred_ALL-Current_1443CSN_5002_CL2_15693CSN_5002_CL2   ",
                 buildCred(0x00FF, CSN_5002_CL2, CSN_5002_CL2))
    writeBinFile("setCred_ALL-Current_1443CSN_5002_CL2_15693CSN_AS_IS  ",
                 buildCred(0x00FF, CSN_5002_CL2, CSN_AS_IS))
    writeBinFile("setCred_ALL-Current_1443CSN_AS_IS_15693CSN_5002_CL2   ",
                 buildCred(0x00FF, CSN_AS_IS, CSN_5002_CL2))

    # Mobile
    writeBinFile("getMobile", getMobile())
    writeBinFile("setMobile_NONE_KEYSALL_FF",
                 buildMobile(0, MOBILE_ACTIVE_KEYSET_SLOT1 | MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))
    writeBinFile("setMobile_NONE_KEYSALL_00",
                 buildMobile(0, MOBILE_ACTIVE_KEYSET_SLOT1 | MOBILE_ACTIVE_KEYSET_SLOT2, 0x00))
    writeBinFile("setMobile_FEA_TRANSPORT_KEYSALL_FF",
                 buildMobile(NFC_FEA_TRANSPORT, MOBILE_ACTIVE_KEYSET_SLOT1 | MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))
    writeBinFile("setMobile_FEA_MFG_KEYSALL_FF",
                 buildMobile(NFC_FEA_MFG, MOBILE_ACTIVE_KEYSET_SLOT1 | MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))
    writeBinFile("setMobile_LEGACY_CRED_KEYSALL_FF",
                 buildMobile(NFC_LEGACY_CREDENTIALS, MOBILE_ACTIVE_KEYSET_SLOT1 | MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))
    writeBinFile("setMobile_ALL_KEYSSLOT1_FF",
                 buildMobile(NFC_LEGACY_CREDENTIALS | NFC_FEA_TRANSPORT | NFC_FEA_MFG, MOBILE_ACTIVE_KEYSET_SLOT1, 0xFF))
    writeBinFile("setMobile_LEGACY_CREDENTIALS_KEYSSLOT1_FF",
                 buildMobile(NFC_LEGACY_CREDENTIALS, MOBILE_ACTIVE_KEYSET_SLOT1 | MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))
    writeBinFile("setMobile_LEGACY_CREDENTIALS_KEYSSLOT2_FF",
                 buildMobile(NFC_LEGACY_CREDENTIALS, MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))
    writeBinFile("setMobile_LEGACY_CREDENTIALS_KEYSSLOT2_FF",
                 buildMobile(NFC_LEGACY_CREDENTIALS, MOBILE_ACTIVE_KEYSET_SLOT2, 0xFF))

    writeBinFile("setKey_LEAF-OCPSK_KEY1",buildKeys(CUST_KEY_LEAF_IP_OCPSK_KEYSET,KEY1))
    writeBinFile("setKey_LEAF-READ_KEY1",buildKeys(CUST_KEY_LEAF_IP_READ_KEYSET,KEY1))

    writeBinFile("setKey_CUST_KEY1",buildKeys(CUST_KEY_LEAF_IP_OCPSK_KEYSET,KEY1))

    writeBinFile("setKey_CUST_KEY1",buildKeys(CUST_KEY_MASTER,KEY1))
    writeBinFile("setKey_NFC-KM1_KEY1",buildKeys(CUST_KEY_NFC_KM1_KEYS,KEY1))
    writeBinFile("setKey_NFC-KC1_KEY1",buildKeys(CUST_KEY_NFC_KC1_KEYS,KEY1))
    writeBinFile("setKey_NFC-KM2_KEY1",buildKeys(CUST_KEY_NFC_KM2_KC2_KEYS,KEY1))
    writeBinFile("setKey_NRC-KC2_KEY1",buildKeys(CUST_KEY_NFC_KC2_KEYS,KEY1))

    for address in range(9):
        for baud in range(7):
            writeBinFile("setOsdp_"+str(address)+"_baudId_"+baudRateToStr(baud),buildOsdp(address,baud))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
