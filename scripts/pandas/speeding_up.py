"""
======================
5.8 efficient pandas
======================
This file shows the how to efficiently use pandas

.. important::
  This lesson is still under development.

"""
import time
from typing import Union

import numpy as np
import pandas as pd

print(pd.__version__, np.__version__)

# %%
# Define a function which prints memory used by a dataframe

def memory_usage(dataframe):
    return round(dataframe.memory_usage().sum() / 1024**2, 4)


#%%
# don't use csv for large data
#-----------------------------

def dump_and_load(dataframe:pd.DataFrame):
    st = time.time()
    dataframe.to_csv("File.csv")
    pd.read_csv("File.csv")
    return round(time.time() - st, 3)

df = pd.DataFrame(np.random.random((100, 10)))

dump_and_load(df)

#%%

df = pd.DataFrame(np.random.random((1000, 20)))
dump_and_load(df)

#%%

df = pd.DataFrame(np.random.random((10_000, 50)))
dump_and_load(df)

#%%

df = pd.DataFrame(np.random.random((100_000, 50)))
dump_and_load(df)

#%%

def dump_and_load_parquet(dataframe:pd.DataFrame):

    dataframe.columns = dataframe.columns.map(str)  # parquet expects column names to be string

    st = time.time()
    dataframe.to_parquet("File.pq")
    pd.read_parquet("File.pq")
    return round(time.time() - st, 3)

dump_and_load_parquet(df)

# %%
# categorical type instead of string type


#%%
# don't think in terms of rows, but in terms columns
#---------------------------------------------------
df = pd.DataFrame(np.random.random((5000, 4)), columns=['a', 'b', 'c', 'd'])
print(df)
#%%
# Iterating over rows is a lot slower than iterating over columns.
# This is mainly because pandas is built around column major format. 
# This means consective values in columns are stored next to each other in memory.

start = time.time()
for col in df.columns:
    for val in df[col]:
        pass
print(time.time() - start)

# %%

start = time.time()
for row_idx in range(len(df)):
    for val in df.iloc[row_idx]:
        pass
print(time.time() - start)

# %%
start = time.time()
for idx, i in enumerate(range(len(df))):
    row = df.iloc[idx]
    row.loc['a'] = row.loc['a'] + row.loc['b']
    df.iloc[idx] = row
print(time.time() - start)

#%%
print(df)
#%%

start = time.time()
df['a'] = df['a'] + df['b']
print(time.time() - start)

# %%
# Use vectorized operations instead of iterating or using ``apply`` method

# %%
# Use chaining instead of creating new dataframes after every operation

#%%
# reduce memory consuption
# --------------------------
# Let's create a dataframe with column which contains only integers
df = pd.DataFrame(np.random.randint(0, 256, 10000000))

print(df.dtypes)
#%%
# The default type fo the column is ``object`` which means pandas does not
# know that the data in column is only integer.
#
# The memory consumed by the dataframe currently is:
print(f"{memory_usage(df)} Mb")

#%%
# However when we check the maximum and minimum value of integers in our dataframe
# they range between 0 and 255.

print(df[0].min(), df[0].max())

#%%
# This means we can store our data as int16. With ``object`` type, we are
# assigning a lot of memory to our data, which is even not necessary.
#
# We can verify that the maximum and minium value in the column is between the
# lower and upper limit of of np.int16.
print(df[0].min() > np.iinfo(np.int16).min and df[0].max() < np.iinfo(np.int16).max)

#%%
# So now let's convert our the data type of our column into np.int16 and check the
# memory consuption now.

df[0] = df[0].astype(np.int16)

print(f"{memory_usage(df)} Mb")

#%%
# we see the memory usage has been reduced significantly.
# Now let's do same with floats.

df = pd.DataFrame(np.random.random(10000000))

print(df.dtypes)

print(f"Initial memory: {memory_usage(df)} Mb")

print(f"min: {df[0].min()} max:  {df[0].max()}")

print(df[0].min() > np.iinfo(np.int16).min and df[0].max() < np.iinfo(np.int16).max)

df[0] = df[0].astype(np.float16)

print(f"Final memory:  {memory_usage(df)} Mb")

# %%
# We can write helper functions to convert the column types in dataframe.
# Below, we write functions, which check the data in each column of a dataframe,
# and assign the the dtype (read as assign the memory) which is just enough for the data in column.
# It means we assign the memory enough for the column but not more than what is required.

def int8(array:Union[np.ndarray, pd.Series])->bool:
    return array.min() > np.iinfo(np.int8).min and array.max() < np.iinfo(np.int8).max

def int16(array:Union[np.ndarray, pd.Series])->bool:
    return array.min() > np.iinfo(np.int16).min and array.max() < np.iinfo(np.int16).max

def int32(array:Union[np.ndarray, pd.Series])->bool:
    return array.min() > np.iinfo(np.int32).min and array.max() < np.iinfo(np.int32).max

def int64(array:Union[np.ndarray, pd.Series])->bool:
    return array.min() > np.iinfo(np.int64).min and array.max() < np.iinfo(np.int64).max

def float16(array:Union[np.ndarray, pd.Series])->bool:
    return array.min() > np.finfo(np.float16).min and array.max() < np.finfo(np.float16).max

def float32(array:Union[np.ndarray, pd.Series])->bool:
    return array.min() > np.finfo(np.float32).min and array.max() < np.finfo(np.float32).max


def maybe_convert_int(series:pd.Series)->pd.Series:
    if int8(series):
        return series.astype(np.int8)
    if int16(series):
        return series.astype(np.int16)
    if int32(series):
        return series.astype(np.int32)
    if int64(series):
        return series.astype(np.int64)
    return series


def maybe_convert_float(series:pd.Series)->pd.Series:

    if float16(series):
        return series.astype(np.float16)
    if float32(series):
        return series.astype(np.float32)

    return series


def maybe_reduce_memory(dataframe:pd.DataFrame, hints=None)->pd.DataFrame:

    init_memory = memory_usage(dataframe)

    if hints:
        assert len(hints) == len(dataframe.columns)
    else:
        hints = {col:'' for col in dataframe.columns}

    for col in dataframe.columns:
        col_dtype = str(dataframe[col].dtypes)

        if col_dtype in  ['int8', 'int16', 'int32', 'int64', 'float16', 'float32', 'float64']:

            if 'int' in  hints[col]:
                dataframe[col] = maybe_convert_int(dataframe[col])
            elif 'float' in hints[col]:
                dataframe[col] = maybe_convert_float(dataframe[col])
            elif 'int' in col_dtype:
                dataframe[col] = maybe_convert_int(dataframe[col])
            elif 'float' in col_dtype or 'float' in  hints[col]:
                dataframe[col] = maybe_convert_float(dataframe[col])

    print(f"memory reduced from {init_memory} to {memory_usage(dataframe)}")
    return dataframe

# %%
# Now we can test our function that how much memory it reduces.

df = pd.DataFrame(np.column_stack([
    np.random.randint(-126, 126, 100_000),
    np.random.randint(-31000, 32760, 100_000),
    np.random.randint(0, 2147483640, 100_000),
]))

print(df.shape)
#%%
# Print the original dtypes

print(df.dtypes)
#%%

maybe_reduce_memory(df)

#%%
# print the converted dtypes

print(df.dtypes)

#%%
# Test with dataframe containing floats

df = pd.DataFrame(np.column_stack([
    np.random.randint(-126, 65000, 100_000) * 1.0,
    np.random.randint(-31000, 100_000, 100_000)*1.0,
]))

print(df.dtypes)
maybe_reduce_memory(df)
print(df.dtypes)

#%%

df = pd.DataFrame(np.column_stack([
    np.random.randint(-126, 126, 100_000),
    np.random.randint(-31000, 32760, 100_000),
    np.random.randint(0, 2147483640, 100_000),
    np.random.randint(-126, 65000, 100_000) * 1.0,
    np.random.randint(-31000, 100_000, 100_000)*1.0,
]))

print(df.dtypes)
maybe_reduce_memory(df)
print(df.dtypes)

#%%

df = pd.DataFrame(np.column_stack([
    np.random.randint(-126, 126, 100_000),
    np.random.randint(-31000, 32760, 100_000),
    np.random.randint(0, 2147483640, 100_000),
    np.random.randint(-126, 65000, 100_000) * 1.0,
    np.random.randint(-31000, 100_000, 100_000)*1.0,
]))

print(df.dtypes)
maybe_reduce_memory(df, hints={0: "int", 1: "int", 2: "int",
                               3: "float", 4: "float"})
print(df.dtypes)

#%%
# For smaller dataframes, teh differene may not seem much but
# when we try to scale things up, the difference is very significant

df = pd.DataFrame(np.column_stack([
    np.random.randint(-126, 126, 1000_000),
    np.random.randint(-31000, 32760, 1000_000),
    np.random.randint(0, 2147483640, 1000_000),
    np.random.randint(-126, 65000, 1000_000) * 1.0,
    np.random.randint(-31000, 100_000, 1000_000)*1.0,
]))

print(df.dtypes)
maybe_reduce_memory(df, hints={0: "int", 1: "int", 2: "int",
                               3: "float", 4: "float"})
print(df.dtypes)

#%% md
# References
#