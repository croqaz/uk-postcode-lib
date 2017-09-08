
import os
import csv
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FOLDER = 'CSV'
OUTPUT_TXT = 'postcodes.txt'


def csv_to_list():
    """
    This function searches all CSV files from the
    specified "CSV_FOLDER" and extracts only the first column;
    the first column should be the UK post-code.
    All the extracted post-codes are normalized and exported
    in a file, each code on a separate line.
    """
    # Sets are the most efficient data structure for storing unique strings
    postcodes = set()

    globpath = f'{BASE_DIR}/{CSV_FOLDER}/*.csv'
    for csvname in glob.glob(globpath):
        print('Processing CSV ::', csvname)
        with open(csvname, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                code = row[0].upper().replace(' ', '')
                postcodes.add(code)

    dump = '\n'.join(sorted(postcodes))
    with open(f'{BASE_DIR}/{OUTPUT_TXT}', 'w') as output:
        output.write(dump)

    print(f'Stat :: {len(postcodes):,} codes, '
          ' {len(dump)/1000_000:,.2f} MB file.')


if __name__ == '__main__':
    csv_to_list()
