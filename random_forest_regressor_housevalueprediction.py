# -*- coding: utf-8 -*-
"""Random Forest Regressor-HouseValuePrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_-wYK5d01kNqI79iCms5hdkqw_AmLB9f
"""

import numpy as np
import sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import os
import matplotlib.pyplot as plt
import pandas as pd
import tarfile
import urllib

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

fetch_housing_data()
housing = load_housing_data()
# housing.info()
# housing["ocean_proximity"].value_counts()
housing = housing.dropna()
le = preprocessing.LabelEncoder()
housing['ocean_proximity'] = le.fit_transform(housing['ocean_proximity'])
# housing = sklearn.preprocessing.normalize(housing)

predict = "median_house_value"
x = np.array(housing.drop([predict], 1))
y = np.array(housing[predict])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=42)

rfReg = RandomForestRegressor()
rfReg.fit(x_train, y_train)

rfReg.score(x_test, y_test)

predictions = rfReg.predict(x_test)

for x in range(20):
    print('predictions: ', predictions[x], 'Actual: ', y_test[x])