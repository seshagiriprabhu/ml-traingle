#!/usr/bin/python3.6
"""
A program to generate traingle and right traingle dataset
"""
from numpy.random import randint
from numpy import sqrt
import csv

# local python import
from utils import EXP_RT_FILE_NAMES
from utils import RT_LABELS

from utils import check_right_triangle
from utils import shuffle, floor_sqrt


MAX_LINES = 1000

RAND_TUPLES = [
    (1, 999), (1000, 1999), (2000, 2999), (3000, 3999),
    (4000, 4999), (5000, 5999), (6000, 6999),
    (7000, 7999), (8000, 8999), (9000, 9999)
]


def create_valid_rt_dataset():
    """Create valid right angle triangle datasets."""

    # File pointer for RT dataset 1
    FP = open(EXP_RT_FILE_NAMES[0], 'w')
    FILE_WRITER = csv.writer(
        FP, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
    )
    FILE_WRITER.writerow(RT_LABELS[0])

    i = 0

    # Holds the set of valid RT triangles (a, b, c)
    # to avoid duplicate points
    valid_triangle = []

    while True:
        if i > MAX_LINES:
            break

        tup1 = RAND_TUPLES[randint(10)]
        tup2 = RAND_TUPLES[randint(10)]

        a = randint(tup1[0], tup1[1])
        b = randint(tup2[0], tup2[1])
        c = int(sqrt(a**2 + b**2))

        # Consider only integer lengths
        if c != floor_sqrt(a**2 + b**2):
            continue

        validity = check_right_triangle(a, b, c)

        # Discard invalid (a, b, c) RTs
        if validity != 1:
            continue

        # if (a, b, c) RT was already generated, discard the current one
        if [a, b, c] in valid_triangle:
            continue
        # (a, b, c) is freshly generated, add them to the list of valid RTs
        else:
            valid_triangle.append([a, b, c])

        # Generate 5 points in the range [10000, 100000] using (a, b, c)
        for j in range(5):
            # (a, b, c) less than 5000 can be multiplied with (10, 20) to get
            # values in range [10000, 100000]
            if a < 5000 and b < 5000 and c < 5000:
                const = randint(10, 19)
            # (a, b, c) greater than 5000 can be multiplied with (2, 9) to get
            # values in range [10000, 100000]
            else:
                const = randint(2, 9)

            a1, b1, c1 = const * a, const * b, const * c
            a1, b1, c1 = shuffle(a1, b1, c1)
            validity1 = check_right_triangle(a1, b1, c1)
            attributes1 = [a1, b1, c1, validity1]
            FILE_WRITER.writerow(attributes1)
            i += 1

        a, b, c = shuffle(a, b, c)
        attributes = [a, b, c, validity]
        FILE_WRITER.writerow(attributes)

        i += 1

    FP.close()
    return valid_triangle


def main():
    """Main function."""
    create_valid_rt_dataset()


if __name__ == "__main__":
    main()
