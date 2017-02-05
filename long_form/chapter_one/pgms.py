from pgmpy import models
from pgmpy import factors
TabularCPD = factors.TabularCPD
food_schedule = models.BayesianModel()

# instantiates a new Bayesian Model called 'student'
food_schedule.add_nodes_from(['breakfast', 'lunch'])

# adds nodes labelled 'diff', 'intel', 'grade' to student
food_schedule.add_edges_from([('breakfast', 'lunch')])

breakfast_cpd = TabularCPD('breakfast', 2, [[0.3], [0.7]])


lunch_cpd = TabularCPD('lunch', 2, [[0.1, 0.3],
                                    [0.9, 0.7]],
                       evidence="breakfast", evidence_card=2)



food_schedule.add_cpds(breakfast_cpd, lunch_cpd)

print(food_schedule.active_trail_nodes('lunch'))

print(food_schedule.active_trail_nodes('lunch', observed='breakfast'))
