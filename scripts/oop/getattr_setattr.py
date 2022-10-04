"""
========================
3.15 getattr vs setattr
========================

This lesson shows the usage of ``setattr`` and ``getattr``
"""

# %%
# The ``getattr`` and ``setattr`` are builtin functions which are used
# to get and set an attribute to a python object. Following examples
# show how to use these functions to set and get attributes of a class.

# %%
# setattr
# --------


class Human:

    def __init__(self, name):
        self.name = name

    def grow(self):
        setattr(self, 'empathy', 10)
        return


human = Human("Ali")

# %%
# When we created the instance of `Human` class, it did not have `empathy` attribute.

# uncomment following line
# human.empathy  # -> AttributeError: 'Human' object has no attribute 'empathy'

# %%
# After executing the `grow` method of `Human` class, the `empathy` attribute is set to
# it using ``setattr`` function.

human.grow()

print(human.empathy)

# %%
# The first argument to ``setattr`` is the object to which we want to set the attribute.
# The second argument is the name of attribute and the third argument is the value of the attribute.
#
# If we want to set/change the value of `empathy` attribute of `human` to 14, we can do this
# using ``setattr`` as below.

setattr(human, "empathy", 14)

print(human.empathy)

# %%
# It will be obvious from above examples that the function ``setattr`` can be used both inside
# the class and outside the class definition.

human.empathy = 100

print(human.empathy)

# %%
# From above example we can infer that doing `human.empathy = 10` is similar to
# `setattr(human, 'empathy', 100)`. This can be translated as, setting
# the attribute of `human` with the name `empathy` to 100.

# %% md
# getattr
# ---------
# ``getattr`` is opposite of ``setattr``. It is used to fetch the attribute value of an object.

print(getattr(human, 'empathy'))

# %%
# In other words, doing `human.empathy` is similar to running `getattr(human, 'empathy')`
# The second argument to both ``setattr`` and ``getattr`` is string (``str``) type.


class Human:

    def __init__(self, name):
        self.name = name

    def grow(self):
        setattr(self, 'empathy', 10)
        return

    def info(self):
        empathy = getattr(self, 'empathy', None)
        return empathy


human = Human("Ali")

# %%
# But what if the object does not have the attribute that we are trying to fetch?

# uncomment following line
# human.empathy  # -> AttributeError: 'Human' object has no attribute 'empathy'

# %%
# Running the above code will give us AttributeError because, the `human` does
# not yet have `empathy` attribute.

# %%

human.info()

# %%
# But why above cell did not throw AttributeError, even though we
# are getting, `empathy` attribute in it?
# This is because the 3rd argument in ``getattr`` function in `info` method is ``None``.
# The 3rd argument is the default value of the attribute which we are trying to fetch.
# This means, when the object `human` did not have `empathy` attribute and we tried
# to get it using ``getattr``, the default value ``None`` was returned.
#
# We can verify this by printing the output of `human.info()`.

print(human.info())

# %%
# However, if we run the `grow` method first, this will result in setting the `empathy`
# attribute to `human`. Consequently, we can see a different output when we run `human.info` after that.

human.grow()

print(human.info())


