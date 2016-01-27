#!/usr/bin/env python
'''
Make a scatter plot of a csv.

Usage:
  ./plot_scatter.py [options] [<file>]

Options:
  --delimiter=DELIMITER    Set the delimiter to DELIMITER.
  --title=TITLE            Print this title.
  --xlabel=XLABEL          Print this x label.
  --ylabel=YLABEL          Print this y label.
  --logx                   Plot log of x.
  --logy                   Plot lot of y.
'''
from docopt import docopt;
import matplotlib.pyplot as plt;
import numpy as np;
import sys;
def process_file(filename=None,d=None):
    if filename:
        data = np.loadtxt(filename)
    else:
        lines = '\n'.join(sys.stdin.readlines());
        data = np.genfromtxt(lines)
    return data[:,0],data[:,1] 

if __name__ == '__main__':
    opts=docopt(__doc__,help=True);
    x,y=process_file(opts['<file>'],opts['--delimiter']);
    if opts['--logx']:
        x = np.log10(x);
    if opts['--logy']:
        y = np.log10(y);
    if opts['--xlabel']:
        plt.xlabel(opts['--xlabel']);
    if opts['--ylabel']:
        plt.ylabel(opts['--ylabel']);
    if opts['--title']:
        plt.title(opts['--title']);
    plt.scatter(x,y);
    plt.show();

