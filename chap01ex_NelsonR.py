"""
Rachel Nelson
Chapter 01 Exercise 1-2
DSC530
"""

from __future__ import print_function, division

#imports packages
import numpy as np
import sys

import nsfg
import thinkstats2

#Reads 2002FebResp.dat.gz (Part 1) as a function
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    #reads dct_file
    dct = thinkstats2.ReadStataDct(dct_file)
    #creates a data frame
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    # returns the data frame
    return df

# Cross validates repondent and pregnancy files by comparing pregnm
# for each respondent with the number of records in the pregnancy file
def ValidatePregnum(respo):
    # reads the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # make the map from caseid to list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)

    # iterate respondent pregnum series
    for index, pregnum in respo.pregnum.items():
        caseid = respo.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from respondent file = pregnancy file
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    respo = ReadFemResp()

    assert(len(respo) == 7643)
    assert(respo.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(respo))

    print('%s: Tests Passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
