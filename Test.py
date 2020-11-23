import numpy as np
import pandas as pd
import thinkplot
import thinkstats2
import first
import statsmodels.formula.api as smf
import nsfg
import regression
import timeseries


live, firsts, others = first.MakeFrames()
live = live[live.prglngth>30]
resp = nsfg.ReadFemResp()
resp.index = resp.caseid

# join tables using caseid
join = live.join(resp, on='caseid', rsuffix='_r')

# replace with NaN in numbabes column
join.numbabes.replace([97], np.nan, inplace=True)
join['age2'] = join.age_r**2

