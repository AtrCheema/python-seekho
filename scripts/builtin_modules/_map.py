"""
=====================
2.13 map
=====================
This lesson shows the usage of builtin function ``map`` in python.
"""

# %%
# Suppose we have function which takes an input and returns square of it

def square(x):
    return x**2

# %%
# Now if we want to call this function on several values, we can
# make a list of all the values on which we want to call it
vals = [1,2,3,4,5]

# %%
# and then we can call this function in a loss
for val in vals:
    print(square(val))

# %%
# an alternative to calling the function in an explicit for loop
# is to make use of ``map`` function.

mapper = map(square, vals)

# %%
# THe ``map`` function returns an iterator which we can convert into a list

print(type(mapper))

# %%
from collections.abc import Iterator
print(isinstance(mapper, Iterator))


# %%
# We can extract all values from iterator by calling ``list`` method on it.

list(mapper)

# %%
# we can also provide any builtin function as first argument to ``map``

list(map(float, vals))

# %%
# we can also use map with functions which take multiple input input arguments.

def power(x, n):
    return x**n

vals1 = [1,2,3,4]
vals2 = [1,2,3,4]
list(map(power, vals1, vals2))

# %%
# Map has several advantages over an explicit for loop e.g
#    * It is fast since it is written in C
#    * It is memory efficient as it returns an iterator
