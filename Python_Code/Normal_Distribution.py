#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:41:15 2020

@author: bryanbain
"""

from scipy.stats import norm

def obsToZ(x, mu, sigma):
    """
    Converts an observed value to its z score.
    x: the observed value
    mu: the mean
    sigma: the standard deviation
    """
    return (x - mu) / sigma

# Find area/prob/percent/etc

print("Are you given a z score or an observed value?: ")
print("1. z score")
print("2. observed value")
z_or_obs = input()

if z_or_obs == "1":
    print("Please select the area you are trying to find.\n")
    print("1. Area to the left")
    print("2. Area to the right")
    print("3. Area between two z scores")
    print("4. Area outside two z scores")
    z_option = input()
    if z_option == "1":
        z_score = float(input("Please enter the z score: "))
        area = norm.cdf(z_score)
        print(f"The area to the left of z = {z_score} is {area:0.4f}")
    elif z_option == "2":
        z_score = float(input("Please enter the z score: "))
        area = norm.sf(z_score)
        print(f"The area to the right of z = {z_score} is {area:0.4f}")  
    elif z_option == "3":
        z_score1 = float(input("Please enter the lower z score: "))
        z_score2 = float(input("Please enter the higher z score: "))
        area = norm.cdf(z_score2) - norm.cdf(z_score1)
        print(f"The area between z = {z_score1} and z = {z_score2} "
              f"is {area:0.4f}")
    elif z_option == "4":
        z_score1 = float(input("Please enter the lower z score: "))
        z_score2 = float(input("Please enter the higher z score: "))
        area = 1 - (norm.cdf(z_score2) - norm.cdf(z_score1))
        print(f"The area outside of z = {z_score1} and z = {z_score2} "
              f"is {area:0.4f}")
elif z_or_obs == "2":
    print("Please select the area you are trying to find.\n")
    print("1. Area to the left")
    print("2. Area to the right")
    print("3. Area between two z scores")
    print("4. Area outside two z scores")
    x_option = input()
    if x_option == "1":
        obs_value = float(input("Please enter the observed value: "))
        mu = float(input("Please enter the mean: "))
        sigma = float(input("Please enter the standard deviation: "))
        area = norm.cdf(obs_value, mu, sigma)
        print(f"The area to the left of x = {obs_value} is {area:0.4f}")
    elif x_option == "2":
        obs_value = float(input("Please enter the observed value: "))
        mu = float(input("Please enter the mean: "))
        sigma = float(input("Please enter the standard deviation: "))
        area = norm.sf(obs_value, mu, sigma)
        print(f"The area to the right of x = {obs_value} is {area:0.4f}")  
    elif x_option == "3":
        obs_value1 = float(input("Please enter the smaller observed value: "))
        obs_value2 = float(input("Please enter the larger observed value: "))
        mu = float(input("Please enter the mean: "))
        sigma = float(input("Please enter the standard deviation: "))
        area = norm.cdf(obs_value2, mu, sigma) - norm.cdf(obs_value1, mu, sigma)
        print(f"The area between x = {obs_value1} and x = {obs_value2} "
              f"is {area:0.4f}")
    elif x_option == "4":
        obs_value1 = float(input("Please enter the smaller observed value: "))
        obs_value2 = float(input("Please enter the larger observed value: "))
        mu = float(input("Please enter the mean: "))
        sigma = float(input("Please enter the standard deviation: "))
        area = 1 - (norm.cdf(obs_value2, mu, sigma) - norm.cdf(obs_value1, mu, sigma))
        print(f"The area outside of x = {obs_value1} and x = {obs_value2} "
              f"is {area:0.4f}")


# Find observed value

print("Are you finding a z score or an observed value?: ")
print("1. z score")
print("2. observed value")
z_or_obs = input()

if z_or_obs == "1":
    print("Please select the area you are given.\n")
    print("1. Area to the left")
    print("2. Area to the right")
    print("3. Middle area two z scores")
    print("4. Area outside of two middle z scores")
    z_option = input()
    if z_option == "1":
        lt_area = float(input("Please enter the area (as a decimal) to the left: "))
        z_score = norm.ppf(lt_area)
        print(f"z = {z_score:0.3f} has an area of {lt_area} to the left")
    elif z_option == "2":
        rt_area = float(input("Please enter the area (as a decimal) to the right: "))
        z_score = norm.isf(rt_area)
        print(f"z = {z_score:0.3f} has an area of {rt_area} to the right") 
    elif z_option == "3":
        mid_area = float(input("Please enter the area (as a decimal) in the middle: "))
        z_scores = norm.interval(mid_area)
        print(f"The z scores are z = {z_scores[0]:0.3f} and z = {z_scores[1]:0.3f}")
    elif z_option == "4":
        out_area = float(input("Please enter the total area (as a decimal) outside the middle: "))
        z_scores = norm.interval(1 - out_area)
        print(f"The z scores are z = {z_scores[0]:0.3f} and z = {z_scores[1]:0.3f}")
        
elif z_or_obs == "2":
    # obs_value = float(input("Please enter the observed value: "))
    mu = float(input("Please enter the population mean: "))
    sigma = float(input("Please enter the standard deviation: "))
    # z_score = obsToZ(obs_value, mu, sigma)
    print("Please select the area you are given.\n")
    print("1. Area to the left")
    print("2. Area to the right")
    print("3. Middle area two z scores")
    print("4. Area outside of two middle z scores")
    x_option = input()
    if x_option == "1":
        lt_area = float(input("Please enter the area (as a decimal) to the left: "))
        obs_value = norm.ppf(lt_area, mu, sigma)
        print(f"x = {obs_value:0.3f} has an area of {lt_area} to the left")
    elif x_option == "2":
        rt_area = float(input("Please enter the area (as a decimal) to the right: "))
        obs_value = norm.isf(rt_area, mu, sigma)
        print(f"z = {obs_value:0.3f} has an area of {rt_area} to the right") 
    elif x_option == "3":
        mid_area = float(input("Please enter the area (as a decimal) in the middle: "))
        obs_values = norm.interval(mid_area, mu, sigma)
        print(f"The observed values are x = {obs_values[0]:0.3f}"
              f" and x = {obs_values[1]:0.3f}")
    elif x_option == "4":
        out_area = float(input("Please enter the total area (as a decimal) outside the middle: "))
        obs_values = norm.interval(1 - out_area, mu, sigma)
        print(f"The observed values are x = {obs_values[0]:0.3f} "
              f"and x = {obs_values[1]:0.3f}")