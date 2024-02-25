#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math
import random
city_data = pd.read_excel (r'data.xlsx')


# In[2]:


Distance_matrix = np.zeros((52,52))

for i in range(52):
    for j in range(52):
        Distance_matrix[i,j] = math.sqrt((city_data.loc[i,1] - city_data.loc[j,1])**2 + (city_data.loc[i,2] - city_data.loc[j,2])**2)
pheromone_matrix = np.zeros((52,52))


# In[3]:


Ant_N = 100
alpha = 1
beta = 1
ants = np.zeros((1,52))
Repetition = 1000
def choose_next_node(current_node):
    p = np.zeros((1,52))
    i = current_node
    s = 0
    for j in range(52):
        s += ((pheromone_matrix[i,j]**alpha)*(Distance_matrix[i,j]**beta))
    for j in range(52):
        p[j] = ((pheromone_matrix[i,j]**alpha)*(Distance_matrix[i,j]**beta))/s
    p_1 = random.random()
    if p_1 > 0.3:
        choose = np.argmax(p)
    else:
        p_1 = random.random()
        cdf = np.array()
        cdf[0] = p[0]
        for i in range (1,52):
            cdf[i] = cdf[i-1] + p[i]
        q = random.random()
        for j in range(52):
            if q<=cdf[j]:
                choose = j
                break
    return choose


# In[4]:


for r in range (Repetition):
    i=0
    for ant in ants:
        current_node = ant
        next_node = choose_next_node(current_node)
        pheromone_matrix[ant,next_node] += 1
        ants[i] = next_node
        i += 1
    #update pheromone_matrix:
    for i in pheromone_matrix:
        if i>0:
            i -= 1
    
        


# In[ ]:





# In[ ]:




