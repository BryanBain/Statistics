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
    
    significance = input("Please enter the significance level, as a decimal: ")
    if significance == 'q':  # quit the program
        quit = True
        break
    pop_proportion = input("Please enter the given population proportion: ")
    if pop_proportion == 'q':  # quit the program
        quit = True
        break
    print("Is this a left-tailed, right-tailed, or two-tailed test?")
    print("1. Left-tailed (Population Proportion < Sample Proportion)")
    print("2. Right-tailed (Population Proportion > Sample Proportion)")
    print("3. Two-tailed (Population Proportion != Sample Proportion)")
    left_right_two = input()
    sample_proportion = input("Please enter the sample proportion of successes: ")
    if sample_proportion == 'q':  # quit the program
        quit = True
        break
    sample_size = input("Please enter the sample size: ")
    if sample_size == 'q':  # quit the program
        quit = True
        break
     
    pop_proportion = float(eval(pop_proportion))
    sample_proportion = float(eval(sample_proportion))
    sample_size = int(sample_size)
    significance = float(significance)
    std_err = math.sqrt(sample_proportion*(1-sample_proportion)/sample_size) # calculate standard error

    test_statistic = obsToZ(sample_proportion, pop_proportion, sample_size)  # calculate test statistic z
    area = stats.norm.cdf(test_statistic, loc=0, scale=1)  # area under curve
    ci_min = stats.norm.interval(1-2*significance, loc=sample_proportion, scale=std_err)[0]  # minimum of confidence interval
    ci_max = stats.norm.interval(1-2*significance, loc=sample_proportion, scale=std_err)[1]  # maximum of confidence interval
    print(f"\nTest statistic: {test_statistic:0.3f}")
    if left_right_two == '1':
        print(f"Population Proportion < Sample Proportion critical value: {stats.norm.ppf(significance):0.4f}")
        print(f"p-value: {area:0.4f}")
        print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
    elif left_right_two == '2':
        print(f"Population Proportion > Sample Proportion critical value: {stats.norm.ppf(1-significance):0.4f}")
        print(f"p-value: {1-area:0.4f}")
        print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
    elif left_right_two == '3':    
        ci_min = stats.norm.interval(1-significance, loc=sample_proportion, scale=std_err)[0]  # minimum of confidence interval
        ci_max = stats.norm.interval(1-significance, loc=sample_proportion, scale=std_err)[1]  # maximum of confidence interval
        print(f"Population Proportion != Sample Proportion critical value: +/-{math.fabs(stats.norm.ppf(significance/2)):0.4f}")
        print(f"p-value: {2*min(area,1-area):0.4f}")
        print(f"{100*(1-significance):.0f}% Confidence Interval: ({ci_min:0.4f}, {ci_max:0.4f})")
    print()
