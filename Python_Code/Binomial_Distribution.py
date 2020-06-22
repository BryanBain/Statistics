"""
Purpose: Calculate binomial distribution values.
Author: Bryan Bain
Date: June 21 2020
File: Binomial_Distribution.py
"""

import scipy.stats as stats

num_trials = 10     # number of trials
p = 0.20            # probability of success
dp = 8              # decimal places to round to

print("x".center(6) + "P(X=x)".center(12) + "P(X <= x)".center(12) +
      "P(X >= x)".center(12))
for i in range(num_trials+1):
    print(f'{i}'.center(6) +
          f'{round(stats.binom.pmf(i,num_trials,p),dp)}'.center(12) +
          f'{round(stats.binom.cdf(i,num_trials,p),dp)}'.center(12) +
          f'{round(1 - stats.binom.cdf(i-1,num_trials,p),dp)}'.center(12))
