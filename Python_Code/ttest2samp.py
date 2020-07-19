"""
Purpose: Perform a t test for two sample means.
Author: Bryan Bain
Date: July 18, 2020
File Name: ttest2samp.py
"""

import scipy.stats as stats
import math
import numpy as np

quit = False

while not quit:
    def getStats():
        """
        Obtain summary statistics from user.
        Returns: mean, standard deviation, and sample size of first sample;
                 mean, standard deviation, and sample size of second sample
        """
        mean_ds1 = float(input("Please enter the mean of sample 1: "))
        sd_ds1 = float(input("Please enter the standard deviation of sample 1: "))
        n1 = int(input("Please enter the sample size of sample 1: "))
        mean_ds2 = float(input("Please enter the mean of sample 2: "))
        sd_ds2 = float(input("Please enter the standard deviation of sample 2: "))
        n2 = int(input("Please enter the sample size of sample 2: ")) 
        return mean_ds1, sd_ds1, n1, mean_ds2, sd_ds2, n2

    def getDataSet():
        """
        Prompts the user to manually enter a dataset.
        """
        done = False
        dataset = []
        print("Please enter the data set. Press 'd' when done, and 'u' to undo.")
        while not done:
            element = input()
            if element == 'd':  # user is done entering data values
                return dataset
            elif element == 'u':  # undo the last data entry
                dataset.pop()
                continue
            elif element == 'q':  # quit the program
                quit = True
                break
            dataset.append(float(element))  # cast entry as a float and append to dataset
            print(dataset)  # prints dataset for user after entering each value
            
    significance = input("Please enter the significance level, as a decimal: ")
    if significance == 'q':  # quit the program
        quit = True
        break
    significance = float(significance)
    
    print("Are the samples dependent or independent?")
    print("1. Dependent")
    print("2. Independent")
    print("Press 'q' to quit.")
    dep_or_ind = input()

    print("Is this a left-tailed, right-tailed, or two-tailed test?")
    print("1. Left-tailed (Mean sample 1 < Mean sample 2)")
    print("2. Right-tailed (Mean sample 1 > Mean sample 2)")
    print("3. Two-tailed (Mean sample 1 != Mean sample 2)")
    left_right_two = input()
    
    if dep_or_ind == '1':  # dependent (matched pairs) datasets
        dataset1 = getDataSet()
        dataset2 = getDataSet()
        if len(dataset1) != len(dataset2):
            print("Datasets are not the same length.")
            quit = True
            break
        diffs = [dataset1[i] - dataset2[i] for i in range(len(dataset2))]  # calculate differences between datasets
        d_bar = np.mean(diffs)
        std_dev = np.std(diffs, ddof=1)
        sample_size = len(diffs)
        df = sample_size - 1

        test_statistic = d_bar/(std_dev/math.sqrt(sample_size))
        area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)
        ci_min = stats.t.interval(1-2*significance, df=df, loc=d_bar, scale=std_dev/math.sqrt(sample_size))[0]  # minimum of confidence interval
        ci_max = stats.t.interval(1-2*significance, df=df, loc=d_bar, scale=std_dev/math.sqrt(sample_size))[1]  # maximum of confidence interval
        print(f"\nMean sample difference: {d_bar:0.4f}")
        print(f"Sample standard deviation: {std_dev:0.4f}")
        print(f"Sample size: {sample_size}")
        print()
        print(f"Test statistic: {test_statistic:0.4f}")
        if left_right_two == '1':
            print(f"Mean sample 1 < Mean sample 2 critical value: {stats.t.ppf(significance,df):0.4f}")
            print(f"p-value: {area:0.4f}")
            print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
        elif left_right_two == '2':
            print(f"Mean sample 1 > Mean sample 2 critical value: {stats.t.ppf(1-significance,df):0.4f}")
            print(f"p-value: {1-area:0.4f}")
            print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
        elif left_right_two == '3':
            ci_min = stats.t.interval(1-significance, df=df, loc=d_bar, scale=std_dev/math.sqrt(sample_size))[0]  # minimum of confidence interval
            ci_max = stats.t.interval(1-significance, df=df, loc=d_bar, scale=std_dev/math.sqrt(sample_size))[1]  # maximum of confidence interval
            print(f"Mean sample 1 != Mean sample 2 critical values: {-1*math.fabs(stats.t.ppf(significance/2,df)):0.4f} and {math.fabs(stats.t.ppf(significance/2,df)):0.4f}")
            print(f"p-value: {2*min(area,1-area):0.4f}")
            print(f"{100*(1-significance):.0f}% Confidence Interval: {ci_min:0.4f}, {ci_max:0.4f}")
        print()
        
#####################################################################################################

    elif dep_or_ind == 'q' or dep_or_ind == 'Q':  # quit program
        quit = True
        break
        
#####################################################################################################
    
    elif dep_or_ind == '2':  # working with independent samples
        print("Are you entering data sets or summary statistics?")
        print("1. Data Sets")
        print("2. Summary Statistics")
        data_or_summary = input()
        
        print("Are the population variances assumed to be equal?")
        print("1. Yes")
        print("2. No")
        pool_or_no = input()
        
        if data_or_summary == '1':  # user will enter datasets
            dataset1 = getDataSet()
            dataset2 = getDataSet()
            diff = np.mean(dataset1) - np.mean(dataset2)
            df1 = len(dataset1) - 1
            df2 = len(dataset2) - 1
            
            if pool_or_no == '1':  # pooled samples
                df = df1 + df2
                var_p = ((df1 * np.var(dataset1, ddof=1)) + (df2 * np.var(dataset2, ddof=1)))/(df)
                sum_recips = (1/len(dataset1)) + (1/len(dataset2))
                test_statistic = diff/(math.sqrt(var_p) * math.sqrt(sum_recips))
                area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)
                ci_min = stats.t.interval(1-2*significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[0]  # minimum of confidence interval
                ci_max = stats.t.interval(1-2*significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[1]  # maximum of confidence interval
                print(f"Mean of sample 1 = {np.mean(dataset1):0.4f}")
                print(f"Sample standard deviation of sample 1 = {np.std(dataset1,ddof=1):0.4f}")
                print(f"Mean of sample 2 = {np.mean(dataset2):0.4f}")
                print(f"Sample standard deviation of sample 2 = {np.std(dataset2,ddof=1):0.4f}")
                print()
                print(f"Test statistic: {test_statistic:0.4f}")
                if left_right_two == '1':
                    print(f"Mean sample 1 < Mean sample 2 critical value: {stats.t.ppf(significance,df):0.4f}")
                    print(f"p-value: {area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
                elif left_right_two == '2':
                    print(f"Mean sample 1 > Mean sample 2 critical value: {stats.t.ppf(1-significance,df):0.4f}")
                    print(f"p-value: {1-area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
                elif left_right_two == '3':
                    ci_min = stats.t.interval(1-significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[0]  # minimum of confidence interval
                    ci_max = stats.t.interval(1-significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[1]  # maximum of confidence interval
                    print(f"Mean sample 1 != Mean sample 2 critical values: {-1*math.fabs(stats.t.ppf(significance/2,df)):0.4f} and {math.fabs(stats.t.ppf(significance/2,df)):0.4f}")
                    print(f"p-value: {2*min(area,1-area):0.4f}")
                    print(f"{100*(1-significance):.0f}% Confidence Interval: {ci_min:0.4f}, {ci_max:0.4f}")
                print()
            
            if pool_or_no == '2':  # non-pooled samples
                v1 = np.var(dataset1, ddof=1)/len(dataset1)
                v2 = np.var(dataset2, ddof=1)/len(dataset2)
                test_statistic = diff/math.sqrt(v1+v2)
                df = (v1 + v2)**2 / (v1**2/df1 + v2**2/df2)
                area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)
                ci_min = stats.t.interval(1-2*significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[0]  # minimum of confidence interval
                ci_max = stats.t.interval(1-2*significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[1]  # maximum of confidence interval
                print(f"Mean of sample 1 = {np.mean(dataset1):0.4f}")
                print(f"Sample standard deviation of sample 1 = {np.std(dataset1,ddof=1):0.4f}")
                print(f"Mean of sample 2 = {np.mean(dataset2):0.4f}")
                print(f"Sample standard deviation of sample 2 = {np.std(dataset2,ddof=1):0.4f}")
                print()
                print(f"Test statistic: {test_statistic:0.4f}")
                if left_right_two == '1':
                    print(f"Mean sample 1 < Mean sample 2 critical value: {stats.t.ppf(significance,df):0.4f}")
                    print(f"p-value: {area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
                elif left_right_two == '2':
                    print(f"Mean sample 1 > Mean sample 2 critical value: {stats.t.ppf(1-significance,df):0.4f}")
                    print(f"p-value: {1-area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
                elif left_right_two == '3':
                    ci_min = stats.t.interval(1-significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[0]  # minimum of confidence interval
                    ci_max = stats.t.interval(1-significance, df=df, loc=diff, scale=math.sqrt(np.var(dataset1, ddof=1)/len(dataset1) + np.var(dataset2, ddof=1)/len(dataset2)))[1]  # maximum of confidence interval
                    print(f"Mean sample 1 != Mean sample 2 critical values: {-1*math.fabs(stats.t.ppf(significance/2,df)):0.4f} and {math.fabs(stats.t.ppf(significance/2,df)):0.4f}")
                    print(f"p-value: {2*min(area,1-area):0.4f}")
                    print(f"{100*(1-significance):.0f}% Confidence Interval: {ci_min:0.4f}, {ci_max:0.4f}")
                print()
        
        elif data_or_summary == '2':  # user will enter summary statistics
            mean1, sd1, n1, mean2, sd2, n2 = getStats()
            diff = mean1 - mean2
            df1 = n1 - 1
            df2 = n2 - 1
            
            if pool_or_no == '1':  # pooled samples
                df = df1 + df2
                s_p = math.sqrt(((df1 * sd1**2) + (df2 * sd2**2))/(df1 + df2))
                test_statistic = diff / (s_p * math.sqrt(1/n1 + 1/n2))
                area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)
                ci_min = stats.t.interval(1-2*significance, df=df, loc=diff, scale=s_p * math.sqrt(1/n1 + 1/n2))[0]  # minimum of confidence interval
                ci_max = stats.t.interval(1-2*significance, df=df, loc=diff, scale=s_p * math.sqrt(1/n1 + 1/n2))[1]  # maximum of confidence interval
                print(f"\nTest statistic: {test_statistic:0.4f}")
                if left_right_two == '1':
                    print(f"Mean sample 1 < Mean sample 2 critical value: {stats.t.ppf(significance,df):0.4f}")
                    print(f"p-value: {area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
                elif left_right_two == '2':
                    print(f"Mean sample 1 > Mean sample 2 critical value: {stats.t.ppf(1-significance,df):0.4f}")
                    print(f"p-value: {1-area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
                elif left_right_two == '3':
                    ci_min = stats.t.interval(1-significance, df=df, loc=diff, scale=s_p * math.sqrt(1/n1 + 1/n2))[0]  # minimum of confidence interval
                    ci_max = stats.t.interval(1-significance, df=df, loc=diff, scale=s_p * math.sqrt(1/n1 + 1/n2))[1]  # maximum of confidence interval
                    print(f"Mean sample 1 != Mean sample 2 critical values: {-1*math.fabs(stats.t.ppf(significance/2,df)):0.4f} and {math.fabs(stats.t.ppf(significance/2,df)):0.4f}")
                    print(f"p-value: {2*min(area,1-area):0.4f}")
                    print(f"{100*(1-significance):.0f}% Confidence Interval: {ci_min:0.4f}, {ci_max:0.4f}")
                print()
                
            elif pool_or_no == '2':  # non-pooled samples
                v1 = sd1**2/n1
                v2 = sd2**2/n2
                df = (v1 + v2)**2 / (v1**2/df1 + v2**2/df2)
                se = math.sqrt(sd1**2/n1 + sd2**2/n2)
                test_statistic = diff / se
                area = stats.t.cdf(test_statistic, df=df, loc=0, scale=1)
                ci_min = stats.t.interval(1-2*significance, df=df, loc=diff, scale=se)[0]  # minimum of confidence interval
                ci_max = stats.t.interval(1-2*significance, df=df, loc=diff, scale=se)[1]  # maximum of confidence interval
                print(f"Mean of sample 1 = {mean1:0.4f}")
                print(f"Sample standard deviation of sample 1 = {sd1:0.4f}")
                print(f"Mean of sample 2 = {mean2:0.4f}")
                print(f"Sample standard deviation of sample 2 = {sd2:0.4f}")
                print()
                print(f"Test statistic: {test_statistic:0.4f}")
                if left_right_two == '1':
                    print(f"Mean sample 1 < Mean sample 2 critical value: {stats.t.ppf(significance,df):0.4f}")
                    print(f"p-value: {area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Upper Bound: {ci_max:0.4f}")
                elif left_right_two == '2':
                    print(f"Mean sample 1 > Mean sample 2 critical value: {stats.t.ppf(1-significance,df):0.4f}")
                    print(f"p-value: {1-area:0.4f}")
                    print(f"{100*(1-significance):.0f}% Lower Bound: {ci_min:0.4f}")
                elif left_right_two == '3':
                    ci_min = stats.t.interval(1-significance, df=df, loc=diff, scale=se)[0]  # minimum of confidence interval
                    ci_max = stats.t.interval(1-significance, df=df, loc=diff, scale=se)[1]  # maximum of confidence interval
                    print(f"Mean sample 1 != Mean sample 2 critical values: {-1*math.fabs(stats.t.ppf(significance/2,df)):0.4f} and {math.fabs(stats.t.ppf(significance/2,df)):0.4f}")
                    print(f"p-value: {2*min(area,1-area):0.4f}")
                    print(f"{100*(1-significance):.0f}% Confidence Interval: {ci_min:0.4f}, {ci_max:0.4f}")
                print()
