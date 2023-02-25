"""
=========================
3.6 str and repr methods
=========================
"""

# %% md
# Default behaviour
# -------------------------------
# Unless we overwrite the default method, for most classes the default output does
# not mean something useful.

# %%

class Insan(object):
    pass


ali = Insan

print(str(ali))
repr(ali)

# %% md
# If a class does not have explicit definition of ``str`` or ``repr`` methods, python will
# used the default output.

# %%


name = 4

str(name)

# %%

repr(name)

# %% md
# `name` belongs to class ``int`` and this class has ``str` and `repr` methods so python
# did not give default output rather used the methods from `int` class.
# but until here we see no apparent difference.

# %%
# Overwriting
# -------------
# If we override one of the two methods:


# %%

class Insan(object):

    def __str__(object):
        return "Insan class"


ali = Insan()
str(ali)

# %%

repr(ali)


# %%

class Insan(object):

    def __repr__(object):
        return "Insan class"


ali = Insan()
str(ali)

# %%

repr(ali)

# %% md
# So if we overwrite ``repr`` method, ``str`` is also overwritten (second case) but if we
# only overwrite ``str`` method, ``repr`` will not be overwritten unless we do it explicitly (first case).
# ``__str__`` is readable and ``__repr__`` is unambiguous
#
# Usually the purpose of `str` method to to give a readable output while that of `repr`
# is give an unambiguous output.
# consider the following example.

# %%

name = 'ali'

repr(name)

# %%

name2 = eval(repr(name))

print(name2 == name)

# %%

name3 = eval(str(name))

print(name3 == name)

# %% md
# ``repr`` is such a representation of an object that by evaluating it (by using ``eval``)
# it will return back the object. ``type(name)`` and ``type(name2)`` will be same.
# This is why ``name`` and ``name2`` were same.  While `str` gives such a representation
# of an object which is for better reading purpose.

# %%

type(name), type(name2)

# %%

type(name3)


# %%

class Revolution:

    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return "Revolution('" + self.name + "', " + str(self.dob) + ")"

    # def __str__(self):
    #     return "Revolution('" + self.name + "', " +  str(self.dob) +  ")"


x = Revolution("Eslami", 1979)

x_str = str(x)
print(x_str)
print("Type of x_str: ", type(x_str))
new = eval(x_str)
print(new)
print("Type of new:", type(new))

# %% md
# So we only overwrote ``repr``, but ``str`` also gave same output as that of ``repr``.
# Moreover check the types of ``str`` and ``repr``.

# %% md
# In above case we were able to evaluate `str` representation of `name` but in some
# cases even this may not be possible as in following case:


# %%

class Revolution:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Revolution('" + self.name + "', " + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", took place in Year: " + str(self.build_year)


x = Revolution("Eslami", 1979)

x_str = str(x)
print(x_str)
print("Type of x_str: ", type(x_str))

# %%

# uncomment following line
# new = eval(x_str)  # SyntaxError

# %%

x_repr = repr(x)
new = eval(x_repr)
print(new)

# %% md
# Consider another example where ``str`` output can not be evaluated

# %%

import datetime

aaj = datetime.datetime.now()
aaj_str = str(aaj)
print(aaj_str)

# %%

aaj_repr = repr(aaj)
print(aaj_repr)

# %%

# uncomment following line
# eval(aaj_str)  # SyntaxError

# %%

eval(aaj_repr)

# %% md
# So ``repr`` is a pure pythonic representation of an object which can be evaluated
# while ``str`` is for reading purpose.
