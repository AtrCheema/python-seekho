"""
=========================
5.2 indexing and slicing
=========================

.. important::
  This lesson is still under development.

"""
import pandas as pd
print(pd.__version__)

#%%

df = pd.DataFrame({'age':[30, 2, 12, 4, 32, 33, 69],
                   'color':['blue', 'green', 'red', 'white', 'gray', 'black', 'red'],
                   'food':['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Mango'],
                   'height':[165, 70, 120, 80, 180, 172, 150],
                   'score':[4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'city':['LHR', 'KRH', 'RWP', 'ISL', 'SKT', 'PSH', 'QTA']
                   },
                  index=['Ali', 'Hasan', 'Husain', 'Fatima', 'Zainab', 'Musa', 'Raza'])
print(df)

#%% md
# The indexing operator, `[]`, can be used for slicing and for selecting rows and columns.
# However, it can not be used for both purposes (slicing and selecting rows/columns) simultaneously.

#%%
# We can select a single column from dataframe as below

print(df['food'])

#%% md
# For selecting multiple columns, we must pass a list of columns.

#%%

print(df[['food', 'score']])

#%% md
# when slice notation is used, then selection happens by row labels or by integer location

#%%

print(df['Fatima':'Musa'])

#%%

print(df[2:6:2])

#%% md
# However, there are more specific methods for indexing and slicing a dataframe. These
# are ``loc``, ``iloc``, ``at`` and ``iat``.
# ``at`` and ``iat`` a meant to access a scalar, that is, a single element in the dataframe,
# while `loc` and `iloc` are ments to access several elements at the same time,
# potentially to perform vectorized operations

#%% md
# loc
# -----
# - only work on index
# - label based
#
#

# It is used when we want to select rows or columns from a dataframe using the names of columns
# or the name of index.

#%% md
# The index operator ``[]`` after ``.loc`` can have two values/identifiers separated by comma ",".
# The first identifier tells which row/rows we want to select and second identifier tells,
# which columns we want to select.

#%%
# For example if we want to select a row whose index is "Fatima", we can use ``loc``.

print(df.loc['Fatima'])

#%% md
# Selecting multiple rows with .loc with a list of strings

#%%

print(df.loc[['Raza', 'Ali', 'Zainab']])

#%% md
# Selecting multiple rows with .loc with slice notation

#%%

print(df.loc['Husain':'Zainab'])

#%% md
# In following code, we simultaneously select rows and columns by their labels.

#%%
print(df.loc[['Ali', 'Zainab'], 'height':])

#%% md
# selecting all rows

#%%

print(df.loc[:, 'color':'score':2])

#%% md
# We can also select rows/columns with conditions. For example if we want
# rows where `age` is above 30, we can do as below

# %%
print(df.loc[df['age']>30])

# %%
# In above code, ``df['age']>30``, is the condition. The output of ``df['age']>30`` is
# a boolean array. Thus when we pass a boolean array to loc, it returns us rows based
# upon the specified condition.
#
# We can have multiple conditions as well

print(df.loc[(df['age']>30) & (df['height']>100)])

# %%
# We can not do above conditioning with strings. What if we want
# all rows where `color` is either blue or green or red. In such
# a case we can provide all the values as a list inside the ``isin``
# method.

print(df.loc[df['color'].isin(['blue', 'green', 'red'])])

#%%
# We can even combine boolean indexing/condition with label based indexing.

print(df.loc[df['age'] > 30, ['food', 'score']])

# %%
# **Question**:
# Which person/people eat mango? Write code using loc and conditions.
#

#%% md
# iloc
# -------
# - integer location based
#
# - work on position


#%% md
# ``iloc`` is used to select rows and columns from dataframe by their location/index value.
# If we don't know the actual names of columns and just want the columns by their locations,
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

print(df.iloc[[2, -2]])

#%% md
# Selecting multiple rows with .iloc with slice notation

#%%

print(df.iloc[:5:3])

#%% md
# Simultaneous selection of rows and columns

#%%

print(df.iloc[[1,4], 2])

#%% md

#boolean selection

#%%

print(df.iloc[(df['age'] > 30).values, [2, 4]])

#%% md
# `at`
# ------
# Selection with .at is nearly identical to .loc but it only selects a single 'cell' in
# your DataFrame. We usually refer to this cell as a scalar value. To use .at,
# pass it both a row and column label separated by a comma.


#%%

print(df.at['Musa', 'color'])

#%% md
# iat
# -----
# Selection with `iat` is nearly identical to `iloc` but it only selects a single
# scalar value. You must pass it an integer for both the row and column locations

#%%

print(df.iat[2, 5])

#%% md
# select rows from a DataFrame based on column values

#%%

print(df.loc[df['food'] == 'Cheese'])

#%%

print(df.loc[df['food'].isin(['Cheese', 'Melon'])])

#%%

print(df[df['food'].isin(['Cheese', 'Melon'])])

#%%

print(df[~df['food'].isin(['Cheese', 'Melon'])])

#%%


