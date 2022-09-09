"""
====================
3.10 class methods
====================

"""

import datetime

# %% md
# In previous section we saw that we can make a method linked to class by removing
# the keyword ``self`` from its input arguments and in this way we can call this
# method from class such as ``ClassName.MethodName()``.

# %%


class Insan:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def PopulationCount():
        return Insan.__counter


Insan.PopulationCount()

# %% md
# Let's say, we also want to count male population, then we can add another static
# method as follows:

# %%


class Insan:
    __counter = 0
    __MaleCounter = 0

    def __init__(self, gender):
        if gender == 'male':
            type(self).__MaleCounter += 1

        type(self).__counter += 1

    @staticmethod
    def PopulationCount():
        return Insan.__counter

    @staticmethod
    def MaleCount():
        return Insan.__MaleCounter


ali = Insan('male')
fatima = Insan('female')

Insan.PopulationCount()

# %%

Insan.MaleCount()

# %% md
# If we want to now add female counter in above class, one way of doing it is
# to indirectly calculating it from total counter and male counter as follows

# %%


class Insan:
    __counter = 0
    __MaleCounter = 0

    def __init__(self, gender):
        if gender == 'male':
            type(self).__MaleCounter += 1

        type(self).__counter += 1

    @staticmethod
    def PopulationCount():
        return Insan.__counter

    @staticmethod
    def MaleCount():
        return Insan.__MaleCounter

    def FemaleCount():
        return Insan.__counter - Insan.__MaleCounter


ali = Insan('male')
fatima = Insan('female')

# %%

print(Insan.PopulationCount())

# %%

print(Insan.MaleCount())

# %%

Insan.FemaleCount()

# %% md
# Another way of achieving this is to use the decorator ``@classmethod``. The use
# of this decorator makes sure that when we call this method, the first default
# implicit argument, that python provides to this method is the class itself.
# Thus we can make use of some static methods of the class without initializing the class

# %%


class Insan:
    __counter = 0
    __MaleCounter = 0

    def __init__(self, gender):
        if gender == 'male':
            type(self).__MaleCounter += 1

        type(self).__counter += 1

    @staticmethod
    def PopulationCount():
        return Insan.__counter

    @staticmethod
    def MaleCount():
        return Insan.__MaleCounter

    @classmethod
    def FemaleCount(cls):
        return cls.__counter - cls.__MaleCounter


ali = Insan('male')
fatima = Insan('female')
zeinab = Insan('female')

print(Insan.PopulationCount())

# %%
print(Insan.MaleCount())

# %%

Insan.FemaleCount()

# %% md
# So until here class methods are behaving same as static methods in addition to
# that we can access other static methods of the class. It may not make a lot of
# sense but we will come to such use of class method once we cover ``inheritance``.
# Now Consider the following example:

# %%


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age


ali = Student('ali', 12)
print(type(ali))

# %% md
# But let's say, for a particular student we don't know his/her age but we know the
# birth year. Thus we would like to build the class from birth year directly as well.

# %%


class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, BirthYear):
        current_year = datetime.date.today().year
        age = current_year - BirthYear
        return cls(name, age)


ali = Student('ali', 12)
print(type(ali))

# %%

hasan = Student.fromBirthYear('hasan', 1997)
print(type(hasan))

# %%

print(hasan.age)

# %% md
# Thus we used the ``class method`` to build/initiate the class from birth year.
# We could have performed the conversion of ``BirthYear`` to ``age`` outside the class as
# well but this way provides a more user friendly interface of the class and
# the code is more organized.

