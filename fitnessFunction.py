import math as m


#schaffer
"""
D       =  10    # Problem Dimension
LB      = -30  # Set Size Lower bound
UB      =  30   # Set Size Upper bound

def FitnessFunction(x):
    s = 0
    p = 0
    q = 0
    for i in range(D-1):
        p = x[i]**2 + x[i+1]**2
        q = m.sqrt(p)
        
        s = s + 0.5 + ( (m.sin(q)**2 - 0.5) / (1 + 0.001*p)**2 )
    return round(s,2)
"""

#*******************************************

#**alpine**
"""
D       =  10    # Problem Dimension
LB      = -30  # Set Size Lower bound
UB      =  30   # Set Size Upper bound

def FitnessFunction(x):
    s = 0
    for i in range(1,D):
        s = s + m.fabs( x[i]*m.sin(x[i]) + 0.1*x[i] )
    return round(s,2)
"""

#*****************************************

#**rosenbrock**
"""
D       =  10    # Problem Dimension
LB      = -30  # Set Size Lower bound
UB      =  30   # Set Size Upper bound

def FitnessFunction(x):
    s = 0
    for i in range(D-1):
        s = s + (100*(x[i+1]-x[i]**2)**2 + (x[i] - 1)**2)
    return round(s,2)
"""

#**********************************************

#**bird**
"""
D       = 2    # Problem Dimension
LB      = -7  # Set Size Lower bound
UB      =  7   # Set Size Upper bound

def FitnessFunction(x):
    s = m.sin(x[0])*m.exp((1-m.cos(x[1]))**2) + m.cos(x[1])*m.exp((1-m.sin(x[0]))**2) + (x[0]-x[1])**2
    return s
"""

#**********************************************
#Ackley
"""
import math as m

D       =  10    # Problem Dimension
LB      = -35  # Set Size Lower Bound
UB      =  35   # Set Size Upper Bound

def FitnessFunction(x):
    s = 0
    for i in range(1,D):
        p = x[i]*x[i]
        q = m.sqrt(p/D)
        a = m.cos(2*m.pi*x[i])
        
    s = -20*m.exp(-0.02*q) - m.exp(a/D) + 20 + m.exp(1)
    return s
"""

#*******************************************
#**Zakharov**
"""
D       =  10    # Problem Dimension
LB      = -3 # Set Size Lower bound
UB      =  3   # Set Size Upper bound

def FitnessFunction(x):
    s = 0
    p = 0
    q = 0
    for i in range(1,D):
        p = x[i]*x[i]
        q = i*x[i]/2
        s = s + p + q**2 + q**4
    return round(s,2)
"""


#********************************************

#**trid**
D       =  10    # Problem Dimension
LB      = -3 # Set Size Lower bound
UB      =  3   # Set Size Upper bound

def FitnessFunction(x):
    s = 0
    p = 0
    q = 0
    for i in range(1,D-1):
        p = (x[i] - 1)**2
        q = x[i] * x[i-1]
        s = s + p  - q
    return round(s,2)

















































