"""
Purpose: Perform a t test for a one sample mean with user input.

Author: Bryan Bain

Date: July 10, 2020

File Name: ttest1samp.py
"""

import scipy.stats as stats
import math
import numpy as np

def obsToT(xbar, mu, sigma, n):  # convert raw data to t statistic
    return (xbar-mu)/(sigma/math.sqrt(n))

mu = float(input("Please enter the original (claimed) mean: "))
significance = eval(input("Please enter the significance level: "))
print()

print("Are you given data or summary statitiscs? ")
print("1. Data set")
print("2. Summary statistics")

data_or_sum = input()
if data_or_sum == "1":  # user enters data set
    done = False
    dataset = []
    print("Please enter the data set. Press 'q' when done.")
    while not done:
        element = input()
        if element == 'q':
            break
        element = float(element)
        dataset.append(element)
    xbar = np.mean(dataset)
    std_dev = np.std(dataset, ddof=1)
    sample_size = len(dataset)
    print()
    print(f"Sample mean: {xbar:0.4f}")
    print(f"Sample standard deviation: {std_dev:0.4f}")
    print(f"Sample size: {sample_size:0.0f}")

else:  # user enters summary statistics
    xbar = float(input("Please enter the sample mean: "))
    std_dev = float(input("Please enter the sample standard deviation: "))
    sample_size = int(input("Please enter the sample size: "))
print()

test_statistic = obsToT(xbar, mu, std_dev, sample_size)
df = sample_size - 1
area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)
ci_min = stats.t.interval(1-significance, df=df, loc=xbar, scale=std_dev/math.sqrt(sample_size))[0]
ci_max = stats.t.interval(1-significance, df=df, loc=xbar, scale=std_dev/math.sqrt(sample_size))[1]
print(f"Test statistic: {test_statistic:0.3f}")
print(f"Ha < H0 p-value: {area:0.4f}")
print(f"Ha > H0 p-value: {1-area:0.4f}")
print(f"Ha != H0 p-value: {2*area:0.4f}")
print(f"{100*(1-significance):.0f}% Confidence Interval: ({ci_min:0.4f}, {ci_max:0.4f})")