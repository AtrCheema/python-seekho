"""
=============================
4.2 stacking vs concatenating
=============================

This file illustrates difference between ``stack``, ``vstack``, ``hstack``,
``column_stack``, ``row_stack`` and ``concatenate``
"""

import numpy as np

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

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.concatenate([a,b], axis=0)) # Error

#%%

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

a = np.random.random(10)
b = np.random.random(10)

print(np.concatenate([a,b]).shape)

print(np.stack([a,b]).shape)

print(np.vstack([a,b]).shape)

print(np.hstack([a,b]).shape)

print(np.row_stack([a,b]).shape)

print(np.column_stack([a,b]).shape)

print(np.dstack([a,b]).shape)

#%%

a = np.random.random((10, 1))
b = np.random.random((10, 1))

print(np.concatenate([a,b]).shape)

print(np.stack([a,b]).shape)

print(np.vstack([a,b]).shape)

print(np.hstack([a,b]).shape)

print(np.row_stack([a,b]).shape)

print(np.column_stack([a,b]).shape)

print(np.dstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 2))

print(np.concatenate([a,b]).shape)

print(np.stack([a,b]).shape)

print(np.vstack([a,b]).shape)

print(np.hstack([a,b]).shape)

print(np.row_stack([a,b]).shape)

print(np.column_stack([a,b]).shape)

print(np.dstack([a,b]).shape)

#%%

a = np.random.random((10, 2))
b = np.random.random((10, 1))

# print(np.concatenate([a,b]).shape)  # ValueError

# print(np.stack([a,b]).shape)  # ValueError

# print(np.vstack([a,b]).shape) # ValueError

print(np.hstack([a,b]).shape)

# print(np.row_stack([a,b]).shape) # ValueError

print(np.column_stack([a,b]).shape)

# print(np.dstack([a,b]).shape)  # ValueError

#%%

a = np.random.random((10, 5, 3))
b = np.random.random((10, 5, 3))

print(np.concatenate([a,b]).shape)

print(np.stack([a,b]).shape)

print(np.vstack([a,b]).shape)

print(np.hstack([a,b]).shape)

print(np.row_stack([a,b]).shape)

print(np.column_stack([a,b]).shape)

print(np.dstack([a,b]).shape)