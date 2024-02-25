#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import numpy as np
import math


# In[62]:


rep_num = 1000
L = 8
Q_list = [1,2,3,4,5,6,7,8]
random.shuffle(Q_list)
neighbors_num = 5
T = 100000000
def neighbor_generator(Q_list):    
    neighbors = np.array([Q_list,Q_list,Q_list,Q_list,Q_list])
    for n in neighbors:
        rand1 = random.randrange(0, 8)
        rand2 = random.randrange(0, 8)
        n[rand1],n[rand2] = n[rand2],n[rand1]    
    return neighbors

def fitness_f(Q_list):
    neighbors = neighbor_generator(Q_list) 
    fit_n = [0,0,0,0,0]
    n_i=0
    for n in neighbors:
        conflict = 0
        for i in range(8):
            for j in range(i+1,8):
                if n[i]-n[j] == i-j:
                    conflict += 1                            
        fit_n[n_i] = 28 - conflict
        n_i+=1
    best_n_fit = max(fit_n)
    index = fit_n.index(best_n_fit)
    return best_n_fit,neighbors[index]
best = Q_list
best_fit = 0
for i in range (rep_num) :
    best_n_fit,best_n = fitness_f(Q_list)
    if best_fit < best_n_fit :
        best_fit = best_n_fit
        best = best_n
    else:
        F = (best_n_fit-best_fit)/T
        p = math.exp(F)
        if random.random() > p:
            best_fit = best_n_fit
            best = best_n
    
    T=T/(2)

print(best)
print(best_fit)       


# In[ ]:





# In[ ]:




