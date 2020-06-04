"""
Purpose: Illustrate how dividing sample variance by n-1 targets the population variance 
better than dividing by n
Author: Bryan Bain
Date: June 2, 2020
File: PopSampVariance.py
"""

import numpy as np
import random as rd

population = [rd.randint(1,100) for _ in range(10000)] # generate 10,000 random integers from 1--100
sample1 = [] 
sample2 = []
sample3 = []

for _ in range(10000): # do the following 10,000 times
    sample = rd.sample(population, 50) # Take a sample of 50 values from the population
    sample1.append(np.var(sample)) # variance with n in denominator
    sample2.append(np.var(sample, ddof=1)) # variance with n-1 in denominator
    sample3.append(np.var(sample, ddof=2)) # Using n-2 in denominator 
    
mean_var1 = np.mean(sample1)
mean_var2 = np.mean(sample2)
mean_var3 = np.mean(sample3)

print(f'Using n in the denominator in the samples, we get a mean variance of {mean_var1:0.6f}')
print(f'Using n-1 in the denominator in the samples, we get a mean variance of {mean_var2:0.6f}')
print(f'Using n-2 in the denominator in the samples, we get a mean variance of {mean_var3:0.6f}\n')
print(f'The actual variance of the population is {np.var(population):0.6f}')
