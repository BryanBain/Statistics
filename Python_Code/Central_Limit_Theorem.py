"""
Purpose: Demonstrate the Central Limit Theorem.

Author: Bryan Bain

Date: July 2, 2020

File Name: Central_Limit_Theorem.py
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt
import scipy.stats as stats
import math

# Uniform distribution of population
data = [rd.uniform(0,1000) for _ in range(50_000)]  # generate a population of 50,000 random uniform values between 0 and 1,000

# Normal distribution of population
# data = [rd.gauss(100,15) for _ in range(50_000)]  # generate a population of 50,000 random normal values with mean 100 and s.d. 15

# Geometric distribution of population
# data = [np.random.geometric(0.75) for _ in range(50_000)]  # generate a population of 50,000 random geometric values with mean of 5

fig,ax = plt.subplots()
ax.hist(data, bins=30, ec='b')
plt.show()
sample_means = []
sample_size = 50
for _ in range(10_000):  # do the following 10,000 times
    sample = rd.choices(data,k=sample_size)  # take a sample of 50 values from the population
    sample_means.append(np.mean(sample))  # add the mean of the sample to the sample_means list

pop_mean = np.mean(data)
mean_sample_means = np.mean(sample_means)
std_samples = np.std(sample_means)
pop_std = np.std(data)
std_err = pop_std / math.sqrt(sample_size)

fig,ax = plt.subplots()
ax.hist(sample_means, bins=30, ec='b')
plt.show()

print(f'The mean of the sample means is {mean_sample_means:0.2f} '
      f'with a standard deviation of {std_samples:0.2f}')
print(f'The mean of the population is {pop_mean:0.2f} '
     f'with a standard deviation of {pop_std:0.2f}')
print(f'The standard error is {std_err:0.2f}')