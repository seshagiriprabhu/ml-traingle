#!/usr/bin/python3.6
"""
A program to plot the triangle and right triangle datasets
"""
import pandas as pnd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# local python import
from utils import T_DATASET1, T_DATASET3
from utils import RT_DATASET1, RT_DATASET3, RT_DATASET5
from utils import IMAGE_FILES


DATASET_FILES = [
    T_DATASET1, T_DATASET3,
    RT_DATASET1, RT_DATASET3, RT_DATASET5
]

for counter, dataset in enumerate(DATASET_FILES):
    DF = pnd.read_csv(dataset)

    THREEDEE = plt.figure(figsize=(19.20, 10.80)).gca(projection='3d')

    if counter == 0:
        x, y, z = DF['side1'], DF['side2'], DF['side3']
        l1, l2, l3 = 'Side 1', 'Side 2', 'Side 3'
        title = "Normal Triangle"
    elif counter == 1:
        x, y, z = DF['side1+side2'], DF['side1+side3'], DF['side2+side3']
        l1, l2, l3 = 'Side1 + Side 2', 'Side 1 + Side 3', 'Side 2 + Side 3'
        title = "Normal Triangle with Sum of Sides"
    elif counter == 2:
        x, y, z = DF['side1'], DF['side2'], DF['side3']
        l1, l2, l3 = 'Side 1', 'Side 2', 'Side 3'
        title = "Right Triangle"
    elif counter == 3:
        x, y, z = DF['side1^2'], DF['side2^2'], DF['side3^2']
        l1, l2, l3 = 'Side1^2', 'Side2^2', 'Side3^2'
        title = "Right Triangle with Side Squares"
    else:
        x, y = DF['side1^2+side2^2'], DF['side1^2+side3^2']
        z = DF['side2^2+side3^2']
        l1, l2 = 'Side1^2 + Side 2^2', 'Side1^2 * Side 3^2'
        l3 = 'Side 2^2 + Side3^2'
        title = "Right Triangle with Sum of Side Squares"

    THREEDEE.scatter(
        x, y, z,
        c=DF['validity'],
        s=60,
        cmap='Accent'
    )
    THREEDEE.set_title(title, fontsize=30)
    THREEDEE.set_xlabel(l1, fontsize=16)
    THREEDEE.set_ylabel(l2, fontsize=16)
    THREEDEE.set_zlabel(l3, fontsize=16)
    plt.savefig(IMAGE_FILES[counter], dpi=72, bbox_inches='tight')
