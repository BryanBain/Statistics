"""
Perform a hypothesis test on a single population proportion.

Author: Bryan Bain

Date: July 12, 2020

File Name: prop_test1samp.py
"""

import scipy.stats as stats
import math

def obsToZ(p_hat, p, n):
    """
    Calculates the test statistic, z, using proportions.
    :param p_hat: sample proportion of successes
    :param p: claimed (original) proportion of successes
    :param n: sample size
    """
    return (p_hat-p)/(math.sqrt(p*(1-p)/n))

quit = False

while not quit:
    
    pop_proportion = input("Please enter the original (claimed) proportion: ")
    if pop_proportion == 'q':  # quit the program
        quit = True
        break
    sample_proportion = input("Please enter the sample proportion of successes: ")
    if sample_proportion == 'q':  # quit the program
        quit = True
        break
    sample_size = input("Please enter the sample size: ")
    if sample_size == 'q':  # quit the program
        quit = True
        break
    significance = input("Please enter the significance level, as a decimal: ")
    if significance == 'q':  # quit the program
        quit = True
        break
    pop_proportion = float(eval(pop_proportion))
    sample_proportion = float(eval(sample_proportion))
    sample_size = int(sample_size)
    significance = float(significance)
    std_err = math.sqrt(sample_proportion*(1-sample_proportion)/sample_size) # calculate standard error

    test_statistic = obsToZ(sample_proportion, pop_proportion, sample_size)  # calculate test statistic z
    area = stats.norm.cdf(test_statistic, loc=0, scale=1)  # area under curve
    ci_min = stats.norm.interval(1-significance, loc=sample_proportion, scale=std_err)[0]  # minimum of confidence interval
    ci_max = stats.norm.interval(1-significance, loc=sample_proportion, scale=std_err)[1]  # maximum of confidence interval
    print(f"Test statistic: {test_statistic:0.3f}")
    print(f"Ha < H0 critical value: {stats.norm.ppf(significance):0.3f} p-value: {area:0.4f}")
    print(f"Ha > H0 critical value: {stats.norm.ppf(1-significance):0.3f} p-value: {1-area:0.4f}")
    print(f"Ha != H0 critical value: +/-{math.fabs(stats.norm.ppf(significance/2)):0.3f} p-value: {2*min(area,1-area):0.4f}")
    print(f"{100*(1-significance):.0f}% Confidence Interval: ({ci_min:0.4f}, {ci_max:0.4f})")
    print()
