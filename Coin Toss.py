import numpy as np
import random
import thinkstats2
import thinkplot

class CoinTest(thinkstats2.HypothesisTest):

    def TestStatistic(self, data):
        heads, tails = data
        test_stat = abs(heads - tails)
        return test_stat

    def RunModel(self):
        heads, tails = self.data
        n = heads + tails
        sample = [random.choice('HT') for _ in range(n)]
        hist = thinkstats2.Hist(sample)
        data = hist['H'], hist['T']
        return data

ct = CoinTest((140, 110))
pvalue = ct.PValue()
print(pvalue)

'''Probably of rolling a number for a dice'''
# function to roll the dice
def rtd(n_simulations = 100000):
    count = 0

    for i in range(n_simulations):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        score = die1 + die2
        if score / 2 == 0 or score > 7:
            count += 1
    return count/n_simulations
print('the probability of rolling an even number or greater than 7 is:',np.round(rtd()*100,2),'%')
