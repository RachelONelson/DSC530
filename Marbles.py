
'''
Problem Description:You and a friend have decided to play a game to drill your statistical intuitions.
The game works like this:
You have a bunch of red and blue marbles. To start the game you grab a handful of marbles of each
color and put them into the bag, keeping track of how many of each color go in. You take turns
reaching into the bag, guessing a color, and then pulling one marble out. You get a point if you
guessed correctly. The trick is you only have three seconds to make your guess, so you have to think
quickly.
You've decided to write a function, guess_blue() to help automatically calculate whether you should
guess "blue" or "red". The function should take four arguments:
    the number of blue marbles you put in the bag to start
    the number of red marbles you put in the bag to start
    the number of blue marbles pulled out so far, and
    the number of red marbles pulled out so far.
guess_blue() should return the probability of drawing a blue marble, expressed as a float. For example,
guess_blue(5, 5, 2, 3) should return 0.6.
'''


def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    # Your code here.
    return (blue_start - blue_pulled)/(blue_start - blue_pulled + red_start - red_pulled)

# Test Cases

print(guess_blue(5, 5, 2, 3))
print(guess_blue(5, 7, 4, 3))
print(guess_blue(12, 18, 4, 6))

'''A box contains 10 white balls, 20 reds, and 30 greens

what is probability of 3 white or 2 red
probability all 5 are the same color
'''

import numpy as np
import random

#create dictionary
d = {}

# assign 60 balls to a color
for i in range(60):
    if i <= 10:
        d[i] = 'white'
    elif i > 10 and i <=30:
        d[i] = 'red'
    else:
        d[i] = 'green'

#Number of simulations
n_simulations = 100000
part_a = 0
part_b = 0

for i in range(n_simulations):
    lst = []
    for i in range(5):
        lst.append(d[random.randint(0,59)])
    #convert to array
    lst = np.array(lst)

    #find number of ech that we picked
    white = sum(lst == 'white')
    red = sum(lst == 'red')
    green = sum(lst == 'green')


# keep track of if the combination met the above criteria
    if white == 3 and red == 2:
        part_a +=1
    if red == 5 or white == 5 or green == 5:
        part_b +=1

print(part_a/n_simulations*100,'%')
print(part_b/n_simulations*100,'%')
