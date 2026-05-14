#!/usr/bin/python3
"""
byteutils.py
Author: Taylor Schmidt, WaveLynx Technologies

Utility functions for common byte operations
"""


def big_endian16(num: int) -> bytes:
    """
    Convert a integer into a big endian 16 bytes object
    """
    return bytes([(num & 0xFF00) >> 8, num & 0xFF])


def crc16(data: bytes) -> bytes:
    """
    Calculate a CCITT CRC over a bytes object.

    WL common start value is 0x6363.
    """
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
