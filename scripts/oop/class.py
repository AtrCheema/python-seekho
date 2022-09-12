"""
===================
3.2 creating class
===================
"""

# %% md
# Creating Classes
# -----------------
#
# We can define a minimal class as follows

# %%


class Insan:
    pass


# %%
#
# A ``class`` definition consists of two parts:
#    * header: keyword ``class`` and name of class and then listing of other classes from which this class inherits i.e. superclasses. 3rd argument is optional.
#    * body: indented statements, Above we have only one statement i.e. ``pass``.


# %% md
# Using classes
# --------------
# We can use this simple class as following

# %%

ali = Insan()
husain = Insan()

# %% md
# Above we have created two objects which are called instances of a class.
# `ali` and `husain` are instances of `Insan` class.
# If we check the type of these instances we can confirm it.

# %%

type(ali), type(husain)

# %%

shabir = husain

# %%

print(husain == shabir)

# %%

print(husain == ali)

# %% md
# So `husain` and `ali` are different although they are instances of
# same class. They are different because they are different instances of the `Insan` class.
