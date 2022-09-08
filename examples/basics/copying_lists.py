"""
===================
1.5 copying lists
===================

"""


## Copying List

#%%

countries1 = ["Pakistan", "Iran", "Turkey"]
countries2 = countries1

print(countries1)

print(countries2)

#%%

print(id(countries1),id(countries2))

#%%

countries2 = ["Qatar", "Malaysia", "Libanon"]
print(countries1)

print(countries2)

#%%

print(id(countries1),id(countries2))

#%% md
# So the `countries2` list became different from `countries1` when we assigned
# a new different object to it.
# What happens when we change the contents of list

#%%

countries1 = ["Pakistan", "Iran", "Turkey"]
countries2 = countries1

countries2[2] = "Syria"

print(countries1)

print(countries2)

#%% md
# The list `countries1` changed automatically. This is because, we don't have two
# lists in reality. We have one list with two names. What we did was `in place`
# change in `countries2` list and did not assign a new object to `countries2`,
# so the the name `countries2` still points to the same object as `countries1`.

#%% md

### Copying using slicing

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

print(id(countries1[3]), id(countries2[3]))

#%% md
# The same can be achieved by using `copy` method of `list` object.

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

### Using `list` function
# The `list` function converts a sequence into list, if it is not already a list

#%%

countries1 = ["Pakistan", "Iran", "Turkey",["Qatar", "Malaysia"]]
countries2 = list(countries1)

print(id(countries1), id(countries2))

#%%

print(id(countries1[3]), id(countries2[3]))

#%% md

### using copy module

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
# Now `countries1` and `counries2` are different and also the sublists
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
# So `deepcopy` method from `copy` module is the safest way to copy a list when
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
