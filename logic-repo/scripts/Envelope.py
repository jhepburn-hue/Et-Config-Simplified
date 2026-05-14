#!/usr/bin/python3

import sys

ARG_HELP: str = "--help"

ARG_CYCONF: int = 1
ARG_BIN: int = 2
ARG_OUT: int = 3
CONFIG_OVERHEAD: int = 4
CRC_TLV_LEN: int = 4

ENVELOPE_HEADER: bytearray = bytearray([0x0E, 0x82])
CRC_HEADER: bytearray = bytearray([0xEF, 0x02])

HELP: str = """

| --------------------- CYCONFIG --------------------------|
|                                                          |
| USAGE: ./confmerge [.cyconfig file] [.bin reader config] |
|                                                          |
| ---------------------------------------------------------|

"""


def big_endian16(num: int) -> list:
    return [(num & 0xFF00) >> 8, num & 0xFF]


def crc16(data: bytes) -> list:
    crc = 0x6363

    for byte in data:
        b = byte ^ (crc & 0xFF)
        b ^= (b << 4) & 0xFF

        c1 = (b << 8) & 0xFFFF
        c2 = (crc >> 8) & 0xFF
        c3 = (b >> 4) & 0xFF
        c4 = (b << 3) & 0xFFFF
        c12 = (c1 | c2) & 0xFFFF
        c34 = (c3 ^ c4) & 0xFFFF
        crc = (c12 ^ c34) & 0xFFFF

    return big_endian16(crc)


def read_config(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()


def validate_config(config: bytes) -> bool:
    return (config[0] == 0x0E) and (config[-4] == 0xEF) and (config[-3] == 0x02)


def strip_config(config: bytes) -> bytes:
    len_bytes: int = config[1] & 0x7F
    return config[(len_bytes + 2) : -4]


if __name__ == "__main__":
    if ARG_HELP in sys.argv:
        print(HELP)
        exit(0)

    if len(sys.argv) < 4:
        print("Too few arguments...")
        exit(1)

    cyconf: bytes = read_config(sys.argv[ARG_CYCONF])
    rdrconf: bytes = read_config(sys.argv[ARG_BIN])

    if not validate_config(cyconf):
        print("cyconf invalid...")
        exit(1)

    if not validate_config(rdrconf):
        print("rdrconf invalid...")
        exit(1)

    cyconf = strip_config(cyconf)
    rdrconf = strip_config(rdrconf)

    outconf = cyconf + rdrconf

    print(f"merging {len(outconf)} bytes of config...")

    # envelope header
    output = bytearray()
    output += ENVELOPE_HEADER
    env_len = len(outconf) + CRC_TLV_LEN
    output += bytearray(big_endian16(env_len))

    # merged config data
    output += outconf

    # crc
    crc = crc16(output[4:])
    output += CRC_HEADER
    output += bytearray(crc)

    with open(sys.argv[ARG_OUT], "wb") as f:
        f.write(output)

    print(f"merged config file written to {sys.argv[ARG_OUT]}")
