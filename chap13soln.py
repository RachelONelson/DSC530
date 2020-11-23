"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function
import pandas
import numpy as np
import thinkplot
import thinkstats2
import survival
import nsfg




def CleanData(resp):
    resp.cmdivorcx.replace([9998, 9999], np.nan, inplace=True)
    resp['notdivorced'] = resp.cmdivorcx.isnull().astype(int)
    resp['duration'] = (resp.cmdivorcx - resp.cmmarrhx) / 12.0
    resp['durationsofar'] = (resp.cmintvw - resp.cmmarrhx) / 12.0
    month0 = pandas.to_datetime('1899-12-15')
    dates = [month0 + pandas.DateOffset(months=cm) 
             for cm in resp.cmbirth]
    resp['decade'] = (pandas.DatetimeIndex(dates).year - 1900) // 10


def ResampleDivorceCurve(resps):
    for _ in range(41):
        samples = [thinkstats2.ResampleRowsWeighted(resp) 
                   for resp in resps]
        sample = pandas.concat(samples, ignore_index=True)
        PlotDivorceCurveByDecade(sample, color='#225EA8', alpha=0.1)
    thinkplot.Show(xlabel='years',
                   axis=[0, 28, 0, 1])


def ResampleDivorceCurveByDecade(resps):
    for i in range(41):
        samples = [thinkstats2.ResampleRowsWeighted(resp) 
                   for resp in resps]
        sample = pandas.concat(samples, ignore_index=True)
        groups = sample.groupby('decade')
        if i == 0:
            survival.AddLabelsByDecade(groups, alpha=0.7)
        EstimateSurvivalByDecade(groups, alpha=0.1)
    thinkplot.Save(root='survival7',
                   xlabel='years',
                   axis=[0, 28, 0, 1])


def EstimateSurvivalByDecade(groups, **options):
    thinkplot.PrePlot(len(groups))
    for name, group in groups:
        print(name, len(group))
        _, sf = EstimateSurvival(group)
        thinkplot.Plot(sf, **options)


def EstimateSurvival(resp):
    complete = resp[resp.notdivorced == 0].duration
    ongoing = resp[resp.notdivorced == 1].durationsofar
    hf = survival.EstimateHazardFunction(complete, ongoing)
    sf = hf.MakeSurvival()
    return hf, sf

# cycles 6 and 7
resp6 = survival.ReadFemResp2002()
resp7 = survival.ReadFemResp2010()

CleanData(resp6)
CleanData(resp7)

married6 = resp6[resp6.evrmarry==1]
married7 = resp7[resp7.evrmarry==1]

#ResampleDivorceCurveByDecade([married6, married7])
