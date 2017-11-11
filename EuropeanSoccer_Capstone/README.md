## European Soccer Capstone Project

My submission to udacity's machine learning engineer nanodegree course. The project analyses the prediction of matches in
European football, using the dataset at [European Soccer Database](https://www.kaggle.com/hugomathien/soccer).


### IPython Notebooks
* [Notebook for match outcome prediction](Notebook_Code/Match_outcome_prediction.ipynb)
* [Notebook for Players' clustering mini project](Notebook_Code/Players_clustering.ipynb)

Please note that as the data is huge, I would not advise running the whole notebook at once. Some of the code cells are merely for demonstrative purposes, i.e. they work if you run them but the code if executed will take a long time, especially in the sections on feature generation.

Most of the results were generated and saved into files; in order to make code cells independent. Even then, some code cells rely on dependencies from code cells above them, so if a code cells complains about a variable/import, please search and run for that variable/dependency.

### Data_Structures
This folder contains the .csv files with feature data; and also intermediate feature files. These files are used by the notebooks
to read data and analyze.

### Data
Raw data containing the soccer database data in the form of a zip file.

### Notebook_Code

* Contains the notebooks for the project.

* Contains the background python code that the notebooks use.

### Proposal

Folder containing the project proposal and related files.

### Final Report
Folder containing the final project report and related files.


## Acknowledgement
I would like to acknowledge the following sources:

* I used the code corresponding to the *visuals.py* file in both of the *Charity ML* and *Customer Segments* project.

* Code from the above mentioned projects to run classifiers, clustering and draw results.

* Some code from sklearn, for example the *the confusion matrix* code available online on sklearn to draw the confusion matrices.
