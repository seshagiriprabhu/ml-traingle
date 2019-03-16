# Applying ML on Triangle Datasets

## Classifiers used
1. Nearest Neighbor (k=3)
2. Gaussian Process (1.0 * RBF(1.0))
3. Decision Tree (max_depth=5)
4. Random Forest(max_depth=5, n_estimators=10, max_features=1)
5. Multi-Layer Perceptron
```python
activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
beta_2=0.999, early_stopping=False, epsilon=1e-08,
hidden_layer_sizes=(30, 30, 30), learning_rate='constant',
learning_rate_init=0.001, max_iter=200, momentum=0.9,
nesterovs_momentum=True, power_t=0.5, random_state=None,
shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
verbose=False, warm_start=False
```
6. AdaBoost
7. Naive Bayes
8. QDA

This journal contains details about our various experiments to apply ML
on normal triangle and right triangle datasets which we have
generated using various properties.

## Experiment #1
Commit - [93ee58dfcbd037787a46cca226b4ebc799e20eaf](https://github.com/seshagiriprabhu/ml-traingle/tree/93ee58dfcbd037787a46cca226b4ebc799e20eaf)

1. Only normal triangles are generated. 
2. The sum of lengths of any two sides of a triangle
should be greater than the third side. 

### Dataset description
1. Triangle - [training.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/93ee58dfcbd037787a46cca226b4ebc799e20eaf/training.csv)
    * Attributes: (a, b, c, validity)

### Results
|                   |   T  |
| ----------------- | ---- |
| kNN               | 0.94 |
| Gaussian Process  | 0.53 |
| Decision Tree     | 0.76 |
| Random Forest     | 0.84 |
| MLP               | 0.97 |
| AdaBoost          | 0.79 |
| Naive Bayes       | 0.84 |
| QDA               | 0.84 |


## Experiment #2
Commit - [c294abe9dbfc52e06954863b8e8d6208814d6a01](https://github.com/seshagiriprabhu/ml-traingle/tree/c294abe9dbfc52e06954863b8e8d6208814d6a01)

Right triangles are generated based on the concept that if one side (`a`) of an RT
is odd, other sides can be generated by 
(a<sup>2</sup> - 1) / 2 and (a<sup>2</sup> + 1) / 2.

Right angle triangles are generated using the following rules:
1. Odd: If n is odd, then n, (n<sup>2</sup> - 1) / 2, (n<sup>2</sup> + 1) / 2
    1. `n` is `randint(100000)`
2. Right triangles can be validated by using the Pythagorus theorm: 
a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>
3. Invalid RTs are generated by randomly assigning `randint(100000)`
values to (a, b, c).

### Dataset description
1. Triangle - [training.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/2357d5fbd3eb4b6e9171e07f0a131e8e48f0167b/data/triangle.csv)
    * Attributes: (a, b, c, validity)

2. Right Triangle (RT 1) - [dataset1.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/2357d5fbd3eb4b6e9171e07f0a131e8e48f0167b/data/dataset1.csv)
    * Attributes: (a, b, c, validity)

3. Right Triangle (RT 2) - [dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/2357d5fbd3eb4b6e9171e07f0a131e8e48f0167b/data/dataset2.csv)
    * Attributes: (a, b, c, a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

4. Right Triangle (RT 3) - [dataset3.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/2357d5fbd3eb4b6e9171e07f0a131e8e48f0167b/data/dataset3.csv)
    * Attributes: (a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

### Results
|                   |  T   | RT 1 | RT 2 | RT 3 |
| ----------------- | ---- | ---- | ---- | ---- |
| kNN               | 0.70 | 1.00 | 0.99 | 1.00 |
| Gaussian Process  | 0.55 | 0.50 | 0.50 | 0.50 |
| Decision Tree     | 0.73 | 0.99 | 0.99 | 1.00 |
| Random Forest     | 0.76 | 1.00 | 0.99 | 1.00 |
| MLP               | 0.68 | 0.74 | 0.95 | 0.91 |
| AdaBoost          | 0.71 | 0.99 | 0.99 | 1.00 |
| Naive Bayes       | 0.69 | 1.00 | 0.94 | 0.96 |
| QDA               | 0.71 | 1.00 | 0.98 | 1.00 |

### Drawback of RT dataset
The RT datasets used in experiment #2 has the following pattern:
1. Difference between large two sides is 1
2. RT triangle numbers are much larger
3. RT triangle data is ordered
4. The b and c values in RT triangle are much closer


## Experiment #3
Commit - [b8db04c46a4b7574e2a02faf6722cb238dace759](https://github.com/seshagiriprabhu/ml-traingle/tree/b8db04c46a4b7574e2a02faf6722cb238dace759)

The right angle triangles generated in the experiment #2 are ordered (a < b < c)
1. To make it unordered, a, b and c are shuffled in the dataset.
2. Invalid RTs are generated by randomly assigning `randint(100000)`
values to (a, b, c).

### Dataset description
1. Triangle - [training.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/triangle.csv)
    * Attributes: (a, b, c, validity)

2. Right Triangle (RT 1) - [dataset1.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/dataset1.csv)
    * Attributes: (a, b, c, validity)

3. Right Triangle (RT 2) - [dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/dataset2.csv)
    * Attributes: (a, b, c, a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

4. Right Triangle (RT 3) - [dataset3.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/dataset3.csv)
    * Attributes: (a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

### Results
|                   |  T   | RT 1 | RT 2 | RT 3 |
| ----------------- | ---- | ---- | ---- | ---- |
| kNN               | 0.72 | 0.94 | 0.95 | 0.97 |
| Gaussian Process  | 0.51 | 0.96 | 0.64 | 0.62 |
| Decision Tree     | 0.70 | 0.94 | 0.94 | 0.95 |
| Random Forest     | 0.74 | 0.95 | 0.94 | 0.95 |
| MLP               | 0.68 | 0.80 | 0.94 | 0.95 |
| AdaBoost          | 0.72 | 0.94 | 0.94 | 0.94 |
| Naive Bayes       | 0.69 | 0.78 | 0.75 | 0.78 |
| QDA               | 0.71 | 0.78 | 1.00 | 1.00 |

### Drawback of RT dataset
The RT datasets used in experiment #3 has the following pattern
1. Difference between large two sides is 1
2. RT triangle numbers are much larger


## Experiment #4
Commit - [efa03e9ba7f0e7a4289a7acf289b33f3eb4ee3f9](https://github.com/seshagiriprabhu/ml-traingle/tree/efa03e9ba7f0e7a4289a7acf289b33f3eb4ee3f9)

Right angle triangles are generated using the following rules:
1. Odd: If n is odd, then n, (n<sup>2</sup> - 1) / 2, (n<sup>2</sup> + 1) / 2
    1. `n` is `randint(100000)`
2. even: If n is even, then n, (n<sup>2</sup> / 4) - 1, (n<sup>2</sup> / 4) + 1
    1. `n` is `randint(100000)`
3. (a, b, c) are shuffled in-order to make the dataset unordered.
4. Invalid RTs are generated by randomly assigning `randint(100000)` 
values to (a, b, c).

### Dataset description
1. Triangle - [training.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/triangle.csv)
    * Attributes: (a, b, c, validity)

2. Right Triangle (RT 1) - [dataset1.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/dataset1.csv)
    * Attributes: (a, b, c, validity)

3. Right Triangle (RT 2) - [dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/dataset2.csv)
    * Attributes: (a, b, c, a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

4. Right Triangle (RT 3) - [dataset3.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b8db04c46a4b7574e2a02faf6722cb238dace759/data/dataset3.csv)
    * Attributes: (a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

### Results
|                   |  T   | RT 1 | RT 2 | RT 3 |
| ----------------- | ---- | ---- | ---- | ---- |
| kNN               | 0.70 | 0.94 | 0.94 | 0.96 |
| Gaussian Process  | 0.45 | 0.56 | 0.61 | 0.61 |
| Decision Tree     | 0.74 | 0.94 | 0.96 | 0.93 |
| Random Forest     | 0.73 | 0.94 | 0.96 | 0.94 |
| MLP               | 0.68 | 0.77 | 0.76 | 0.52 |
| AdaBoost          | 0.68 | 0.92 | 0.95 | 0.94 |
| Naive Bayes       | 0.74 | 0.88 | 0.93 | 0.92 |
| QDA               | 0.74 | 0.88 | 1.00 | 1.00 |

### Drawbacks of RT Dataset
The RT datasets used in the experiment #4 has the following pattern:
1. Difference between the largest sides of an RT is either 1/2.


## Experiment #5
Commit - [b85f9c61d168a56878addcc8f7f8b66f2d4a2d2b](https://github.com/seshagiriprabhu/ml-traingle/tree/b85f9c61d168a56878addcc8f7f8b66f2d4a2d2b)

Right angle triangles are generated using the following rules:
1. Odd: If n is odd, then n, (n<sup>2</sup> - 1) / 2, (n<sup>2</sup> + 1) / 2
    1. `n` is `randint(100)`
2. even: If n is even, then n, (n<sup>2</sup> / 4) - 1, (n<sup>2</sup> / 4) + 1
    1. `n` is `randint(100)`
3. (a, b, c) is multiplied by a `randint(99)` constant.
4. (a, b, c) are shuffled in-order to make the dataset unordered.
5. Invalid RTs are generated by randomly by adding `randint(99)` constant
to (a, b, c).

### Dataset description
1. Triangle (T) - [training.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b85f9c61d168a56878addcc8f7f8b66f2d4a2d2b/data/training.csv)
    * Attributes: (a, b, c, validity)

2. Right Triangle (RT 1) - [dataset1.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b85f9c61d168a56878addcc8f7f8b66f2d4a2d2b/data/dataset1.csv)
    * Attributes: (a, b, c, validity)

3. Right Triangle (RT 2) - [dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b85f9c61d168a56878addcc8f7f8b66f2d4a2d2b/data/dataset2.csv)
    * Attributes: (a, b, c, a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

4. Right Triangle (RT 3) - [dataset3.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/b85f9c61d168a56878addcc8f7f8b66f2d4a2d2b/data/dataset3.csv)
    * Attributes: (a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

### Results
|                   |  T   | RT 1 | RT 2 | RT 3 |
| ---               | ---- | ---- | ---- | ---- |
| kNN               | 0.66 | 0.80 | 0.77 | 0.79 |
| Gaussian Process  | 0.47 | 0.47 | 0.53 | 0.55 |
| Decision Tree     | 0.67 | 0.77 | 0.77 | 0.74 |
| Random Forest     | 0.70 | 0.83 | 0.78 | 0.82 |
| MLP               | 0.67 | 0.68 | 0.58 | 0.63 |
| AdaBoost          | 0.69 | 0.75 | 0.81 | 0.84 |
| Naive Bayes       | 0.71 | 0.63 | 0.68 | 0.64 |
| QDA               | 0.71 | 0.71 | 0.80 | 0.72 |

### Special Notes about this RT dataset
1. If (a, b, c) values are high, then the accuracy of classifiers
are higher than the above mentioned results of Experiment #5.
2. So small values are chosen for constant (`randint(99)`) and
`n` (`randint(1000)`


## Experiment #6
Commit - [95cd61d7ef3208b780c2176d0e1f794bef238399](https://github.com/seshagiriprabhu/ml-traingle/tree/95cd61d7ef3208b780c2176d0e1f794bef238399)

Triangle and Right triangle is generated the same way as in Experiment #5.
New datasets are added with different attributes.
3D plots of some of the datasets are also generated using `matplot`.

### Dataset description
1. Triangle (T 1) - [t_dataset1.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/t_dataset1.csv)
    * Attributes: (a, b, c, validity)
    * 3D plot - [t_image1.png](https://github.com/seshagiriprabhu/ml-traingle/blob/32dacc8d4da4ef33dce1ff44f5827037ac3d1826/image/t_image1.png)

2. Triangle (T 2) - [t_dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/t_dataset2.csv)
    * Attributes: (a, b, c, a + b, a + c, b + c, validity)

3. Triangle (T 2) - [t_dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/t_dataset3.csv)
    * Attributes: (a + b, a + c, b + c, validity)
    * 3D plot - [t_image2.png](https://github.com/seshagiriprabhu/ml-traingle/blob/32dacc8d4da4ef33dce1ff44f5827037ac3d1826/image/t_image2.png)

4. Right Triangle (RT 1) - [rt_dataset1.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/rt_dataset1.csv)
    * Attributes: (a, b, c, validity)
    * 3D plot - [rt_image1.png](https://github.com/seshagiriprabhu/ml-traingle/blob/32dacc8d4da4ef33dce1ff44f5827037ac3d1826/image/rt_image1.png)

5. Right Triangle (RT 2) - [rt_dataset2.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/rt_dataset2.csv)
    * Attributes: (a, b, c, a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)

6. Right Triangle (RT 3) - [rt_dataset3.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/rt_dataset3.csv)
    * Attributes: (a<sup>2</sup>, b<sup>2</sup>, c<sup>2</sup>, validity)
    * 3D plot - [rt_image2.png](https://github.com/seshagiriprabhu/ml-traingle/blob/32dacc8d4da4ef33dce1ff44f5827037ac3d1826/image/rt_image2.png)

7. Right Triangle (RT 4) - [rt_dataset4.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/rt_dataset4.csv)
    * Attributes: (a + b, a + c, b + c, validity)
    * 3D plot - [rt_image3.png](https://github.com/seshagiriprabhu/ml-traingle/blob/0e4c35c854223df64c1e801103747a1149fe798e/image/rt_image3.png)

8. Right Triangle (RT 5) - [rt_dataset4.csv](https://github.com/seshagiriprabhu/ml-traingle/blob/95cd61d7ef3208b780c2176d0e1f794bef238399/data/rt_dataset5.csv)
    * Attributes: (a<sup>2</sup> + b<sup>2</sup>, a<sup>2</sup> + c<sup>2</sup>, b<sup>2</sup> + c<sup>2</sup>, validity)
    * 3D plot - [rt_image4.png](https://github.com/seshagiriprabhu/ml-traingle/blob/0e4c35c854223df64c1e801103747a1149fe798e/image/rt_image4.png)

### Results
|                   | T 1  | T 2  | T 3  | RT 1 | RT 2 | RT 3 | RT 4 | RT 5 |
| ----------------- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| kNN               | 0.95 | 0.94 | 0.89 | 0.82 | 0.74 | 0.76 | 0.79 | 0.73 | 
| Gaussian Process  | 0.44 | 0.46 | 0.53 | 0.54 | 0.53 | 0.56 | 0.55 | 0.56 |
| Decision Tree     | 0.82 | 0.86 | 0.77 | 0.81 | 0.77 | 0.81 | 0.72 | 0.66 |
| Random Forest     | 0.82 | 0.84 | 0.80 | 0.83 | 0.79 | 0.81 | 0.69 | 0.66 |
| MLP               | 0.98 | 0.68 | 0.93 | 0.69 | 0.55 | 0.69 | 0.78 | 0.61 |
| AdaBoost          | 0.77 | 0.90 | 0.61 | 0.88 | 0.81 | 0.79 | 0.72 | 0.69 |
| Naive Bayes       | 0.84 | 0.73 | 0.68 | 0.61 | 0.66 | 0.62 | 0.60 | 0.58 |
| QDA               | 0.85 | 0.56 | 0.80 | 0.74 | 0.78 | 0.75 | 0.72 | 0.99 |