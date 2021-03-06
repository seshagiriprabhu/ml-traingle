#!/usr/bin/python3.6
"""Utility file which contains constants required
for other programs in the project.
"""
import os
from numpy.random import permutation
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


# Classifier related constants
CLASSIFIER_NAMES = [
    "Nearest Neighbors",
    # "Linear SVM",
    # "RBF SVM",
    # "Gaussian Process",
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
    # GaussianProcessClassifier(1.0 * RBF(1.0), copy_X_train=False),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    MLPClassifier(
        activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
        beta_2=0.999, early_stopping=False, epsilon=1e-08,
        hidden_layer_sizes=(100,), learning_rate='constant',
        learning_rate_init=0.001, max_iter=200, momentum=0.9,
        nesterovs_momentum=True, power_t=0.5, random_state=None,
        shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
        verbose=False, warm_start=False
    ),
    AdaBoostClassifier(),
    GaussianNB(),
    QuadraticDiscriminantAnalysis()
]


# Directory related constants
APP_DIR = os.path.dirname(os.path.realpath(__file__))

# Dataset directory constants
DATA_DIR = os.path.join(APP_DIR, 'data')
EXP_DIR = os.path.join(DATA_DIR, 'experiment')
EXP1_DIR = os.path.join(DATA_DIR, 'experiment1')
EXP2_DIR = os.path.join(DATA_DIR, 'experiment2')
EXP3_DIR = os.path.join(DATA_DIR, 'experiment3')
EXP4_DIR = os.path.join(DATA_DIR, 'experiment4')
EXP5_DIR = os.path.join(DATA_DIR, 'experiment5')
EXP6_DIR = os.path.join(DATA_DIR, 'experiment6')
EXP7_DIR = os.path.join(DATA_DIR, 'experiment7')
EXP8_DIR = os.path.join(DATA_DIR, 'experiment8')

# Image directory constants
IMAGE_DIR = os.path.join(APP_DIR, 'image')
IMG_DIR = os.path.join(IMAGE_DIR, 'exp-image')
IMG1_DIR = os.path.join(IMAGE_DIR, 'exp1-image')
IMG2_DIR = os.path.join(IMAGE_DIR, 'exp2-image')
IMG3_DIR = os.path.join(IMAGE_DIR, 'exp3-image')
IMG4_DIR = os.path.join(IMAGE_DIR, 'exp4-image')
IMG5_DIR = os.path.join(IMAGE_DIR, 'exp5-image')
IMG6_DIR = os.path.join(IMAGE_DIR, 'exp6-image')
IMG7_DIR = os.path.join(IMAGE_DIR, 'exp7-image')
IMG8_DIR = os.path.join(IMAGE_DIR, 'exp8-image')

# First N: RT dataset
EXP_RT_DATASET1 = os.path.join(EXP_DIR, 'rt_dataset_s1.csv')
EXP_RT_DATASET2 = os.path.join(EXP_DIR, 'rt_dataset_u1.csv')
EXP_RT_FILE_NAMES = [EXP_RT_DATASET1, EXP_RT_DATASET2]

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
EXP6_RT_DATASET6 = os.path.join(EXP6_DIR, "rt_dataset6.csv")
EXP6_RT_FILE_NAMES = [
    EXP6_RT_DATASET1, EXP6_RT_DATASET2,
    EXP6_RT_DATASET3, EXP6_RT_DATASET4,
    EXP6_RT_DATASET5, EXP6_RT_DATASET6
]

# Experiment 7: Triangle dataset constants
EXP7_T_DATASET1 = os.path.join(EXP7_DIR, "t_dataset1.csv")
EXP7_T_DATASET2 = os.path.join(EXP7_DIR, "t_dataset2.csv")
EXP7_T_DATASET3 = os.path.join(EXP7_DIR, "t_dataset3.csv")
EXP7_T_FILE_NAMES = [
    EXP7_T_DATASET1, EXP7_T_DATASET2, EXP7_T_DATASET3
]

# Experiment 7: Right angle triangle dataset constants
EXP7_RT_DATASET1 = os.path.join(EXP7_DIR, "rt_dataset1.csv")
EXP7_RT_DATASET2 = os.path.join(EXP7_DIR, "rt_dataset2.csv")
EXP7_RT_DATASET3 = os.path.join(EXP7_DIR, "rt_dataset3.csv")
EXP7_RT_DATASET4 = os.path.join(EXP7_DIR, "rt_dataset4.csv")
EXP7_RT_DATASET5 = os.path.join(EXP7_DIR, "rt_dataset5.csv")
EXP7_RT_DATASET6 = os.path.join(EXP7_DIR, "rt_dataset6.csv")
EXP7_RT_FILE_NAMES = [
    EXP7_RT_DATASET1, EXP7_RT_DATASET2,
    EXP7_RT_DATASET3, EXP7_RT_DATASET4,
    EXP7_RT_DATASET5, EXP7_RT_DATASET6
]

# Experiment 8: Triangle dataset constants
EXP8_T_DATASET1 = os.path.join(EXP8_DIR, "t_dataset1.csv")
EXP8_T_DATASET2 = os.path.join(EXP8_DIR, "t_dataset2.csv")
EXP8_T_DATASET3 = os.path.join(EXP8_DIR, "t_dataset3.csv")
EXP8_T_FILE_NAMES = [
    EXP8_T_DATASET1, EXP8_T_DATASET2, EXP8_T_DATASET3
]

# Experiment 8: Right angle triangle dataset constants
EXP8_RT_DATASET1 = os.path.join(EXP8_DIR, "rt_dataset_s1.csv")
EXP8_RT_DATASET2 = os.path.join(EXP8_DIR, "rt_dataset_s2.csv")
EXP8_RT_DATASET3 = os.path.join(EXP8_DIR, "rt_dataset_s3.csv")
EXP8_RT_DATASET4 = os.path.join(EXP8_DIR, "rt_dataset_s4.csv")
EXP8_RT_DATASET5 = os.path.join(EXP8_DIR, "rt_dataset_s5.csv")
EXP8_RT_DATASET6 = os.path.join(EXP8_DIR, "rt_dataset_s6.csv")
EXP8_RT_DATASET11 = os.path.join(EXP8_DIR, "rt_dataset_u1.csv")
EXP8_RT_DATASET12 = os.path.join(EXP8_DIR, "rt_dataset_u2.csv")
EXP8_RT_DATASET13 = os.path.join(EXP8_DIR, "rt_dataset_u3.csv")
EXP8_RT_DATASET14 = os.path.join(EXP8_DIR, "rt_dataset_u4.csv")
EXP8_RT_DATASET15 = os.path.join(EXP8_DIR, "rt_dataset_u5.csv")
EXP8_RT_DATASET16 = os.path.join(EXP8_DIR, "rt_dataset_u6.csv")
EXP8_RT_FILE_NAMES = [
    EXP8_RT_DATASET1, EXP8_RT_DATASET2,
    EXP8_RT_DATASET3, EXP8_RT_DATASET4,
    EXP8_RT_DATASET5, EXP8_RT_DATASET6,
    EXP8_RT_DATASET11, EXP8_RT_DATASET12,
    EXP8_RT_DATASET13, EXP8_RT_DATASET14,
    EXP8_RT_DATASET15, EXP8_RT_DATASET16
]

# First N: RT dataset
IMG_RT_IMAGE1 = os.path.join(IMG_DIR, "rt_image_s1.png")
IMG_RT_IMAGE2 = os.path.join(IMG_DIR, "rt_image_u1.png")
IMG_RT_FILES = [IMG_RT_IMAGE1, IMG_RT_IMAGE2]

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
IMG6_RT_IMAGE6 = os.path.join(IMG6_DIR, "rt_image6.png")
IMG6_RT_FILES = [
    IMG6_RT_IMAGE1, IMG6_RT_IMAGE2,
    IMG6_RT_IMAGE3, IMG6_RT_IMAGE4,
    IMG6_RT_IMAGE5, IMG6_RT_IMAGE6
]

# Experiment 7 related image file constants
IMG7_T_IMAGE1 = os.path.join(IMG7_DIR, "t_image1.png")
IMG7_T_IMAGE2 = os.path.join(IMG7_DIR, "t_image2.png")
IMG7_T_IMAGE3 = os.path.join(IMG7_DIR, "t_image3.png")
IMG7_T_FILES = [IMG7_T_IMAGE1, IMG7_T_IMAGE2, IMG7_T_IMAGE3]

IMG7_RT_IMAGE1 = os.path.join(IMG7_DIR, "rt_image1.png")
IMG7_RT_IMAGE2 = os.path.join(IMG7_DIR, "rt_image2.png")
IMG7_RT_IMAGE3 = os.path.join(IMG7_DIR, "rt_image3.png")
IMG7_RT_IMAGE4 = os.path.join(IMG7_DIR, "rt_image4.png")
IMG7_RT_IMAGE5 = os.path.join(IMG7_DIR, "rt_image5.png")
IMG7_RT_IMAGE6 = os.path.join(IMG7_DIR, "rt_image6.png")
IMG7_RT_FILES = [
    IMG7_RT_IMAGE1, IMG7_RT_IMAGE2,
    IMG7_RT_IMAGE3, IMG7_RT_IMAGE4,
    IMG7_RT_IMAGE5, IMG7_RT_IMAGE6
]

# Experiment 8 related image file constants
IMG8_T_IMAGE1 = os.path.join(IMG8_DIR, "t_image1.png")
IMG8_T_IMAGE2 = os.path.join(IMG8_DIR, "t_image2.png")
IMG8_T_IMAGE3 = os.path.join(IMG8_DIR, "t_image3.png")
IMG8_T_FILES = [IMG8_T_IMAGE1, IMG8_T_IMAGE2, IMG8_T_IMAGE3]

IMG8_RT_IMAGE1 = os.path.join(IMG8_DIR, "rt_image_s1.png")
IMG8_RT_IMAGE2 = os.path.join(IMG8_DIR, "rt_image_s2.png")
IMG8_RT_IMAGE3 = os.path.join(IMG8_DIR, "rt_image_s3.png")
IMG8_RT_IMAGE4 = os.path.join(IMG8_DIR, "rt_image_s4.png")
IMG8_RT_IMAGE5 = os.path.join(IMG8_DIR, "rt_image_s5.png")
IMG8_RT_IMAGE6 = os.path.join(IMG8_DIR, "rt_image_s6.png")
IMG8_RT_IMAGE11 = os.path.join(IMG8_DIR, "rt_image_u1.png")
IMG8_RT_IMAGE12 = os.path.join(IMG8_DIR, "rt_image_u2.png")
IMG8_RT_IMAGE13 = os.path.join(IMG8_DIR, "rt_image_u3.png")
IMG8_RT_IMAGE14 = os.path.join(IMG8_DIR, "rt_image_u4.png")
IMG8_RT_IMAGE15 = os.path.join(IMG8_DIR, "rt_image_u5.png")
IMG8_RT_IMAGE16 = os.path.join(IMG8_DIR, "rt_image_u6.png")
IMG8_RT_FILES = [
    IMG8_RT_IMAGE1, IMG8_RT_IMAGE2,
    IMG8_RT_IMAGE3, IMG8_RT_IMAGE4,
    IMG8_RT_IMAGE5, IMG8_RT_IMAGE6,
    IMG8_RT_IMAGE11, IMG8_RT_IMAGE12,
    IMG8_RT_IMAGE13, IMG8_RT_IMAGE14,
    IMG8_RT_IMAGE15, IMG8_RT_IMAGE16,
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
RT_LABEL6 = [
    'side1^2', 'side2^2', 'side3^2',
    'side1^2+side2^2', 'side1^2+side3^2',
    'side2^2+side3^2', 'validity'
]
RT_LABELS = [
    RT_LABEL1, RT_LABEL2, RT_LABEL3,
    RT_LABEL4, RT_LABEL5, RT_LABEL6
]


DATASET_T_FILES = [
    EXP1_T_FILE_NAMES, EXP2_T_FILE_NAMES, EXP3_T_FILE_NAMES,
    EXP4_T_FILE_NAMES, EXP5_T_FILE_NAMES, EXP6_T_FILE_NAMES,
    EXP7_T_FILE_NAMES, EXP8_T_FILE_NAMES
]

DATASET_RT_FILES = [
    EXP2_RT_FILE_NAMES, EXP3_RT_FILE_NAMES, EXP4_RT_FILE_NAMES,
    EXP5_RT_FILE_NAMES, EXP6_RT_FILE_NAMES, EXP7_RT_FILE_NAMES,
    EXP8_RT_FILE_NAMES, EXP_RT_FILE_NAMES
]

IMAGE_T_FILES = [
    IMG1_T_FILES, IMG2_T_FILES, IMG3_T_FILES,
    IMG4_T_FILES, IMG5_T_FILES, IMG6_T_FILES,
    IMG7_T_FILES, IMG8_T_FILES
]

IMAGE_RT_FILES = [
    IMG2_RT_FILES, IMG3_RT_FILES, IMG4_RT_FILES,
    IMG5_RT_FILES, IMG6_RT_FILES, IMG7_RT_FILES,
    IMG8_RT_FILES, IMG_RT_FILES
]


def shuffle(a, b, c):
    """Shuffle the given points."""
    perm = permutation([a, b, c])
    return perm[0], perm[1], perm[2]


def floor_sqrt(x):
    """Floor of square root."""
    # Base cases
    if (x == 0 or x == 1):
        return x

    # Staring from 1, try all numbers until
    # i*i is greater than or equal to x.
    i = result = 1
    while result <= x:

        i += 1
        result = i * i

    return i - 1


def check_triangle(a, b, c):
    """Check the sum of the lengths of any two sides of
    a triangle is greater than the length of the third side.

    Parameters:
    (a, b, c) (int, int, int): Sides of a triangle.

    Returns:
    0/1: zero if not a triangle, one otherwise.
    """
    if a + b > c and b + c > a and a + c > b:
        return 1
    return 0


def check_right_triangle(a, b, c):
    """Check the RT property of given points
    using Pythagoras theorm.

    Parameters:
    (a, b, c) (int, int, int): Sides of a triangle.

    Returns:
    0/1: zero if not an RT triangle, one otherwise.
    """
    if a**2 + b**2 == c**2 or \
            a**2 + c**2 == b**2 or \
            c**2 + b**2 == a**2:
        return 1

    return 0
