
import os
import csv
import glob
import json
import gzip
from marisa_trie import Trie

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FOLDER = 'CSV'
OUTPUT_GZ = 'postcodes.gz'


def code_from_csv():
    """
    This function searches all CSV files from the
    specified "CSV_FOLDER" and extracts only the first column;
    the first column should be the UK post-code.
    """
    globpath = '{}/{}/*.csv'.format(BASE_DIR, CSV_FOLDER)
    for csvname in glob.glob(globpath):
        print('Loading CSV ::', csvname)
        with open(csvname, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                code = row[0].upper().replace(' ', '')
                yield code


def write_to_file():
    """
    All the extracted post-codes are normalized and exported in a file.
    """
    # Sets are the most efficient data structure for storing unique strings
    postcodes = {}

    for code in code_from_csv():
        out_code = code[:-3]
        inw_code = code[-3:]
        if out_code not in postcodes:
            postcodes[out_code] = set()
        postcodes[out_code].add(inw_code)

    # Calculate length before joining the set
    codes = sum(len(val) for val in postcodes.values())

    for key, val in postcodes.items():
        postcodes[key] = ','.join(sorted(val))

    out_path = '{}/{}'.format(BASE_DIR, OUTPUT_GZ)
    with gzip.open(out_path, 'wt') as output:
        json.dump(postcodes, output, indent=2, sort_keys=True)
    f_size = os.stat(out_path).st_size / 1000 / 1000

    print('Stat :: {:,} codes, {:,.2f} MB file.'.format(codes, f_size))


if __name__ == '__main__':
    write_to_file()
