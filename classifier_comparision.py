#!/usr/bin/python3.6
"""
A program which classifies a given dataset using
various classic ML classifiers.
"""
from __future__ import print_function

import os
import pandas as pnd
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# Classifier related constants
NAMES = [
    "Nearest Neighbors",
    # "Linear SVM",
    # "RBF SVM",
    "Gaussian Process",
    "Decision Tree",
    "Random Forest",
    "Neural Net",
    "AdaBoost",
    "Naive Bayes",
    "QDA"
]

CLASSIFIERS = [
    KNeighborsClassifier(3),
    # SVC(kernel="linear", C=0.025),
    # SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(
        activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
        beta_2=0.999, early_stopping=False, epsilon=1e-08,
        hidden_layer_sizes=(30, 30, 30), learning_rate='constant',
        learning_rate_init=0.001, max_iter=200, momentum=0.9,
        nesterovs_momentum=True, power_t=0.5, random_state=None,
        shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
        verbose=False, warm_start=False
    ),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()
]


# File related constants
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(APP_DIR, 'data')
TRIANGLE_FILE = os.path.join(DATA_DIR, "triangle.csv")
DATASET1_FILE = os.path.join(DATA_DIR, "dataset1.csv")
DATASET2_FILE = os.path.join(DATA_DIR, "dataset2.csv")
DATASET3_FILE = os.path.join(DATA_DIR, "dataset3.csv")
DATASET_FILES = [
    TRIANGLE_FILE, DATASET1_FILE, DATASET2_FILE, DATASET3_FILE
]
TESTING_DATASET_NAMES = [
    "Normal Triangle",
    "Right Triangle Dataset 1",
    "Right Triangle Dataset 2",
    "Right Triangle Dataset 3"
]
TESTING_DATASET = []


def main():
    """Main function."""

    for filename in DATASET_FILES:
        TESTING_DATASET.append(pnd.read_csv(filename))

    for i in range(len(TESTING_DATASET)):
        if i == 0 or i == 1:
            X_train, X_test, y_train, y_test = train_test_split(
                TESTING_DATASET[i].loc[:, 'side1':'side3'],
                TESTING_DATASET[i].loc[:, 'validity'],
                test_size=0.20,
                train_size=0.80,
                random_state=345123
            )

        if i == 2:
            X_train, X_test, y_train, y_test = train_test_split(
                TESTING_DATASET[i].loc[:, 'side1':'side32'],
                TESTING_DATASET[i].loc[:, 'validity'],
                test_size=0.20,
                train_size=0.80,
                random_state=269380
            )

        else:
            X_train, X_test, y_train, y_test = train_test_split(
                TESTING_DATASET[i].loc[:, 'side12':'side32'],
                TESTING_DATASET[i].loc[:, 'validity'],
                test_size=0.20,
                train_size=0.80,
                random_state=7887631
            )

        print("-" * 40)
        print(TESTING_DATASET_NAMES[i])
        print("-" * 40)

        for name, classifier in zip(NAMES, CLASSIFIERS):
            classifier.fit(X_train, y_train)
            score = classifier.score(X_test, y_test)
            print(name + ": %.2f" % (score))

        print("-" * 40 + "\n")


if __name__ == "__main__":
    main()
