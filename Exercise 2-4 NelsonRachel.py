from __future__ import print_function, division

#imports packages
import numpy as np
import sys
import nsfg
import thinkstats2
import math
import matplotlib



# reads pregnancy data from NSFG found on page 17 of text
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

# divides birth into first births and other births found on page 20 of text
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

group1 = live[live.birthord == 1]
group2 = live[live.birthord != 1]

first_hist = thinkstats2.Hist(firsts.totalwgt_lb, label='first births')
other_hist = thinkstats2.Hist(others.totalwgt_lb, label='other births')

# calculates the means of first and other births with fb = first births and ob = other births
fbm = firsts.totalwgt_lb.mean()
obm = others.totalwgt_lb.mean()
# calculates the standard deviations of first and other births
fstd = firsts.totalwgt_lb.std()
ostd = others.totalwgt_lb.std()
print("{:.2f}".format(fstd)+ " = first time baby std")
print("{:.2f}".format(ostd)+ " = other baby std")

# standard statistics
mean = firsts.totalwgt_lb.mean()
var = firsts.totalwgt_lb.var()
std = firsts.totalwgt_lb.std()

# looks at the empirical rule (95/99.7) distributions by calculating sigma
# standard deviations * mean with fb = first births and ob = other births
fb95_max = fbm + (fstd*2)
fb95_min = fbm + -(fstd*2)
ob95_max = obm + (ostd*2)
ob95_min = obm + -(ostd*2)
fb98_max = fbm + (fstd*3)
fb98_min = fbm + -(fstd*3)
ob98_max = obm + (ostd*3)
ob98_min = obm + -(ostd*3)


#Summary Statistics
print("95% of first pregnancies have babies between "+"{:.2f}".format(fb95_min)+ " and "+"{:.2f}".format(fb95_max)+ " lbs, with the mean being "+"{:.2f}".format(fbm)+" lbs.")
print("95% of other pregnancies have babies between "+"{:.2f}".format(ob95_min)+ " and "+"{:.2f}".format(ob95_max)+ " lbs, with the mean being "+"{:.2f}".format(obm)+" lbs.")
print("98% of first pregnancies have babies between "+"{:.2f}".format(fb98_min)+ " and "+"{:.2f}".format(fb98_max)+ " lbs.")
print("98% of other pregnancies have babies between "+"{:.2f}".format(ob95_min)+ " and "+"{:.2f}".format(ob95_max)+ " lbs.")

#calculate cohen d
def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()

    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1+n2)
    d = diff / math.sqrt(pooled_var)
    return d

#gets cohen's distance for first time and compares to other birth baby weights
wtdiffb = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)

#gets cohen's distance for first time and compares to other pregnancy lengths
wtdiffw = CohenEffectSize(firsts.prglngth, others.prglngth)

print("The difference between birth weights in groups is " +"{:.2f}".format(wtdiffb))
print("The difference between pregnancy lengths in groups is " +"{:.2f}".format(wtdiffw))

"""
Investigate whether first babies are lighter or heavier than others
First babies weigh a mean of 7.2 lbs, while other babies weigh a mean of 7.33 lbs. 
The difference of means suggest that first babies are lighter than other babies since both of a standard deviation around 1.4 lbs
The difference between birth weights in groups is -0.09 while the difference between pregnancy lengths is 0.03 with weights showing a small decrease (meaning lighter weights) 
and lengths showing a smaller positive increase (meaning longer time)
"""