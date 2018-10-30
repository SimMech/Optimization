

# https://www.youtube.com/watch?v=cXHvC_FGx24

# Optimization problem description:
# ====
# ojective is to Minimize x1*x4*(x1+x2+x3)+x3
# 
# Subject to: x1*x2*x3*x4 >= 25 in fact f(x)>=0 
# so the inequality constraint is x1*x2*x3*x4-25=0 
# 
# Qulity constraint is x1**2+x2**2+x3**2+x4**2=40 in fact g(x)=0
# So the quality constraint is x1**2+x2**2+x3**2+x4**2-40=0
# 
# Boundaries are 1<=x1,x2,x3,x4<=5
# Initial conditions x0=(1,5,5,1)

# In[27]:

import numpy as np
from scipy.optimize import minimize


# In[30]:

def objective(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    return x1*x4*(x1+x2+x3)+x3

def constraint1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0

def constraint2(x):
    sumSQ=x[0]*x[0]+x[1]*x[1]+x[2]*x[2]+x[3]*x[3]-40
    return sumSQ
    
x0=[1,5,5,1]
print(objective(x0))


# In[31]:

b=(1.0,5.0)
bnds=(b,b,b,b)
con1={'type':'ineq','fun':constraint1}
con2={'type':'eq','fun':constraint2}
cons=[con1,con2]

# In[32]:

sol=minimize(objective,x0,method='SLSQP', bounds=bnds,constraints=cons)
print(sol)