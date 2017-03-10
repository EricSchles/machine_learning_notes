import matplotlib.pyplot as plt
import statsmodels.api as sm
from inflation_calc import CPI
import requests
import lxml.html
import math
import pandas as pd

#https://data.bls.gov/timeseries/LNS12000000 - data on Labor Force Statistics from the Current Population Survey
full_employment_df = pd.read_excel("full_employment.xlsx")
full_employment = {}
for index in full_employment_df.index:
    full_employment[int(full_employment_df.ix[index]["year"])] = full_employment_df.ix[index]["employment"]

html = lxml.html.fromstring(requests.get("http://www.multpl.com/us-gdp-inflation-adjusted/table").text)
left = html.xpath('//td[@class="left"]')
years = [elem.text_content().split(",")[1].strip() for elem in left]
right = html.xpath('//td[@class="right"]')
gdp = [float(elem.text_content().replace("trillion","").strip())* math.pow(10,12) for elem in right]
tmp = {years[index]:gdp[index] for index in range(len(years))}
GDP = {}
cpi = CPI()
df = pd.DataFrame()
years = list(full_employment.keys())
cpi_usa = {year:cpi.data["United States"][year] for year in years}

for year in years:
    GDP[int(year)] = tmp[str(year)]
    
for year in years:
    df = df.append({"cpi":cpi_usa[year], "gdp":math.log(GDP[year]), "employment":full_employment[year]}, ignore_index=True)
y = df["gdp"]
X = df[["cpi", "employment"]]
model = sm.OLS(y, X)
result = model.fit()
print(result.summary())
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
