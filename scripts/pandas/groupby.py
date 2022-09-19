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
# and `realpython <https://realpython.com/pandas-groupby/>`_
# However, it has been modified for easy of practice and understanding.

import pandas as pd

print(pd.__version__)

#######################################

df = pd.DataFrame( {'a':['A','A','B','B','B','C'], 'b':[1,2,5,5,4,6]})

df

#######################################

df.groupby('a')['b'].apply(list)

#######################################

df.groupby('a')['b'].apply(list).reset_index(name='new')


