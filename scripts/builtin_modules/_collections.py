"""
================
2.5 collections
================
.. important::
  This lesson is still under development.
"""

books = {"AlSadr": ["Our Philosophy", "Our Economy"],
         "Mutahri": ["Divine Justice", "Man and Destiny"]}

# %%
# defaultdict
# --------------
# In a normal dictionary, when we try to access value of a non-existent
# key, we will get ``KeyError``.
man = {'name': 'Ali'}

print(man['name'])
# %%

# uncomment following line
# man['height'] # KeyError

# %%
# If however, we want to avoid this error, we can make use of ``defaultdict``
# function. The input to ``defaultdict`` must be a callable.

from collections import defaultdict

print(int())

# %%

man = defaultdict(int)
man['weight'] = 75
print(man['height'])

# %%
# deque
# --------------

from collections import  deque
a = deque([1,2,3], maxlen=5)

print(a)
# %%
a.append(4)
print(a)

a.append(5)
print(a)

a.append(6)
print(a)

# %%

a.appendleft(1)
print(a)

# %%
my_deque = deque([1, 2, 3], maxlen=3)

my_deque.append(4)

print(my_deque)

# %%
# namedtuple
# --------------

from collections import  namedtuple

# %%
# OrderedDict
# --------------
from collections import  OrderedDict

# %%
# Counter
# --------------
from collections import  Counter

# %%
# KeysView
# ---------
# It is used to check whether an object is the keys of a dictionary or not.

try:
    from collections import KeysView
except ImportError:  # python>3.9
    from collections.abc import KeysView
# %%
# if we wish to check that whether a python object is key or value, we can
# achieve this as following

isinstance(books.keys(), KeysView)  # -> True


# %%
# ValuesView
# -----------
# It is used to check whether an object is the values of a dictionary or not.

try:
    from collections import ValuesView
except ImportError:  # python>3.9
    from collections.abc import ValuesView
# %%
# similarly for dictionary values
isinstance(books.values(), ValuesView)  # -> True

# %%
# Reversible
try:
    from collections import Reversible
except ImportError:  # python>3.9
    from collections.abc import Reversible

# %%
# Set
# ---------

try:
    from collections import Set
except ImportError:  # python>3.9
    from collections.abc import Set

# %%
# Sequence
# ---------

try:
    from collections import Sequence
except ImportError:  # python>3.9
    from collections.abc import Sequence
