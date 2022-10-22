"""
=================
3.13 inheritance
=================

"""

# %%
# Inheritance means one class can inherit ``attributes`` and ``methods`` of parent class.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def say_salam(self):
        print('Salam, my name is', self.name)


class Muslim(Human):
    pass


ali = Muslim('Ali')
ali.say_salam()

# %% md
# The ``Muslim`` class itself does not have a method ``say_salam`` but since
# it is inheriting from ``Human`` class and ``say_slam`` exists in ``Human``
# class, we do end up calling ``say_salam`` method fo ``Human`` class.
#
#
# We can check the type of the ``ali`` which is an object and is an ``instance``
# of class ``Muslim``. There are two ways to verify this.

# %%


isinstance(ali, Muslim), type(ali) == Muslim

# %% md
# However, ``isinstance`` checks the parent classes as well but ``type`` function does not do so.

# %%

isinstance(ali, Human), type(ali) == Human

# %%

arjun = Human('arjun')

isinstance(arjun, Human), isinstance(arjun, Muslim)

# %% md
# So it is always safe to check the type of an object by ``instance``.
#
# Inheritance can occur between more than two classes as well. In following, ``Pakistani``
# class inherits from `Muslim` class which itself inherits from ``Human`` class.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name


class Muslim(Human):
    pass


class Pakistani(Muslim):
    pass


ali = Pakistani('ali')

isinstance(ali, Human)

# %% md
# We can override the methods of parent or super class in its child class by
# simply redefining the ``method``.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):

    def introduction(self):
        print('Salam, my name is', self.name)


ali = Muslim("ali")

ali.introduction()

# %%

Human.introduction(ali)

# %% md
# If in a child class we want to call/use method from a parent/super class, we can call method
# from parent/super class using the `super()` function as following.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):

    def introduction(self):
        print("I will call introduction method of parent class")
        super().introduction()


ali = Muslim("ali")

ali.introduction()

# %% md
# Above, the ``introduction`` method of ``Muslim`` class calls the ``introduction`` method of ``Human``.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):

    def introduction(self):
        print("salam: my name is ", self.name)


class Pakistani(Muslim):

    def introduction(self):
        print("I will call introduction method of parent class")
        super().introduction()


ali = Pakistani("ali")

ali.introduction()

# %% md
# If a method is not present in super / parent class , python will keep on looking
# in all parent / super classes in the hierarchy until it finds the method or
# attribute being called.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):
    pass


class Pakistani(Muslim):

    def introduction(self):
        print("I will call introduction method of parent class")
        super().introduction()


ali = Pakistani("ali")

ali.introduction()


# %%

class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):
    pass


class Pakistani(Muslim):
    pass


ali = Pakistani("ali")

ali.introduction()

# %% md
# However, if the called method does not exist in any of the parent classes, then python
# will throw ``AttributeError``.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction1(self):
        print('Hello, my name is', self.name)


class Muslim(Human):
    pass


class Pakistani(Muslim):
    pass


ali = Pakistani("ali")

# uncomment following line
# ali.introduction()  # AttributeError

# %% md
# If in a child class , we want to implement a method of a parent class but not of immediate parent
# class, we can directly call that method.
#
# Below, ``Pakistani`` class is inheriting from ``Muslim`` but in introduction method of
# ``Pakistani``, we don’t want to call ``introduction`` method of ``Muslim`` class rather we
# want to call ``introduction`` method of ``Human`` class.We can do this by ``Human.introduction()``

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):

    def introduction(self):
        print('Salam, my name is', self.name)


class Pakistani(Muslim):

    def introduction(self):
        Human.introduction(self)
        print("I am a Pakistani. ")


ali = Pakistani("ali")

ali.introduction()

# %% md
# One of the function of method overriding is to implement abstract methods.

# %%


class Human(object):

    def nationality(self):
        raise NotImplementedError("implement this method in child class")


class Pakistani(Human):

    def nationality(self):
        return "pakistani"


class Iranian(Human):
    def nationality(self):
        return "iranian"


class Israili(Human):
    pass


ali = Pakistani()
ali.nationality()

# %%

armaghan = Iranian()
armaghan.nationality()

# %%

yakov = Israili()

# uncomment following line
# yakov.nationality()  # NotImplementedError

# %% md
# We can enlist all base classes in a hierarchy of given class.

class Human(object):
    pass


class Muslim(Human):
    pass


class Pakistani(Human):
    pass


class Punjabi(Pakistani):
    pass


print(Punjabi.__mro__)

# %%

print(Muslim.__mro__)

# %% md
# We can initiate a child class with additional arguments than required to initiate the
# parent class. For this we have to overwrite ``__init__()`` method of the child class.

# %%


class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):

    def __init__(self, name, sect):
        self.sect = sect
        super(Muslim, self).__init__(name)

    def introduction(self):
        print('Salam, my name is {} and my sect is {}'.format(self.name, self.sect))


# Uncomment following line
# ali = Muslim("ali")  # TypeError

# %% md
# Above, the ``Muslim`` class now requires two arguments for initiation i.e. `name``
# and `sect`. We did not provide value for ``sect``.

# %%


ali = Muslim("ali", None)
ali.introduction()

# %% md
# Instead of using ``super(ChildClass, self).__init__()`` we can also simple say ``super().__init__()``.


# %%

class Human(object):

    def __init__(self, name):
        self.name = name

    def introduction(self):
        print('Hello, my name is', self.name)


class Muslim(Human):

    def __init__(self, name, sect):
        self.sect = sect
        super().__init__(name)

    def introduction(self):
        print('Salam, my name is {} and my sect is {}'.format(self.name, self.sect))


ali = Muslim("ali", None)
ali.introduction()

# %%

type(ali.sect)

# %%

kapil = Human('kapil')

# uncomment following line
# kapil.sect  # AttributeError

# %% md
# Since ``kapil`` is an instance of ``Human`` class which does not have any attribute named
# ``sect``, thus we could not access this attribute.

# %%
# multiple-inheritance
# ---------------------
# A class can also inherit from multiple classes and this is called ``multiple-inheritance``.

# %%


class Spirit(object):
    chastity = 'NaN'
    bravery = 'NaN'
    tolerance = 'NaN'


class Body(object):
    weight = 20


class Human(Spirit, Body):
    pass


ali = Human()
print(ali.chastity)

# %%

print(ali.weight)

# %% md
# If an attribute of the child class is called, it is first looked in the child class,
# then in the first parent class and then in second parent class.

# %%


class Spirit(object):
    chastity = 'NaN'
    bravery = 'NaN'
    identity = 'NaN'


class Body(object):
    identity = 'name'


class Human(Spirit, Body):
    pass


ali = Human()
print(ali.identity)

# %% md
# Above, ``identity`` attribute exists for ``Body`` and ``Spirit`` class but
# since ``Spirit`` class comes first, so ``NaN`` is printed which is value of
# ``identity`` attribute of ``Spirit`` class. Sometimes, we may want to initialize
# both parent classes with separate initializing arguments. In following, ``Body``
# class requires two initiating arguments while ``Spirit`` class can be initialized
# with as many arguments as possible.

# %%


class Spirit(object):
    def __init__(self, **kwargs):
        print("initializing spirit")
        for k, v in kwargs.items():
            print('setting: ', k, 'to ', v)
            setattr(self, k, v)
        print("finished initializing spirit")


class Body(object):
    def __init__(self, weight, height):
        print("initializing body")
        self.weight = weight
        self.height = height
        print("finished initializing body")


class Human(Spirit, Body):
    def __init__(self, name, weight, height, **kwargs):
        print("initializing Human")
        self.name = name
        Spirit.__init__(self, **kwargs)
        Body.__init__(self, weight, height)


ali = Human('ali', 60, 175, chastity='NotANumber')

print("Name: ", ali.name)
print("Weight: ", ali.weight)
print("Height: ", ali.height)
print("Chastity: ", ali.chastity)

# %% md
# Instead of initializing both parent classes separately, call to ``super()`` method
# will suffice to initiate all parent classes at once.


# %%

class Spirit(object):
    def __init__(self, **kwargs):
        print("initializing spirit")
        for k, v in kwargs.items():
            print('setting: ', k, 'to ', v)
            setattr(self, k, v)
        print("finished initializing spirit")


class Body(object):
    def __init__(self, weight, height):
        print("initializing body")
        self.weight = weight
        self.height = height
        print("finished initializing body")


class Human(Spirit, Body):
    def __init__(self, name, weight, height, **kwargs):
        print("initializing Human")
        self.name = name
        super().__init__(weight=weight, height=height, **kwargs)


ali = Human('ali', 60, 175, chastity='NotANumber', honesty="undefined")

print("Name: ", ali.name)
print("Weight: ", ali.weight)
print("Height: ", ali.height)
print("Chastity: ", ali.chastity)
