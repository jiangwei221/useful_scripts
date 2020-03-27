'''
move all files and folders one level up.
'''
import argparse
import os


def str2bool(v: str) -> bool:
    return v.lower() in ('true', '1', 'yes', 'y', 't')


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
    parser.add_argument('--tear_down_dir', required=True, type=str, help='which folder you want to tear down')
    parser.add_argument('--add_prefix', required=True, type=str2bool, help='make parent dir name as orefix for the files')

    opt = parser.parse_args()

    assert os.path.isdir(opt.tear_down_dir), f'{opt.tear_down_dir} is not a directory'

    renaming_counter = 0
    source_path_list = []
    target_path_list = []
    for cur, dirs, files in os.walk(opt.tear_down_dir):
        for file in sorted(files):
            source_path = os.path.join(cur, file)
            target_path = source_path.replace(opt.tear_down_dir + '/', opt.tear_down_dir + '_')
            print(f'{source_path} -> {target_path}')
            source_path_list.append(source_path)
            target_path_list.append(target_path)
            renaming_counter += 1

    if renaming_counter <= 0:
        print('Found no file to move')
        exit(1)
    print(f'Above is the preview of the renaming, in total {renaming_counter} files')

    if not confirm('Please confirm you want to do this moving'):
        print('Stop moving, no file is moved')
        exit(0)

    for source_path, target_path in zip(source_path_list, target_path_list):
        os.rename(source_path, target_path)

    print('Above moving is done')


if __name__ == "__main__":
    main()
