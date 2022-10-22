"""
====================
2.12 itertools
====================

.. important::
  This lesson is still under development.

"""

import itertools


# %%
# combinations
# -------------
x = [1,2,3]

# %%
print([x for x in itertools.combinations(x, 2)])

# %%

print([x for x in itertools.combinations(x, 3)])

# %%

print([x for x in itertools.combinations(x, 10)])

# %%
# product
# --------

for prod in (itertools.product([1, 2], [11, 12])):
    print(prod)

# %%

for prod in (itertools.product([1,2,3], [11, 12, 13])):
    print(prod)

# %%
for prod in (itertools.product([1, 2], [11, 12], [21, 23])):
    print(prod)

# %%
# permutations
# -------------
print([x for x in itertools.permutations([1,2,3])])

# %%

print([x for x in itertools.permutations([1,2,3], 2)])

# %%
# zip_longest
# ------------
# It is used to iterate over sequences of unequal lengths.

from itertools import zip_longest

d1 = {'a': 1, 'b': 2}
d2 = {'aa': 11, 'bb': 22, 'cc': 33}

for a, b in zip_longest(d1.items(), d2.items()):
    print(type(a), type(b))

# %%

d3 = [1,2,3,4]

for a,b,c in zip_longest(d1.items(), d2.items(), d3):
    print(type(a), type(b), type(c))

d4 = {}

for a,b,c,d in zip_longest(d1.items(), d2.items(), d3, d4.items()):
    print(type(a), type(b), type(c), type(d))