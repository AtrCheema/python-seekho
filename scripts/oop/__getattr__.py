"""
==================
3.16 __getattr__
==================
This lesson describes the usage of ``__getattr__``

"""


########################################################
# If a ``class`` (more correctly ab object) does not have an attribute and we try to access this attribute
# we will get ``AttributeError``.

class Human:
    pass


h = Human()

# uncomment following 1 line
# h.horns

# %%
# The `Human` class does not have an attribute `horns` and therefore
# when we run `h.horns`, we will get AttributeError

########################################################
# However, if we want to avoid such an error, we can overwrite
# ``__getattr__`` method of the class. This method must take one input
# argument.


class Human:
    def __getattr__(self, item):
        print(f"attribute {item} has not been set to Human")
        return


h = Human()
print(h.horns)

########################################################
# When python tries to search attributes of a class, then ``__getattr__``
# method is called at the end of its search. If this method is not
# overwritten by the user, python will raise ``AttributeError``, as it
# was done earlier.


########################################################
# One advantage/usage of this method is what we can call *dynamic attribute creation*.


TempUnitConverter = {
    "FAHRENHEIT": {
        "Fahrenheit": lambda fahrenheit: fahrenheit,  # fahrenheit to Centigrade
        "Kelvin": lambda fahrenheit: [(x + 459.67) * 5/9 for x in fahrenheit],  # fahrenheit to kelvin
        "Centigrade": lambda fahrenheit: [(x - 32.0) / 1.8 for x in fahrenheit]  # fahrenheit to Centigrade
    },
    "KELVIN": {
        "Fahrenheit": lambda kelvin: [x * 9/5 - 459.67 for x in kelvin],  # kelvin to fahrenheit
        "Kelvin": lambda k: k,     # Kelvin to Kelvin
        "Centigrade": lambda kelvin: [x - 273.15 for x in kelvin]  # kelvin to Centigrade}
    },
    "CENTIGRADE": {
        "Fahrenheit": lambda centigrade: [x * 1.8 + 32.0 for x in centigrade],  # Centigrade to fahrenheit
        "Kelvin": lambda centigrade: [x + 273.15 for x in centigrade],  # Centigrade to kelvin
        "Centigrade": lambda centigrade: centigrade
    }
}


class Temperature(object):
    """
    The idea is to write the conversion functions in a dictionary and
    then dynamically create attribute if the attribute
    is present in converter as key otherwise raise WongUnitError.
    converts temperature among units [kelvin, centigrade, fahrenheit]

    """

    def __init__(self, val, input_unit):
        self.val = val

        self.input_unit = input_unit

    def __getattr__(self, out_unit):
        # pycharm calls this method for its own working, executing default behaviour at such calls
        if out_unit.startswith('_'):
            return self.__getattribute__(out_unit)
        else:
            if out_unit not in TempUnitConverter[self.input_unit]:
                raise ValueError(f"output in {out_unit} is not allowed. Allowed units are: ", self.allowed)

            val = TempUnitConverter[self.input_unit][str(out_unit)](self.val)
            return val

    @property
    def allowed(self):
        return list(list(TempUnitConverter.values())[0].keys())

    @property
    def input_unit(self):
        return self._input_unit

    @input_unit.setter
    def input_unit(self, in_unit):
        if in_unit.upper() == 'CELSIUS':
            in_unit = 'CENTIGRADE'
        if in_unit.upper() not in TempUnitConverter:
            raise ValueError(f"Input in {in_unit} is not allowed", self.allowed)
        self._input_unit = in_unit.upper()


temp = [i for i in range(10)]
T = Temperature(temp, 'Centigrade')

print(T.Kelvin)

# %%

print(T.Fahrenheit)

# %%

print(T.Centigrade)

# %%
# Above we did not explicitly defined ``Kelvin``, ``Fahrenheit`` or ``Centigrade``
# attributes of the ``Temperature`` class.
# but these attributes are created after ``__getattr__`` method is called.


T = Temperature(temp, 'Fahrenheit')
print(T.Centigrade)
print(T.Kelvin)


# %%

T = Temperature(temp, 'Kelvin')
print(T.Centigrade)
print(T.Fahrenheit)

# %% md
# **Questions:**
#    * Why `Temperature(temp, 'Celsius').Kelvin` works but not `Temperature(temp, 'Celsius').Celsius`?
#    * Change the `Temperature` class so that T.centigrade gives same answer as that of `T.Centigrade`.
#    * Change the `Temperature` class so that `T.Celsius` also works.
