"""
===============
3.11 property
===============

"""
# %% md
# Let's say we have a for human body metabolism which has temperature as one of
# its parameters(attributes) and we want to have controle over this parameter in
# such a way that we can set the temperature from outside as well while the model
# itself also changes the temperature parameter when it is run.

# %%

class Model:

    def __init__(self, temp):
        self.temp = temp


x = Model(39)
print(x.temp)

x.temp = 35
print(x.temp)

# %% md
# Thus we can set the temperature from outside the class.
# But what if after some time we want to set certain condition on temperature
# attribute such as the tempeperature should never be above 45 degrees and below 20 degrees.


# %%

class Model:

    def __init__(self, temp):
        self.set_temp(temp)

    def set_temp(self, x):
        if x > 45:
            x = 45
        if x < 20:
            x = 20
        self.temp = x

    def get_temp(self):
        return self.temp


x = Model(39)
print(x.temp)

# %% md
# We can set the temperature as before but then we may violate the condition as well

# %%

x.temp = 55
print(x.temp)

# %% md
# In order to set the temperature, we have to now make use of method `set_temp`.

# %%

x.set_temp(55)
print(x.temp)

# %% md
# if we want to change the temperature value based upon its current value, we can do as following

# %%

print(x.get_temp())
x.set_temp(x.get_temp() * 0.9)
print(x.get_temp())

# %% md
# we were able to decrease the temperature but there are two problems.
# * First the statement ``x.set_temp(x.get_temp()*0.9)`` does not look so elegant,
# it would have been much better and clearer if we could do like ``x.temp = x.temp*0.9``.
# * There are two ways to set and get temperature which is against the
# zen of python [1]_ which states
# **There should be one-- and preferably only one --obvious way to do it**.
# Based upon above discussion we would have liked ``temp`` to behave like attribute (`x.temp`)
# but still be able to perform some checks on it behind the scene (which we could do by
# ``x.temp()``) and there should be only one way to set and get its value as well.
# We can solve the second problem by making ``temp`` a private attribute i.e. by making it
# ``__temp``, and then we have to use only setters ``x.set_temp()`` and getters ``x.get_temp``.


# %%

class Model:

    def __init__(self, temp):
        self.set_temp(temp)

    def set_temp(self, x):
        if x > 45:
            x = 45
        if x < 20:
            x = 20
        self.__temp = x

    def get_temp(self):
        return self.__temp


x = Model(39)
print(x.get_temp())

x.set_temp(55)
print(x.get_temp())

# %% md
# But python provides a better solution to solve both of above two problems
# i.e. the `@property` decorator.


# %%

class Model:

    def __init__(self, temp):
        self.temp = temp

    @property
    def temp(self):
        # get temperature from the model through some process
        return self._temp

    @temp.setter
    def temp(self, x):
        if x > 45:
            x = 45
        if x < 20:
            x = 20
        self._temp = x
        return


x = Model(39)
print(x.temp)

x.temp = x.temp * 0.9
print(x.temp)

# %% md
# Just a side note, we don't have provide the default value of `temp` upon class
# initiation. We can make the method to get the current temperature state of the
# model. In many cases our model will be saved in an external file. For simplicity,
# suppose, our model is saved as dictionary `MODEL`. We can make use of property
# to manipulate `temp`.

# %%

MODEL = {'temp': 39}


class Model:

    def __init__(self):
        pass

    @property
    def temp(self):
        # get temperature from the model through some process
        t = MODEL['temp']
        return t

    @temp.setter
    def temp(self, x):
        if x > 45:
            x = 45
        if x < 20:
            x = 20
        MODEL['temp'] = x
        return


x = Model()
print(x.temp)

x.temp = x.temp * 0.9
print(x.temp)

# %% md
# run the model and check the temperature again

# %%

MODEL

# %% md
# What happens if we skip setter i.e. `@temp.setter`? This will make the attribute
# readonly, and any user of the class will not be able to modify its value from
# outside the class using instance.

# %%


MODEL = {'temp': 39}


class Model:

    def __init__(self):
        pass

    @property
    def temp(self):
        # get temperature from the model through some process
        t = MODEL['temp']
        return t


x = Model()
print(x.temp)

# %%

# uncomment followingline
# x.temp = x.temp * 0.9  # AttributeError


print(x.temp)

# %% md
# run the model and check the temperature again
#
# .. [1] `<https://www.python.org/dev/peps/pep-0020/>`_
