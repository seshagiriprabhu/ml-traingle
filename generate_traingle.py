from random import randint
import csv

FILE_NAMES = ["testing.csv", "training.csv"]


def check_traingle(a, b, c):
    """The sum of the lengths of any two sides of a triangle is greater than
    the length of the third side.
    """
    if a + b > c and b + c > a and a + c > b:
        return 1
    return 0


if __name__ == "__main__":

    for x in range(2):
        FP = open(FILE_NAMES[x], 'w')

        FILE_WRITER = csv.writer(
            FP, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
        )

        FILE_WRITER.writerow(['side1', 'side2', 'side3', 'validity'])

        for i in range(1000):
            a = randint(1, 100000)
            b = randint(1, 100000)
            c = randint(1, 100000)
            FILE_WRITER.writerow([a, b, c, check_traingle(a, b, c)])
