'''
python/numpy argument passing and assignment
'''
import numpy as np


def i_will_modify_x(x):
    x += 1


def i_wont_modify_x(x):
    x = x.copy()
    x += 1


def i_will_modify_x2(x):
    y = x
    y += 1


def main():
    x = np.array([1, 2, 3, 4])
    print('original x:', x)
    i_will_modify_x(x)
    print('inplace modified x: ', x)
    x = np.array([1, 2, 3, 4])
    i_will_modify_x2(x)
    print('assign x to y: ', x)
    x = np.array([1, 2, 3, 4])
    i_wont_modify_x(x)
    print('x stay the same: ', x)


if __name__ == "__main__":
    main()
