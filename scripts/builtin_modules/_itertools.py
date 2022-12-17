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