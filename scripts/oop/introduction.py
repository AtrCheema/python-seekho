"""
=================
3.1 introduction
=================

"""

# %% md
# Everything is object and it has a type.

# %%

a = 23
type(23)

# %%

a = 2.5
type(a)

# %%

name = 'Ali'
type(name)

# %%


def print_name(the_name):
    print('name is: ', the_name)


type(print_name)

# %%

import math

type(math)

# %%

dakus = ['zerdari', 'nawaz', 'establishment']
type(dakus)

# %%

insan = {'name': 'ali', 'age': 30, 'weight': 72.5}
type(insan)

# %%

for key,val in insan.items():
    print(type(key), type(val))

# %% md
# ``insan`` is an instance of class ``dict`` and we can access all functions (methods)
# of class ``dict`` through the instance insan.

# %%

insan.pop('weight')

# %%

print(insan)
