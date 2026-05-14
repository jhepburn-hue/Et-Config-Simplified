# Copyright (c) 2025 WaveLynx Technologies LLC

"""
TLV/STLV encoding/decoding operations
"""

import logging
import math

from crc import crc_ccitt


logger = logging.getLogger(__name__)


def _encode_length(buff: bytearray, length: int) -> bytearray:
    if length < 0x80:
        buff.append(length)
    else:
        cnt = math.ceil(length.bit_length() / 8)
        buff.append(0x80 | cnt)
        buff.extend(length.to_bytes(cnt, "big"))
    return buff


def _decode_length(buff: bytes, len_idx: int) -> tuple[int, int]:
    length = buff[len_idx]
    if length & 0x80:
        cnt = length & 0x7F
        length = int.from_bytes(buff[len_idx + 1 : len_idx + cnt + 1], "big")
        len_idx += cnt
    return length, len_idx + 1


def tlv_encode(tag: int, length: int, value: bytes) -> bytes:
    """Encode a TLV into bytes.

    :param tag: Tag to encode.
    :param length: Length of value to encode.
    :param value: Value bytes to encode.
    :return: Encoded TLV bytes.
    """
    assert 0 <= tag <= 0xFF, "Tag out of range"
    assert 0 <= length <= 0xFFFFFFFF, "Length out of range"

    logger.info("TLV data to encode:")
    logger.info("+- tag........0x{:02X}".format(tag))
    logger.info("+- length.....{}".format(length))
    logger.info("+- value......{}".format(value.hex() if len(value) else "None"))

    buff = bytearray([tag])
    buff = _encode_length(buff, length)
    buff.extend(value)

    logger.info(f"Encoded buffer: {buff.hex()}")

    return buff


def tlv_decode(buff: bytes) -> tuple[int, int, bytes, bytes]:
    """Decode buffer into a TLV buffer

    :param buff: Byte array to decode
    :return: (tag, length, value, leftover_bytes)
    """
    logger.info(f"Decoding buffer: {buff.hex()}")

    tag = buff[0]
    length, val_idx = _decode_length(buff, 1)
    value = buff[val_idx : val_idx + length]
    leftover_bytes = buff[val_idx + length + 1 :]

    logger.info("Decoded TLV data:")
    logger.info("+- tag................0x{:02X}".format(tag))
    logger.info("+- length.............{}".format(length))
    logger.info("+- value..............{}".format(value.hex() if len(value) else "None"))
    logger.info("+- leftover_bytes.....{}".format(leftover_bytes.hex() if len(leftover_bytes) else "None"))

    return tag, length, value, leftover_bytes


def stlv_encode(status: int, tag: int, length: int, value: bytes) -> bytes:
    """Encode an STLV into bytes.

    :param status: Status to encode.
    :param tag: Tag to encode.
    :param length: Length of value to encode.
    :param value: Value bytes to encode.
    :return: Encoded TLV bytes.
    """
    assert 0 <= status <= 0xFF, "Status out of range"
    assert 0 <= tag <= 0xFF, "Tag out of range"
    assert 0 <= length <= 0xFFFFFFFF, "Length out of range"

    logger.info("STLV data to encode:")
    logger.info("+- status.....0x{:02X}".format(status))
    logger.info("+- tag........0x{:02X}".format(tag))
    logger.info("+- length.....{}".format(length))
    logger.info("+- value......{}".format(value.hex() if len(value) else "None"))

    buff = bytearray([status, tag])
    buff = _encode_length(buff, length)
    buff.extend(value)
    crc = crc_ccitt(buff, iv=0x6363)
    logger.info("+- CRC........0x{:04X}".format(crc))
    buff.extend(crc.to_bytes(2, "little"))

    logger.info(f"Encoded buffer: {buff.hex()}")

    return buff


def stlv_decode(buff: bytes) -> tuple[int, int, int, bytes, bytes]:
    """Decode buffer into an STLV buffer

    :param buff: Byte array to decode
    :return: (status, tag, length, value, leftover_bytes)
    """
    logger.info(f"Decoding buffer: {buff.hex()}")

    status = buff[0]
    tag = buff[1]
    length, val_idx = _decode_length(buff, 2)
    value = buff[val_idx : val_idx + length]
    crc = int.from_bytes(buff[val_idx + length : val_idx + length + 2], "little")
    calc_crc = crc_ccitt(buff[: val_idx + length], iv=0x6363)
    leftover_bytes = buff[val_idx + length + 2 :]

    logger.info("Decoded STLV data:")
    logger.info("+- status.............0x{:02X}".format(status))
    logger.info("+- tag................0x{:02X}".format(tag))
    logger.info("+- length.............{}".format(length))
    logger.info("+- value..............{}".format(value.hex() if len(value) else "None"))
    logger.info("+- CRC................0x{:04X}".format(crc))
    logger.info("+- leftover_bytes.....{}".format(leftover_bytes.hex() if len(leftover_bytes) else "None"))

    assert crc == calc_crc, "CRC mismatch. Received 0x{:04X}, expected 0x{:04X}".format(crc, calc_crc)

    return status, tag, length, value, leftover_bytes
