# coding:utf-8
import os


def do(path):
    """
    D:\temp\3rdZS_TJZX_179_TJZX1898-TJZX2815\TJZX_2815_zoudan_CAD_Lung_DVD.json -->>
    D:\temp\3rdZS_TJZX_179_TJZX1898-TJZX2815\TJZX_2815_CAD_Lung_DVD.json
    """
    for roots, _, files in os.walk(path):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            new_name = filename.replace('_' + filename.split('_')[2], '')
            new_filename = os.path.join(roots, new_name)
            old_filename = os.path.join(roots, filename)
            print(old_filename)
            os.rename(old_filename, new_filename)


if __name__ == '__main__':
    do(r'D:\temp')
