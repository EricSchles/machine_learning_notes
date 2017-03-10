import matplotlib.pyplot as plt
import statsmodels.api as sm
import requests
import lxml.html
import math
import pandas as pd
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

def is_nan(obj):
    if type(obj) == type(float()):
        return math.isnan(obj)
    else:
        return False

def sex_mapping(x):
    if x["Sex"] == "male":
        return 0
    if x["Sex"] == "female":
        return 1

def pclass_mapping(x):
    if x["PClass"] == "1st":
        return 1
    if x["PClass"] == "2nd":
        return 2
    if x["PClass"] == "3rd":
        return 3
    
df = pd.read_csv("Titanic.csv")
df["Sex"] = df.apply(sex_mapping, axis=1)
df["PClass"] = df.apply(pclass_mapping, axis=1)

X = list(df.columns)
X.remove("Unnamed: 0")
X.remove("Name")
X.remove("SexCode")
X.remove("Survived")
X.remove("PClass")
df.dropna(inplace=True)
model = sm.OLS(df["Survived"], df[X])
result = model.fit()
print(result.summary())

