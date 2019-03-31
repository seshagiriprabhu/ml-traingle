#!/usr/bin/python3.6
"""
A program to generate valid triangle dataset

Dataset destination: data/experiment/rt_dataset1.csv
"""
import csv
from numpy import sqrt
from numpy.random import randint

# local python import
from utils import EXP_RT_FILE_NAMES, RT_LABELS
from utils import check_right_triangle, shuffle, floor_sqrt


RAND_TUPLES = [
    (1, 999), (1000, 1999), (2000, 2999), (3000, 3999),
    (4000, 4999), (5000, 5999), (6000, 6999),
    (7000, 7999), (8000, 8999), (9000, 9999)
]


def create_valid_rt_points(max_lines=1000):
    """Create max_lines number of valid right angle triangle points.

    Parameters:
    max_lines (int, default=1000): max no of valid RT requested.

    Returns:
    valid_triangle (list): List of sorted valid RT triangles.
    """

    i = 0
    # Holds the set of valid RT triangles (a, b, c)
    # to avoid duplicate points
    valid_triangle = []

    while True:
        if i > max_lines:
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
            i += 1

        x = 0
        # Generate 5 points in the range [10000, 100000] using (a, b, c)
        while x < 6:
            # (a, b, c) less than 5000 can be multiplied with (10, 20) to get
            # values in range [10000, 100000]
            if a < 5000 and b < 5000 and c < 5000:
                const = randint(10, 19)
            # (a, b, c) greater than 5000 can be multiplied with (2, 9) to get
            # values in range [10000, 100000]
            else:
                const = randint(2, 9)

            a1, b1, c1 = const * a, const * b, const * c
            validity = check_right_triangle(a1, b1, c1)

            # Avoid duplicate entries
            if [a1, b1, c1] in valid_triangle:
                continue

            # Only write valid (a1, b1, c1)
            if validity:
                valid_triangle.append([a1, b1, c1])
                x += 1
                i += 1

    return valid_triangle


def write_into_files(valid_triangle):
    """Write the valid_triangle list into dataset csv files.

    Unsorted:
    rt_dataset_u1.csv - [a, b, c, validity]

    Sorted:
    rt_dataset_s1.csv - [a, b, c, validity]

    Parameters:
    valid_triangle (list): List of sorted valid triangles.
    """

    # File pointer for RT datasets
    FP, FILE_WRITER = [], []

    """
    1. Open all the dataset files.
    2. Create csv filewriter.
    3. Write labels into files as the first row.
    """
    for counter, filename in enumerate(EXP_RT_FILE_NAMES):
        FP.append(open(EXP_RT_FILE_NAMES[counter], 'w'))
        FILE_WRITER.append(
            csv.writer(
                FP[counter], delimiter=',', quotechar='"',
                quoting=csv.QUOTE_MINIMAL
            )
        )
        FILE_WRITER[counter].writerow(RT_LABELS[0])

    for [a, b, c] in valid_triangle:
        # FILE_WRITER[0] is sorted
        [x, y, z] = sorted([a, b, c])
        FILE_WRITER[0].writerow([x, y, z, 1])

        a, b, c = shuffle(a, b, c)
        # FILE_WRITER[1] is unsorted
        FILE_WRITER[1].writerow([a, b, c, 1])

    for fp in FP:
        fp.close()


def main():
    """Main function."""
    valid_triangle_list = create_valid_rt_points()
    write_into_files(valid_triangle_list)


if __name__ == "__main__":
    main()
