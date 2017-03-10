import matplotlib.pyplot as plt
import statsmodels.api as sm
import requests
import lxml.html
import math
import pandas as pd
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

def sex_mapping(x):
    if x["sex"] == "male":
        return 0
    if x["sex"] == "female":
        return 1

def child_mapping(x):
    if x["child"] == "no":
        return 0
    if x["child"] == "yes":
        return 1

df = pd.read_csv("Fair.csv")
tmp = pd.DataFrame()
df["sex"] = df.apply(sex_mapping, axis=1)
df["child"] = df.apply(child_mapping, axis=1)

X = list(df.columns)
X.remove("nbaffairs")
X.remove("Unnamed: 0")
X.remove("age")
X.remove("child")
X.remove("occupation")
X = df[X]

scores = []
for neighbor in range(1,20):
    msk = np.random.rand(len(df)) < 0.8
    train = df[msk]
    test = df[~msk]
    X = list(df.columns)
    X.remove("nbaffairs")
    X.remove("Unnamed: 0")
    X_train = train[X]
    X_test = test[X]
    Y_train = train["nbaffairs"]
    Y_test = test["nbaffairs"]
    neigh = KNeighborsRegressor(n_neighbors=neighbor)
    neigh.fit(X_train, Y_train)
    scores.append(neigh.score(X_test, Y_test))

for index,score in enumerate(scores):
    print("K:",index,"Score",score)
    
# msk = np.random.rand(len(df)) < 0.8
# train = X[msk]
# test = X[~msk]
# clf = SVR()
# clf.fit(train, y)

# print(clf.score(test, y))

model = sm.OLS(df["nbaffairs"], df[X])
result = model.fit()
print(result.summary())

# Plot outputs
# fig, ax = plt.subplots(figsize=(8,6))
# x = df["age"]
# y = df["nbaffairs"]
# res = result
# ax.plot(x, y, 'o', label="data")
# ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
# ax.legend(loc='best');
# plt.show()
