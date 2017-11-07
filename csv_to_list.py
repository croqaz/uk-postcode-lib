
import os
import csv
import glob

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FOLDER = 'CSV'
OUTPUT_TXT = 'postcodes.txt'


def code_from_csv():
    """
    This function searches all CSV files from the
    specified "CSV_FOLDER" and extracts only the first column;
    the first column should be the UK post-code.
    """
    globpath = f'{BASE_DIR}/{CSV_FOLDER}/*.csv'
    for csvname in glob.glob(globpath):
        print('Processing CSV ::', csvname)
        with open(csvname, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in csvreader:
                code = row[0].upper().replace(' ', '')
                yield code


def csv_to_list():
    """
    All the extracted post-codes are normalized and exported
    in a file, each code separated by comma.
    """
    # Sets are the most efficient data structure for storing unique strings
    postcodes = set()

    for code in code_from_csv():
        postcodes.add(code)

    dump = ','.join(sorted(postcodes))
    with open(f'{BASE_DIR}/{OUTPUT_TXT}', 'w') as output:
        output.write(dump)

    # 1,698,194 codes, 12.65 MB file
    print(f'Stat :: {len(postcodes):,} codes, '
          f'{len(dump)/1000_000:,.2f} MB file.')


if __name__ == '__main__':
    csv_to_list()
