"""
====================
5.4 reading/writing
====================
This file describes how to read data from files and write data into files using
pandas.

.. important::
  This lesson is still under development.

"""

# %%

import pandas as pd

# %%

df = pd.read_csv("https://raw.githubusercontent.com/AtrCheema/AI4Water/master/ai4water/datasets/arg_busan.csv")

type(df)

#%%
df

# %%
df.to_csv("arg_busan.csv")

# %%
# The index of df was 0,1,2,... By default, to_csv function writes the index to
# csv
print(df.index)

# %%
print(df.index.name)

# %%
# we can avoid writing the index to csv file by setting ``index=False``.

df.to_csv("arg_busan.csv", index=False)

# %%
# we can also explicitly tell pandas what label for index to use when writing the index
# to csv file.

df.to_csv("arg_busan.csv", index_label="index")

# %%
# if we want to save a dataframe to Excel file we can do it as following
df.to_excel("arg_busan.xlsx")  # we must have ``openpyxl`` package for that

# %%
# we can define the sheet name and exclude the index as following

df.to_excel("arg_busan.xlsx", index=False, sheet_name="data")

# %%
# to read the excel file as dataframe we can make use of read_excel function

df = pd.read_excel("arg_busan.xlsx")
df

# %%
# we can tell which column should be used as index for the dataframe

df = pd.read_excel("arg_busan.xlsx", index_col="index")
df

# %%
print(type(df.index))

# %%
# Although we index of dataframe is date and time but pandas does not recognize
# it as data and time but it recognizes it just as numbers

df = pd.read_excel("arg_busan.xlsx", index_col="index", parse_dates=True)

df

# %%
# Now the index of dataframe is read as ``DateTimeIndex``
print(type(df.index))

# %%