"""
=========================
5.2 indexing and slicing
=========================

This lesson shows how to select rows or columns from pandas dataframe.

"""
import pandas as pd
print(pd.__version__)

#%%
# Let's create a dataframe

df = pd.DataFrame({
    'name':  ['Ali', 'Hasan', 'Husain', 'Ali', 'Muhammad', 'Jafar', 'Musa', 'Raza', 'Taqi', 'Naqi', 'Askari'],
    'age':   [63,     47,      57,       57,     57,         65,      55,     55,    24,     40,     27],
    'other': ['muavia','muavia','yazid','walid','hisham','mansur','harun','mamun','Mutasim','Mutasim','mutaz'],
    'cityb': ['MKH',    'MAD',   'MAD',  'MAD',  'MAD',   'MAD',   'MAD',  'MAD',  'MAD',    'MAD',   'MAD'],
    'duration':[29,      10,      11,       34,     19,    32,      35,     20,     16,      34,       6],
    'YoB_H': [-22,       3,       4,        38,     56,    83,      128,    148,    195,     212,      232],
    'YOB_G': [600,       625,     626,      659,    676,   702,     745,    766,    811,     828,      844],
    'YoM_H': [40,        50,      61,       95,     114,   148,     183,    203,    220,     254,      260],
    'YoM_G': [661,       670,     680,      712,    733,   765,     799,    818,    835,     868,      874],
    'dynasty':[None,'umayad','umayad','umayad','umayad','abbasid','abbasid','abbasid','abbasid','abbasid','abbasid'],
    'cityd':  ['NJF',  'MAD',   'KBL',    'MAD',  'MAD',      'MAD',   'BGD',  'MAS',  'BGH',   'SAM',    'SAM']
},
    index=['first', 'second', 'third', 'fourth', 'fifth',  'sixth', 'seventh', 'eigth', 'ninth', 'tenth', 'eleventh']
)
print(df)

# %%
print(df.shape)

# %%

#%% md
# The indexing operator, ``[]``, can be used for slicing and for selecting rows and columns.
# However, it can not be used for both purposes (slicing and selecting rows/columns) simultaneously.

#%%
# We can select a single column from dataframe as below

print(df['name'])

#%% md
# For selecting multiple columns, we must pass a list of columns.

#%%

print(df[['other', 'YoM_H']])

#%% md
# when slice notation ``:`` is used, then selection happens either by row labels
# or by integer location

#%%
# Select rows starting from index of `second` till `tenth`
print(df['second':'tenth'])

#%%
# Select every second row starting from 3rd till 7th
print(df[2:6:2])

#%% md
# However, there are more specific methods for indexing and slicing a dataframe. These
# are ``loc``, ``iloc``, ``at`` and ``iat``.
# ``at`` and ``iat`` are meant to access a scalar, i.e, a single element in the dataframe,
# while ``loc`` and ``iloc`` are used to access several elements at the same time,
# potentially to perform vectorized operations

#%% md
# ``loc``
# --------
# - only work on index
# - label based
#
#

# %%
# It is used when we want to select rows or columns from a dataframe using the names of columns
# or the name of index.

#%% md
# The index operator ``[]`` after ``.loc`` can have two values/identifiers separated
# by comma ",". The first identifier (before comma) tells which row/rows we want to
# select and second identifier tells, which columns we want to select.

#%%
# For example if we want to select a row whose index is "third", we can use ``loc``.

print(df.loc['third'])

#%% md
# Above we did not specify the second identifier i.e. there is no comma. This is because
# the if we don't specify the columns, it will give all the columns.
#
# We can select multiple rows with .loc with a list of strings

#%%

print(df.loc[['second', 'fourth', 'sixth']])

#%% md
# Selecting multiple rows with .loc with slice notation ``:``

#%%

print(df.loc['second':'fifth'])

#%% md
# In following code, we simultaneously select rows and columns by their labels.
# Before comman, we tell which rows we want and after comma we tell which columns
# we want.

#%%
print(df.loc[['fifth', 'sixth'], 'other':])

#%% md
# If we want to select all the rows, we can use colon i.e. ``:``.

#%%

print(df.loc[:, 'name':'cityd':2])

#%% md
# Above we wanted to select all the rows (indicated by ``:``) and every second
# columns starting from `name` to `cityd`.
#
# We can also select rows/columns with conditions. For example if we want
# rows where `age` is above 50, we can do as below

# %%
print(df.loc[df['age']>50])

# %%
# In above code, ``df['age']>50``, is the condition. The output of ``df['age']>50`` is
# a boolean array. Thus when we pass a boolean array to ``loc``, it returns us rows based
# upon the specified condition.
#
# We can have multiple conditions as well

print(df.loc[(df['age']>50) & (df['duration']>30)])

# %%
# We can not do above conditioning with strings. What if we want
# all rows where `other` is either muavia or yazid. In such
# a case we can provide all the values as a list inside the ``isin``
# method.

print(df.loc[df['other'].isin(['muavia', 'yazid'])])

#%%
# We can even combine boolean indexing/condition with label based indexing.

print(df.loc[df['age'] > 30, ['other', 'YoM_H']])

# %%
# **Question**:
# Write the names of the people who were in `umayad` dynasty using loc?
#

#%% md
# ``iloc``
# ---------
# - integer location based
#
# - work on position


#%% md
# ``iloc`` is used to select rows and columns from dataframe by their location/index/position value.
# If we don't know the actual names of columns and just want the columns by their locations/position,
# we can use iloc. For example if we want the last row from dataframe, we can do as below

# %%
print(df.iloc[-1])

# %%
# If we want the last column, we can do as below
print(df.iloc[:, -1])

#%%
# The ``:`` above tells that we want all rows.
#
# If we want 5th row, we can dow as below
print(df.iloc[4])

#%% md
# If we want to select multiple rows, we need to pass a list.

#%%
# Select thrid and second last row
print(df.iloc[[2, -2]])

#%% md
# Selecting multiple rows with .iloc with slice notation

#%%
# Select every second row starting from first till 8th
print(df.iloc[:7:2])

#%% md
# Simultaneous selection of rows and columns

#%%
# Select second and fifth row and third column
print(df.iloc[[1,4], 2])

#%% md
# As we did with ``loc``, we can also use a boolean array for selection to ``iloc``.

#%%
# Select 3rd and fifth column but where age is greater than 30
print(df.iloc[(df['age'] > 30).values, [2, 4]])

# %%
# **Question**:
# Select first and last rows and from first and last columns using ``iloc``

#%% md
# ``at``
# ------
# Selection with .at is nearly identical to .loc but it only selects a single 'cell' in
# your DataFrame. We usually refer to this cell as a scalar value. To use .at,
# pass it both a row and column label separated by a comma.


#%%

print(df.at['sixth', 'duration'])

#%% md
# ``iat``
# -------
# Selection with `iat` is nearly identical to `iloc` but it only selects a single
# scalar value. You must pass it an integer for both the row and column locations

#%%

print(df.iat[2, 5])

# %% md
# **Question**:
# Calculate the average age of people in `umayad` and `abbasid` dynasties using ``loc`` and ``iloc``?


# %% md
# **Question**:
# Calculate the `years in office` by subtracting YoM_H from YoB_H and find out which one had the longest and shortest stay in office?