"""
==========
4. methods
==========
This class discusses the concept of method in python.
"""


# %% md
# Forget for the time being what the word `methods` mean in English, method here means
# `functions associated with classes` Let's write a simple function which takes an
# `object` as input and prints the `name` attribute of that object"

# %%

def say_salam(obj):
    print("Salam, I am " + obj.name + "!")
    return

# %% md
# We also define a simple class named `Insan` as we did in previous examples.

# %%

class Insan:
    pass

# %% md
# We can use the function ``salam`` by using the isntance of class ``Insan`` which is ``x``.

# %%


x = Insan()
x.name = "Ali"
say_salam(x)  # >> Salam, I am Ali!

# %% md
# ``say_salam`` is a function at this time, and we can verify this by checking its type

# %%

type(say_salam)

# %% md
# but we can bind/link it to class `Insan` as following


# %%


def say_salam(obj):
    print("Salam, I am " + obj.name)


class Insan:
    taruf = say_salam


# %% md
# Now we can make use of the function ``say_salam`` which is linked to class
# ``Insan`` as following

# %%


x = Insan()

x.name = "Ali"

Insan.taruf(x)

# %% md
# attributes in the ``Insan`` class are:


# %%

print(Insan.__dict__)

# %% md
# ``taruf`` is a method and can be called as

# %%

x.taruf()

# %% md
# so ``Insan.taruf`` and ``x.taruf` are equivalent. Although the method ``say_salam``
# takes one argument ``obj`` as input but we did not provide any input argument while
# calling it through ``x.taruf()`` and no error was thrown? This is because when the
# function ``say_salam`` was linked to the class ``Insan``, and when we call this method,
# the first argument is by default the instance i.e. ``x`` in this case.
# In this case we defined the method outside the body of class ``Insan`` and then linked
# it to class, but this is not the usual way to define methods. The proper way is
# to define it inside the class(indented)
# We connect this function which is method now to the class by its first argument
# which is usually ``self``.  ``self`` corresponds to the ``Insan`` object ``x``

# %%

class Insan:
    def say_salam(self):
        print("Salam, I am " + self.name)
        return

ali = Insan()

# uncomment following line
# ali.say_salam()  # AttributeError

# %% md
# The problem with above code is that the class ``Insan`` does not have an attribute
# ``name``.So the class must have an attribute ``name`` before using the method ``say_salam``.

# %%

ali.__dict__

# %% md
#  Lets define the attribute before using the method ``say_salam``

# %%

class Insan:
    def say_salam(self):
        print("Salam, I am " + self.name)


ali = Insan()
ali.name = 'Ali'  # define an attribute of instance ali
ali.say_salam()

# %%

ali.__dict__

# %% md
# so whats the difference btw ``method`` and ``function``?
# ``self`` is just a convention, we can use ``this``, ``apna`` or any other keyword but
# it is better to just follow the convention so that others can follow your work


# %%

class Insan:
    def say_salam(apna):
        print("Salam, I am " + apna.name)


ali = Insan()
ali.name = 'Ali'  # define an attribute of instance ali
ali.say_salam()

# %% md
# As said earlier, defining  class attributes outside class is not proper way.
# We need the class ``Insan`` to have the attribute ``name`` before using the method
# ``say_salam``. So we need a systematic way that the class, upon its creation
# (initialization) must have the attribuite ``name``.This is done with ``init``
# method, which we will learn in next lesson.
