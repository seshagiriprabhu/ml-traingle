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

## Install python dependences
`scikit`, `numpy`, `pandas`, `matplotlib` are the third party python libraries used.
```bash
pip install -r requirements.txt
```

## Run the program
The program `classifier_comparision_t.py` uses triangle dataset files 
(`t_dataset[1-3].py`) which contains 1000 entries upto experiment 6 and 
1 million for experiment 7, 80% of the entries are used for training and
20% is for testing the classifier.
```bash
$ python classifier_comparision_t.py
```

The program `classifier_comparision_rt.py` uses right triangle dataset files 
(`rt_dataset[1-3].py`) which contains 1000 entries upto experiment 6 and 
1 million for experiment 7, 80% of the entries are used for training and
20% is for testing the classifier.
```bash
$ python classifier_comparision_rt.py
```

## (Optional) Ubuntu dependences
`python-tk` is a debian package which is used by the `plot_dataset_3d.py` 
program to 3D plot the triangle and right triangle datasets.
```bash
sudo apt-get install python-tk
```

## Plot datasets
`plot_dataset_3d_show.py` can be used to plot 3D datasets
of all the experiments. `python-tk` is required to be installed in-order
to display the screen in which the `matplot3d` displays the plot.
```bash
python plot_dataset_3d_show.py
```
