"""
=============
5.6 groupby
=============
This lesson shows the usage of groupby in pandas

.. important::
  This lesson is still under development.

"""

# %% md
# The material in this lesson is mostly inspired from
# `pandas documentation for groupby <https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html>`_
# and `realpython <https://realpython.com/pandas-groupby/>`_ .

import time

import numpy as np
import pandas as pd

print(time.asctime())
print(np.__version__)
print(pd.__version__)

#######################################

url = "https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/dobowe/2020/codz_2020_01.zip"

df = pd.read_csv(
    url, compression='zip', encoding="ISO-8859-1",  engine='python', 
    on_bad_lines="skip",
    names=['stn_id', 'year', 'day', 'water_level_cm', 'q_cms', 'temp_C', 'month'],
    usecols=[0, 3, 5, 6, 7, 8, 9],
    dtype={'stn_id': int, 'year': 'int', 'day': 'int', 'water_level_cm': np.float32, 'q_cms': np.float32, 'temp_C': np.float32, 'month': 'int'},
    parse_dates={'date': ['year', 'month', 'day']},
    index_col='date'
    )

df

# %%

print(df.shape)

# %%

df['stn_id'].unique()

# %%

df['stn_id'].nunique()

# %%

grouper = df.groupby('stn_id')

grouper

# %%

type(grouper)

# %%

grouper.ngroups

# %%

grouper.groups

# %%

grouper.get_group(149180020)


# %%

type(grouper.get_group(149180020))

# %%

grouper.get_group(149180020).shape

# %%

grouper.get_group(149180020).head()

# %%

grouper.get_group(149180020).tail()

# %%

for name, group in grouper:
    print(name, group.shape)
    break

# %%

for idx, (name, group) in enumerate(grouper):
    print(name, group.shape)
    if idx > 5:
        break
  
# %%

for idx, (name, group) in enumerate(grouper):
    pass

print(idx)

# %%
# What is the mean discharge for each station?

for idx, (name, group) in enumerate(grouper):
    print(name, group['q_cms'].mean())
    if idx > 5:
        break
    
# %%
# What is the mean, min and max temperature for each station?

for idx, (name, group) in enumerate(grouper):
    print(name, group['temp_C'].mean(), group['temp_C'].min(), group['temp_C'].max())
    if idx > 5:
        break

# %%
# replace values > 99.8 and less than 100 with np.nan
df.loc[(df['temp_C']>99.8) & (df['temp_C']<100.0), 'temp_C'] = np.nan

# %%

for idx, (name, group) in enumerate(grouper):
    if not np.isnan(group['temp_C'].mean()):
      print(name, group['temp_C'].mean(), group['temp_C'].min(), group['temp_C'].max())
    if idx > 50:
        break
  