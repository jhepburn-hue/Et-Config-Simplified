#!/usr/bin/python3

import json
import sys
from typing import List

"""
This script generates the brivo TCI json file list for batch creating their unified config files.
"""

UTF_8: str = "utf-8"

BRIVO_LK_NUMBER: str = "Lk50010"

BRIVO_RANGE1_TCI_PREFIX: str = "0230"
BRIVO_RANGE2_TCI_PREFIX: str = "0231"
BRIVO_RANGE3_TCI_PREFIX: str = "0232"
BRIVO_RANGE4_TCI_PREFIX: str = "0233"

LK_PREFIX: str = "Lk"
BRIVO_LK_START: int = 60000
DFNAME_PREFIX: str = "A00000039656434103F532F000"

KEY_ID: str = "id"
KEY_KEYSET: str = "keyset"
KEY_DFNAME: str = "dfname"
KEY_TCI: str = "tci"

ARG_OUTFILE: int = 1


def gen_tci_range(prefix: str) -> List[str]:
    return [prefix + bytes([i]).hex() for i in range(0, 256)]


if __name__ == "__main__":
    tcis: List[str] = (
        gen_tci_range(BRIVO_RANGE1_TCI_PREFIX)
        + gen_tci_range(BRIVO_RANGE2_TCI_PREFIX)
        + gen_tci_range(BRIVO_RANGE3_TCI_PREFIX)
        + gen_tci_range(BRIVO_RANGE4_TCI_PREFIX)
    )

    profiles: List[dict] = [
        {
            KEY_TCI: tcis[i],
            KEY_DFNAME: DFNAME_PREFIX + tcis[i],
            KEY_ID: LK_PREFIX + str(BRIVO_LK_START + i),
            KEY_KEYSET: BRIVO_LK_NUMBER,
        }
        for i in range(0, len(tcis))
    ]

    OUTFILE: str = sys.argv[ARG_OUTFILE]

    with open(OUTFILE, "w", encoding=UTF_8) as f:
        json.dump(profiles, f, indent=2)
