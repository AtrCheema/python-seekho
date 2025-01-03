"""
===================
1.5 copying lists
===================

This lessor describes how to copy a list in Python.

.. important::
  This lesson is still under development.
"""


#%%
# Suppose we have a list of countries

countries1 = ["Iraq", "Iran", "Lebanon"]
countries2 = countries1

print(countries1)

print(countries2)

#%%
# Above we have created a new list `countries2` and assigned the list `countries1`
# to it. Now both the lists `countries1` and `countries2` are same. We
# can check this by checking their memory address.

print(id(countries1),id(countries2))

#%%
# We can see, both the lists `countries1` and `countries2` point to same object in memory.
# This means, even though we have two list variables, in reality we have only
# one object.
#
# What will happen if we redfine the list `countries2`?

countries2 = ["Qatar", "Malaysia", "Turkey"]
print(countries1)

print(countries2)

#%%

print(id(countries1),id(countries2))

#%% md
# Now `countries1` and `countries2` are different objects. 
# So the `countries2` list became different from `countries1` when we assigned
# a different object to it.
# What happens when we change the contents of list

#%%

countries1 = ["Pakistan", "Iran", "Turkey"]
countries2 = countries1

countries2[2] = "Syria"

print(countries1)

print(countries2)

#%% md
# Even though we only changed `countries2`, the list `countries1` changed automatically. This is because, we did't have two
# lists to begin with. We have one list with two names. What we did was `in place`
# change in `countries2` list and did not assign a new object to `countries2`,
# so the the name `countries2` still points to the same object as `countries1`.

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    nasalkush_countries = ["us", "uk", "germany"]
#    istemari_countries = nasalkush_countries
#
#    nasalkush_countries.extend(["france"])
#
#    print(istemari_countries)

#%% md
# Copying using slicing
# ----------------------
# The above problem can be avoided by using the slice operator

#%%

countries1 = ["Pakistan", "Iran", "Turkey"]
countries2 = countries1[:]
countries2[2] = 'Syria'

print(countries1)

print(countries2)

#%%

print(id(countries1), id(countries2))

#%% md
# Now `countries1` and `countries2` are not same objects.
#%% md
# The same can be achieved by using `copy` method of `list` object.

#%%

countries1 = ["Pakistan", "Iran", "Turkey"]
countries2 = countries1.copy()

print(id(countries1), id(countries2))

# What about sublists in a list?

#%%

countries1 = ["Pakistan", "Iran", "Turkey",["Qatar", "Malaysia"]]
countries2 = countries1[:]

print(countries1)

print(countries2)

#%%

countries2[0] = "Syria"
print(countries1)

print(countries2)

#%%

countries2[3][1] = "Iraq"
print(countries1)

print(countries2)

#%% md
# So again `countries1` is changed even though we changed only `countries2` list.
# This is because when we copy a list containing sublists, the sublists are
# not copied but their reference is copied.


#%%
# We can check that the sublists in both lists (countries1 and countries1) are same objects.
print(id(countries1[3]), id(countries2[3]))

#%% md
# The same can problem arisis when use `copy` method of `list` object.

#%%

countries1 = ["Pakistan", "Iran", "Turkey",["Qatar", "Malaysia"]]
countries2 = countries1.copy()

print(id(countries1), id(countries2))

#%%

countries2[3][1] = "Iraq"

print(countries1)

print(countries2)

#%%

print(id(countries1[3]), id(countries2[3]))

#%% md
# Using ``list`` function
# ------------------------
# The ``list`` function converts a sequence into list, if it is not already a list

#%%

countries1 = ["Pakistan", "Iran", "Turkey",["Qatar", "Malaysia"]]
countries2 = list(countries1)

print(id(countries1), id(countries2))

#%%

print(id(countries1[3]), id(countries2[3]))

#%% md
# using copy module
# ------------------

#%%

from copy import copy

countries1 = ["Pakistan", "Iran", "Turkey",["Qatar", "Malaysia"]]
countries2 = copy(countries1)

print(id(countries1), id(countries2))

#%%

print(id(countries1[3]), id(countries2[3]))

#%%

from copy import deepcopy

countries1 = ["Pakistan", "Iran", "Turkey",["Qatar", "Malaysia"]]

countries2 = deepcopy(countries1)

print(id(countries1), id(countries2))

#%% md
# Now `countries1` and `countries2` are different and also the sublists
# in both lists are different now.

#%%

print(id(countries1[3]), id(countries2[3]))

#%% md
# So if we make change in one sublist, the sublist in other list will not be affected.

#%%

countries2[3][1] = "Iraq"

print(countries1)

print(countries2)

#%% md
# but the strings in them are not copied so they still have same id.

#%%

print(id(countries1[0]), id(countries2[0]))

#%% md
# So ``deepcopy`` method from `copy` module is the safest way to copy a list when
# it contain sublists but it is also the slowest one among others.
# But what if the two sublists in a list are themselves same objects?

#%%

countries1 = ["Pakistan", "Iran"]
b = [countries1,countries1] # there's only 1 object countries1
c = deepcopy(b)

# check the result
c[0] is countries1 # return False, a new object a' is created


#%%

c[0] is c[1]

#%% md
# In such a scenario, copying with nested for loops is the safest way.
# `for loops` will be described later.

#%%

countries1 = ["Pakistan", "Iran"]
b = [countries1,countries1] # there's only 1 object countries1

c = [[i for i in row] for row in b]

#%%

c[0] is countries1

#%%

c[0] is c[1]

# %%
# If you don't understand the above code, don't worry. We will discuss it later.
# For now, just remember that if you have a list containing lists, then
# `deepcopy` method will not work as expected.
