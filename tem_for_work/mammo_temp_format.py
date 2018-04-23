# coding:utf-8
import copy
import json
from pathlib import Path


def convert(json_file, out_file):
    print(json_file, out_file)
    with open(json_file) as fp:
        data = json.load(fp)
    origin = copy.deepcopy(data)

    # count
    origin['count'] = str(origin.get('count'))

    nodules = origin.get('MammoDisease', {})
    for _, v in nodules.items():
        roi_type = v.get('ROIType')
        vv = v.get('VerifiedInfo', {})
        vv.pop('ROIType', None)

        # "Malignacy" = ''
        v['Malignancy'] = ''

        # sourceType
        v['SourceType'] = v.get('SourceType') or vv.get('SourceType')
        vv.pop('SourceType', None)

        # "Lesion"
        lesion = vv.pop('Malignancy', '')
        # print(lesion)
        vv['Lesion'] = '1' if lesion == 1 else ''

        # BI-RADS / Disease
        bi_rads = vv.pop('BI-RADS', '') or v.get('BI-RADS', '')
        disease = vv.pop('Disease', '') or v.get('Disease', '')
        v['BI-RADS'] = str(bi_rads)
        v['Disease'] = str(disease)

        # BB
        if roi_type == 'Rectangle':
            for bb in ['CenterX', 'CenterY', 'DimX', 'DimY']:
                vv.pop(bb, None)
        elif roi_type == 'TiltedRectangle':
            v['TiltedRectangle'] = v.get('TiltedRectangle') or vv['TiltedRectangle']
        elif roi_type == 'Polygon':
            v['Polygon'] = v.get('Points') or vv['Points']

    with open(out_file, 'w') as f:
        json.dump(origin, f, indent=4, sort_keys=True)


def main():
    tp_dir = Path(r"D:\1\Group 2_100case_changed\Group 2")
    # tp_dir = Path(r"D:\test1")
    # i = 0
    for pat_dir in tp_dir.iterdir():
        for side_dir in pat_dir.iterdir():
            for json_file in side_dir.iterdir():
                # Convert
                # out_file = Path(json_file.parent, '{}_out.json'.format(json_file.stem))
                convert(json_file, json_file)
                # i += 1

    # print(i)


if __name__ == '__main__':
    main()
