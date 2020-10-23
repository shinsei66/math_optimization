import time
import pulp
sts = time.time()

problem = pulp.LpProblem('lo1', pulp.LpMaximize )
x1 = pulp.LpVariable('x1',lowBound= 0, cat='Continuous')
x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')
x3 = pulp.LpVariable('x3',lowBound= 0 ,upBound= 30, cat='Continuous')
problem += 15*x1 + 18*x2 + 30*x3
problem += 2*x1 + x2 + x3 <= 60
problem += x1 + 2*x2 + x3 <= 60
status = problem.solve()
ed = time.time()

print('Optimization calculation took {:.2f} sec'.format(ed-sts))
print('Opt. Val is {}'.format(problem.objective.value()))
print("x1 = {}, x2 = {}, x3 = {} ".format(x1.value(), x2.value(), x3.value()) )