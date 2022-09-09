"""
=============
3.14 __call__
=============
This lesson shows the usage of ``__call__`` method of a class.

"""


def human(age):
    print(f"my age is {age}")
    return


##############################
# We have a function named ``Human`` and we can ``call`` this function using ``()``.

human(12)

############################
# What if we want a class (or an instance of a class) to behave like function.
# To be specific if we want to use an instance of a class as a function, so that
# we can ``call`` this instance, we will write ``__class__`` method of the class.


class Human:

    def __init__(self, age):
        self.age = age

    def __call__(self):
        print(f"my age is {self.age}")
        return


############################
# The ``Human`` class has two (user defined) methods i.e. ``__init__`` and ``__call__``.
# The ``__init__`` method is used/called when we initialize th class and create its instance.

human = Human(12)

############################
# Now if we use the instance ``human`` as function i.e. if we call ``human`` using ``()``,
# the ``__call__`` method will be executed.

human()

# %%
# The ``__call__`` can be defined to take any keyword, non-keyword arguments, optional or
# obligatory arguments


class Human:

    def __init__(self, age):
        self.age = age

    def __call__(self, characteristic):
        print(f"I am {characteristic}")
        return


human = Human(63)
human("mortal")

# %%


class Human:

    def __init__(self, age):
        self.age = age

    def __call__(self, *args, **kwargs):
        print(f"{args} {kwargs}")
        return


human = Human(63)
human()

# %%
human(1)

# %%
human(1, a=2)
