# coding:utf-8

from pathlib import Path
import shutil


def main():
    files_dict = {}
    end_files = []
    for filename in Path(r'E:\bjch_niis').iterdir():
    # for filename in Path(r'D:\test').iterdir():
        prefix = filename.stem.split('_')[0]
        files_dict.setdefault(prefix, []).append(filename)
    print(files_dict)

    for k, v in files_dict.items():
        file_size = 0
        end_file = ''
        for file_name in v:
            size = file_name.stat().st_size
            # print('filename = {}, daxiao = {}'.format(file_name, int(size) > int(file_size)))
            # print(size, file_size)
            if size > file_size:
                # print(111)
                end_file = file_name
                file_size = size
        print(end_files)
        end_files.append(end_file)

    for one_file in end_files:
        out_file = Path(r'E:\bjch_result_niis', one_file.name)
        # out_file = Path(r'D:\test1', one_file.name)
        shutil.copy(str(one_file), out_file)


if __name__ == '__main__':
    main()
