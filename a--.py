algoname = raw_input("algo name : ")
#algoname = "rosenbrock"

execfile("GA.py")
execfile("R.py")
execfile("DE.py")
execfile("PSO.py")


import csv

f = open("RandomBasicResult.csv") 
read=csv.reader(f)
r=[]
i=[]
for row in read:
    r.append(row[1])
    i.append(row[0])
del r[0]
del i[0]
print r
print i
f.close

f = open("resultGABasic.csv") 
read=csv.reader(f)
g=[]
for row in read:
    g.append(row[1])
del g[0]
print g
f.close

f = open("resultDEBasic.csv") 
read=csv.reader(f)
d=[]
for row in read:
    d.append(row[1])
del d[0]
print d
f.close

f = open("resultPSOBasic.csv") 
read=csv.reader(f)
p=[]
for row in read:
    p.append(row[1])
del p[0]
print p
f.close


import numpy as np
import matplotlib.pyplot as plt

plot1 = plt.plot(i, r, c='r', alpha=50, label='RANDOM')
plot2 = plt.plot(i, g, c='g', alpha=50, label="GA")
plot3 = plt.plot(i, d, c='b', alpha=50, label="DE")
plot4 = plt.plot(i, p, c='y', alpha=50, label="PSO")

plt.xlabel('Iterations')
plt.ylabel('Fitness')
plt.title('Performance Comparison ('+ algoname + ")")

plt.legend(loc='upper right')
plt.xlim(0,200)
#plt.ylim(0,20000)

plt.savefig(algoname+'.png', dpi=1200)
plt.show()





