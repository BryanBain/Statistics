"""
Purpose: Create a scatterplot of a bivariate dataset and
determine the linear regression equation, linear correlation
coefficient, and the coefficient of determination.

Author: Bryan Bain

Date: June 30, 2020

File name: Linear_Regression.py
"""

import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

x = []
y = []

fig, ax = plt.subplots()
slope, intercept, r, p, std_err = stats.linregress(x,y)
x1 = np.linspace(min(x)-1,max(x)+1,1000)
y1 = slope*x1 + intercept
ax.plot(x,y,'bo',x1,y1)
ax.grid()
plt.show()
print(f'Slope: {slope:0.4f}')
print(f'Y-intercept: {intercept:0.4f}')
print(f'r: {r:0.4f}')
print(f'r^2: {r*r:0.4f}')

