"""
=================
3.12 Descriptors
=================
"""

# %%
# Descriptors are another way to control, what happens when a value of an attribute
# is set or accessed. We do it while making a class with at least one of
# ``__get__``, ``__set__`` and ``__del__`` methods.

# %%


class MyDescriptor(object):
    """
    Basic descriptor to set and get value.
    """

    def __init__(self, initval=None):
        print("__init__ of MyDescriptor called with initial value: ", initval)
        self.__set__(self, initval)

    def __get__(self, instance, owner):
        print(instance, owner)
        print('Getting  self.val: ', self.val)
        return self.val

    def __set__(self, instance, value):
        print('Setting self.val to ', value)
        self.val = value


class Model(object):
    temp = MyDescriptor(37)  # Descriptor is attached at class definition time


body = Model()

# %%
# When we created an instance of `Model` class, the `MyDescriptor` was initiated. When
# `MyDescriptor` was initiated, its ``__init__`` method was called and got
# the string printed.

print(body.temp)  # a function call from `MyDescriptor` class is hiding here

# %%
# Above when we ran `body.temp`, the ``__get__`` method of `MyDescriptor`
# class for `temp` attribute ran.

body.temp = 38  # a function call is hiding here

# %%

print(body.temp)

# %% md
# Thus we see when we get the value of attribute ``temp``, the method ``__get__`` in
# `MyDescriptor` gets executed and similarly when we set a value to attribute
# `temp`, the method ``__set__`` in `MyDescriptor` gets executed.

# %% md
# In ``__get__`` method of `MyDescriptor` class, instance is `body` and and owner is `Model`.

# %% md
# If we want to know what attributes are stored in ``__dict__`` of class and instance,
# we can do as following

# %%

print(body.__dict__)

# %% md
# The ``__get__`` and ``__set__`` of descriptor can be applied only on those
# attributes which are present in ``__dict__`` of owner class i.e. `Model` in this case.

# %%

# alternative to print(Model.__dict__)


for key, val in Model.__dict__.items():
    print(key, ': ', val)

# %%
# alternative to print(MyDescriptor.__dict__)

for key, val in MyDescriptor.__dict__.items():
    print(key, ': ', val)

# %% md
# We can call `get` from class and its instance but `set` can and should only be
# called from instance. If we do it from class, this means overriding descriptor.

# %%


print(Model.temp)

# %%

Model.temp = "useless"
print(Model.temp)

# %%

print(body.temp)

# %% md
# This means we should do some type checking before assigning a value to an attribute.
# Consider `descriptor` from another angle below.


# %%

class LazyDescriptor(object):
    def __init__(self, name, inival):
        self._val = inival
        self.name = name

    def __get__(self, instance, owner):
        print('get in descriptor called')
        instance.__dict__[self.name] = self._val
        return self._val


class Model(object):
    temp = LazyDescriptor("temp", 37)


body = Model()

# %%

print(body.temp)

# %%
# Above we we ran `body.temp`, the ``__get__`` method of descriptor was called.

print(body.temp)

# %% md
# So the first time we referenced temp, it called the descriptor but not the
# second time. Let's look at the `__dict__` for better understanding.

# %%

body = Model()
print(body.__dict__)

# %%

print(body.temp)

# %%

print(body.__dict__)

# %%

print(body.temp)

# %%

print(body.__dict__)

# %% md
#
# So when we tried to access the value of `x` for the first time, the `key` was
# not in ``object.__dict__`` so the descriptor's ``__get__`` was called but when it is
# already present, the ``__get__`` from descriptor was not called. This is
# because of order in which python looks for attributes of objects. For complete
# sequence of rules `see this link <http://simeonfranklin.com/talk/descriptors.html#slide-42>`_.
# We can achieve exactly same by another way as well.

# %%


class LazyProperty(object):
    def __init__(self, val):
        self._val = val
        self.name = val.__name__

    def __get__(self, instance, owner):
        print("get in descriptor called")
        result = self._val(instance)
        instance.__dict__[self.name] = result
        return result


class Model(object):
    @LazyProperty
    def temp(self):
        return 42


body = Model()

# %%

print(body.temp)

# %%

print(body.temp)

# %% md
# Usage cases
# -------------
# Suppose we define a class which takes the `name`, `weight` and `height` as input/for
# initiation and has a method to calculate body mass index i.e. `bmi`.

# %%


class Insan:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight  # in kg
        self.height = height  # in meters

    def bmi(self):
        return self.weight / self.height ** 2


ali = Insan('ali', 78, 1.7)
ali.bmi()

# %% md
# The problem with the above code is that one can assign negative values to weight.

# %%

ali.weight = -10
ali.bmi()

# %% md
# Definitely it is wrong and we should perform some checks before setting the new value.
# We can do it by using `property`


# %%

class Insan:
    def __init__(self, name, weight, height):
        self.name = name
        self._weight = weight  # in kg
        self.height = height  # in meters

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError('weight cannot be negative.')
        self._weight = value

    def bmi(self):
        return self.weight / self.height ** 2


ali = Insan('ali', 78, 1.7)

# uncomment following line
# ali.weight = -80  # ValueError
ali.bmi()

# %% md
# Thus upon negative weight, it threw error. But `height` can still be assigned a negative value.

ali = Insan('ali', 78, 1.7)
ali.height = -1.8
print(ali.height)

# %% md
# Let's make use of `property` once more.


# %%

class Insan:
    def __init__(self, name, weight, height):
        self.name = name
        self._weight = weight  # in kg
        self._height = height  # in meters

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError('weight cannot be negative.')
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('height cannot be negative.')
        self._height = value


ali = Insan('Ali', 78, 1.7)

# uncomment following line
# ali.weight = -80  # ValueError

# %% md
# But we are repeating our code. Both the properties are essentially doing
# same thing i.e. throwing errors on negative value assignment, so remember
# our code should be DRY (do not repeat yourself)
# To helps us, python has the concept of `descriptors`. We can define a
# descriptor which can have ``set``, ``get`` and ``del`` methods. The following
# code defines the descriptor `NonNegative`. Then inside class `Insan`, we
# define class attributes and bind them with the descriptor thus making sure
# that these attributes will always be non-negative otherwise an error will be thrown.

# %%

class NonNegative:
    def __init__(self, name):
        # the name attribute is needed because when the NonNegative object is
        # created , the assignment to attribute named weight/height hasn't
        # happen yet. Thus, we need to explicitly pass the name weight/height to the
        # initializer of the object to use as the key for the instance's __dict__.
        self.name = name

    def __get__(self, instance, owner):
        # we need to reach into the __dict__ object directly, because the
        # builtins would be intercepted
        #  by the descriptor protocols too and cause the RecursionError.
        return instance.__dict__[self.name]  # getattr(instance, self._name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("{} Cannot be negative.".format(self.name))
        # instead of using builtin function getattr and setattr, we need to reach
        # into the __dict__ object directly, because the builtins would be intercepted
        #  by the descriptor protocols too and cause the RecursionError.
        instance.__dict__[self.name] = value  # setattr(instance, self._name, value)


class Insan:
    weight = NonNegative('weight')
    height = NonNegative('height')

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight  # in kg
        self.height = height  # in meters

    def bmi(self):
        return self.weight / self.height ** 2


ali = Insan('Ali', 78, 1.7)
ali.bmi()

# %% md
# Now we can not assign negative values to attributes ``weight`` and ``height`` of class ``Insan``.

# %%

# uncomment following line
# ali.weight = -80 # ValueError: Cannot be negative

# %%

# uncomment following line
# ali.height = -1.8  # ValueError: Cannot be negative

# %% md

### In python 3.6+

# The `descriptor` definition in python 3.6+ is more flexible.


# %%

class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('{} Cannot be negative.'.format(self.name))
        instance.__dict__[self.name] = value

    # __set_name__ is called at the time the owning class owner is created.
    # The descriptor has been assigned to name. With this protocol, we can now
    # remove the __init__  and bind the attribute name to the descriptor
    def __set_name__(self, owner, name):
        self.name = name


class Insan:
    weight = NonNegative()
    height = NonNegative()

    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight  # in kg
        self.height = height  # in meters

    def bmi(self):
        return self.weight / self.height ** 2


ali = Insan('Ali', 78, 1.7)
ali.bmi()

# %%

# uncomment following line
# ali.weight = -80  # ValueError: Cannot be negative

# %%

# uncomment following line
# ali.height = -1.8  # ValueError: Cannot be negative

# %% md
# Let's say, we want to calculate a new quantity say `bmi` which is multiplication of
# `BMI` with `temperature` in Celsius. We can define a property to convert the
# temperature into Celsius, in case the temperature is provided in Fahrenheit.

# %%

class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('{} Cannot be negative.'.format(self.name))
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Insan:
    weight = NonNegative()
    height = NonNegative()

    def __init__(self, name, weight, height, temp_f):
        self.name = name
        self.weight = weight  # in kg
        self.height = height  # in meters
        self.fahrenheit = temp_f

    @property
    def celsius(self):
        return 5 * (self.fahrenheit - 32) / 9.0

    @celsius.setter
    def celsius(self, val):
        self.fahrenheit = 32 + 9 * val / 5.0

    def bmit(self):
        return self.weight / self.height ** 2 * self.celsius


ali = Insan('Ali', 78, 1.7, 98.2)
ali.bmit()

# %%

print(ali.celsius)

# %% md
# But we can also define it as `descriptor` as follows. Furthermore we are also
# performing non-negative check in this descriptor as well.


# %%

class Celsius:

    def __get__(self, instance, owner):
        return 5 * (instance.fahrenheit - 32) / 9

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('{} Cannot be negative.'.format(self.name))
        instance.fahrenheit = 32 + 9 * value / 5

    def __set_name__(self, owner, name):
        self.name = name


class NonNegative:

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('{} Cannot be negative.'.format(self.name))
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Insan:
    weight = NonNegative()
    height = NonNegative()

    celsius = Celsius()

    def __init__(self, name, weight, height, temp_f):
        self.name = name
        self.weight = weight  # in kg
        self.height = height  # in meters
        self.fahrenheit = temp_f  # temperature in fahrenheit

    def bmit(self):
        return self.weight / self.height ** 2 * self.celsius


ali = Insan('Ali', 78, 1.7, 98.2)
ali.bmit()

# %%

print(ali.fahrenheit)

# %%

print(ali.celsius)

# %%

# uncomment following line
# ali.celsius = -30  # ValueError

# %% md
# Caveat
# --------
# Because the descriptors are linked with class and not with instance, so when we create
# a new instance, the values get overridden by new instance if they are not linked with instance.

# %%


class Descriptor:
    def __init__(self):
        self.__temp = 0

    def __get__(self, instance, owner):
        return self.__temp

    def __set__(self, instance, value):
        if isinstance(float(value), float):
            print(value)
        else:
            raise TypeError("Body Temperature must be float or integer")

        if value < 20:
            raise ValueError("Body Temperature can never be less than 20")

        self.__temp = value

    def __set_name__(self, owner, name):
        self.name = name


class Model:
    temp = Descriptor()

    def __init__(self, name, weight, temp):
        self._name = name
        self.weight = weight
        self.temp = temp

    def __str__(self):
        return "{0} with weight {1} has body temperature {2} Celsius.".format(self._name, self.weight, self.temp)


body1 = Model("Ali", 80, 40)
print(body1)

# %%

print(body1.__dict__)

# %%

body2 = Model("Hasan", 75, 37)
print(body2)

# %%

print(body1)

# %% md
# The solution is to bind the attribute with instance in descriptor as shown below.

# %%


class Descriptor:
    def __init__(self):
        self.__temp = 0

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if isinstance(float(value), float):
            print(value)
        else:
            raise TypeError("Body Temperature must be float or integer")

        if value < 20:
            raise ValueError("Body Temperature can never be less than 20")

        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Model:
    temp = Descriptor()

    def __init__(self, name, weight, temp):
        self.name = name
        self.weight = weight
        self.temp = temp

    def __str__(self):
        return "{0} with weight {1} has body temperature {2} Celsius.".format(self.name, self.weight, self.temp)


body1 = Model("Ali", 80, 40)
print(body1)

# %%

print(body1.__dict__)

# %%

body2 = Model("Hasan", 75, 37)
print(body2)

# %%

print(body1)

# %% md
# Using WeakKeyDictionary
# -------------------------
# Usually the attributes from descriptors are saved in ``WeakKeyDictionary``. The
# above code can be implemented using ``WeakKeyDictionary`` as shown below

# %%

from weakref import WeakKeyDictionary


class Descriptor:
    def __init__(self):
        self.data = WeakKeyDictionary()

    def __get__(self, instance, owner):
        return self.data[instance]

    def __set__(self, instance, value):
        if isinstance(float(value), float):
            print(value)
        else:
            raise TypeError("Body Temperature must be float or integer")

        if value < 20:
            raise ValueError("Body Temperature can never be less than 20")

        self.data[instance] = value

    def __set_name__(self, owner, name):
        self.name = name


class Model:
    temp = Descriptor()

    def __init__(self, name, weight, temp):
        self.name = name
        self.weight = weight
        self.temp = temp

    def __str__(self):
        return "{0} with weight {1} has body temperature {2} Celsius.".format(self.name, self.weight, self.temp)


body1 = Model("Ali", 80, 40)
print(body1)

# %%

body2 = Model("Hasan", 75, 37)
print(body2)

# %%

print(body1)

# %% md

# %%
# **References:**
#
# The material in this lesson is inspired from following posts
#
#    * `talk on descriptors <http://simeonfranklin.com/talk/descriptors.html>`_
#    * `Python course eu website <https://www.python-course.eu/python3_descriptors.php>`_
#    * `Encapsulation with descriptors <https://pyvideo.org/pycon-us-2013/encapsulation-with-descriptors.html>`_
#    * `Some great answers on stackoverflow <https://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors>`_
#    * `A post by Daw Ran Liou <https://dev.to/dawranliou/writing-descriptors-in-python-36>`_
#    * `DataCamp <https://www.datacamp.com/community/tutorials/python-descriptors>`_
