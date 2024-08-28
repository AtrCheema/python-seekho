"""
===================================
4.1 understanding dimensions/axis
===================================

"""

import numpy as np

print(np.__version__)

#%%

a = np.array([1.0])

print(a)

#%%
print(a.shape)

#%%
print(a.ndim)

#%%
a = np.array([1,2,3])

print(a)

# %%

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')

#%%

a = np.random.random((4, 5))

print(a)

# %%

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')
# %%
# A numpy array should not be understood as rows and columns. 
# Rather a numpy array of shape (4,5) can be understood as four arrays each of shape (5,)

a = np.random.random((3, 4, 5))

print(a)

# %%

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')

#%%
# An array of shape (3, 4, 5) can be understood as three arrays each of shape (4, 5)
# while each of these (4, 5) arrays can be understood as four arrays each of shape (5,).

a = np.random.random((2, 3, 4, 5))

print(a)

# %%

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')

#%%
# Similarly an array of shape (2,3,4,5) can be understood as two arrays each of shape (3,4,5)
# and so on.
# 
# Thinking in this way, makes it easier to conceptualize higher dimensional arrays.
# 
# The naming of axis in numpy is also consistent with this understanding.
# The axis starts from 0 and goes up to n-1 where n is the number of dimensions.
# The axis 0 is the outermost axis and the axis n-1 is the innermost axis.
# Consider the example of mean.
# If we do np.mean(a), it will calculate the mean of all the elements in the array.

print(np.mean(a))

# %%
# If we do np.mean(a, axis=0), it will calculate the mean along the axis 0.

print(np.mean(a, axis=0).shape)

# %%
# If we do np.mean(a, axis=1), it will calculate the mean along the axis 1.

print(np.mean(a, axis=1).shape)

# %%
# If we do np.mean(a, axis=2), it will calculate the mean along the axis 2.

print(np.mean(a, axis=2).shape)

# %%
# If we do np.mean(a, axis=3), it will calculate the mean along the axis 3.

print(np.mean(a, axis=3).shape)

# %%
# But if we specify an axis that does not exist, it will give an ``AxisError`` error.

# Uncomment the following line to see the error
#
# print(np.mean(a, axis=4).shape)
