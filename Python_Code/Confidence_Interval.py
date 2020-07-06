"""
Purpose: Calculate confidence intervals for population mean and proportion.

Author: Bryan Bain

Date: July 6, 2020

File name: Confidence_Interval.py
"""


import math
import numpy as np
import scipy.stats as stats

# Confidence interval for population mean
x_bar = 2.45
sigma = 0.12
sample_size = 100
conf_level = 0.98

print(stats.norm.interval(conf_level, loc = x_bar, scale=sigma/math.sqrt(sample_size)))

# Confidence interval for population proportion
num_successes = 30
sample_size = 40
conf_level = 0.98

p = num_successes/sample_size
print(stats.norm.interval(conf_level, loc = p, scale=math.sqrt(p*(1-p)/sample_size)))