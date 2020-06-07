"""
Purpose: Computer simulation of flipping a coin several times to examine the
staistical significance of an event happening.

Author: Bryan Bain 
    
Date: June 7, 2020
    
File: StatisSignifCoinFlip.py
"""

import random as rd

coin = ['H', 'T']
tails_count = 0
successes = 0
num_flips = 10_000

for _ in range(num_flips):
    for i in range(100):  # 100 flips each time
        if rd.choice(coin) == 'T':  # coin came up tails
            tails_count += 1  # add 1 to the tails count
    if tails_count >= 90:  # going to see if tails comes up at least 90 times
        successes += 1  # if it does, increase the successes count
    tails_count = 0. # reset tails count for the next 100 flips

print(f'The probability of obtaining at least 90 tails in 100 flips '
      f'of a coin is {100*successes/num_flips:.6f}%')
