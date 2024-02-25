#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import random

#initialization:
pop_n = 100
iteration = 100
x = np.random.randint(-10,10,(100,3))
x_domain = [-10 , 10] # for x1 , x2 , x3
x_m = []
f = []
k_best = []


# In[ ]:


def force(g, i,j,x,d):
    force_x = (g * x_m[i],x_m[j])*(x[j,d] - x[i,d]) / (sqr((x[j,0] - x[i,0])**2+(x[j,1] - x[i,1])**2+(x[j,2] - x[i,2])**2))
    
    return force_x


# In[ ]:


def move(x_m,x,g,k_best):
    force_x = []
    force_f = []
    a = []
    v = [0,0,0]
    for i in x:
        force_xd =[]
        for j in k_best:
            for d in range(0,3):
                force_xd.append(force(g,i,j,x,d))
            force_x.append(force_xd)
        for q in range(0,3):
            force_f.append(sum(force_x(q,:)))
            a.append(force_f[q]/x_m[i.index()])
            v[q] = v[q]*random.random() + a[q]
            i = i[q] + v[q]  
    
    return x


# In[ ]:


def fitness(x,f):
    for i in range(0,100):
        x1 = x[i,1]
        x2 = x[i,2]
        x3 = x[i,3]
        f.append(x1 + x2/2 + x2**3)
    
    return f


# In[ ]:


def mass(x,f,x_m):
    q = []
    for i in range(0,100):
        q.append((f[i] - min(f)) / (max(f) - min(f)))
    for i in range(0,100):
        x_m.append(q[i]/sum(q))
    
    return x_m


# # main ICA:

# In[ ]:


for i in range (0,iteration):
    g = 10*exp(i/iteration)
    f = fitness(x,f)
    k_best.append(f[0:10])
    x_m = mass(x,f,x_m)
    x = move(x_m,x,g,k_best)
print(k_best)

