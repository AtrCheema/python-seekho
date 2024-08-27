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
print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')


#%%

a = np.random.random((2, 3))

print(a)

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')
#%%
# A numpy array should not be understood as rows and columns. 
# Rather a numpy array of shape (2,3) can be understood as two arrays each of shape (3,)

a = np.random.random((2, 3, 4))

print(a)

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')

#%%
# An array of shape (2,3,4) can be understood as two arrays each of shape (3,4)
# and each of these three arrays itself is an array of shape (4,)

a = np.random.random((2, 3, 4, 5))

print(a)

print(f'length: {len(a)}, size: {a.size}, dim: {a.ndim}, shape: {a.shape}')

#%%
# An array of shape (2,3,4,5) can be understood as two arrays each of shape (3,4,5)
# and each of these three arrays itself is an array of shape (4,5).
# 
# Thinking in this way, we can understand the dimensions of an array and the axis along which we can perform operations.