from __future__ import print_function
import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

dta = sm.datasets.sunspots.load_pandas().data

dta.index = pd.Index(sm.tsa.datetools.dates_from_range('1700','2008'))
del dta["YEAR"]

import code
code.interact(local=locals())
