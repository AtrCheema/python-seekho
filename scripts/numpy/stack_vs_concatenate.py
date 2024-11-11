"""
=============================
4.2 stacking vs concatenating
=============================

This lesson illustrates difference between ``stack``, ``vstack``, ``hstack``,
``column_stack``, ``row_stack`` and ``concatenate``
"""
import time
import numpy as np

print(time.asctime())
print(np.__version__)

#%%
# stack
# =============
# all arrays must have same shape

#%%
# both 1d arrays

a = np.random.random(10)
b = np.random.random(10)

print(np.stack([a,b]).shape)


#%%
# both 2D

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.stack([a,b]).shape)

#%%

print(np.stack([a,b], axis=1).shape)

#%%

print(np.stack([a,b], axis=2).shape)

#%%
a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.stack([a,b]).shape)

#%%

print(np.stack([a,b], axis=0).shape)

#%%

print(np.stack([a,b], axis=1).shape)

#%%

print(np.stack([a,b], axis=2).shape)

#%%

# print(np.stack([a,b], axis=3).shape) # np.AxisError

#%%
# different shapes

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.stack([a,b]).shape)  # ValueError

#%%

# print(np.stack([a,b], axis=0).shape)  # ValueError

#%%

# print(np.stack([a,b], axis=1).shape)  # ValueError


#########################################
# concatenate
#=============

a = np.random.random(10)
b = np.random.random(10)

print(np.concatenate([a,b]).shape)

#%%

print(np.concatenate([a,b], axis=0).shape)

#%%

# print(np.concatenate([a,b], axis=1).shape)  # Error

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.concatenate([a,b]).shape)

#%%

print(np.concatenate([a,b], axis=1).shape)

#%%
# The shapes of the arrays must be same except in the dimension corresponding to axis

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.concatenate([a,b], axis=0)) # Error

#%%
# In above example, axis 0 has 10 but axis 1 has 2 and 1. So, it is not possible to concatenate

print(np.concatenate([a,b], axis=1).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.concatenate([a,b]).shape)

#%%

print(np.concatenate([a,b], axis=1).shape)

#%%

# print(np.concatenate([a,b], axis=2).shape)  # AxisError

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.concatenate([a,b]).shape)
#%%

print(np.concatenate([a,b], axis=1).shape)

#%%

print(np.concatenate([a,b], axis=2).shape)

#####################################################
# vstack
#=======

a = np.random.random(10)
b = np.random.random(10)

print(np.vstack([a,b]).shape)

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.vstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.vstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 1))

print(np.hstack([a,b]).shape)

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.hstack([a,b]).shape)

####################################################
# hstack
#=======

a = np.random.random(10)
b = np.random.random(10)

print(np.hstack([a,b]).shape)

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.hstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.hstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 1))

print(np.hstack([a,b]).shape)

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.hstack([a,b]).shape)

##################################################
# column stack
#=============

a = np.random.random(10)
b = np.random.random(10)

print(np.column_stack([a,b]).shape)

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.column_stack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.column_stack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 1))

print(np.column_stack([a,b]).shape)

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.column_stack([a,b]).shape)

###############################################3
# row stack
#==========

a = np.random.random(10)
b = np.random.random(10)

print(np.row_stack([a,b]).shape)

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.row_stack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.row_stack([a,b]).shape)

#%%
# shape has to be same

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.row_stack([a,b]).shape) ValueError

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.row_stack([a,b]).shape)

###################################################
# dstack
# ==========
# depth wise stacking

a = np.random.random(10)
b = np.random.random(10)

print(np.dstack([a,b]).shape)

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.dstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.dstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.dstack([a,b]).shape)  # ValueError

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.dstack([a,b]).shape)

###################################################
# comparison
#===========
# 1D arrays

a = np.random.random(10)
b = np.random.random(10)

print('concatenate: ', np.concatenate([a,b]).shape)

print('stack        ', np.stack([a,b]).shape)

print('vstack:      ', np.vstack([a,b]).shape)

print('hstack:      ', np.hstack([a,b]).shape)

print('row_stack:   ', np.row_stack([a,b]).shape)

print('column_stack:', np.column_stack([a,b]).shape)

print('dstack:      ', np.dstack([a,b]).shape)

#%%
# 2D arrays

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print('concatenate:  ', np.concatenate([a,b]).shape)

print('stack:        ', np.stack([a,b]).shape)

print('vstack:       ', np.vstack([a,b]).shape)

print('hstack:       ', np.hstack([a,b]).shape)

print('row_stack:    ', np.row_stack([a,b]).shape)

print('column_stack: ', np.column_stack([a,b]).shape)

print('dstack:       ', np.dstack([a,b]).shape)

#%%
# 2D arrays
a = np.random.random((10, 2))
b = np.random.random((10, 2))

print('concatenate: ', np.concatenate([a,b]).shape)

print('stack:       ', np.stack([a,b]).shape)

print('vstack:      ', np.vstack([a,b]).shape)

print('hstack:      ', np.hstack([a,b]).shape)

print('row_stack:   ', np.row_stack([a,b]).shape)

print('column_stack:',np.column_stack([a,b]).shape)

print('dstack:      ', np.dstack([a,b]).shape)

#%%
# 2D arrays with different shapes

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.concatenate([a,b]).shape)  # ValueError

# print(np.stack([a,b]).shape)  # ValueError

# print(np.vstack([a,b]).shape) # ValueError

print('hstack:       ', np.hstack([a,b]).shape)

# print(np.row_stack([a,b]).shape) # ValueError

print('column_stack: ', np.column_stack([a,b]).shape)

# print(np.dstack([a,b]).shape)  # ValueError

#%%
# 3D arrays

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print('concatenate: ', np.concatenate([a,b]).shape)

print('stack:       ', np.stack([a,b]).shape)

print('vstack:      ', np.vstack([a,b]).shape)

print('hstack:      ', np.hstack([a,b]).shape)

print('row_stack:   ', np.row_stack([a,b]).shape)

print('column_stack:', np.column_stack([a,b]).shape)

print('dstack:      ', np.dstack([a,b]).shape)
