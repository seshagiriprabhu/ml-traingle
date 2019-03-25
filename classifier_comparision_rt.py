#!/usr/bin/python3.6
"""
A program which classifies a triangle datasets using
various classic ML classifiers.
"""

from __future__ import print_function

import pandas as pnd
from sklearn.model_selection import train_test_split

# local python import
from utils import CLASSIFIERS, CLASSIFIER_NAMES
from utils import EXP7_RT_FILE_NAMES as EXP_RT_FILE_NAMES
from utils import RT_LABELS


def main():
    """Main function."""

    testing_dataset = []
    for filename in EXP_RT_FILE_NAMES:
        testing_dataset.append(pnd.read_csv(filename))

    for counter in range(len(testing_dataset)):
        # Splitting the columns into data and target
        ds_x = testing_dataset[counter].iloc[:, :-1]
        target = testing_dataset[counter].loc[:, 'validity']
        kwargs = dict(test_size=0.2, train_size=0.8, random_state=269380)
        X_train, X_test, y_train, y_test = train_test_split(ds_x, target, **kwargs)

        print("-" * 40)
        print("Dataset: Right Angle Triangle")
        print(RT_LABELS[counter - 3])
        print("-" * 40)

        for name, classifier in zip(CLASSIFIER_NAMES, CLASSIFIERS):
            classifier.fit(X_train, y_train)
            score = classifier.score(X_test, y_test)
            print(name + ": %.2f" % (score))

        print("-" * 40 + "\n")


if __name__ == "__main__":
    main()
