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


NAMES = [
    "Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
    "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
    "Naive Bayes", "QDA"
]

CLASSIFIERS = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(gamma=2, C=1),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()
]

APP_DIR = os.path.dirname(os.path.realpath(__file__))
TRAINING_FILE = os.path.join(APP_DIR, "training.csv")
DATASET = pnd.read_csv(TRAINING_FILE)


def main():
    """Main function."""
    X_train, X_test, y_train, y_test = train_test_split(
        DATASET.loc[:, 'side1':'side3'],
        DATASET.loc[:, 'validity'],
        test_size=0.20,
        train_size=0.80,
        random_state=269380
    )

    for name, classifier in zip(NAMES, CLASSIFIERS):
        print("-" * 64)
        print(name + " Classification Result")
        print("-" * 64)

        classifier.fit(X_train, y_train)
        score = classifier.score(X_test, y_test)

        print('%.2f' % (score))
        print("-" * 64 + "\n")


if __name__ == "__main__":
    main()
