"""
===============
1. introduction
===============
"""
#%%

import numpy as np
import pandas as pd

print(pd.__version__, np.__version__)

#%%

df = pd.DataFrame(np.random.random((10, 3)))
df

#%%

df.shape

#%%

df = pd.DataFrame(np.random.random((10, 3)), columns=['a', 'b', 'c'])
df

#%%

df.columns

#%%

type(df.columns)

#%%

df.columns.to_list()

#%%

type(df.columns.to_list())

#%%

df.index

#%%

df = pd.DataFrame(np.random.random((10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
df

#%%

df.index

#%%

df.index.name

#%%

df.index.name = 'years'
df

#%%

df.index.name

#%%

type(df)

#%%

df = pd.DataFrame(np.random.randint(0, 10, (10, 1)),
                  columns=['a'],
                 index=[2000+i for i in range(10)])
df

#%%

type(df)

#%%

df.columns

#%% md

## Series

#%%

s = pd.Series(np.random.random(10))
s

#%%

type(s)

#%%

s.shape

#%%

s.name

#%%

s = pd.Series(np.random.random(10),
              name="a")
s

#%%

s.name

#%% md

# the Series is literally the data structure for a single column of a DataFrame.

#%%

df = pd.DataFrame(np.random.random((10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
df

#%%

type(df['a'])

#%%

s = pd.Series(np.random.random(10),
              index=[2000+i for i in range(10)],
              name="a")
s

#%%

df.values

#%%

type(df.values)

#%%

df = pd.DataFrame(np.random.randint(0, 14, (10, 3)),
                  columns=['a', 'b', 'c'],
                 index=[2000+i for i in range(10)])
df

#%%

type(df.values)

#%%

df.values.shape

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
df

#%%

df.pop('d')
df

#%%

df.columns = ['x', 'y', 'z']
df

#%% md

# row count of pandas dataframe

#%%

len(df.index)

#%%

df.shape[0]

#%% md

# change the order of DataFrame columns

#%%

cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]
df

#%% md

##  drop rows of Pandas DataFrame whose value in a certain column is NaN

#%%

df = pd.DataFrame(np.random.randn(6,3))
df

#%%

df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
df

#%%

#dropping all rows having NaN values
df.dropna()

#%%

#dropping NaN in specific columns
df[df[2].notna()]

#%% md

## count the NaN values in a column in DataFrame

#%%

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
df

#%%

df.isna().sum()

#%%

#for columns
df.isnull().sum(axis = 0)

#%%

#for rows
df.isnull().sum(axis = 1)

#%% md

## check if any value is NaN in a DataFrame

#%%

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan
df

#%%

#how many NaN
df.isnull()

#%%

#column wise
df.isnull().any()

#%%

#if there is any NaN in entire data
df.isnull().any().any()

#%% md

## replace NaN values by Zeroes in a column of a Dataframe?

#%%

df = pd.DataFrame(np.random.randn(6,3))
df.iloc[::2,0] = np.nan; df.iloc[::4,2] = np.nan; df.iloc[::3,2] = np.nan;
df

#%%

df.fillna(0)

#%%

#To fill the NaNs in only one column
df[2].fillna(0, inplace=True)
df

#%% md

## check if a column exists in Pandas

#%%

df = pd.DataFrame(np.random.randn(6,3))
df

#%%

if 0 in df.columns:
     print("true")


#%% md

## Python dict into a dataframe

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

# pd.DataFrame(d) # ValueError: If using all scalar values, you must pass an index
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
df

#%%

df['a']/df['b']

#%% md
# add an empty column to a dataframe?

#%%

df["d"] = ""
df

#%%

df['d']

#%%

df["d"] = np.nan
df

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
df

#%%

df.rename(columns={'a':'log(A)'}, inplace=True)
df

#%% md
# print DataFrame without index


#%%

df

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

df.shape[1]

#%% md

### create empty DataFrame

#%%

df = pd.DataFrame(columns=['A','B','C','D','E','F','G'])
df

#%%

df.shape

#%%

df = pd.DataFrame(index=range(1,8))
df

#%%

df.shape
