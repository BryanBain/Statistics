#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 19:41:15 2020

@author: bryanbain
"""

from scipy.stats import norm

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