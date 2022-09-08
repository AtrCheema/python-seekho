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
print(a.shape)
print(a.ndim)

#%%

a = np.random.random((3,3))

print(a)
print(a.shape)
print(a.ndim)
#%%

a = np.random.random((3,3, 3))

print(a)
print(a.shape)
print(a.ndim)

#%%

a = np.random.random((3, 3, 3, 3))

print(a)

print(a.shape)
print(a.ndim)