"""
Problem definition:

You are a developer at a start up - congrats!

You're boss comes to you and says, I need to know how many users are really enjoying our platform!

And I need some quantitative measures of how to convert users from passive or only sort of active, to very active!

Can you help me with this?

"""

import random
#please use this version of the pgmpy - https://github.com/pgmpy/pgmpy
from pgmpy.models import BayesianModel
from pgmpy.estimators import ParameterEstimator
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.estimators import BayesianEstimator
import pandas as pd
#active users
#passive users
#new users

"""
Goals: 
1. identify users as passive or active
2. figure out what takes a user from passive to active or from new directly to active.
	2a. try a marketing campaign digital only
	2b. try a leaflet and digital marketing campaign
 	2c. try a tv and radio only campaign

"""

"""
Solving subtask 1:

1. last activity update, compare to previous last login

Random Variable: activity_level - high, medium, low

def high:= logged in multiple times per week
def medium := logged in once per week - once per two weeks
def low := logged in once per month

2.  duration

def high := spends 1 or more hours per session on platform
def medium := spends 30 minutes - 1 hour  per session on platform
def low := spends 29 - 1 minute or less per session on platform

3. number of pages viewed

def high := 20 pages or more
def medium := 20 - 5 pages 
def low := 5 - 1 pages or less
"""

high = "high, "*10
medium = "medium, "*25
low = "low, "*24

high = [elem for elem in high.strip().split(",") if elem != '']
medium = [elem for elem in medium.strip().split(",") if elem != '']
low = [elem for elem in low.strip().split(",") if elem != '']

dhigh = "high, "*25
dmedium = "medium, "*24
dlow = "low, "*10

dhigh = [elem for elem in dhigh.strip().split(",") if elem != '']
dmedium = [elem for elem in dmedium.strip().split(",") if elem != '']
dlow = [elem for elem in dlow.strip().split(",") if elem != '']

pvhigh = "high, "*25
pvmedium = "medium, "*24
pvlow = "low, "*10

pvhigh = [elem for elem in pvhigh.strip().split(",") if elem != '']
pvmedium = [elem for elem in pvmedium.strip().split(",") if elem != '']
pvlow = [elem for elem in pvlow.strip().split(",") if elem != '']

active_users = "active, "*35
passive_users = "passive, "*24

active_users = [elem for elem in active_users.strip().split(",") if elem != '']
passive_users = [elem for elem in passive_users.strip().split(",") if elem != '']

data = pd.DataFrame(data = {'last_activity' : high + medium + low, 'duration': dhigh + dmedium + dlow, 'pages_viewed': pvhigh + pvmedium + pvlow, 'user_type' : active_users + passive_users })

model = BayesianModel([ 
	('last_activity', 'duration'),
	('duration', 'pages_viewed'), 
	('pages_viewed', 'user_type')])

pe = ParameterEstimator(model, data)

#print("\n", pe.state_counts('last_activity'))  # unconditional
#print("\n", pe.state_counts('user_type'))  # conditional on fruit and size

mle = MaximumLikelihoodEstimator(model, data)
#print(mle.estimate_cpd('last_activity'))  # unconditional
#print(mle.estimate_cpd('user_type'))  # conditional


# Calibrate all CPDs of `model` using MLE:
model.fit(data)

est = BayesianEstimator(model, data)

result = est.estimate_cpd('user_type', prior_type='BDeu', equivalent_sample_size=10)
import code
code.interact(local=locals())
