#!/usr/bin/python3.6
"""
A program to generate traingle dataset for a given
experiment imported from utils.py
"""
import csv
from numpy.random import randint

# local python import
from utils import EXP8_T_FILE_NAMES as EXP_T_FILE_NAMES
from utils import T_LABELS, check_triangle


def create_triangle_datasets():
    """Create normal triangle datasets.

    t_dataset1 - (a, b, c, validity)
    t_dataset2 - (a, b, c, a + b, a + c, b + c, validity)
    t_dataset3 - (a + b, a + b, b + c, validity)
    """

    # File pointer for the first triangle dataset
    FP1 = open(EXP_T_FILE_NAMES[0], 'w')
    FILE_WRITER1 = csv.writer(
        FP1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER1.writerow(T_LABELS[0])

    # File pointer for the second triangle dataset
    FP2 = open(EXP_T_FILE_NAMES[1], 'w')
    FILE_WRITER2 = csv.writer(
        FP2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER2.writerow(T_LABELS[1])

    # File pointer for third triangle dataset
    FP3 = open(EXP_T_FILE_NAMES[2], 'w')
    FILE_WRITER3 = csv.writer(
        FP3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER3.writerow(T_LABELS[2])

    for j in range(1000):
        a = randint(100000)
        b = randint(100000)
        c = randint(100000)
        validity = check_triangle(a, b, c)

        attributes1 = [a, b, c, validity]
        FILE_WRITER1.writerow(attributes1)

        attributes2 = [a, b, c, a + b, a + c, b + c, validity]
        FILE_WRITER2.writerow(attributes2)

        attributes3 = [a + b, a + c, b + c, validity]
        FILE_WRITER3.writerow(attributes3)

    FP1.close()
    FP2.close()
    FP3.close()


def main():
    """Main function."""
    create_triangle_datasets()


if __name__ == "__main__":
    main()
