'''
Change the filename extension(suffix) of files under one directory
'''

import argparse
import os


def confirm(question='OK to continue?'):
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input(question + ' [y/n] ').lower()
    return answer == "y"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files_dir', required=True, type=str, help='the containing directory of files need to be renamed')
    parser.add_argument('--source_ext', required=True, type=str, help='original extension name')
    parser.add_argument('--target_ext', required=True, type=str, help='target extension name')
    parser.add_argument('--recursive', action='store_true', default=False, help='rename the files under subdirectory')

    opt = parser.parse_args()

    assert os.path.isdir(opt.files_dir), '{0} is not a directory'.format(opt.files_dir)
    assert opt.source_ext[0] == '.', 'Extension name should start with .(dot)'
    assert opt.target_ext[0] == '.', 'Extension name should start with .(dot)'
    assert opt.source_ext != opt.target_ext, 'Target extension({0}) should not be the same as source extension({1})'.format(opt.target_ext, opt.source_ext)

    renaming_counter = 0
    source_path_list = []
    target_path_list = []
    for cur, dirs, files in os.walk(opt.files_dir):
        for file in sorted(files):
            if file.endswith(opt.source_ext):
                source_path = os.path.join(cur, file)
                target_path = os.path.join(cur, file[0:-len(opt.source_ext)] + opt.target_ext)
                print('{0} -> {1}'.format(source_path, file[0:-len(opt.source_ext)] + opt.target_ext))
                source_path_list.append(source_path)
                target_path_list.append(target_path)
                renaming_counter += 1
        if not opt.recursive:
            break

    if renaming_counter <= 0:
        print('Found no file with extension: {0}'.format(opt.source_ext))
        exit(1)
    print('Above is the preview of the renaming, in total {0} files'.format(renaming_counter))

    if not confirm('Please confirm you want to do this renaming'):
        print('Stop renaming, no file is renamed')
        exit(0)

    for source_path, target_path in zip(source_path_list, target_path_list):
        os.rename(source_path, target_path)

    print('Above renaming is done')


if __name__ == "__main__":
    main()
