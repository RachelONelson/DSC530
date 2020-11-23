import numpy as np
import thinkplot
import pandas as pd
import thinkstats2
import statistics

#%% Import Data table from credit card csv file and gives the header and summary of the table

data = pd.read_csv("creditcard.csv")
data.head(5)
data.describe()
fraud = data[data.Class == 1]
others = data[data.Class != 1]

rand = np.random.random(1000)
answer = statistics.median(data.Amount)
answer2 = statistics.mean(data.Amount)

# Counts fraud and non fraud then divides the two and prints result
n = len(fraud)


# Simulation probability of flipping heads
ph = 0.5
# Number of coin flips to simulate
num_flips = 25
# Simulate Coin flips
def flip_coin(N, p=0.5):
    prob = [p, (1 - p)]
    return np.random.choice(['H','T'], size=N, p=prob)
# Accumulate flips
flips=flip_coin(num_flips, ph)
# Count Heads
num_heads = np.sum(flips == 'H')
# Display results
print("Flips:", " ".join(flips))
print(f"Number of Heads: {num_heads}")
print(f'P(H) = {num_heads/num_flips} (Number of Heads/Total Flips)')


# Assume equal probability over all states
prob_die = 6 * [(1/6)]
# Number of dice rolls
num_rolls = 25
# Simulate a dice roll
def roll_die(N, prob = prob_die):
    return np.random.choice(['1', '2', '3', '4', '5', '6'], size=N, p=prob)
# Accumulate rolls
rolls=roll_die(num_rolls)
# Accumulate rolls of an 'Ace'
num_ones = np.sum(rolls == '1')
#Display results
print("Rolls:", " ".join(rolls))
print(f"Number of Ones: {num_ones}")
print(f'P(1) = {num_ones/num_rolls} (Number of Ones/Total Rolls)')





import random
def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
        return heads
def simulate(n):
    trials = []
    for i in range(n):
        trials.append(coin_trial())
    return(sum(trials)/n)
print(simulate(10))
simulate(100)
simulate(1000)
simulate(1000000)

import numpy as np

# sets up a dictonary that will randomly choose
d = {}

#60 marbles
for i in range(60):
    # number of white marbles is 10
    if i < 10:
        d[i] = 'White'
    # mi,ber pf red marbles is 20
    elif i > 9 and i < 30:
        d[i] = 'red'
    # of green marbles is 30
    else:
        d[i] = 'green'

#initialize important variables
n_sumulations = 100000
parta = 0
partb = 0

# run simulation
for i in range(n_sumulations):
    lst = []
    for i in range(500):
        lst.append(d[random.randint(0, 59)])

#converto to a numpy array
lst = np.array(lst)

white = sum(lst == 'White')
red = sum(lst == 'red')
green = sum(lst == 'green')

if white == 3 and red == 2:
    parta +=1
if red == 5 or white == 5 or green == 5:
    partb +=1

print((parta/n_sumulations)*100)
print('The probability of 3 whites and two reds is:',parta/n_sumulations*100,'%')
print('The probability of 3 whites and two reds is:' ,partb/n_sumulations*100,'%')



# Sample Space
cards = 52
# Outcomes
aces = 4
# Divide possible outcomes by the sample set
ace_probability = aces / cards
# Print probability rounded to two decimal places
print(round(ace_probability, 2))
ace_probability_percent = ace_probability * 100
# Print probability percent rounded to one decimal place
print(str(round(ace_probability_percent, 0)) + '%')


