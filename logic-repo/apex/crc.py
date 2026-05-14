# Copyright (c) 2025 WaveLynx Technologies LLC

"""
Reader CRC calculations
"""


def crc_ccitt(data: bytes, iv: int = 0xFFFF) -> int:
    """CRC-CCITT (or ISO/IEC 13239) calculation.
    Polynomial: x^16 + x^12 + x^5 + 1 (0x8408)

    :param data: Data bytes to calculate CRC from
    :param iv: Initial value
    :return: Calculated CRC-16
    """
    crc = iv
    for b in data:
        b ^= crc & 0xFF
        b ^= (b << 4) & 0xFF
        s1 = (b << 8) & 0xFFFF
        s2 = (crc >> 8) & 0xFF
        s3 = (b >> 4) & 0xFF
        s4 = (b << 3) & 0xFFFF
        crc = (s1 | s2) ^ (s3 ^ s4)
    return crc
