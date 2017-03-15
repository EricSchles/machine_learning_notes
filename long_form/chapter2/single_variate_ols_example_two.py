import matplotlib.pyplot as plt
import statsmodels.api as sm
import requests
import lxml.html
import math
import pandas as pd

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

df = sm.datasets.get_rdataset("Fair", "Ecdat")["data"]
tmp = pd.DataFrame()
df["sex"] = df.apply(sex_mapping, axis=1)
df["child"] = df.apply(child_mapping, axis=1)
df = df[df.nbaffairs != 0]

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
# Plot outputs
# fig, ax = plt.subplots(figsize=(8,6))
# x = df["age"]
# y = df["nbaffairs"]
# res = result
# ax.plot(x, y, 'o', label="data")
# ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
# ax.legend(loc='best');
# plt.show()
