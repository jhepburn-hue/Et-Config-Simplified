#!/usr/bin/python3
"""
encoding.py
Author: Taylor Schmidt, WaveLynx Technologies

This module handles standard base64 encoding and decoding for Sequoia
"""

import base64


def encode_base64(indata: bytes) -> str:
    """
    Standard encoding of bytes into b64 string

    Params:
      - indata: input bytes

    Returns:
      - output encoded str
    """
    return base64.b64encode(indata).decode("utf-8")


def decode_base64(indata: str) -> bytes:
    """
    Standard decoding of b64 string into bytes

    Params:
      - indata: b64 str

    Returns:
      - output decoded bytes
    """
    return base64.b64decode(indata.encode("utf-8"))
