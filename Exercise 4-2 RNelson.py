"""
title: "Exercise 4-2"
author: Rachel Nelson
date: 9/26/2020
class: DSC530-T303 Data Exploration and Analysis (2211-1)
"""
# import
import numpy as np
import nsfg
import first
import thinkstats2
import thinkplot

#Generates 1000 numbers from random.random
rand = np.random.random(1000)

#plots the PMF of the random numbers
pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Random numbers', ylabel='PMF')
thinkplot.show()

#plots the CDF of the random numbers
cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Random numbers', ylabel='CDF')
thinkplot.show()

print("Because the CDF is appproximately a straight line, the distribution is uniform")

