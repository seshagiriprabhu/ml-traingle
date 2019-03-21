# Classification of traingles using ML classifiers
The code uses the below given classifers to test their accuracy on 
predicting traingles.

```python
Classifiers = [
    "Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
    "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
    "Naive Bayes", "QDA"
]
```

## Installing python dependences
`scikit`, `numpy`, `pandas`, `matplotlib` are the third party python libraries used.
```bash
pip install -r requirements.txt
```

## Run the program
The program `classifier_comparision.py` uses `training.csv` files which
contains 1000 entries, 80% of the entries are used for training and 20%
is for testing the classifier.
```bash
$ python classifier_comparision.py
```

## (Optional) Ubuntu dependences
`python-tk` is a debian package which is used by the `plot_dataset_3d.py` 
program to 3D plot the triangle and right triangle datasets.
```bash
sudo apt-get install python-tk
```

## Plotting datasets
`plot_dataset_3d.py` can be run to plot the triangle and right triangles.
```bash
python plot_dataset_3d_show.py
```
