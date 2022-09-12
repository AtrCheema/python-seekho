"""
=================
3.1 introduction
=================

"""

# %% md
# In python everything is an ``object`` and it has a ``type``.
# The ``type`` of an ``object`` tells, what kind of characteristics it has,
# or what kind of operations it can perform or can be performed on it.

# %%

a_int = 23
print(type(a_int))

# %%

a_float = 2.5
print(type(a_float))

# %%

a_name = 'Ali'
print(type(a_name))

# %%


def print_name(the_name):
    print('name is: ', the_name)


print(type(print_name))

# %%

import math

print(type(math))

# %%

looters = ['zardari', 'nawaz', 'establishment']
print(type(looters))

# %%

insan = {'name': 'ali', 'age': 30, 'weight': 72.5}
print(type(insan))

# %%

for key, val in insan.items():
    print(type(key), type(val))

# %% md
# Since `insan` is an instance of class ``dict`` therefore we can access all functions (methods)
# ``dict`` class through its instance `insan`. These methods include ``pop`` or ``update`` etc.

# %%

insan.pop('weight')

# %%

print(insan)

# %%
# We can always check the methods and attributes available for the instance of
# a class by ``dir(object)``

print(dir(insan))

# %%
# Any method/attribute that starts with single or double underscore "_" is not
# for public use. Considering this, we can use any attribute/method of an `insan`
# which we printed above. For example, we can do `insan.update` or `insan.vlaues` or `insan.keys`
# etc. For ``methods``, we have to 'call' them like insan.values() and for other
# attributes, we don't need to call them.

print(dir(a_name))

# %%
# The attributes of `a_name` are different as compared to those of `insan`. Therefore,
# we can not do `insan.startswith()` or `a_name.values()`.

# %%
# **Question**:
# What methods/functions can be applied on `a_int` and `a_float` objects defined above?
# Give examples of five such functions
# by applying them.
