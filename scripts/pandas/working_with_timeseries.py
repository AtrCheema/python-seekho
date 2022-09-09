"""
=============================
5.3 working with timeseries
=============================

In this file you will learn about following concepts of pandas

- TimeStamp
- DateTimeIndex
- freq
- Timedelta
- Period
- asfreq
- offsets
- resampling

"""

import numpy as np
import pandas as pd

print(np.__version__)
print(pd.__version__)

#%%

pd.set_option('display.max_rows', 20)

#%%
# Let's define a dataframe and check its index

df = pd.DataFrame(np.arange(31))

print(df.index)

#%%
# the index is a range from 0 to 1 with step size of 1 of type ``RangeIndex``.

df

#%%
# we can verify the type of index

print(type(df.index))

#%%
# Let's define a more useful index for the dataframe i.e., dates with daily time step

index = [f"2011-01-{i}" for i in range(1, 32)]

print(index)

#%%
# assign this index to dataframe

df.index = index

df

#%%

print(type(df.index))

#%%
# still pandas does not recognize the index as date/time

##################################################
# we can explicitly pandas that the new index is a date and time index

index = pd.to_datetime(index)

print(index)

#%%

print(type(index))

#%%
# now we have created an index whose type is DateTimeIndex i.e. pandas recognizes
# it as date/time. Let's assign this as index to the dataframe.

df.index = index

print(df.index)

#%%
# So now the type of index of the dataframe is date/time.
#
# The `DateTimeIndex` is indeed an array of `TimeStamps` i.e. each member
# of DateTimeIndex is a TimeStamp.

print(df.index[0])

#%%

print(type(df.index[0]))


##################################
# creating datetime index
#========================
# Above we converted a normal index which was of type list into DateTimeIndex using
# ``to_datetime`` function. We can directly create DateTimeInex using ``date_range`` function.

index = pd.date_range(start="20110101", freq="D", periods=31)

print(type(index))

#%%

print(index)

#%%
# We can also define the frequency or time-step of our DateTimeIndex.

index = pd.date_range(start="20110101", end="20110131", freq="D")

print(type(index))

#%%

print(index)

#%%
# the index (of dataframe) has a special attribute called ``freq`` which defines the time-step
# of the index. It is only available for the index of type ``DateTimeIndex``.

print(df.index.freq)

#%%
# There can be two reasons for the ``freq`` to be None. Either the data/DateTimeIndex does not
# have constant time-steps. In such a case freq (time-step) can not be computed. But sometimes
# even if the index is of type DateTimeIndex and has constant time-step but it can have None freq.
# This is what happened above. In both cases we can ask pandas to infer the freq/time-step
# of the index.

print(pd.infer_freq(df.index))

#%%
# Now we can assign the frequency to the DataFrame.index (not DataFrame).
# This is kind of reminding the DataFrame that this is the time-step of your index.

df.index.freq = pd.infer_freq(df.index)

print(df.index.freq)

#%%
# we can see once 'reminded', the pandas now tells us the frequency of its index.

print(type(df.index.freq))

#%%

print(type(df.index.freqstr))

#######################################
# forcing a frequency
#---------------------

df = pd.DataFrame(np.arange(31),
                  index=pd.date_range("20110101", periods=31, freq="D"))

#%%
df

#%%
df.index.freq

#%%
df = df.drop(labels="2011-01-03")

df

#%%
df.index.freq

#%%
pd.infer_freq(df.index)

#%%
# if we forcefully try to assign a frequency, pandas will throw ``ValueError``.

# Try by uncommenting following line

# df.index.freq = "D"  # -> ValueError

#%%

df.asfreq('D')

#%%

######################################
# advantages of having a frequency
#---------------------------------
# One major advantage of having a frequency i.e `freq` attribute
# defined is that we can easily change the frequency/time-step of
# the data (timeseries).

# resampling

#%%
# upsampling
#-----------
# changing the timestep from larger to smaller such as from daily to hourly
df = pd.DataFrame(np.random.randint(0, 5, 5),
                  index=pd.date_range("20110101", periods=5, freq="D"),
                  columns=['a'])
df

#%%

df.resample("6H")

#%%

df.resample("6H").mean()

#%%

df.resample("6H").ffill()
#%%

df.resample("6H").mean().ffill()

#%%

df.resample("6H").interpolate(method="linear")

#%%
# sometimes, we may wish to equally distribute a quantity during upsampling
# For example if we have total amount of rainfall for a day, then linearly
# interpolating daily rainfall values to hourly will be wrong. In such a
# case we will wish to distribute daily rainfall to equally to hourly steps

df1 = df.resample('6H').mean().ffill()
df1['a'] = df1['a'] / df1.groupby('a')['a'].transform(len)  # len/'size'
df1


#%%
# downsampling
#-------------
# from low timestep to high timestep e.g.  from hourly to daily

df = pd.DataFrame(np.random.randint(0, 5, 24),
                  index=pd.date_range("20110101", periods=24, freq="H"),
                  columns=['a'])
df

#%%

df.resample("6H").mean()

#%%

df.resample("6H").sum()

#%%
# changing frequency
#--------------------
# Sometimes we have quantities, which are not measured at exactly the same
# frequency where we want. For example below data is measured with inconsistent
# time-steps.

df = pd.DataFrame([np.nan, 1100, 1400, np.nan, 14000],
                   index=pd.to_datetime(["2011-05-25 10:00:00",
                                         "2011-05-25 16:40:00",
                                         "2011-05-25 17:06:00",
                                         "2011-05-25 17:10:00",
                                         "2011-05-25 17:24:00"]),
                  columns=['a'])

df

#%%
# Our target is to convert this data to 6 minute. A naive way would
# be to change the frequency and do not fill the new nans.

df.resample('6Min').first()

#%%
# You see the number of values change from 5 to 75
#
# a better option will be to do backfill or forward fill

df.resample('6min').bfill(limit=1)

#%%
# it will be even better to do a linear interpolation between available values.

df.resample('6min').interpolate()


#%%
df.resample('6min').interpolate('nearest')

#%%
# PeriodIndex
#------------
# Similar to the concept of DateTimeIndex is the concept of PeriodIndex. Just as a DateTimeIndex
# can be considered as an array of TimeStamps, a PeriodIndex is array of Period. A Period is an
# interval between two TimeStamps. Therefore a Period has ``start_time``
# and ``end_time`` attributes

p = pd.Period("2011-01-01")

print(type(p))

#%%

p.start_time

#%%

p.end_time

#%%

print(type(p.start_time)), print(type(p.end_time))

#%%

p.freq

#%%

pidx = pd.period_range("20110101", "20121231", freq="M")
pidx

#%%
print(type(pidx))


#%%
# each member of PeriodIndex **pidx** is a Period

print(type(pidx[0]))

#%%
# For an overview of difference between TimeStamp and PeriodIndex, see
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#overview