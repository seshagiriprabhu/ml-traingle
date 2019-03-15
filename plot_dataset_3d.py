#!/usr/bin/python3.6
"""
A program to plot the triangle and right triangle datasets
"""
import os
import pandas as pnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# File related constants
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(APP_DIR, 'data')
TRIANGLE_FILE = os.path.join(DATA_DIR, "triangle.csv")
DATASET1_FILE = os.path.join(DATA_DIR, "dataset1.csv")
DATASET_FILES = [TRIANGLE_FILE, DATASET1_FILE]

for dataset in DATASET_FILES:
    DF = pnd.read_csv(dataset)

    THREEDEE = plt.figure().gca(projection='3d')
    THREEDEE.scatter(
        DF['side1'],
        DF['side2'],
        DF['side3'],
        c=DF['validity'],
        s=60,
        cmap='Accent'
    )
    THREEDEE.set_xlabel('Side 1')
    THREEDEE.set_ylabel('Side 2')
    THREEDEE.set_zlabel('Side 3')
    plt.show()
