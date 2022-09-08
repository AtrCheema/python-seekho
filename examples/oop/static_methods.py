"""
===================
3.9 static methods
===================

In previous section we wrote a code to count number of instances of class using
a public attribute of a class. If we make this attribute `private` , we can create
a method inside the class to acquire its value. In following example, we do it
by ``PopulationCount`` method.
"""



# %%


class Insan:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def PopulationCount(self):
        return Insan.__counter


ali = Insan()
print(ali.PopulationCount())
hasan = Insan()
print(hasan.PopulationCount())

# %% md
# So far so good. But we have a problem, first, the ``PopulationCount`` does not
# have anything to do with the instance of class `Insan` i.e. `ali` and second,
# if we want access this method directly from class' instance, we will encounter
# an error as shown below.

# %%

# uncomment following line
# Insan.PopulationCount()  # TypeError

# %% md
# This is because, the method ``PopulationCount`` takes one input argument ``self``.
# When we call this method using instance of class, python implicity puts the
# class' instance, ``ali`` in this case, as an input argument but now we are not
# calling this method from instance, so python does not provide the implicit
# first input argument to this method.
# We could however, avoid this error by explicitly providing the instance ``ali``
# as first input argument.

# %%

Insan.PopulationCount(ali)

# %% md
# However, this is not a good way. An alternative would be to avoid the ``self`` statement when
# defining the method in the class.


# %%

class Insan:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def PopulationCount():
        return Insan.__counter


Insan.PopulationCount()

# %% md
# But now we can't access this method from the instance, because when we access
# this method from instance, python implicitly gives instance `ali` as first
# input argument to this method but the method does not take any input argument
# as the error message also depicts this.

# %%

# uncomment following two lines
# ali = Insan()  # TypeError
# ali.PopulationCount()

# %% md
# The way to solve this problem is to put the decorate `@staticmethod`. By doing so, python will not
# put the instance implicitly as first input argument.


# %%

class Insan:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def PopulationCount():
        return Insan.__counter


print(Insan.PopulationCount())
ali = Insan()
print(ali.PopulationCount())
hasan = Insan()
print(hasan.PopulationCount())
print(Insan.PopulationCount())

# %% md
# why to use them?
#------------------
#
# Static methods are used to group a utility function with a class.

# %%


class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")


date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

# %% md
# since ``toDashDate`` works only for dates, it's logical to keep it inside
# the Dates class
# Consider another example. Suppose we have a large number of examples which
# perform mathmatical functions such as ``ceil``, ``multiply``, ``exponent``, ``devide``
# on some input arguments. Then it would be logical to just group all such
# functions one one class such as ``math`` and use the functions as ``math.ceil(2.2)``
# or ``math.exp(2.3)`` etc.

# %%


class math():

    @staticmethod
    def ceil(x):
        # perform ceil operation
        return

    @staticmethod
    def exp(x):
        # perform exponent operation
        return

    # more methods


# %% md
# This increases code readability.
