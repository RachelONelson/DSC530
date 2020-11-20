from __future__ import print_function, division

#imports packages
import numpy as np
import sys
import nsfg
import thinkstats2

# reads pregnancy data from NSFG found on page 17 of text
preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]

# divides birth into first births and other births found on page 20 of text
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

first_hist = thinkstats2.Hist(firsts.prglngth, label='first births')
other_hist = thinkstats2.Hist(others.prglngth, label='other births')

# calculates the means of first and other births with fb = first births and ob = other births
fbm = firsts.prglngth.mean()
obm = others.prglngth.mean()
# calculates the standard deviations of first and other births
fstd = firsts.prglngth.std()
ostd = others.prglngth.std()

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
print("95% of first pregnancies give birth between "+"{:.2f}".format(fb95_min)+ " and "+"{:.2f}".format(fb95_max)+ " weeks, with the mean being "+"{:.2f}".format(fbm)+" weeks.")
print("95% of other pregnancies give birth between "+"{:.2f}".format(ob95_min)+ " and "+"{:.2f}".format(ob95_max)+ " weeks, with the mean being "+"{:.2f}".format(obm)+" weeks.")
print("98% of first pregnancies give birth between "+"{:.2f}".format(fb98_min)+ " and "+"{:.2f}".format(fb98_max)+ " weeks.")
print("98% of other pregnancies give birth between "+"{:.2f}".format(ob95_min)+ " and "+"{:.2f}".format(ob95_max)+ " weeks.")
print(firsts.prglngth.max())

"""
Which Summary statistic would you use if you wanted to get a story on the evening news?
Whoa Baby! First time pregnancies have a max pregnancy length of 48 weeks!

Which summary statistics would you use if you wanted to reassure an anxious parent?
I would tell the parent that the average birth for first time mothers is 38 weeks, with 95% of first pregnancies giving birth between 33-44 weeks.

Do first babies arrive late?
98% of first pregnancies give birth between 30.23 and 46.98 weeks while other pregnancies occur between 33.29 and 43.75 weeks. However, the 
average of both first and other babies born is 38 weeks. Due to this statistic, 
I would not make the conclusion that first babies arrive late, but instead have a three week more variability for the baby to be bore either before or after the 
average of 38 weeks. 
"""