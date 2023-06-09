# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# GPS Works and Scripts Collection
# Author:   Steven Anderson
# Created:  MAY 2023
# Brief:    Algorithm that reads in an ephemeris message and
#           computes a satellite's ECEF position vector. Uses
#           OOP for practice.  Algorithm credit Kaplan.
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

import constantsKaplan as const
import math
import pandas as pd

class computedParams:
    semiMajorAxis = 0       # semi major axis [m]
    corrMeanMotion = 0      # corrected mean motion [rad/s]
    tk = 0                  # time from ephemeris epoch [s]
    Mk = 0                  # mean anomaly

# define local variables
t = 253848                  # receiver time
refTimeOfEphemeris = 0      # resultant reference time of ephemeris (with errors)

# create object(s)
sat2 = computedParams()

# read in ephmeris data as a dataframe
df = pd.read_csv('ephemeris2.csv')

# calculate semimajor axis
sat2.semiMajorAxis = df.loc[6].at['value']**2

# calculate corrected mean motion
sat2.corrMeanMotion = math.sqrt(const.mu / sat2.semiMajorAxis**3) + df.loc[14].at['value']

# calculate time from ephemeris epoch
# TODO: will need to give a t (GPS system time when signal transmitted)
# TODO: check all this time calculation...not sure on it
refTimeOfEphemeris = df.loc[2].at['value'] + df.loc[3].at['value'] + df.loc[4].at['value'] \
      + df.loc[5].at['value']  # t0e + L1/L2 correction + clock offset + clock drift
sat2.tk = t - refTimeOfEphemeris

# calculate Mean Anomaly (Mean anomaly at reference time + tk*corrected mean motion)
sat2.Mk = df.loc[2].at['value']

## PRINT RESULTS
print('  Semi Major Axis (m): ', sat2.semiMajorAxis)
print('  Corrected Mean Motion (rad/s): ', sat2.corrMeanMotion)
print('  Time from Ephemeris (rs): ', sat2.tk)
