import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn import linear_model
import requests
import lxml.html
import math
import pandas as pd
from scipy import stats
import numpy as np
import scipy

def is_nan(obj):
    if type(obj) == type(float()):
        return math.isnan(obj)
    else:
        return False

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

#http://vincentarelbundock.github.io/Rdatasets/datasets.html
#http://statsmodels.sourceforge.net/0.6.0/datasets/index.html
df = sm.datasets.get_rdataset("Fair", "Ecdat")["data"]
tmp = pd.DataFrame()
df["sex"] = df.apply(sex_mapping, axis=1)
df["child"] = df.apply(child_mapping, axis=1)
df = df[df.nbaffairs != 0]
df = df.dropna()

print("verifying that gamma fits our distribution")
for k in range(1,2):
    print("for K=",k)
    for column in df.columns:
        gamma_distribution = [np.random.gamma(k) for _ in range(len(df[column]))]
        print(scipy.stats.mannwhitneyu(gamma_distribution, df[column]))
    
for column in df.columns:
    if column == "nbaffairs":
        continue
    list_of_seen_values = []
    for index in df.index:
        if not df.ix[index][column] in list_of_seen_values:
            tmp = tmp.append(df.ix[index])
            list_of_seen_values.append(df.ix[index][column])
    tmp = tmp.reset_index(drop=True)
    model = sm.OLS(tmp["nbaffairs"], tmp[column])
    result = model.fit()
    print(column)
    print(result.summary())

for column in df.columns:
    reg_ridge = linear_model.BayesianRidge()
    reg_ard = linear_model.ARDRegression()
    ols = linear_model.LinearRegression()
    reg = linear_model.Ridge(alpha=0.5)
    reg_cv = linear_model.RidgeCV(alphas=[0.1, 0.3, 0.5, 0.7, 1.0, 5.0, 10.0])
    theil_sen = linear_model.TheilSenRegressor()
    huber = linear_model.HuberRegressor()
    x_values = [[elem] for elem in list(df[column])]
    y_values = [elem for elem in list(df["nbaffairs"])]
    ridge_result = reg_ridge.fit(x_values, list(df["nbaffairs"]))
    ard_result = reg_ard.fit(x_values, y_values)
    ols_result = ols.fit(x_values,y_values)
    reg_result = reg.fit(x_values,y_values)
    reg_cv_result = reg_cv.fit(x_values,y_values)
    theil_sen_result = theil_sen.fit(x_values, y_values)
    huber_result = huber.fit(x_values,y_values)
    print(column,"bayesian ridge score:",ridge_result.score(x_values, y_values))
    print(column,"ARD score:",ard_result.score(x_values,y_values))
    print(column,"OLS score:",ols_result.score(x_values,y_values))
    print(column,"Ridge score:",reg_result.score(x_values,y_values))
    print(column,"Ridge CV score:",reg_cv_result.score(x_values,y_values))
    print(column,"Theil Sen score:",theil_sen_result.score(x_values,y_values))
    print(column,"Huber score:",huber_result.score(x_values,y_values))
# Plot outputs
# fig, ax = plt.subplots(figsize=(8,6))
# x = df["age"]
# y = df["nbaffairs"]
# res = result
# ax.plot(x, y, 'o', label="data")
# ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
# ax.legend(loc='best');
# plt.show()
