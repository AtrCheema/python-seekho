"""
===============
3.3 Attributes
===============
"""

# %% md
# Attribute usually means some specific quality. In python
# attribute is different than property.


# %%

class Insan:
    pass


x = Insan()
y = Insan()

# %% md
# We have created two objects/instances of class `Insan` namely `x` and `y`.
# We can bind attributes to class instances as follows:

x.name = "Ali"
x.dob = "1601"

# %%

y.name = "Hasan"
y.dob = "1624"

# %%
# We can now check that the attributes have been associated with `x` and `y`.

print(x.name)

# %%

print(y.dob)

# %% md
# It should be noticed that we have associated `name` and `dob` attributes to
# instances of `Insan` class i.e., `x` and `y` and not with `Insan` class.
# This is a dynamic way of attribute creation. Usually attributes are built
# inside the class, which we will cover later.
# what attributes does the instance `x` has? We can find it out as following

# %%

print(x.__dict__)

# %%

print(y.__dict__)

# %% md
# We can also bind attributes to class names as well.


class Insan(object):
    pass


x = Insan()

Insan.cast = "Jat"

# %%
# attribute ``cast`` associated with instance `x` currently

print(x.cast)

# %%
# change the attribute cast associated with instance `x`

x.cast = "cheema"

# %%

print(x.cast)

# %%
# what is attribute `cast` associated with class name 'Insan'?

print(Insan.cast)  # >> Jat

# %%

y = Insan()
print(y.cast)  # what is attribute `cast` associated with instance `y`?

# %% md
# ``y`` was never assigned an attributed named ``cast`` still it threw a value, why?
#
# Let's make the attribute ``cast`` associated with `Insan` as `Insaniyat` now

# %%

Insan.cast = "insaniyat"
print('y_cast: ', y.cast)
print('x_cast: ', x.cast)

# %%

print(x.__dict__)

# %%

print(y.__dict__)

# %% md
# empty so if we call the attribute `cast` for instance `y`, python will first look
# into y attributes and if it does not find then it will look into attributes of `Insan`

# %%

# mappingproxy({'__module__': '__main__', '__weakref__': , '__doc__': None, '__dict__': , 'cast': 'insaniyat'})
print(Insan.__dict__)

# %% md
# So even though `y` instance itself does not have an attribute named `cast` so
# it checked whether the attribute `cast` exists in attributes of class `Insan`?
# If yes (which is the case) so `y` gets the attribute from `Insan` while `x`
# already had attribute named `cast` so it did not get attribute from class `Insan`.

# %% md
# if we try to get an attribute which is non-existing, we will get an ``AttributeError``

# %%

# uncomment following line
# x.age  # >> AttributeError: `Insan` object has no attribute `age`

# %% md
# one way to prevent such error is to provide a default value for the attribute by

# %%

getattr(x, 'age', 90)

# %% md
# We can bind attributes to function names similarly


# %%


def chor(name):
    return name + ' chor hai'


chor.age = 61
print(chor.age)  # >> 61

# %% md
# we can use this trick to count number of function calls

# %%


def chor(name):
    chor.no_of_calls = getattr(chor, "no_of_calls", 0) + 1
    return name


for i in range(10):
    chor('nawaz')

# %%

print(chor.no_of_calls)

# %% md
# to properly create class instances we need to define `methods` in the class body,
# which we will learn next
