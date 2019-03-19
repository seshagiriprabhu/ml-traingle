#!/usr/bin/python3.6
"""Utility file which contains constants required
for other files to run.
"""
import os

# Directory related constants
APP_DIR = os.path.dirname(os.path.realpath(__file__))

# Dataset directory constants
DATA_DIR = os.path.join(APP_DIR, 'data')
EXP1_DIR = os.path.join(DATA_DIR, 'experiment1')
EXP2_DIR = os.path.join(DATA_DIR, 'experiment2')
EXP3_DIR = os.path.join(DATA_DIR, 'experiment3')
EXP4_DIR = os.path.join(DATA_DIR, 'experiment4')
EXP5_DIR = os.path.join(DATA_DIR, 'experiment5')

# Image directory constants
IMAGE_DIR = os.path.join(APP_DIR, 'image')
IMG1_DIR = os.path.join(IMAGE_DIR, 'exp1-image')
IMG2_DIR = os.path.join(IMAGE_DIR, 'exp2-image')
IMG3_DIR = os.path.join(IMAGE_DIR, 'exp3-image')
IMG4_DIR = os.path.join(IMAGE_DIR, 'exp4-image')
IMG5_DIR = os.path.join(IMAGE_DIR, 'exp5-image')
IMG6_DIR = os.path.join(IMAGE_DIR, 'exp6-image')


# Experiment 1: Triangle dataset constants
EXP1_T_DATASET = os.path.join(EXP1_DIR, 'triangle.csv')
EXP1_T_FILE_NAMES = [EXP1_T_DATASET]

# Experiment 2: Triangle dataset constants
EXP2_T_DATASET = os.path.join(EXP2_DIR, 'triangle.csv')
EXP2_T_FILE_NAMES = [EXP2_T_DATASET]

# Experiment 2: Right angle triangle dataset constants
EXP2_RT_DATASET1 = os.path.join(EXP2_DIR, 'rt_dataset1.csv')
EXP2_RT_DATASET2 = os.path.join(EXP2_DIR, 'rt_dataset2.csv')
EXP2_RT_DATASET3 = os.path.join(EXP2_DIR, 'rt_dataset3.csv')
EXP2_RT_FILE_NAMES = [
    EXP2_RT_DATASET1, EXP2_RT_DATASET2, EXP2_RT_DATASET3
]

# Experiment 3: Triangle dataset constants
EXP3_T_DATASET = os.path.join(EXP3_DIR, 'triangle.csv')
EXP3_T_FILE_NAMES = [EXP3_T_DATASET]

# Experiment 3: Right angle triangle dataset constants
EXP3_RT_DATASET1 = os.path.join(EXP3_DIR, 'rt_dataset1.csv')
EXP3_RT_DATASET2 = os.path.join(EXP3_DIR, 'rt_dataset2.csv')
EXP3_RT_DATASET3 = os.path.join(EXP3_DIR, 'rt_dataset3.csv')
EXP3_RT_FILE_NAMES = [
    EXP3_RT_DATASET1, EXP3_RT_DATASET2, EXP3_RT_DATASET3
]

# Experiment 4: Triangle dataset constants
EXP4_T_DATASET = os.path.join(EXP4_DIR, 'triangle.csv')
EXP4_T_FILE_NAMES = [EXP4_T_DATASET]

# Experiment 4: Right angle triangle dataset constants
EXP4_RT_DATASET1 = os.path.join(EXP4_DIR, 'rt_dataset1.csv')
EXP4_RT_DATASET2 = os.path.join(EXP4_DIR, 'rt_dataset2.csv')
EXP4_RT_DATASET3 = os.path.join(EXP4_DIR, 'rt_dataset3.csv')
EXP4_RT_FILE_NAMES = [
    EXP4_RT_DATASET1, EXP4_RT_DATASET2, EXP4_RT_DATASET3
]

# Experiment 5: Triangle dataset constants
EXP5_T_DATASET = os.path.join(EXP5_DIR, 'triangle.csv')
EXP5_T_FILE_NAMES = [EXP5_T_DATASET]

# Experiment 5: Right angle triangle dataset constants
EXP5_RT_DATASET1 = os.path.join(EXP5_DIR, 'rt_dataset1.csv')
EXP5_RT_DATASET2 = os.path.join(EXP5_DIR, 'rt_dataset2.csv')
EXP5_RT_DATASET3 = os.path.join(EXP5_DIR, 'rt_dataset3.csv')
EXP5_RT_FILE_NAMES = [
    EXP5_RT_DATASET1, EXP5_RT_DATASET2, EXP5_RT_DATASET3
]

# Experiment 6: Triangle dataset constants
EXP6_DIR = os.path.join(DATA_DIR, 'experiment6')
EXP6_T_DATASET1 = os.path.join(EXP6_DIR, "t_dataset1.csv")
EXP6_T_DATASET2 = os.path.join(EXP6_DIR, "t_dataset2.csv")
EXP6_T_DATASET3 = os.path.join(EXP6_DIR, "t_dataset3.csv")
EXP6_T_FILE_NAMES = [
    EXP6_T_DATASET1, EXP6_T_DATASET2, EXP6_T_DATASET3
]

# Experiment 6: Right angle triangle dataset constants
EXP6_RT_DATASET1 = os.path.join(EXP6_DIR, "rt_dataset1.csv")
EXP6_RT_DATASET2 = os.path.join(EXP6_DIR, "rt_dataset2.csv")
EXP6_RT_DATASET3 = os.path.join(EXP6_DIR, "rt_dataset3.csv")
EXP6_RT_DATASET4 = os.path.join(EXP6_DIR, "rt_dataset4.csv")
EXP6_RT_DATASET5 = os.path.join(EXP6_DIR, "rt_dataset5.csv")
EXP6_RT_FILE_NAMES = [
    EXP6_RT_DATASET1, EXP6_RT_DATASET2,
    EXP6_RT_DATASET3, EXP6_RT_DATASET4,
    EXP6_RT_DATASET5
]


# Experiment 1 related image file constants
IMG1_T_IMAGE1 = os.path.join(IMG1_DIR, "t_image1.png")
IMG1_T_FILES = [IMG1_T_IMAGE1]

# Experiment 2 related image file constants
IMG2_T_IMAGE1 = os.path.join(IMG2_DIR, "t_image1.png")
IMG2_T_FILES = [IMG2_T_IMAGE1]

IMG2_RT_IMAGE1 = os.path.join(IMG2_DIR, "rt_image1.png")
IMG2_RT_IMAGE2 = os.path.join(IMG2_DIR, "rt_image2.png")
IMG2_RT_IMAGE3 = os.path.join(IMG2_DIR, "rt_image3.png")
IMG2_RT_FILES = [
    IMG2_RT_IMAGE1, IMG2_RT_IMAGE2, IMG2_RT_IMAGE3
]

# Experiment 3 related image file constants
IMG3_T_IMAGE1 = os.path.join(IMG3_DIR, "t_image1.png")
IMG3_T_FILES = [IMG3_T_IMAGE1]

IMG3_RT_IMAGE1 = os.path.join(IMG3_DIR, "rt_image1.png")
IMG3_RT_IMAGE2 = os.path.join(IMG3_DIR, "rt_image2.png")
IMG3_RT_IMAGE3 = os.path.join(IMG3_DIR, "rt_image3.png")
IMG3_RT_FILES = [
    IMG3_RT_IMAGE1, IMG3_RT_IMAGE2, IMG3_RT_IMAGE3
]

# Experiment 4 related image file constants
IMG4_T_IMAGE1 = os.path.join(IMG4_DIR, "t_image1.png")
IMG4_T_FILES = [IMG4_T_IMAGE1]

IMG4_RT_IMAGE1 = os.path.join(IMG4_DIR, "rt_image1.png")
IMG4_RT_IMAGE2 = os.path.join(IMG4_DIR, "rt_image2.png")
IMG4_RT_IMAGE3 = os.path.join(IMG4_DIR, "rt_image3.png")
IMG4_RT_FILES = [
    IMG4_RT_IMAGE1, IMG4_RT_IMAGE2, IMG4_RT_IMAGE3
]

# Experiment 5 related image file constants
IMG5_T_IMAGE1 = os.path.join(IMG5_DIR, "t_image1.png")
IMG5_T_FILES = [IMG5_T_IMAGE1]

IMG5_RT_IMAGE1 = os.path.join(IMG5_DIR, "rt_image1.png")
IMG5_RT_IMAGE2 = os.path.join(IMG5_DIR, "rt_image2.png")
IMG5_RT_IMAGE3 = os.path.join(IMG5_DIR, "rt_image3.png")
IMG5_RT_FILES = [
    IMG5_RT_IMAGE1, IMG5_RT_IMAGE2, IMG5_RT_IMAGE3
]

# Experiment 6 related image file constants
IMG6_T_IMAGE1 = os.path.join(IMG6_DIR, "t_image1.png")
IMG6_T_IMAGE2 = os.path.join(IMG6_DIR, "t_image2.png")
IMG6_T_IMAGE3 = os.path.join(IMG6_DIR, "t_image3.png")
IMG6_T_FILES = [IMG6_T_IMAGE1, IMG6_T_IMAGE2, IMG6_T_IMAGE3]

IMG6_RT_IMAGE1 = os.path.join(IMG6_DIR, "rt_image1.png")
IMG6_RT_IMAGE2 = os.path.join(IMG6_DIR, "rt_image2.png")
IMG6_RT_IMAGE3 = os.path.join(IMG6_DIR, "rt_image3.png")
IMG6_RT_IMAGE4 = os.path.join(IMG6_DIR, "rt_image4.png")
IMG6_RT_IMAGE5 = os.path.join(IMG6_DIR, "rt_image5.png")
IMG6_RT_FILES = [
    IMG6_RT_IMAGE1, IMG6_RT_IMAGE2,
    IMG6_RT_IMAGE3, IMG6_RT_IMAGE4,
    IMG6_RT_IMAGE5
]


# Label constants
T_LABEL1 = ['side1', 'side2', 'side3', 'validity']
T_LABEL2 = [
    'side1', 'side2', 'side3', 'side1+side2', 'side1+side3',
    'side2+side3', 'validity'
]
T_LABEL3 = ['side1+side2', 'side1+side3', 'side2+side3', 'validity']
T_LABELS = [T_LABEL1, T_LABEL2, T_LABEL3]

RT_LABEL1 = ['side1', 'side2', 'side3', 'validity']
RT_LABEL2 = ['side1', 'side2', 'side3', 'side1^2', 'side2^2', 'side3^2', 'validity']
RT_LABEL3 = ['side1^2', 'side2^2', 'side3^2', 'validity']
RT_LABEL4 = ['side1+side2', 'side1+side3', 'side2+side3', 'validity']
RT_LABEL5 = ['side1^2+side2^2', 'side1^2+side3^2', 'side2^2+side3^2', 'validity']
RT_LABELS = [RT_LABEL1, RT_LABEL2, RT_LABEL3, RT_LABEL4, RT_LABEL5]
