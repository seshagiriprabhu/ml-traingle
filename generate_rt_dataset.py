#!/usr/bin/python3.6
"""
A program to generate right traingle dataset for experiments
"""
import os
import pandas as pnd
import csv
from numpy.random import randint

# local python import
from utils import EXP8_RT_FILE_NAMES as EXP_RT_FILE_NAMES
from utils import EXP_RT_FILE_NAMES as VALID_RT_FILE_NAMES
from utils import RT_LABELS, check_right_triangle, shuffle
from generate_valid_rt import create_valid_rt_points


def create_attributes_list(a, b, c, validity):
    """Create a list containing RT attributes for the
    current experiment datasets.

    Parameters:
    side1, side2, side3 (int, int, int): Lengths of side of triangle.
    validity (bool): 1 if (side1, side2, side3) is RT, 0 otherwise

    Returns:
    attributes (list): List of attributes specially created for
      the current experiment.
    """
    attributes = []

    # unsorted dataset attributes
    attributes.append([a, b, c, validity])
    attributes.append([a, b, c, a**2, b**2, c**2, validity])
    attributes.append([a**2, b**2, c**2, validity])
    attributes.append([a + b, a + c, b + c, validity])
    attributes.append([a**2 + b**2, a**2 + c**2, b**2 + c**2, validity])
    attributes.append([
        a**2, b**2, c**2, a**2 + b**2,
        a**2 + c**2, b**2 + c**2, validity
    ])

    return attributes


def write_exp_rt_datasets(sorted_rt_triangles, unsorted_rt_triangles):
    """Create sorted and unsorted RT datasets.

    Parameters:
    sorted_rt_triangles (list): List of sorted valid RT triangles.
    unsorted_rt_triangles (list): List of unsorted valid RT triangles.
    """

    FP, FILE_WRITER = [], []

    """
    1. Open all the dataset files.
    2. Create csv filewriter.
    3. Write labels as the first row of the files.
    """
    for counter, filename in enumerate(EXP_RT_FILE_NAMES):
        FP.append(open(filename, 'w'))
        FILE_WRITER.append(
            csv.writer(
                FP[counter], delimiter=',', quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
        )
        FILE_WRITER[counter].writerow(RT_LABELS[counter % len(RT_LABELS)])

    valid_rt_list = [
        sorted_rt_triangles, unsorted_rt_triangles
    ]

    for counter, valid_rt in enumerate(valid_rt_list):
        for [a, b, c] in valid_rt:
            if c < 90000:
                const = randint(2, 9999)
            else:
                const = randint(-9999, -2)

            # Invalid RT
            ia, ib, ic = const + a, const + b, const + c

            # Just to make sure that it is valid or not
            # although adding constant to a valid RT
            # creates invalid RTs
            validity_i = check_right_triangle(ia, ib, ic)

            # Assign attributes based on LABELs for valid RTs
            attributes = create_attributes_list(a, b, c, 1)

            # Assign attributes based on LABELs for invalid RTs
            attributes_i = create_attributes_list(ia, ib, ic, validity_i)

            """
            FILE_WRITER has 2 * len(RT_LABELS) elements
            first len(RT_LABELS) numbers are sorted: rt_dataset_s*
            remaining len(RT_LABELS) numbers are unsorted: rt_dataset_u*
            """
            for count in range(len(FILE_WRITER) // 2):
                # counter is zero, only write into sorted datasets
                # counter is one, only write into unsorted datasets
                index = (counter * len(RT_LABELS)) + count
                FILE_WRITER[index].writerow(attributes[count])
                FILE_WRITER[index].writerow(attributes_i[count])

    # close all the opened file pointers
    for filepointer in FP:
        filepointer.close()


def main():
    """Main function."""
    # sorted valid RT dataset exists
    if os.path.isfile(VALID_RT_FILE_NAMES[0]):
        df = pnd.read_csv(VALID_RT_FILE_NAMES[0])
        sorted_rt_triangles = [
            [row[col] for col in df.columns[:3]] for row in df.to_dict('records')
        ]

    # unsorted valid RT dataset exists
    if os.path.isfile(VALID_RT_FILE_NAMES[1]):
        df = pnd.read_csv(VALID_RT_FILE_NAMES[1])
        unsorted_rt_triangles = [
            [row[col] for col in df.columns[:3]] for row in df.to_dict('records')
        ]

    # valid RT dataset doesn't exist
    else:
        rt_triangles = create_valid_rt_points()
        sorted_rt_triangles = []
        unsorted_rt_triangles = []

        for [a, b, c] in rt_triangles:
            [x, y, z] = sorted([a, b, c])
            sorted_rt_triangles.append([x, y, z])

            [x, y, z] = shuffle([a, b, c])
            unsorted_rt_triangles.append([x, y, z])

    write_exp_rt_datasets(sorted_rt_triangles, unsorted_rt_triangles)


if __name__ == "__main__":
    main()
