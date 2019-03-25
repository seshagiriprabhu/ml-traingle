#!/usr/bin/python3.6
"""
A program to plot the triangle and right triangle datasets
"""
import os.path
import numpy as np
import pandas as pnd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D

# local python import
from utils import DATASET_T_FILES, DATASET_RT_FILES
from utils import IMAGE_T_FILES, IMAGE_RT_FILES

mpl.rcParams['legend.fontsize'] = 10

for count, T_FILES in enumerate(DATASET_T_FILES):
    for counter, dataset in enumerate(T_FILES):

        # No need to plot the graph if file already exists
        if os.path.isfile(IMAGE_T_FILES[count][counter]):
            print("File %s already exists!" % IMAGE_T_FILES[count][counter])
            continue

        DF = pnd.read_csv(dataset)

        THREEDEE = plt.figure(figsize=(19.20, 10.80)).gca(projection='3d')

        if counter == 0 or counter == 1:
            x, y, z = DF['side1'], DF['side2'], DF['side3']
            l1, l2, l3 = 'Side 1', 'Side 2', 'Side 3'
            title = "Normal Triangle"
        if counter == 2:
            x, y, z = DF['side1+side2'], DF['side1+side3'], DF['side2+side3']
            l1, l2, l3 = 'Side1 + Side 2', 'Side 1 + Side 3', 'Side 2 + Side 3'
            title = "Normal Triangle with Sum of Sides"
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
        plt.savefig(IMAGE_T_FILES[count][counter], dpi=200, bbox_inches='tight')
        print("Generated %s file" % IMAGE_T_FILES[count][counter])


for count, RT_FILES in enumerate(DATASET_RT_FILES):
    for counter, dataset in enumerate(RT_FILES):

        # If file already exists, no need to generate it again
        if os.path.isfile(IMAGE_RT_FILES[count][counter]):
            print("File %s already exists!" % IMAGE_RT_FILES[count][counter])
            continue

        # rt_dataset2.csv has long values which matplotlib cannot handle
        if counter == 2 and count < 1:
            continue

        DF = pnd.read_csv(dataset)
        THREEDEE = plt.figure(figsize=(19.20, 10.80)).gca(projection='3d')

        if counter == 0 or counter == 1:
            x, y, z = DF['side1'], DF['side2'], DF['side3']
            l1, l2, l3 = 'Side 1', 'Side 2', 'Side 3'
            title = "Right Triangle"
        elif counter == 2:
            x, y, z = DF['side1^2'], DF['side2^2'], DF['side3^2']
            l1, l2, l3 = 'Side1^2', 'Side2^2', 'Side3^2'
            title = "Right Triangle with Side Squares"
        elif counter == 3:
            x, y = DF['side1+side2'], DF['side1+side3']
            z = DF['side2+side3']
            l1, l2, l3 = 'Side1 + Side 2', 'Side1 + Side 3', 'Side 2 + Side3'
            title = "Right Triangle with Sum of Sides"
        else:
            x, y = DF['side1^2+side2^2'], DF['side1^2+side3^2']
            z = DF['side2^2+side3^2']
            l1, l2 = 'Side1^2 + Side 2^2', 'Side1^2 * Side 3^2'
            l3 = 'Side 2^2 + Side3^2'
            title = "Right Triangle with Sum of Side Squares"

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
        plt.savefig(IMAGE_RT_FILES[count][counter], dpi=200, bbox_inches='tight')
        print("Generated %s file" % IMAGE_RT_FILES[count][counter])
