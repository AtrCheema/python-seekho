"""
=====================
3.17 magical methods
=====================

This file describes the so called magical methods in python. Magical methods are
those methods which start with double underscore ``__`` sign. We have already
seen some of the magical methods such as ``__init__`` or ``__call__`` etc.
"""

#%%
# ``__add__``
#-------------

class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __add__(self, other):
        return self.value - other

ns_int = NonSenseInteger(10)

print(ns_int + 5)

#%%
# using ``__add__`` method of a class, we can define how the addition on the instance
# of this class will work. Here we have told that addition will work as subtraction

print(5 + ns_int)

#%%
# ``__radd__``
#-------------

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

#%%
# ``__mul__``
#------------

class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __mul__(self, other):
        return self.value + other

ns_int = NonSenseInteger(10)

print(ns_int * 5)

#%% md
# Although 10 * 5 is 50, but we got 15, because we modified the multiplication behavior of our
# NoneSenseInteger class.

print(5 * ns_int)

#%%
# ``__rmul__``
#-------------

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

#%%
# ``__sub__``
#------------

class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __sub__(self, other):
        return self.value + other

ns_int = NonSenseInteger(10)
print(ns_int - 5)

#%%

print(5 - ns_int)

#%%
# ``__rsub__``
#-------------

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


#%%
# ``__truediv__``
#----------------

class NonSenseInteger(int):

    def __init__(self, value):
         self.value = value

    def __truediv__(self, other):
        return self.value * other

ns_int = NonSenseInteger(10)
print(ns_int / 5)

#%%

print(5 / ns_int)

#%%
# ``__rtruediv__``
#-----------------

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

#%%
# ``__repr__``
#-------------

class Insan:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"name: {self.name} gender {self.gender}"

ali = Insan('ali', 'male')
print(ali)

#%%
# ``__str__``
#------------

class Insan:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __repr__(self):
        return f"name: {self.name} gender {self.gender}"

    def __str__(self):
        return f"{self.name}, {self.gender}"

ali = Insan('ali', 'male')
str(ali)

#%%
ali

#%%
# ``__enter__``
#--------------

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
    pass

#%%

with Insan('Ali', 600, 63) as person:
    print("entered")
    person.married('Falima')

#%%
# ``__iter__`` and ``__next__``
#------------------------------

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

#%%
next(ali)

#%%

next(ali)

#%%

# uncomment following line
# next(ali)

#%%

ali = Insan(2)
# uncomment following two lines
# for child in ali:
#     print(child)

#%%
# The for loop requests an iterator from the iterable object, and then calls
# ``__next__`` on that iterable until it hits the ``StopIteration`` exception.
# This happens under the surface is also the reason why we would want
# iterators to implement the ``__iter__`` as well

#%%

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

# uncomment following two lines
# for child in ali:
#     print(child)

#%%

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

#%%

for child in ali:
    print(child)

#%%
# ``__len__``
#------------

class Family:
    def __init__(self, num_children):
        self.num_children = num_children

    def __len__(self):
        return 1 + 1 + self.num_children

fam = Family(3)

len(fam)

#%%
