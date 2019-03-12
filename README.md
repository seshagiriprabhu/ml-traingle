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
`scikit`, `numpy`, `pandas` are the third party python libraries used.
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
