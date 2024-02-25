#!/usr/bin/env python
# coding: utf-8

# In[23]:


import random
import math
import matplotlib.pyplot as plt

#initialization
c1 = 1.5
c2 = 1.5
w = 1
pbest = []
pbestx = []
pbesty = []
gbest = 100
vx = []
vy = []
xt = []
yt = []
s = 300
iterations = 1000   
gbestlist = []


# In[24]:


#Rastrigin function
def fitness(x, y):
    f= 10 + ((x**2) - (5* math.cos(2*math.pi*x))) + ((y**2) - (5*math.cos(2*math.pi*y)))
    return f

# Particles Initialization
for i in range(s):
    xt.append(random.uniform(-10, 10))
    yt.append(random.uniform(-10, 10))
    pbestx.append(xt[i])
    pbesty.append(yt[i])
    vx.append(1)
    vy.append(1)      

for j in range (iterations):
    w=3*w/iterations
    gbestlist.append(fitness(pbestx[gbest], pbesty[gbest]))
    for i in range(s):   
        r1 = random.uniform(0,1)
        r2 = random.uniform(0,1)
        vx[i] = w*vx[i] + r1 * c1 * random.uniform(-1, 1) * (pbestx[i] - xt[i]) + r2 * c2 * random.uniform(-1, 1) * (pbestx[gbest] - xt[i])
        vy[i] = w*vy[i] + r1 * c1 * random.uniform(-1, 1) * (pbesty[i] - yt[i]) + r2 * c2 * random.uniform(-1, 1) * (pbesty[gbest] - yt[i])            
        xt[i] = (xt[i] + vx[i])
        yt[i] = (yt[i] + vy[i])
        if(fitness(xt[i], yt[i]) < fitness(pbestx[i], pbesty[i])):
            pbestx[i] = xt[i]         
            pbesty[i] = yt[i]         
        if(fitness(xt[i], yt[i]) < fitness(pbestx[gbest], pbesty[gbest])):         
            gbest = i


# In[25]:


print("Min: " + str(fitness(pbestx[gbest], pbesty[gbest])))
print("[X,Y]=: " +"["+ str(pbestx[gbest]) + ","+ str(pbesty[gbest])+"]" )
plt.plot(gbestlist)
plt.xlabel('Iterations')
plt.ylabel('G_best')
plt.show()


# In[ ]:





# In[ ]:




