# coding:utf-8

import openpyxl
from pathlib import Path
import os


def row_count(csv_file):
    # wb = openpyxl.load_workbook(csv_file)
    with open(csv_file) as f:
        print(len(f.readlines()))
        return len(f.readlines())


def main():
    origin_dir = Path(r'D:\test2')
    for csv_file in origin_dir.iterdir():
        if not csv_file.suffix == '.csv':
            continue
        # csv
        row_cnt = row_count(csv_file)
        print(row_cnt < 1063)
        if row_cnt < 1063:
            os.remove(csv_file)


if __name__ == '__main__':
    main()
