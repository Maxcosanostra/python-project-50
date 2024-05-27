#!/usr/bin/env python

import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish', help='set format of output'
    )
    args = parser.parse_args()

    file1 = args.first_file
    file2 = args.second_file
    output_format = args.format

    diff = generate_diff(file1, file2, format_name=output_format)
    print(diff)


if __name__ == '__main__':
    main()
