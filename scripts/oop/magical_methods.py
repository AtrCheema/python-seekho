"""
=====================
3.17 magic methods
=====================

This file describes the so called magic methods in python. Magic methods are
those methods which start with double underscore ``__`` sign. We have already
seen some of the magic methods such as ``__init__`` in :ref:`sphx_glr_auto_examples_oop_init.py`
, ``__call__`` in :ref:`sphx_glr_auto_examples_oop_call.py` and about ``__repr__``
and ``__str__`` in :ref:`sphx_glr_auto_examples_oop_str_repr.py` lessons. Here
we will cover some more.
"""

# %%
# ``__add__``
# -------------
# This method determines the behavior when addition is performed on the instance
# of its class. Thus, using ``__add__`` method of a class, we can define
# how the addition on the instance of this class will work. For example, in
# class `NonSenseInteger` below, we
# are defining ``__add__`` method, so any instance of `NonSenseInteger` class
# will behave the way we are defining in ``__add__`` method.


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __add__(self, other):
        return self.value - other


ns_int = NonSenseInteger(10)

print(ns_int + 5)

# %%
# Above we have defined that addition will work as subtraction.

print(5 + ns_int)

# %%
# However, above, when the instance of class is on right side of addition operation,
# the addition did not happened the way we defined in ``__add__`` method.

# %%
# ``__radd__``
# -------------
# The ``__add__`` method does not determines the addition behavior of a class
# when the instance of the class is on right side of ``+`` operator.
# In order to overwrite this behavior i.e., the working of addition operation when
# the instance of class is on right side of ``+``, the have to write ``__radd__``
# method.


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __add__(self, other):
        return self.value - other

    def __radd__(self, other):
        return self.value * other


ns_int = NonSenseInteger(10)

print(ns_int + 5)
print(5 + ns_int)

# %%
# Above we see that when `ns_int` is on left side, subtraction was performed
# as we defined in ``__add__`` method and when `ns_int` was on right side,
# multiplication was performed as we defined inside ``__radd__`` method.

# %%
# ``__mul__``
# ------------
# This method determines the behavior when multiplication is performed on the instance
# of its class.


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __mul__(self, other):
        return self.value + other


ns_int = NonSenseInteger(10)

print(ns_int * 5)

# %% md
# Although 10 * 5 is 50, but we got 15, because we modified the multiplication behavior of our
# `NoneSenseInteger` class.

print(5 * ns_int)

# %%
# ``__rmul__``
# -------------


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __mul__(self, other):
        return self.value + other

    def __rmul__(self, other):
        return self.value - other


ns_int = NonSenseInteger(10)
print(ns_int * 5)
print(5 * ns_int)

# %%
# ``__sub__``
# ------------
# This method determines the behavior when subtraction operation is performed on the instance
# of its class.


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __sub__(self, other):
        return self.value + other


ns_int = NonSenseInteger(10)
print(ns_int - 5)

# %%

print(5 - ns_int)

# %%
# ``__rsub__``
# -------------


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __sub__(self, other):
        return self.value + other

    def __rsub__(self, other):
        return self.value * other


ns_int = NonSenseInteger(10)
print(ns_int - 5)
print(5 - ns_int)


# %%
# ``__truediv__``
# ----------------
# This method determines the behavior when division operation is performed on the instance
# of the class.

class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __truediv__(self, other):
        return self.value * other


ns_int = NonSenseInteger(10)
print(ns_int / 5)

# %%

print(5 / ns_int)

# %%
# ``__rtruediv__``
# -----------------


class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __truediv__(self, other):
        return self.value * other

    def __rtruediv__(self, other):
        return self.value + other


ns_int = NonSenseInteger(10)

print(ns_int / 5)
print(5 / ns_int)

# %%
# ``__enter__`` and ``__exit__``
# ------------------------------
# The ``__enter__`` and ``__exit__`` methods are used by the context
# manage i.e. ``with``. They are executed/called when we 'enter' and
# 'exit' the context manager.


class Insan:
    def __init__(self, name, year, age):
        self.name = name
        self.year = year
        self.age = age

    def __enter__(self):
        print(f"{self.name} was born in year {self.year}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} lived until {self.year + self.age} year")
        return

    def married(self, spouse_name:str):
        print(f"{self.name} married with {spouse_name}")
        return


with Insan('Ali', 600, 63) as person:
    print("entered")

# %%
# If you note the print order of strings,
# you will find out that ``__enter__`` method was executed before
# ``print()`` function was called. Similarly, ``__exit__`` method
# was executed after ``print()`` function was called i.e. at
# the time of exiting the context manager. This becomes more
# clear from following example.


# %%
# what if we implment only ``__exit__`` and not ``__enter__``?
class Insan:
    def __init__(self, name, year, age):
        self.name = name
        self.year = year
        self.age = age

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.name} lived until {self.year + self.age} year")
        return

    def married(self, spouse_name:str):
        print(f"{self.name} married with {spouse_name}")
        return

# %%
# uncomment following three lines
# with Insan('Ali', 600, 63) as person:
#     print("entered")
#     person.married('Falima') # -> AttributeError: __enter__

# %%
# The error message shows that it is not possible to use `Insan`
# class with context manager without implementing ``__enter__``
# method for this class. This is because when we say
# `with Insan('Ali', 600, 63) as person:`, the ``__enter__`` method
# of `Insan` class is called implicitly. When the method does not
# exist, we get the error as shown above.

# %%
# Same is true if we implement only ``__enter__`` and not ``__exit__``
class Insan:
    def __init__(self, name, year, age):
        self.name = name
        self.year = year
        self.age = age

    def __enter__(self):
        print(f"{self.name} was born in year {self.year}")
        return self

    def married(self, spouse_name:str):
        print(f"{self.name} married with {spouse_name}")
        return

# %%
# uncomment following three lines
# with Insan('Ali', 600, 63) as person:
#     print("entered")
#     person.married('Falima') # -> AttributeError: __enter__

# %%
# ``__iter__`` and ``__next__``
# ------------------------------
# The ``__next__`` magic method determines what will happen when we call ``next`` function
# on the instance of the class.


class Insan:
    def __init__(self, num_child):
        self.children = [f"child_{i}" for i in range(num_child)]
        self.index = 0

    def __next__(self):
        item = self.children[self.index]
        self.index += 1
        return item


ali = Insan(2)

print(ali.children)

# %%
next(ali)

# %%

next(ali)

# %%
# If we call the ``next`` function again on `ali`, we will get IndexError
# due to what is happening inside ``__next__`` method above.

# uncomment following line
# next(ali)

# %%
# Although, we can apply ``next`` function on `ali` but we can still not
# use it in a ``for`` loop.

ali = Insan(2)

# uncomment following two lines
# for child in ali:
#     print

# %%

import collections

isinstance(ali, collections.abc.Iterable)

# %%
# Since `ali` is not an "iterable", due to which we can not use it in ``for`` loop.
# The reason is that the ``for`` loop requests an iterator from the iterable object, and then calls
# ``__next__`` on that iterable until it hits the ``StopIteration`` exception.
# This happens under the surface which is also the reason why we would want
# iterators to implement the ``__iter__`` as well.

# %%
# **Question:**
# why the code ``isinstance(ali, collections.abc.Iterator)`` returns False?

# %%


class Insan:
    def __init__(self, num_child):
        self.children = [f"child_{i}" for i in range(num_child)]
        self.index = 0

    def __next__(self):
        item = self.children[self.index]
        self.index += 1
        return item

    def __iter__(self):
        return self


ali = Insan(2)

# %%
isinstance(ali, collections.abc.Iterator)

# %%
isinstance(ali, collections.abc.Iterable)

# %%
# Now we can use `ali` in a for loop but,

# uncomment following two lines
# ali = Insan(2)
# for child in ali:
#     print(child)

# %%
# but after the last iteration, we will get ``IndexError`` because of the way we have
# implemented the ``__next__`` method above.

# %%
# **Question:**
# Elaborate the above mentioned reasoning?


class Insan:
    def __init__(self, num_child):
        self.children = [f"child_{i}" for i in range(num_child)]
        self.index = 0

    def __next__(self):
        try:
            item = self.children[self.index]
        except IndexError:
            raise StopIteration

        self.index += 1
        return item

    def __iter__(self):
        return self


ali = Insan(2)

# %%
# Above we have implemented the ``__next__`` method in a way to raise ``StopIteration``
# error instead of ``IndexError``. Since the ``for`` loop under the hood runs until ``StopIteration``
# and then the for loop just bypasses the ``StopIteration``, we can now use the `ali`
# in ``for`` loop safely.

for child in ali:
    print(child)

# %%
# However, there is a problem in the above code, if we run the abvoe for loop again,
# we don't get any output as shown below,
for child in ali:
    print(child)

# %%
class Insan:
    def __init__(self, num_child):
        self.children = [f"child_{i}" for i in range(num_child)]
        self.index = 0

    def __next__(self):
        try:
            item = self.children[self.index]
        except IndexError:
            self.index = 0
            raise StopIteration

        self.index += 1
        return item

    def __iter__(self):
        return self

ali = Insan(2)
for child in ali:
    print(child)

# %%
for child in ali:
    print(child)

# %%
# ``__len__``
# ------------
# This method determines the output of ``len`` function, when applied
# on the instance of a class.


class Family:
    def __init__(self, num_children):
        self.num_children = num_children

    def __len__(self):
        return 1 + 1 + self.num_children


fam = Family(3)

len(fam)

# %%
# Since `fam` is instance of ``Family`` class, the answer
# to ``len`` function was same as we determined in ``__len__`` method.
#
# Had we not defined the ``__len__`` method for `Family` class,
# we would have got ``TypeError`` if we had applied ``len`` function on it.


class Family:
    def __init__(self, num_children):
        self.num_children = num_children


fam = Family(3)

# uncomment the following line
# len(fam)  # -> TypeError: object of type 'Family' has no len()

# %%
# ``__getitem__`` and ``__setitem__``
# ------------------------------------

class Data:
    def __init__(self, values):
        self.values = values

    def __getitem__(self, item):
        return self.values[item]

data = Data([1, 2, 3, 4])

# %%
print(data[0])

# %%
print(data[1])

# %%

# uncomment following two lines
# for idx in range(5):
#     print(data[idx])  # -> IndexError: list index out of range

# %%
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __getitem__(self, item):
        return self.x[item], self.y[item]

data = Data([1,2,3], [11, 12, 13])
print(data[0])

# %%

data = Data([1, 2, 3, 4], [11, 12, 13])

# uncomment following line
# print(data[3])  # -> IndexError: list index out of range

# %%
class Data:
    def __init__(self, x, y):
        assert len(x) == len(y), 'length of x and y should be equal'
        self.x = x
        self.y = y
    def __getitem__(self, item):
        return self.x[item], self.y[item]

# uncomment following line
# data = Data([1, 2, 3, 4], [11, 12, 13])  # -> AssertionError: length of x and y should be equal

# %%

data = Data([1, 2, 3], [11, 12, 13])

# %%
# ``__del__``
# ------------

# %%
# ``__contains__``
# -----------------

class Country:
    def __init__(self, provinces):
        self.provinces = provinces
    def __contains__(self, item):
        return item in self.provinces

pak = Country(['balochistan', 'kpk', 'sind', 'punjab', 'gb'])

print('sind' in pak)

# %%

print('sindh' in pak)

# %%
# ``__copy__`` and ``__deepcopy__``
# ----------------------------------

# %%
# ``__all__``
# ------------

# https://rszalski.github.io/magicmethods/