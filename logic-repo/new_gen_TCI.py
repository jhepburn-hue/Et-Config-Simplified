import json
import sys
from typing import List

"""
This script generates the TCI JSON file list for batch creating TCI config files.
"""

UTF_8: str = "utf-8"

DFNAME_PREFIX: str = "A00000039656434103F532F000"
KEY_ID: str = "id"
KEY_KEYSET: str = "keyset"
KEY_DFNAME: str = "dfname"
KEY_TCI: str = "tci"


def gen_tci_range(start_tci: str, amount: int) -> List[str]:
    """
    Generate a range of TCI values starting from the given TCI.
    """
    prefix = start_tci[:4]
    start_index = int(start_tci[4:], 16)
    return [prefix + format(i, "02X") for i in range(start_index, start_index + amount)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <output_file.json>")
        sys.exit(1)

    outfile = sys.argv[1]

    # Interactive prompts for user inputs
    print("Please enter the required data:")
    start_tci = input("Starting TCI value (e.g., 024A00): ").strip()
    lk_start = int(input("Starting LK number (e.g., 60000): ").strip())
    lk_number = input("Key ID (e.g., 50033): ").strip()
    amount = int(input("Number of TCIs to generate: ").strip())

    # Generate TCIs
    tcis: List[str] = gen_tci_range(start_tci, amount)

    # Create profiles
    profiles: List[dict] = [
        {
            KEY_TCI: tcis[i],
            KEY_DFNAME: DFNAME_PREFIX + tcis[i],
            KEY_ID: f"Lk{lk_start + i}",
            KEY_KEYSET: f"Lk{lk_number}",
        }
        for i in range(len(tcis))
    ]

    # Write to JSON file
    with open(outfile, "w", encoding=UTF_8) as f:
        json.dump(profiles, f, indent=2)

    print(f"Generated {amount} TCI profiles and saved to {outfile}.")
