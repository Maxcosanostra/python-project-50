#!/usr/bin/env python

import argparse
import json
from gendiff.diff_gen import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    file1 = 'gendiff/files/file1.json'
    file2 = 'gendiff/files/file2.json'
    output_format = args.format

    diff = generate_diff(file1, file2)

    if output_format == 'json':
        print(json.dumps(diff, indent=2))
    else:
        print(diff)


if __name__ == '__main__':
    main()
