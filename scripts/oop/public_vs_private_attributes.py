"""
=================================
3.7 public vs private attributes
=================================

Based on accessibility, attributes can be categorized into 3 categories:
*    Public
*    Protected
*    Private

| ** Naming ** | ** Type ** | ** Description ** |
| --- | --- | --- |
| name | public | The attribute is available both inside and outside class |
|_name | protected | should not be should outside class definition |
|__name | private | inaccessible and invisible outside class definition |

"""

# %%


class Insan():

    def __init__(self):
        self.__ghar = "I am private"
        self._gari = "I am protected"
        self.name = "I am public"


x = Insan()

print(x.name)

# %%

print(x._gari)

# %%

# uncomment following line
# x.__ghar  # AttributeError

# %% md
# Although the ``Insan`` class do have an attribute anmed ``__priv``, however the error
# is saying **Insan object has no attribute __priv**. What better privacy can there be?
# We can also set the values of public attributes.

# %%

x.name = 'hasan'

print(x.name)

# %% md
# As said earlier private attribute is not accessible outside the class but we can
# use them inside class definition as follows:


# %%

class Insan():

    def __init__(self):
        self.__ghar = "I am private"
        self._gari = "I am protected"
        self.name = "I am public"

    def get_ghar(self):
        return self.__ghar


ali = Insan()
ali.get_ghar()

# %% md
# name mangling
# --------------
# Every attribute with double underscore will be changed to ``object._class__attribte``

# %%

print(ali._Insan__ghar)

# %% md
# Ways of accessing and setting attribute values


# %%

class Insan:

    def __init__(self, name=None, dob=2000):
        self.__name = name
        self.__dob = dob

    def say_salam(self):
        if self.__name:
            print("Salam, I am " + self.__name)
        else:
            print("Salam, I am a person without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_dob(self, by):
        self.__dob = by

    def get_dob(self):
        return self.__dob

    def __repr__(self):
        return "Insan('" + self.__name + "', " + str(self.__dob) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", born in Year: " + str(self.__dob)


x = Insan("Mutahri", 1920)
y = Insan("Sadr", 1935)

for fard in [x, y]:
    fard.say_salam()
    if fard.get_name() == "Sadr":
        fard.set_dob(1353)
    print("I was born in the year " + str(fard.get_dob()) + "!")

