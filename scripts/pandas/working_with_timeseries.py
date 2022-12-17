"""
=============================
5.3 working with time series
=============================

.. important::
  This lesson is still under development.

In this file you will learn about following concepts of pandas

- DateTimeIndex
- TimeStamp
- freq
- Timedelta
- offsets
- resampling
- Period

"""

import numpy as np
import pandas as pd

pd.set_option('display.max_rows', 20)

print(np.__version__)
print(pd.__version__)

#%%
# Let's define a dataframe and check its index

df = pd.DataFrame(np.arange(31))

print(df)

# %%
# Since dataframe is nothing but numpy arrays with indexes which means each row and column
# has a label (index). Therefore, we can also interpret dataframes as indexed numpy arrays.
# When we create a dataframe, pandas automatically assigns a suitable index (row labels) to it.

print(df.index)

#%%
# The index is a range from 0 to 1 with step size of 1 and is of of type ``RangeIndex``.

#%%
# we can verify the type of index

print(type(df.index))

# %%
# DateTimeIndex
# ========================
# Let's define a more useful index for the dataframe i.e., dates with daily time step

index = [f"2011-01-{i}" for i in range(1, 32)]

print(index)

#%%
# At this point the `index` is a list of strings where each string indicates a day/date.

#%%
# Now let's assign this index to our dataframe

df.index = index

print(df)

#%%
# We can see that the index of our the dataframe is now the date.
# But does pandas recognizes this new index as date or does it considers it still as strings?

print(type(df.index))

#%%
# So it turns out that pandas does not recognize the index as date/time

##################################################
# Therefore, we can explicitly tell pandas that the new index is a date and time index

index = pd.to_datetime(index)

print(index)

#%%
# The ``to_datetime`` function of pandas converts an array of dates into DateTimeIndex
# object. It can accepts dates in a wide range of formats. We can verify the type
# of our new index.

print(type(index))

#%%
# now we have created an index whose type is DateTimeIndex i.e. pandas recognizes
# it as date/time. Let's assign this as index to the dataframe.

df.index = index

print(df.index)

#%%
# So now the type of index of the dataframe is date/time.

##################################
# creating datetime index
# ---------------------------
# Above we converted a normal index which was of type list into DateTimeIndex using
# ``to_datetime`` function. We can directly create DateTimeIndex using ``date_range`` function.

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

# %%
# TimeStamps
# ============
#
# The `DateTimeIndex` is indeed an array of `TimeStamps` i.e. each member
# of DateTimeIndex is a TimeStamp.

print(df.index[0])

#%%

print(type(df.index[0]))

# %%
# we can check whether a TimeStamp is in a DateTimeIndex or not
print(index[1] in index)

# %%
# we can also compare two TimeStamps
print(index[0] > index[1])

#%%
# freq
# =========
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

df = pd.DataFrame(np.arange(31), index=pd.date_range("20110101", periods=31, freq="D"))

#%%
print(df)

#%%
print(df.index.freq)

#%%
df = df.drop(labels="2011-01-03")

print(df)

#%%
print(df.index.freq)

#%%
pd.infer_freq(df.index)

#%%
# if we forcefully try to assign a frequency, pandas will throw ``ValueError``.

# Try by uncommenting following line

# df.index.freq = "D"  # -> ValueError

#%%
# Resampling
# ============
# Resampling means changing the frequency of time series.
#
# One major advantage of having a frequency i.e `freq` attribute
# defined is that we can easily change the frequency/time-step of
# the data (time series).

df.asfreq('D')

# %%
# Above when we tried to resample our time series data at daily time step, the
# time steps where we did not have any value, were assigned NaN values.

#%%
# upsampling
# -----------
# This refers to changing the time step from larger to smaller such as from daily
# to hourly
df = pd.DataFrame(np.random.randint(0, 5, 5),
                  index=pd.date_range("20110101", periods=5, freq="D"),
                  columns=['a'])
print(df)

#%%

df.resample("6H")

#%%
# Until now we have told pandas to resample at a particular time step but we have
# not told which method to use. We can as an example use the `mean` to resample.

df.resample("6H").mean()

#%%
# But this did not fill the NaNs in our new data.

df.resample("6H").ffill()

#%%
# .mean() returns us a pandas object. We can in fact call ``ffill`` on it as well.

df.resample("6H").mean().ffill()

#%%
# A better way to resample is apply some interpolation method. For example linear
# interpolation.

df.resample("6H").interpolate(method="linear")

#%%
# Sometimes, we may wish to equally distribute a quantity during upsampling
# For example if we have total amount of rainfall for a day, then linearly
# interpolating daily rainfall values to hourly will be wrong. In such a
# case we will wish to distribute daily rainfall to equally to hourly steps

df1 = df.resample('6H').mean().ffill()
df1['a'] = df1['a'] / df1.groupby('a')['a'].transform(len)  # len/'size'
print(df1)


#%%
# downsampling
# -------------
# It refers to resampling from low time step to high time step e.g.  from hourly to daily

df = pd.DataFrame(np.random.randint(0, 5, 24),
                  index=pd.date_range("20110101", periods=24, freq="H"),
                  columns=['a'])
print(df)

#%%

df.resample("6H").mean()

#%%

df.resample("6H").sum()

#%%
# inconsistent time step
# ------------------------
# Sometimes we have quantities, which are not measured at exactly the same
# frequency where we want. For example below data is measured with inconsistent
# time steps.

df = pd.DataFrame([np.nan, 1100, 1400, np.nan, 14000],
                   index=pd.to_datetime(["2011-05-25 10:00:00",
                                         "2011-05-25 16:40:00",
                                         "2011-05-25 17:06:00",
                                         "2011-05-25 17:10:00",
                                         "2011-05-25 17:24:00"]),
                  columns=['a'])

print(df)

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
# Period
# =========
# A Period is an interval between two TimeStamps. Therefore a Period has ``start_time``
# and ``end_time`` attributes

p = pd.Period("1979-02-01")

print(type(p))

#%%

print(p.start_time)

#%%

print(p.end_time)

#%%

print(type(p.start_time)), print(type(p.end_time))

#%%

print(p.freq)

#%%
# PeriodIndex
# -----------
# Similar to the concept of DateTimeIndex is the concept of PeriodIndex. Just as a DateTimeIndex
# can be considered as an array of TimeStamps, a PeriodIndex is array of Period.


pidx = pd.period_range("20110101", "20121231", freq="M")
print(pidx)

#%%
print(type(pidx))


#%%
# each member of PeriodIndex array i.e., **pidx** is a Period

print(type(pidx[0]))

#%%
# For an overview of difference between TimeStamp and PeriodIndex,
# `see this <https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#overview>`_
