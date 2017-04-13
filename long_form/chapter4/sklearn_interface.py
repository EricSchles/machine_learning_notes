import matplotlib.pyplot as plt
#import statsmodels.api as sm
from sklearn import svm
from sklearn import linear_model
from sklearn.metrics import r2_score
from inflation_calc import CPI
import requests
import lxml.html
import math
import pandas as pd
import numpy as np

html = lxml.html.fromstring(requests.get("http://www.multpl.com/us-gdp-inflation-adjusted/table").text)
left = html.xpath('//td[@class="left"]')
years = [elem.text_content().split(",")[1].strip() for elem in left]
right = html.xpath('//td[@class="right"]')
gdp = [float(elem.text_content().replace("trillion","").strip())* math.pow(10,12) for elem in right]
tmp = {years[index]:gdp[index] for index in range(len(years))}
GDP = {}
cpi = CPI()
df = pd.DataFrame()
years = range(1960,2017)
cpi_usa = {year:cpi.data["United States"][year] for year in years}

for year in cpi_usa:
    GDP[int(year)] = tmp[str(year)]
    
for year in cpi_usa.keys():
    df = df.append({"cpi":cpi_usa[year], "gdp":math.log(GDP[year])}, ignore_index=True)

X_data = np.array([[elem] for elem in df["cpi"]])
Y_data = np.array(df["gdp"])
model_svm = svm.SVR()
result_svm = model_svm.fit(X_data, Y_data ) #sm.OLS(Y, X)
y_pred_svm = [result_svm.predict([[elem]]) for elem in df["cpi"]]
print("R^2 SVM:",r2_score(Y_data, y_pred_svm))
reg_ridge = linear_model.BayesianRidge()
result_ridge = reg_ridge.fit(X_data, Y_data ) #sm.OLS(Y, X)
y_pred_ridge = [result_ridge.predict([[elem]]) for elem in df["cpi"]]
print("R^2 Bayesian Ridge Regression:",r2_score(Y_data, y_pred_ridge))

#import code
#code.interact(local=locals())
# Plot outputs
# fig, ax = plt.subplots(figsize=(8,6))
# x = df["cpi"]
# y = df["gdp"]
# res = result
# ax.plot(x, y, 'o', label="data")
# ax.plot(x, res.fittedvalues, 'r--.', label="OLS")
# ax.legend(loc='best');
# plt.show()
