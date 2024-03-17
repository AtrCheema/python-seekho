"""
========================
1.21. builtin functions
========================
This lesson shows the usage of builtin functions available in python.
These functions are available in python without importing any module.
These are not all the builtin functions but only those which are used frequently.


.. important::
  This lesson is still under development.
"""

# %%
# slice
# =======

a = [1,2,3,4,5,6,7,8,9,10]
print(a[slice(2)])

# %%
print(a[slice(2, 8)])

# %%
print(a[slice(2, 8, 2)])

# %%
a = "This is a string"
print(a[slice(2)])
print(a[slice(2, 8)])
print(a[slice(2, 8, 2)])

# %%
a = (1,2,3,4,5,6,7,8,9,10)
print(a[slice(2)])
print(a[slice(2, 8)])
print(a[slice(2, 8, 2)])

# %%
a = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
# print(a[slice(2)])

# %%
# Indeed, any python object which can be sliced using ``[]`` operator, can also be sliced
# using ``slice`` function. 
# Although, ``[]`` operator and ``slice`` function look similar however they differ in
# their behavior. ``[]`` operator returns the values whereas ``slice`` function returns
# a ``slice`` object. Moreover, ``slice`` function is more readable and flexible.

# %%
# zip
# =====
# zip is used to iterate over two or more than two sequences.

for i,j in zip([1,2,3], [11, 12, 13, 14]):
    print(i, j)

# %%
# any
# ======
vals = [1,2,3]
print(any([val>3 for val in vals]))

# %%
vals = [1,2,3, 4]
print(any([val>3 for val in vals]))

# %%
# all
# =====
vals = [1,2,3,4,5]
print(all([isinstance(val, int) for val in vals]))

# %%
vals = [1,2,3,4,5.0]
print(all([isinstance(val, int) for val in vals]))

# %%
vals = [1,2,3,4,5.0]
print(all([isinstance(val, (int, float)) for val in vals]))

# %%
vals = [1,2,3,4,'5.0']
print(all([isinstance(val, (int, float)) for val in vals]))

# %%
# sorted
# ========
vals = ['a', 'b', 'c']
for val in sorted(vals):
    print(val)

# %%
vals = ['a', 'c', 'b']
for val in sorted(vals):
    print(val)

# %%
vals = [1,5,3,10.0]
for val in sorted(vals):
    print(val)

# %%
# reversed
# ===========
vals = ['a', 'b', 'c']
for val in reversed(vals):
    print(val)

# %%
# enumerate
# ==========
vals = ['a', 'b', 'c']
for idx, val in enumerate(vals):
    print(idx, val)

# %%
# **Question:**
#
# What will be the output of the following code?
#
# .. code-block:: python
#
#    names = ['jamaludin', 'zaynaldin', 'nurullah shustari', 'kamil dehlavi', 'baqir sadr]
#    years = ['1385', '1558', '1610', '1809', '1979']
#    for (idx,name), year in zip(enumerate(names), years):
#        print(idx, name, year)

# %%
# **Question:**
#
# Consider the following list
#
# .. code-block:: python
#
#    dob_years = ['1334', '1506', '1542', '1700s', '1935']
#
# Now modify the ``for`` loop in the previous example to also iterate over 
# ``dob_years`` list along with ``names`` and ``years``.

# %%
# map
# =====
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
# An alternative to calling the function in an explicit for loop
# is to make use of ``map`` function.

mapper = map(square, vals)

# %%
# The ``map`` function returns an iterator which we can be converted into a ``list``

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

# %%
# **Question:**
#
# Convert the years in following list from Hijri to Gregorian [1]_ calenden using ``map`` function
#
# .. code-block:: python
#
#    hijri_years = [40, 50, 61, 95, 114, 148, 183, 203, 220, 254, 260]


# %%
#
# .. [1] `<https://github.com/dralshehri/hijridate>`_