"""
================
3.5 init method
================

"""
# %% md
# This method is used to define the attributes of a class which we want that class
# to have right upon its creation. This means the code in ``init`` method is executed
# at the time of creation of an instance of class. Thus we use ``init`` method to
# initialize the class, hence name ``init``. It can be anywhere inside class but
# convention is to put it at the top inside a class.

# %%


class Insan:
    def __init__(self):
        self.legs = '2 legs'
        print("__init__ method inside class is being executed!")


# %%

x = Insan()
x.legs

# %% md
# we see that although we only created an instance of class (we call it initialization
# of an instance as well) and the code inside init method (we don't use the word
# function for it anymore) got executed.
# The proper way to add `taruf` method to our Insan class is:

# %%

class Insan:

    def __init__(self, name=None, legs='2 legs'):
        self.name = name
        self.legs = legs

    def taruf(self):
        if self.name:
            print("Salam, I am " + self.name + ' and I have ' + self.legs)
        else:
            print("Salam, I am a Insan but my name has not yed been defined" + ' and I have ' + self.legs)


# %%

x = Insan()
x.taruf()

# %%

y = Insan("Ali", legs='1 leg')
y.taruf()

# %% md
# Notice how we passed the string ``Ali`` when we were creating class instance and
# got it transferred to the method ``taruf`` without being explicitly doing it.
# The method ``taruf`` takes no input arguments (actually it takes one, which it
# does implicitly) however it prints the value of `name` which we provided to
# it when we were creating the class instance ``y``.


# %% md
# Let's create a new class instance and use a different name


y = Insan("Hasan")
y.taruf()  # >> Salam, I am Hasan

# %% md
# The attribute ``name`` is shared by the whole class and can be accessed anywhere in
# the class by using the word ``self`` at its start.
# This is because we initialized it inside ``init`` method.

# %%

print(y.name)

# %%

print(y.legs)

# %%

print(y.__dict__)
