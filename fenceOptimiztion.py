# Optimization problem description:
# ====
# http://tutorial.math.lamar.edu/Classes/CalcI/Optimization.aspx 
# Objective is to Maximize x1*x2 or Minimize -1*x1*x2.
# 
# Equality constraint is x1+2*x2=500 in fact g(x)=0
# So the quality constraint is g(x)=x1+2*x2-500=0
# 
# Boundaries are (x1,x2)>0,(x1,x2<500)
# Initial conditions x0=(.01,.01)

# In[1]:

import numpy as np
from scipy.optimize import minimize


# In[2]:

def objective(x):
    x1 = x[0]
    x2 = x[1]
    return -1*x1*x2

def constraint2(x):
    return x[0]+2*x[1]-500

x0=[0.01,0.01]
print(objective(x0))

b1=(0,500)
b2=(0,500)
bnds=(b1,b2)
con2={'type': 'eq','fun': constraint2}
cons=[con2]

sol=minimize(objective,x0,method='SLSQP',bounds=bnds,constraints=cons)
print(sol)