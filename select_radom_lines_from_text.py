'''
Select random lines out of a text file and save to another file.
'''

import argparse
import os
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source_file', required=True, type=str, help='the source file')
    parser.add_argument('--save_to_file', required=True, type=str, help='save to')
    parser.add_argument('--num_lines', type=int, default=1, help='how many lines needed')

    opt = parser.parse_args()

    assert os.path.isfile(opt.source_file), '{0} is not a file'.format(opt.source_file)
    assert opt.source_file != opt.save_to_file, 'source and target cannot be the same'
    assert opt.num_lines >= 0, 'cannot save a negative number of lines'

    num_lines = sum(1 for line in open(opt.source_file))
    lines_index = random.sample(range(num_lines), opt.num_lines)
    with open(opt.source_file, 'r') as infile, open(opt.save_to_file, 'w') as outfile:
        for i, line in enumerate(infile):
            if i in lines_index:
                outfile.write(line)

    print(f'In total {opt.num_lines} random lines are selected from {os.path.basename(opt.source_file)} and written to {os.path.basename(opt.save_to_file)}')


if __name__ == "__main__":
    main()
