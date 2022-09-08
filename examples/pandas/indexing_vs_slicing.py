"""
=========================
5.2 indexing and slicing
=========================
"""
import pandas as pd
print(pd.__version__)

#%%

df = pd.DataFrame({'age':[30, 2, 12, 4, 32, 33, 69],
                   'color':['blue', 'green', 'red', 'white', 'gray', 'black', 'red'],
                   'food':['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese', 'Melon', 'Beans'],
                   'height':[165, 70, 120, 80, 180, 172, 150],
                   'score':[4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'state':['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'])
df

#%% md
# The indexing operator, `[]`, can slice can select rows and columns too but not simultaneously.

#%%

df['food']

#%% md
# Selecting multiple columns in a dataframe

#%%

df[['food', 'score']]

#%% md
# when slice notation is used, then selection happens by row labels or by integer location

#%%

df['Penelope':'Christina']

#%%

df[2:6:2]

#%% md
#
#`at` and `iat` a meant to access a scalar, that is, a single element in the dataframe,
# while `loc` and `iloc` are ments to access several elements at the same time,
# potentially to perform vectorized operations

#%% md
# loc
#-----
#- only work on index
#
#
# - label based

# label means columns and index

#%% md
# To select a single row of data, place the index label inside of the brackets following `loc`.

#%%

df.loc['Penelope']

#%% md
# Selecting multiple rows with .loc with a list of strings

#%%

df.loc[['Cornelia', 'Jane', 'Dean']]

#%% md
# Selecting multiple rows with .loc with slice notation

#%%

df.loc['Aaron':'Dean']

#%% md
# Simultaneous selection of rows and columns

#%%

df.loc[['Jane', 'Dean'], 'height':]

#%% md
# boolean selection

#%%

df.loc[df['age'] > 30, ['food', 'score']]

#%% md
# selecting all rows

#%%

df.loc[:, 'color':'score':2]

#%% md
# iloc
#-------
# - integer location based
#
# - work on position


#%% md
# Selecting a single row with .iloc with an integer

#%%

df.iloc[4]

#%% md
# Selecting multiple rows with .iloc with a list of integers

#%%

df.iloc[[2, -2]]

#%% md
# Selecting multiple rows with .iloc with slice notation

#%%

df.iloc[:5:3]

#%% md
# Simultaneous selection of rows and columns

#%%

df.iloc[[1,4], 2]

#%% md

#boolean selection

#%%

df.iloc[(df['age'] > 30).values, [2, 4]]

#%% md
# `at`
#------
# Selection with .at is nearly identical to .loc but it only selects a single 'cell' in
# your DataFrame. We usually refer to this cell as a scalar value. To use .at,
# pass it both a row and column label separated by a comma.


#%%

df.at['Christina', 'color']

#%% md
# iat
#-----
# Selection with `iat` is nearly identical to `iloc` but it only selects a single
# scalar value. You must pass it an integer for both the row and column locations

#%%

df.iat[2, 5]

#%% md
# select rows from a DataFrame based on column values

#%%

df.loc[df['food'] == 'Cheese']

#%%

df.loc[df['food'].isin(['Cheese', 'Melon'])]

#%%

df[df['food'].isin(['Cheese', 'Melon'])]

#%%

df[~df['food'].isin(['Cheese', 'Melon'])]

#%%


