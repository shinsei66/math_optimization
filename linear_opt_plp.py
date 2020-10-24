import time
import pulp
#線形最適化問題
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

#整数最適化問題
sts = time.time()

problem = pulp.LpProblem('lio2', pulp.LpMinimize )
x = pulp.LpVariable('x',lowBound= 0, cat='Integer')
y = pulp.LpVariable('y', lowBound=0, cat='Integer')
z = pulp.LpVariable('z',lowBound= 0 ,cat='Integer')
problem += y + z
problem += x + y + z == 32
problem += 2*x + 4*y + 8*z == 80
status = problem.solve()
ed = time.time()

print('Optimization calculation took {:.2f} sec'.format(ed-sts))
print('Opt. Val is {}'.format(problem.objective.value()))
print("Crane = {}, Turtle = {}, Octopus = {} ".format(x.value(), y.value(), z.value()) )