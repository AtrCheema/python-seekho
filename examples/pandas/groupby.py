"""
==========
6. groupby
==========
This file shows the usage of groupby in pandas
"""

import pandas as pd

print(pd.__version__)

#######################################


df = pd.DataFrame( {'a':['A','A','B','B','B','C'], 'b':[1,2,5,5,4,6]})

df

#######################################

df.groupby('a')['b'].apply(list)

#######################################

df.groupby('a')['b'].apply(list).reset_index(name='new')

# %% md
# https://realpython.com/pandas-groupby/
# https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html
#
