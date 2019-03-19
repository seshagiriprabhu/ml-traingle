#!/usr/bin/python3.6
"""
A program which classifies a given dataset using
various classic ML classifiers.
"""
from __future__ import print_function

import pandas as pnd
# from sklearn.svm import SVC
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

# local python import
from utils import EXP6_T_FILE_NAMES, EXP6_RT_FILE_NAMES
from utils import T_LABELS, RT_LABELS

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


def main():
    """Main function."""

    testing_dataset = []
    for filename in EXP6_T_FILE_NAMES:
        testing_dataset.append(pnd.read_csv(filename))

    for filename in EXP6_RT_FILE_NAMES:
        testing_dataset.append(pnd.read_csv(filename))

    for counter in range(len(testing_dataset)):
        # Splitting the columns into data and target
        ds_x = testing_dataset[counter].iloc[:, :-1]
        target = testing_dataset[counter].loc[:, 'validity']
        kwargs = dict(test_size=0.2, train_size=0.8, random_state=269380)
        X_train, X_test, y_train, y_test = train_test_split(ds_x, target, **kwargs)

        print("-" * 40)
        if counter < 3:
            print("Dataset: Normal Triangle")
            print(T_LABELS[counter])
        else:
            print("Dataset: Right Angle Triangle")
            print(RT_LABELS[counter - 3])
        print("-" * 40)

        for name, classifier in zip(NAMES, CLASSIFIERS):
            classifier.fit(X_train, y_train)
            score = classifier.score(X_test, y_test)
            print(name + ": %.2f" % (score))

        print("-" * 40 + "\n")


if __name__ == "__main__":
    main()
