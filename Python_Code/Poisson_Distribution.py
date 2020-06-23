"""
Purpose: Calculate Poisson distribution values.
Author: Bryan Bain
Date: June 23 2020
File: Poisson_Distribution.py
"""

import scipy.stats as stats

mu = 4             # mean observations in a given interval
num_successes = 5  # number of successes
dp = 8             # decimal places to round to

print("x".center(6) + "P(X=x)".center(12) + "P(X <= x)".center(12) +
      "P(X >= x)".center(12))
for i in range(num_successes+1):
    print(f'{i}'.center(6) +
          f'{round(stats.poisson.pmf(i,mu),dp)}'.center(12) +
          f'{round(stats.poisson.cdf(i,mu),dp)}'.center(12) +
          f'{round(1 - stats.poisson.cdf(i-1,mu),dp)}'.center(12))