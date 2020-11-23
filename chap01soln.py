"""Chapter 01"""


from __future__ import print_function, division

#imports packages
import numpy as np
import sys
import nsfg
import thinkstats2



#Reads respondent file 2002FebResp.data.gz
def ReadFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz',
                nrows=None):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', nrows=nrows)
    CleanFemResp(df)
    return df


def CleanFemResp(df):
    pass

# Prints the value counts for the "pregnum" variable
def ValidatePregnum(resp):
    # read the pregnancy frame
    preg = nsfg.ReadFemPreg()

    # Uses .nsfg.makepregmap to make a dictionary that maps from each caseid to a list of idices into the pregnancy dataframe
    preg_map = nsfg.MakePregMap(preg)
    
    # iterate through the respondent pregnum series
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]

        # check that pregnum from the respondent file equals # records in pregnancy files
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True


def main(script):
    resp = ReadFemResp()

    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))

    print('%s: Tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
