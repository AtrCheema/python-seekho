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
man = {}

# uncomment following line
# man['height'] # KeyError

# If however, we want to avoid this error, we can make use of ``defaultdict``
# function. The input to ``defaultdict`` must be a callable.

from collections import defaultdict

print(int())

# %%

man = defaultdict(int)
print(man['height'])

# %%
# deque
# --------------

from collections import  deque

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

# KeysView
# ---------

try:
    from collections import KeysView
except ImportError:  # python>3.9
    from collections.abc import KeysView
# %%
# if we wish to check that whether a python object is key or value, we can
# achieve this as following

from collections.abc import KeysView, ValuesView
isinstance(books.keys(), KeysView)  # -> True


# %%
# ValuesView
# -----------
try:
    from collections import ValuesView
except ImportError:  # python>3.9
    from collections.abc import ValuesView
# %%
# similarly for dictionary values
isinstance(books.values(), ValuesView)  # -> True

# Reversible
try:
    from collections import Reversible
except ImportError:  # python>3.9
    from collections.abc import Reversible

# Set
# ---------

try:
    from collections import Set
except ImportError:  # python>3.9
    from collections.abc import Set

# Sequence
# ---------

try:
    from collections import Sequence
except ImportError:  # python>3.9
    from collections.abc import Sequence

# %%
# deque
# --------

from collections import deque

my_deque = deque([1, 2, 3], maxlen=3)

my_deque.append(4)

print(my_deque)
