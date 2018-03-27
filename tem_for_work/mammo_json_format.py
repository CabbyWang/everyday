import os
import json
import click


@click.command()
@click.option("--path", prompt="Enter the dir", help="path to walk")
def do(path):
    """
    format the old jsons of mammogram\n
    e.g python mammo_json_format.py xxx
    """
    for roots, _, files in os.walk(path):
        for filename in files:
            if not filename.endswith('.json'):
                continue
            with open(filename) as fp:
                origin = json.load(fp)
            items = origin.get('MammoDisease', {})
            for k, v in items.items():
                for key in ['points', 'vertex']:
                    if key in v:
                        v.setdefault('VerifiedInfo', {})[key] = v.pop(key)


if __name__ == '__main__':
    do()
