import os
import shutil


def do(source_path, out_path):
    for roots, _, files in os.walk(source_path):
        for filename in files:
            if filename.endswith('.json'):
                file_abspath = os.path.join(roots, filename)
                out_abspath = os.path.join(out_path, file_abspath.split(source_path + '\\')[1])
                os.makedirs(os.path.dirname(out_abspath), mode=0o777, exist_ok=True)
                shutil.copy(file_abspath, out_abspath)


if __name__ == '__main__':
    do(r'D:\test', r'D:\out')
