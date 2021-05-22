'''
show how many plots a day
'''

import argparse
import os
import datetime

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import IPython


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--plots_dirs', nargs='+', required=True, type=str, help='plots directory')

    opt = parser.parse_args()
    for dir in opt.plots_dirs:
        assert os.path.isdir(dir), '{0} is not a directory'.format(dir)

    date_to_count = {}
    for dir in opt.plots_dirs:
        for cur, _, files in os.walk(dir):
            for file in sorted(files):
                if file.endswith('.plot'):
                    cdate = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(cur, file))).date()
                    if cdate not in date_to_count:
                        date_to_count[cdate] = 1
                    else:
                        date_to_count[cdate] += 1
            break

    x = list(date_to_count.keys())
    y = list(date_to_count.values())
    y_sum = np.cumsum(y)
    plt.subplot(1, 2, 1)
    plt.title('Number of plots per day')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.bar(x, y)
    plt.gcf().autofmt_xdate()

    plt.subplot(1, 2, 2)
    plt.title('Total plots')
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(x, y_sum)
    plt.gcf().autofmt_xdate()
    plt.show()


if __name__ == "__main__":
    main()
