#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

import random

#initialization:
pop_n = 100
iteration = 100
emp_n = 5
countries = np.random.randint(-10,10,(100,3))
emps = np.random.randint(0,99,(1,5))
x_domain = [-10 , 10] # for x1 , x2 , x3
emp_colonies = {emps[0]:[0:20],emps[1]:[21:40],emps[2]:[41:60],emps[3]:[61:80],emps[4]:[81:100]}

for i in emp_colonies:
    for j in range(0,20):
        if i[j] in emps:
            i.remove(i[j])


# In[ ]:


def function(x1,x2,x3):
    # MAX f1 = x1 + (3 * x2)
    # MAX f2 = (x1 ** 2)+ (1 / x3)
    # tabdil vazn dar be tak hadafe: f = f1 + (2 * f2)
    
    f1 = x1 + (3 * x2)
    f2 = (x1 ** 2)+ (1 / (1 + x3))
    f = f1 + (2 * f2)
    
    return f


# In[ ]:


def fitness1(x1,x2,x3):
    f = function(x1,x2,x3)
    f = f + 100
    return f


# In[ ]:


def fitness(c):
    fe = fitness1(countries[c])
    fc = 0
    for i in emp_colonies[c]:
        fc += fitness1(countries[i])
    f = fe + fc / len(emp_colonies[c])

    return f


# In[ ]:


def move_colonies():
    BETA = 0.2
    for i in emp_colonies:
        for j in emp_colonies[i]:
            for r in range(0,3):
                countries[j,r] = countries[j,r] + countries[i,r] * BETA
                        
        
    return


# In[ ]:


def check_displacement():
     for i in emp_colonies:
        for j in emp_colonies[i]:
            if fitness1(countries[i]) < fitness1(countries[j]):
                temp = i
                i = j
                j = temp    
    return


# In[ ]:


def selection(f_l):
    s = sum(f_l)
    cdf = []
    cdf.append(0)
    c=0
    for  i in f_l:
        cdf.append(i/s + cdf(c))
        c+=1

    p = random.random()
    for i in cdf:
        if i=<p<i+1:
            e = i
    return e


# In[ ]:


def competition():
    f = {emps[0]:0,emps[1]:0,emps[2]:0,emps[3]:0,emps[4]:0}
    for i in f:
        f[i] = fitness(i)
    f_s = sorted(f.items(), key=lambda x:x[1])
    f_l = []
    for i in f_s:
        f_l.append(i)
    e = selection(f_l)
    min_e = f_l[4]
    e1 = emp_colonies[e]
    e2 = emp_colonies[min_e]
    e1.append(e2[0])
    e2.remove(e2[0])
    
    return


# # main ICA:

# In[ ]:


for i in range (0,iteration):
    check_displacement()
    move_colonies()
    competition()
    if len(emps)<4:
        breack
print(emps)

