#!/usr/bin/python3.6
"""
A program to plot the triangle and right triangle datasets
"""
import numpy as np
import pandas as pnd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D

# local python import
from utils import DATASET_T_FILES, DATASET_RT_FILES

mpl.rcParams['legend.fontsize'] = 10

for count, T_FILES in enumerate(DATASET_T_FILES):
    if count < 4 or count > 5:
        continue

    for counter, dataset in enumerate(T_FILES):
        if counter > 0:
            continue

        DF = pnd.read_csv(dataset)

        THREEDEE = plt.figure(figsize=(19.20, 10.80)).gca(projection='3d')

        if counter == 0 or counter == 1:
            x, y, z = DF['side1'], DF['side2'], DF['side3']
            l1, l2, l3 = 'Side 1', 'Side 2', 'Side 3'
            title = "Normal Triangle Experiment #" + str(count + 1)

        colors = np.where(DF['validity'] == 1, 'red', 'blue')

        THREEDEE.scatter(
            x, y, z,
            c=colors,
            s=60,
            alpha=0.5, edgecolors='none',
            label='Valid Triangle'
        )
        THREEDEE.set_title(title, fontsize=30)
        THREEDEE.set_xlabel(l1, fontsize=16)
        THREEDEE.set_ylabel(l2, fontsize=16)
        THREEDEE.set_zlabel(l3, fontsize=16)
        red_patch = mpatches.Patch(color='red', label='Valid Triangle')
        blue_patch = mpatches.Patch(color='blue', label='Invalid Triangle')
        THREEDEE.legend(handles=[red_patch, blue_patch])
        plt.show()
        plt.close()


for count, RT_FILES in enumerate(DATASET_RT_FILES):
    if count < 3 or count == 5:
        continue

    for counter, dataset in enumerate(RT_FILES):
        if counter > 0:
            continue

        DF = pnd.read_csv(dataset)
        THREEDEE = plt.figure(figsize=(19.20, 10.80)).gca(projection='3d')

        x, y, z = DF['side1'], DF['side2'], DF['side3']
        l1, l2, l3 = 'Side 1', 'Side 2', 'Side 3'
        if count < 6:
            title = "Right Triangle Experiment #" + str(count + 1)
        else:
            title = "First 1000 valid right triangles"

        colors = np.where(DF['validity'] == 1, 'red', 'blue')
        THREEDEE.scatter(
            x, y, z,
            c=colors,
            s=60,
            alpha=0.5, edgecolors='none'
        )
        THREEDEE.set_title(title, fontsize=30)
        THREEDEE.set_xlabel(l1, fontsize=16)
        THREEDEE.set_ylabel(l2, fontsize=16)
        THREEDEE.set_zlabel(l3, fontsize=16)
        red_patch = mpatches.Patch(
            color='red',
            label='Valid Right Angle Triangle'
        )
        blue_patch = mpatches.Patch(
            color='blue',
            label='Invalid Right Angle Triangle'
        )
        THREEDEE.legend(handles=[red_patch, blue_patch])
        plt.show()
        plt.close()
