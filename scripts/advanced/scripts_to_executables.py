"""
==============================
7.10 Scripts to executables
==============================
"""

import os
import sys
from collections import Counter


def main(path, start:int=26):

    if not os.path.exists(path):
        print(f"{path} does not exist.")
        return

    stations = [file[start:] for file in os.listdir(path)]
    uniques = set(stations)

    # find duplicates in stations
    counts = Counter(stations)
    duplicates = {item:count for item, count in counts.items() if count > 1}
    if duplicates:
        print(f"Found {len(duplicates)} duplicates in {path}")
        for duplicate, count in duplicates.items():
            print(f"{duplicate} found {count} times")
        
        print(f"There are {len(uniques)} unique files.")
    else:
        print(f"No duplicates found in {path}")


if __name__ == "__main__":

    path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    start = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    main(path, start)


# %%
# pyinstaller --onefile scripts_to_executables.py

# %%
# dist/scripts_to_executables

# %%
# dist/scripts_to_executables /mnt/datawaha/hyex/atr/gscad_database/raw/BOMAustralia/zip_files

# %%
# dist/scripts_to_executables /mnt/datawaha/hyex/atr/gscad_database/raw/BOMAustralia/zip_files 26