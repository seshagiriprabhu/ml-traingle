#!/usr/bin/python3.6
"""
A program to generate traingle and right traingle dataset
"""
from numpy.random import randint
import csv
import os

# File related constants
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(APP_DIR, 'data')
TRIANGLE_FILE = os.path.join(DATA_DIR, "triangle.csv")
DATASET1 = os.path.join(DATA_DIR, "dataset1.csv")
DATASET2 = os.path.join(DATA_DIR, "dataset2.csv")
DATASET3 = os.path.join(DATA_DIR, "dataset3.csv")
RIGHT_TRIANGLE_FILE_NAMES = [DATASET1, DATASET2, DATASET3]

# Label related constants
LABEL1 = ['side1', 'side2', 'side3', 'validity']
LABEL2 = ['side1', 'side2', 'side3', 'side12', 'side22', 'side32', 'validity']
LABEL3 = ['side12', 'side22', 'side32', 'validity']


def check_triangle(a, b, c):
    """The sum of the lengths of any two sides of a triangle is greater than
    the length of the third side.
    """
    if a + b > c and b + c > a and a + c > b:
        return 1
    return 0


def check_right_triangle(a, b, c):
    """Pythagoras theorm."""
    if a**2 + b**2 == c**2 or \
            a**2 + c**2 == b**2 or \
            c**2 + b**2 == a**2:
        return 1

    return 0


def main():
    """Main function."""
    # Create normal triangle dataset
    # Triangle dataset
    # Attributes: (a, b, c, validity)
    FP = open(TRIANGLE_FILE, 'w')
    FILE_WRITER = csv.writer(
        FP, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER.writerow(LABEL1)

    for i in range(1000):
        a = randint(100000)
        b = randint(100000)
        c = randint(100000)
        FILE_WRITER.writerow([a, b, c, check_triangle(a, b, c)])
    FP.close()

    # Create right angle triangle datasets.
    # Dataset 1 - Right angle triangle.
    # Attributes: (a, b, c, validity)
    FP1 = open(RIGHT_TRIANGLE_FILE_NAMES[0], 'w')
    FILE_WRITER1 = csv.writer(
        FP1, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER1.writerow(LABEL1)

    # Dataset 2 - Right angle triangle.
    # Attributes: (a, b, c, a**2, b**2, c**2, validity)
    FP2 = open(RIGHT_TRIANGLE_FILE_NAMES[1], 'w')
    FILE_WRITER2 = csv.writer(
        FP2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER2.writerow(LABEL2)

    # Dataset 3 - Right angle triangle.
    # Attributes: (a**2, b**2, c**2, validity)
    FP3 = open(RIGHT_TRIANGLE_FILE_NAMES[2], 'w')
    FILE_WRITER3 = csv.writer(
        FP3, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER3.writerow(LABEL3)

    for i in range(1000):
        a = randint(100000)

        # If n is odd, then n, (n**2-1)/2, (n**2+1)/2 is a right triangle.
        if a % 2 == 1:
            b = (a**2 - 1) / 2
            c = (a**2 + 1) / 2

        else:
            b = randint(100000)
            c = randint(100000)

        validity = check_right_triangle(a, b, c)

        FILE_WRITER1.writerow([a, b, c, validity])
        FILE_WRITER2.writerow([a, b, c, a**2, b**2, c**2, validity])
        FILE_WRITER3.writerow([a**2, b**2, c**2, validity])

    FP1.close()
    FP2.close()
    FP3.close()


if __name__ == "__main__":
    main()
