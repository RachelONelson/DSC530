
"""
title: "Week 5 Exercises 5-1, 5-2, 6-1"
author: Rachel Nelson
date: 10/3/2020
class: DSC530-T303 Data Exploration and Analysis (2211-1)
"""
# import
import numpy as np
import thinkstats2
import thinkplot
import brfss
import hinc
import scipy.stats
import statistics
from scipy.stats import skew
# Exercise 5-1
# defines the mean and standard deviation
mean = 178
std = 7.7
# get the loc mean and std using scipy.stats.norm
dist = scipy.stats.norm(loc=mean, scale=std)
# uses the dist to get the low and high and then calculates the % within the range
# 5'10 and 6'1 have been converted to centimeters
low = dist.cdf(177.8)
high = dist.cdf(185.42)
answer = (high-low)*100 # take the high and minus the low cdf to get the population, times by 100 to get %
print(
'The % of US male population between 5 feet and 10 inches and 6 feet and 1 inch is', "{:
.2f}".format(answer),"%")
print(
'
'
) # prints blank line to separate exercises
# Exercise 5-2
# The parameters xm and α determine the location and shape of the distribution
xm = 1
α = 1.7
median = 1.5
# Plots the distribution
dist = scipy.stats.pareto(b=α, scale=xm)
# What is the mean height in pareto?
answer = dist.mean()
print(
'The mean height in Pareto world is is', "{:
.2f}".format(answer)
)
# What fraction of people are shorter than the mean?
answer = dist.cdf(dist.mean()
)
print(
'The fraction of the population shorter than the mean is', "{:
.2f}".format(answer)
)
# Out of 7 billion people, how many do we expect to be taller than 1 km?
answer = (1 - dist.cdf(1000)
) * 7e9
print(
'Out of 7 billion people, we expect',"{:
.0f}".format(answer), 'to be taller than 1 km'
)
#How tall do we expect the tallest person to be?
answer = dist.ppf(1 - 1/7e9)
print(
'We expect the tallest person to be',"{:
.2f}".format(answer), 'tall'
)
print(
'
'
) # prints blank line to separate exercises
# Exercise 6-1
def InterpolateSample(df, log_upper=6.0)
:
"""Makes a sample of log10 household income.
Assumes that log10 income is uniform in each range.
df: DataFrame with columns income and freq
log_upper: log10 of the assumed upper bound for the highest range
returns: NumPy array of log10 household income
"""
# compute the log10 of the upper bound for each range
df[
'log_upper'
] = np.log10(df.income)
# get the lower bounds by shifting the upper bound and filling in
# the first element
df[
'log_lower'
] = df.log_upper.shift(1)
df.loc[0, 'log_lower'
] = 3.0
# plug in a value for the unknown upper bound of the highest range
df.loc[41, 'log_upper'
] = log_upper
# use the freq column to generate the right number of values in
# each range
arrays = []
for _, row in df.iterrows()
:
vals = np.linspace(row.log_lower, row.log_upper, int(row.freq)
)
arrays.append(vals)
# collect the arrays into a single sample
log_sample = np.concatenate(arrays)
return log_sample
# reads data from the hinc data source into a dataframe
income_df = hinc.ReadData()
log_sample = InterpolateSample(income_df, log_upper=6.0)
log_cdf = thinkstats2.Cdf(log_sample)
thinkplot.Cdf(log_cdf)
thinkplot.Config(xlabel='Household income (log $)
',
ylabel='CDF'
)
sample = np.power(10, log_sample)
cdf = thinkstats2.Cdf(sample)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='Household income ($)
',
ylabel='CDF'
)
thinkplot.show()
# Compute the median, mean, skewness and pearson's skewness of the sample
answer = sample.mean()
print(
'The mean of the sample is',"{:
.2f}".format(answer)
)
answer = statistics.median(sample)
print(
'The median of the sample is',"{:
.2f}".format(answer)
)
answer = skew(sample)
print(
'The skewness of the sample is',"{:
.2f}".format(answer)
)
answer = (3 * (sample.mean() - statistics.median(sample)
)
)/sample.std()
print(
'The pearsons median skewness of the sample is',"{:
.2f}".format(answer)
)
# what fraction of households reports a taxable income below the mean?
answer = cdf.Prob(sample.mean()
)*100
print("{:
.0f}".format(answer),
'% of households reports a taxable income below the mean'
)
# how do the results depend on the assumed upper bound?
print(
'To estimate mean and other statistics from this data, we have to make some assumptions about the upper bound'
)
