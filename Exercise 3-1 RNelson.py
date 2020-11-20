"""
title: "Exercise 3-1"
author: Rachel Nelson
date: 9/26/2020
class: DSC530-T303 Data Exploration and Analysis (2211-1)
"""

#import packages
import numpy as np
import pandas
import nsfg
import first
import thinkstats2
import thinkplot

# NSFG respondent variable NUMKDHH to construction the actual distribution for the
# number of children under 18 in the household
resp = nsfg.ReadFemResp()
pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')


# computer the biased distributoin we would see if surveyed the children and asked them how
# many children including themselves are under 18 in their household
def BiasPmf(pmf, label):
    new_pmf = pmf.Copy(label=label)
    for x, p in pmf.Items():
        new_pmf.Mult(x, x)
    new_pmf.Normalize()
    return new_pmf

#plot actual and observed distributions
biased_pmf = BiasPmf(pmf, label='observed')
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Config(xlabel='Number of children', ylabel='pmf')
thinkplot.show()

# compute their means
print('The actual mean is: ', "{:.2f}".format(pmf.Mean()))
print('The biased mean is: ', "{:.2f}".format(biased_pmf.Mean()))




