#!/usr/bin/python3.6
"""
A program to generate traingle and right traingle dataset
"""
from numpy.random import randint
import csv

# local python import
from utils import EXP_RT_FILE_NAMES
from utils import RT_LABELS


def check_right_triangle(a, b, c):
    """Pythagoras theorm."""
    if a**2 + b**2 == c**2 or \
            a**2 + c**2 == b**2 or \
            c**2 + b**2 == a**2:
        return 1

    return 0


def shuffle(a, b, c):
    rand = randint(3)
    if rand == 0:
        return a, b, c
    elif rand == 1:
        return c, a, b
    else:
        return b, c, a


def create_rt_datasets():
    """Create right angle triangle datasets."""

    # File pointer for RT dataset 1
    FP = open(EXP_RT_FILE_NAMES[0], 'w')
    FILE_WRITER = csv.writer(
        FP, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER.writerow(RT_LABELS[0])

    for x in range(2, 1000):
        # If n is odd, then n, (n**2-1)/2, (n**2+1)/2 is a right triangle.
        if x % 2 == 1:
            y = (x**2 - 1) / 2
            z = (x**2 + 1) / 2

        # If n is even, then n, (n**2/4)-1, (n**2/4)+1 is a right triangle.
        else:
            y = (x**2 / 4) - 1
            z = (x**2 / 4) + 1

        a, b, c = shuffle(x, y, z)
        validity = check_right_triangle(a, b, c)

        # Assign attributes based on the LABELS
        attributes = [a, b, c, validity]
        FILE_WRITER.writerow(attributes)

    FP.close()


def main():
    """Main function."""
    create_rt_datasets()


if __name__ == "__main__":
    main()
