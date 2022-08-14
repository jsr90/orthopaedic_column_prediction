Created by Jesús Sánchez Rodríguez
jsr90pro@gmail.com

The purpose of this project is to create a classifier based on
6 radiological column inputs, that classifies those inputs into
normal or abnormal column.

Link to the dataset: https://www.kaggle.com/datasets/jessanrod3/vertebralcolumndataset

Structure of the project:

data
    Dataset_spine.csv
    data.csv
models
    model.joblib
templates
    index.html
app.py
model_comparison.ipynb
variables-analysis-of-vertebral-column-dataset.ipynb
readme.txt

Running order:
    1. variables-analysis-of-vertebral-column-dataset.ipynb
    2. model_comparison.ipynb
    3. app.py

The first one remplaces outliers and NaN values withe the column mean.
The second one compares 6 differents models and take the more performant.
The last one creates the web app based on index.html.