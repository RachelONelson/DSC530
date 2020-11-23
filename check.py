import numpy as np
import sys
import thinkstats2
import first
import pandas
import nsfg
import first
import statsmodels.formula.api as smf

live, firsts, others = first.MakeFrames()
live = live[live.prglngth>30]
resp = nsfg.ReadFemResp()
resp.index = resp.caseid
join = live.join(resp, on='caseid', rsuffix='_r')

