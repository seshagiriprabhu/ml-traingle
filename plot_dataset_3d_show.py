#!/usr/bin/python3.6
"""
A program to 3D plot a given CSV file
"""
import os
import sys
from argparse import ArgumentParser
import numpy as np
import pandas as pnd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['legend.fontsize'] = 10


def display_csv_dataset(dataset):
    """Display the given CSV dataset.

    Parameters:
    dataset (file): csv file
    """
    df = pnd.read_csv(dataset)
    labels = list(df.columns.values)

    three_dee = plt.figure(figsize=(19.20, 10.80)).gca(projection='3d')
    colors = np.where(df['validity'] == 1, 'red', 'blue')

    three_dee.scatter(
        df[labels[0]], df[labels[1]], df[labels[2]],
        c=colors, s=60, alpha=0.5,
        edgecolors='none', label='Valid Triangle'
    )
    three_dee.set_xlabel(labels[0], fontsize=16)
    three_dee.set_ylabel(labels[1], fontsize=16)
    three_dee.set_zlabel(labels[2], fontsize=16)
    red_patch = mpatches.Patch(color='red', label='Valid Triangle')
    blue_patch = mpatches.Patch(color='blue', label='Invalid Triangle')
    three_dee.legend(handles=[red_patch, blue_patch])

    plt.show()
    plt.close()


def dataset(astring):
    """Test if the dataset file exists.

    Parameters:
    astring: argstring passed to the --dataset option
    """
    if not os.path.isfile(astring):
        print("File %s does not exist" % astring)
        raise ValueError
    return astring


def main():
    """Main function."""
    parser = ArgumentParser(description="3D plot for T/RT datasets")
    parser.add_argument(
        '-d', '--dataset', dest='dataset',
        default=None, required=True,
        help='CSV dataset file to plot'
    )
    parsed_args = parser.parse_args()

    # verify if the given csv is valid and parsable
    try:
        df = pnd.read_csv(parsed_args.dataset)

    except pnd.io.common.EmptyDataError:
        print("File %s is empty", parsed_args.dataset)
        sys.exit(0)

    except Exception as error:
        print("Error in reading %s file", parsed_args.dataset)
        print(error)
        sys.exit(0)

    display_csv_dataset(parsed_args.dataset)


if __name__ == "__main__":
    main()
