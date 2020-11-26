'''
Find closest images
'''

import argparse
import os
from shutil import copyfile

import numpy as np
from PIL import Image
import imageio


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--query',   required=True,  type=str, help='the path to the query image')
    parser.add_argument('--db_dir', required=True,  type=str, help='image dir to search')
    parser.add_argument('--top_k', default=10,  type=int, help='top k')
    parser.add_argument('--save_to', default='./temp',  type=str, help='top k')

    opt = parser.parse_args()

    assert os.path.isfile(opt.query), '{0} is not a file'.format(opt.query)
    assert os.path.isdir(opt.db_dir), '{0} is not a dir'.format(opt.db_dir)
    if not os.path.exists(opt.save_to):
        os.makedirs(opt.save_to)
    query_img = imageio.imread(opt.query, pilmode='RGB')
    dists = []
    names = []
    i = 0
    for cur, dirs, files in os.walk(opt.db_dir):
        for file in sorted(files):
            if file.endswith(('.png', '.PNG', 'jpg', 'JPG')):
                db_path = os.path.join(cur, file)
                db_img = Image.open(db_path)
                db_img = db_img.resize(query_img.shape[:2][::-1])
                db_img = np.array(db_img)
                mse = ((query_img.astype(np.float32)/255.0 - db_img.astype(np.float32)/255.0)**2).mean(axis=None)
                dists.append(mse)
                names.append(db_path)
                print(i)
                i += 1
    top_k_id = np.argsort(np.array(dists))[:opt.top_k]
    top_k_path = [names[i] for i in top_k_id]
    for i, file in enumerate(top_k_path):
        copyfile(file, os.path.join(opt.save_to, os.path.basename(file)))
        print(f'top {i+1} neighbor: {file}')
    # import IPython
    # IPython.embed()
    # assert 0

if __name__ == "__main__":
    main()
