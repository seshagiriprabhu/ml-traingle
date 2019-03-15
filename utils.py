#!/usr/bin/python3.6
"""Utility file which contains constants required
for other files to run.
"""
import os

# File related constants
APP_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(APP_DIR, 'data')

T_DATASET1 = os.path.join(DATA_DIR, "t_dataset1.csv")
T_DATASET2 = os.path.join(DATA_DIR, "t_dataset2.csv")
T_DATASET3 = os.path.join(DATA_DIR, "t_dataset3.csv")
T_FILE_NAMES = [T_DATASET1, T_DATASET2, T_DATASET3]

RT_DATASET1 = os.path.join(DATA_DIR, "rt_dataset1.csv")
RT_DATASET2 = os.path.join(DATA_DIR, "rt_dataset2.csv")
RT_DATASET3 = os.path.join(DATA_DIR, "rt_dataset3.csv")
RT_DATASET4 = os.path.join(DATA_DIR, "rt_dataset4.csv")
RT_DATASET5 = os.path.join(DATA_DIR, "rt_dataset5.csv")
RT_FILE_NAMES = [
    RT_DATASET1, RT_DATASET2, RT_DATASET3, RT_DATASET4, RT_DATASET5
]

# Normal triangle dataset related constants
T_LABEL1 = ['side1', 'side2', 'side3', 'validity']
T_LABEL2 = [
    'side1', 'side2', 'side3', 'side1+side2', 'side1+side3',
    'side2+side3', 'validity'
]
T_LABEL3 = ['side1+side2', 'side1+side3', 'side2+side3', 'validity']
T_LABELS = [T_LABEL1, T_LABEL2, T_LABEL3]

# Right triangle related constants
RT_LABEL1 = ['side1', 'side2', 'side3', 'validity']
RT_LABEL2 = ['side1', 'side2', 'side3', 'side12', 'side22', 'side32', 'validity']
RT_LABEL3 = ['side12', 'side22', 'side32', 'validity']
RT_LABEL4 = ['side1+side2', 'side1+side3', 'side2+side3', 'validity']
RT_LABEL5 = ['side12+side22', 'side12+side32', 'side22+side32', 'validity']
RT_LABELS = [RT_LABEL1, RT_LABEL2, RT_LABEL3, RT_LABEL4, RT_LABEL5]
