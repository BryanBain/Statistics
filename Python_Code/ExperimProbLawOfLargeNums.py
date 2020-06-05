import random as rd

possibilities = ['H', 'T'] 
num_tails = 0
num_flips = 1_000_000  # change this value to adjust the number of coin flips.

for _ in range(num_flips):
    result = rd.choice(possibilities)  # flip the coin
    if result == 'T':
        num_tails += 1

print(f'The probability of flipping tails is {num_tails/num_flips}')