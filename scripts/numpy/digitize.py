"""
=========================
4.3 quantile and digitize
=========================

This file describes the concept of quantile and how to cclculate it in numpy
and various functions around it.

"""

import numpy as np

print(np.__version__)

#%%

x = np.array([1,2,3,4,5])

np.quantile(x, 0.5)

#%%

x = np.array([1,2,2,3,3,4,5])

np.quantile(x, 0.5)

#%%
# so quantile actually means that what will be that value that if
# we distribute the values of the array 50% on one side and 50% on other
# side. 50% because we have used 0.5

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(np.quantile(x, 0.5))

#%%

print(np.quantile(x, 0.2))

#%%

print(np.quantile(x, [0.2, 0.5]))

#%%

print(np.quantile(np.arange(10, 20), [0.2, 0.5]))

#%%
# what if the array is 2D

#%%
print(np.quantile(np.arange(20).reshape(-1, 10), [0.2, 0.5]))

#%%
#
# .. code-block:: python
#
#  np.quantile([1.8, 11.8], 0.2)
#  # 3.8
#  np.quantile([4.5, 14.5], 0.5)
#  # 9.5
#