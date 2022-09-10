"""
================
2.5 collections
================

"""

books = {"AlSadr": ["Our Philosophy", "Our Economy"],
         "Mutahri": ["Divine Justice", "Man and Destiny"]}

from collections import defaultdict
from collections import  deque
from collections import  namedtuple
from collections import  OrderedDict
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
