"""
Purpose: Perform a t test for a one sample mean with user input.

Author: Bryan Bain

Date: July 10, 2020

File Name: ttest1samp.py
"""

import scipy.stats as stats
import math
import numpy as np

def obsToT(xbar, mu, sigma, n):
    return (xbar-mu)/(sigma/math.sqrt(n))

quit = False

while not quit:
    
    mu = input("Please enter the given population mean: ")
    if mu == 'q':  # quit the program
        quit = True
        break
    significance = input("Please enter the significance level, as a decimal: ")
    if significance == 'q':  # quit the program
        quit = True
        break
    mu = float(mu)
    significance = float(significance)
    print()
    
    print("Is this a left-tailed, right-tailed, or two-tailed test?")
    print("1. Left-tailed (Population Mean < Claimed Mean)")
    print("2. Right-tailed (Population Mean > Claimed Mean)")
    print("3. Two-tailed (Population Mean != Claimed Mean)")
    left_right_two = input()

    print("Are you given data or summary statitiscs? ")
    print("1. Data set")
    print("2. Summary statistics")

    data_or_sum = input()
    if data_or_sum == 'q':  # quit the program
        quit = True
    elif data_or_sum == "1":  # user will be manually entering a dataset
        done = False
        dataset = []
        print("Please enter the data set. Press 'd' when done, and 'u' to undo.")
        while not done:
            element = input()
            if element == 'd':  # user is done entering data values
                break
            elif element == 'u':  # undo the last data entry
                dataset.pop()
                print(dataset)
                continue
            elif element == 'q':  # quit the program
                quit = True
                break
            dataset.append(float(element))  # cast entry as a float and append to dataset
            print(dataset)  # prints dataset for user after entering each value
        xbar = np.mean(dataset)
        std_dev = np.std(dataset, ddof=1)
        sample_size = len(dataset)
        print()
        print(f"Sample mean: {xbar:0.4f}")
        print(f"Sample standard deviation: {std_dev:0.4f}")
        print(f"Sample size: {sample_size:0.0f}")
    else:  # user will manually enter summary statistics
        xbar = input("Please enter the sample mean: ")
        if xbar == 'q':  # quit the program
            quit = True
            break
        xbar = float(xbar)
        std_dev = input("Please enter the sample standard deviation: ")
        if std_dev == 'q':  # quit the program
            quit = True
            break
        std_dev = float(std_dev)
        sample_size = input("Please enter the sample size: ")
        if sample_size == 'q':  # quit the program
            quit = True
            break
        sample_size = int(sample_size)
    print()
    
    test_statistic = obsToT(xbar, mu, std_dev, sample_size)  # calculate test statistic t
    df = sample_size - 1  # degrees of freedom
    area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)  # area under curve
    ci_min = stats.t.interval(1-2*significance, df=df, loc=xbar, scale=std_dev/math.sqrt(sample_size))[0]  # minimum of confidence interval
    ci_max = stats.t.interval(1-2*significance, df=df, loc=xbar, scale=std_dev/math.sqrt(sample_size))[1]  # maximum of confidence interval
    print(f"Test statistic: {test_statistic:0.4f}")
    if left_right_two == '1':
        print(f"Population Mean < Claimed Mean critical value: {stats.t.ppf(significance,df):0.4f}")
        print(f"p-value: {area:0.4f}")
        print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
    elif left_right_two == '2':
        print(f"Population Mean > Claimed Mean critical value: {stats.t.ppf(1-significance,df):0.4f}")
        print(f"p-value: {1-area:0.4f}")
        print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
    elif left_right_two == '3':   
        ci_min = stats.t.interval(1-significance, df=df, loc=xbar, scale=std_dev/math.sqrt(sample_size))[0]  # minimum of confidence interval
        ci_max = stats.t.interval(1-significance, df=df, loc=xbar, scale=std_dev/math.sqrt(sample_size))[1]  # maximum of confidence interval
        print(f"Population Mean != Claimed Mean critical value: +/-{math.fabs(stats.t.ppf(significance/2,df)):0.4f}")
        print(f"p-value: {2*min(area,1-area):0.4f}")
        print(f"{100*(1-significance):.0f}% Confidence Interval: ({ci_min:0.4f}, {ci_max:0.4f})")
    print()
