
import os
import json
from csv_to_list import code_from_csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_TXT = 'post_optim.txt'


def csv_to_dict():
    """
    All the extracted post-codes are normalized and exported
    in a file, grouped by outward code.
    """
    # Outward part is key, inward part is added in the set
    postcodes = {}

    for code in code_from_csv():
        out_code = code[:-3]
        inw_code = code[-3:]
        if out_code not in postcodes:
            postcodes[out_code] = set()
        postcodes[out_code].add(inw_code)

    # Calculate length before joining the set
    codesnr = sum(len(val) for val in postcodes.values())

    for key, val in postcodes.items():
        postcodes[key] = ','.join(sorted(val))

    with open(f'{BASE_DIR}/{OUTPUT_TXT}', 'w') as output:
        json.dump(postcodes, output, indent=2, sort_keys=True)

    # 1,698,194 codes, 6.5 MB file
    print(f'Stat :: {codesnr:,} codes.')


if __name__ == '__main__':
    csv_to_dict()
