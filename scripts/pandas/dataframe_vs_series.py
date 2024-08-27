"""
==================
5.1 introduction
==================
"""
#%%

import numpy as np
import pandas as pd

print(pd.__version__, np.__version__)

#%%
# Suppose we have an array [0.4, 0.3, 0.5, 0.2, 0.6, 0.3]. Let's say
# the values in this array represent concentrations in water measured
# every hour from 13 pm to 19 pm. However, with just an array, we don't
# have the ability to encode this information. If we want to add the (temporal) reference of each value
# we have to add it ourself for example by saving that in a separate array.
# Pandas comes with this in-built ability that we can add reference or labels to arrays.
# Every array in pandas has two kinds of references. The reference for the rows which
# is called ``index`` and the reference for the columns which is called ``columns``.
# Therefore we can call pandas a library which have referenced/labelled arrays.
#
# The core data structure in pandas is ``DataFrame`` which consists of one or more
# columns. A single column in a DataFrame is a ``Series``.

df = pd.DataFrame(np.random.random((10, 3)))
print(df)

#%%
# The data in columns is stored as numpy arrays. Therefore, a DataFrames and Series
# have a lot of characteristics similar to that of numpy arrays.
print(df.shape)

#%%
# By default the columns names are just integers starting from 0, however
# we can define the column names ourselves as well.

df = pd.DataFrame(np.random.random((10, 3)), columns=['a', 'b', 'c'])
print(df)

#%%

print(df.columns)

#%%
# The columns are list like structures. However they are not exactly lists.
print(type(df.columns))

#%%
# We can however, convert the columns to list though.
df.columns.to_list()

#%%

print(type(df.columns.to_list()))

#%%
# The default label for the rows i.e. ``index`` consists of numbers starting from 0.
print(df.index)

#%%
# However, we can set ``index`` of our choice as well.

df = pd.DataFrame(np.random.random((10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
print(df)

#%%

print(df.index)

#%%
# The default name of ``index`` is ``None``.
print(df.index.name)

#%%
# However, we can set the name of index as well.
df.index.name = 'years'
print(df)

#%%

print(df.index.name)

#%%

print(type(df))

#%%

df = pd.DataFrame(np.random.randint(0, 10, (10, 1)),
                  columns=['a'],
                 index=[2000+i for i in range(10)])
print(df)

#%%

print(type(df))

#%%

print(df.columns)

# %% md
# Series
# =========
# A Series consists of a single column. It can be constructed using ``pd.Series``.

s = pd.Series(np.random.random(10))
print(s)

#%%

print(type(s))

#%%

print(s.shape)

#%%

print(s.name)

#%%

s = pd.Series(np.random.random(10),
              name="a")
print(s)

#%%

print(s.name)

#%% md
# the Series is literally the data structure for a single column of a DataFrame.

#%%

df = pd.DataFrame(np.random.random((10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
print(df)

#%%
# A single column in a DataFrame is a Series.

print(type(df['a']))

#%%

s = pd.Series(np.random.random(10),
              index=[2000+i for i in range(10)],
              name="a")
print(s)

#%%
# Since pandas is based upon numpy arrays. We can extract actual numpy
# arrays from DataFrame using `.values` method.
print(df.values)

#%%

print(type(df.values))

#%%

df = pd.DataFrame(np.random.randint(0, 14, (10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
print(df)

#%%

print(type(df.values))

#%%

print(df.values.shape)

#%%

df.describe()

#%%

df.head()

#%%

df.head(8)

#%% md
# Get the last N rows of a DataFrame

#%%

df.tail()

#%%

df.tail(7)

#%%

df.mean()


#%%

df.to_dict()

#%%

df.to_dict('list')

#%%

df['d'] = np.random.randint(0, 10, (10,))
print(df)

#%%

df.pop('d')
print(df)

#%%

df.columns = ['x', 'y', 'z']
print(df)

#%% md
# row count of pandas dataframe

#%%

len(df.index)

#%%

print(df.shape[0])

#%% md
# change the order of DataFrame columns

#%%

cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]
print(df)

#%% md
#  drop rows of Pandas DataFrame whose value in a certain column is NaN

#%%

df = pd.DataFrame(np.random.randn(6,3))
print(df)

#%%

df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
print(df)

#%%
# dropping all rows having NaN values
df.dropna()

#%%
# dropping NaN in specific columns
print(df[df[2].notna()])

#%% md
# count the NaN values in a column in DataFrame

#%%

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
print(df)

#%%

df.isna().sum()

#%%
# for columns
df.isnull().sum(axis = 0)

#%%
# for rows
df.isnull().sum(axis = 1)

#%% md
# check if any value is NaN in a DataFrame

#%%

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
print(df)

#%%
# how many NaN
df.isnull()

#%%
# column wise
df.isnull().any()

#%%
# if there is any NaN in entire data
df.isnull().any().any()

#%% md
# replace NaN values by Zeroes in a column of a Dataframe?

#%%

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
print(df)

#%%

df.fillna(0)

#%%
# To fill the NaNs in only one column

df[2].fillna(0, inplace=True)
print(df)

#%% md
# check if a column exists in Pandas

#%%

df = pd.DataFrame(np.random.randn(6,3))
print(df)

#%%

if 0 in df.columns:
     print("true")

#%% md
# Python dict into a dataframe

#%%

d = {
    '2012-06-08': 388,
    '2012-06-09': 388,
    '2012-06-10': 388,
    '2012-06-11': 389,
    '2012-06-12': 389,
    '2012-06-13': 389,
    '2012-06-14': 389,
    '2012-06-15': 389,
    '2012-06-16': 389,
    '2012-06-17': 389,
    '2012-06-18': 390,
    '2012-06-19': 390,
    '2012-06-20': 390,
}

#%%

pd.DataFrame(d.items())

#%%

pd.DataFrame(d.items(), columns=['Date', 'DateValue'])

#%%
#
# uncomment following line
# pd.DataFrame(d) # ValueError: If using all scalar values, you must pass an index

# %%
pd.DataFrame([d])

#%%

pd.DataFrame.from_dict(d, orient='index', columns=['DateVaue'])

#%% md
# Count the frequency that a value occurs in a dataframe column

#%%

df = pd.DataFrame(np.random.randint(0, 14, (10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
df['a'].value_counts()

#%%

for index, row in df.iterrows():
    print(index, row, '\n')

#%%

df = pd.DataFrame(np.random.randint(0, 14, (10, 3)),
                  columns=['a', 'b', 'c'])
print(df)

#%%

print(df['a']/df['b'])

#%% md
# add an empty column to a dataframe?

#%%

df["d"] = ""
print(df)

#%%

print(df['d'])

#%%

df["d"] = np.nan
print(df)

#%% md
# What does axis in pandas mean?

#%%

df.mean(axis=0)

#%%

df.mean(axis=1)

#%% md
# Replace NaN with blank/empty string

#%%

df.replace(9, np.nan)

#%%

df.replace(np.nan, '')

#%% md
# Rename specific column(s) in pandas

#%%

df = pd.DataFrame(np.random.randint(0, 14, (10, 3)), columns=['a', 'b', 'c'])
print(df)

#%%

df.rename(columns={'a':'log(A)'}, inplace=True)
print(df)

#%% md
# print DataFrame without index


#%%

print(df)

#%%

df.style.hide_index()

#%% md
# replace nan values with average of columns

#%%

df.fillna(df.mean())

#%% md
# retrieve the number of columns in a dataframe?

#%%

len(df.columns)

#%%

print(df.shape[1])

#%% md
# We can create empty DataFrame by telling
# how many columns should exist or how many rows should exist.

#%%

df = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
print(df)

#%%

print(df.shape)

#%%

df = pd.DataFrame(index=range(1,8))
print(df)

#%%

print(df.shape)
