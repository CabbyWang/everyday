# coding:utf-8
import json
from pathlib import Path


def filter_file(json_file):
    checked_list = ['PG', 'GT']
    with open(json_file) as fp:
        origin = json.load(fp)
        nodules = origin.get('Nodules', {})
        new_items = []
        for k, v in nodules.items():
            if not isinstance(v, dict):
                continue
            vv = v.get('VerifiedNodule', {})
            # if any(vv.get(checked, 'false').lower() == 'true' for checked in checked_list):
            if any(checked in vv for checked in checked_list):
                new_items.append(v)
        count = len(new_items)
        if not count:
            return
        new_nodules = {}
        for i, item in enumerate(new_items):
            new_nodules.setdefault('Nodules', {})['item{}'.format(i)] = item
            new_nodules['Nodules']['item{}'.format(i)]['VerifiedNodule']['labelIndex'] = str(i)
        new_nodules['AdditionalDiseases'] = origin.get('AdditionalDiseases', {})
        new_nodules['labelVersion'] = origin.get('labelVersion')
        new_nodules['version'] = origin.get('version')
        new_nodules['count'] = str(count)
        return new_nodules


def main():
    origin_dir = Path(r'D:\temp\83例标注后文件\标注后文件')
    out_dir = Path(r'D:\test')
    for json_file in origin_dir.iterdir():
        if not json_file.stem.endswith('_CAD_Lung_yxg'):
            continue
        new_nodules = filter_file(json_file)
        if new_nodules:
            name = json_file.name
            out_file = Path(out_dir, name)
            print(out_file)
            with open(out_file, 'w') as fp:
                json.dump(new_nodules, fp, indent=4)
                # json.dump(new_nodules, fp, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
