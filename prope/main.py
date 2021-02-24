from pyomo.environ import *
import matplotlib.pyplot as plt
import numpy as np
import random

model = AbstractModel()
model.N = Param(mutable=True)
model.i = RangeSet(1, model.N)
model.j = Set(initialize=model.i)
model.a = Param(mutable=True)
model.b = Param(mutable=True)


def initval(model, i):
    return random.uniform(0,1)



model.x = Var(model.i, bounds=(0,model.b), within=NonNegativeReals, initialize=initval)
model.x = Var(model.i, bounds=(0,model.a), within=NonNegativeReals, initialize=initval)
model.x = Var(within=NonNegativeReals)


def C1_rule(model,i,j):
    if i!=j:
        return (model.x[i]-model.x[j])**2+(model.y[i]-model.y[j])**2 >=model.r**2
    else:
        return Constraint.Skip

model.C1     = Constraint(model.i,model.j,rule=C1_rule)


def C2_rule(model,i):
    return (model.a/model.b*model.x[i]+model.a >=model.y[i]

model.C2     = Constraint(model.i,rule=C2_rule)


model.obj = Objective(expr=model.r, sense=maximize)
opt = SolverFactory('ipopt')

# instance.display()
