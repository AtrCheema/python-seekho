"""
==================
16. __getattr__
==================
This file shows the usage of ``__getattr__``

"""


from weakref import WeakKeyDictionary

import numpy as np


########################################################
# If a class does not have an attribute and we try to access this attribute
# we will get AttributeError.

class Human: pass

h = Human()
# uncomment following 1 line
# h.horns

#%%
# The Human does not have an attribute ``horns`` and therefore
# when we run ``h.horns``, we will get AttributeError

########################################################
# However, if we want to avoid such an error, we can overwrite
# ``__getattr__`` method of the class. This method must take one input
# argument.

class Human:
    def __getattr__(self, item):
        print(f"attribute {item} has not been set to Human")
        return

h = Human()
h.horns

########################################################
# When python tries to search attributes of a class, then this
# method is called at the end of its search. If this method is not
# overwritten by the user, python will raise ``AttributeError``, as it
# was done earlier.


########################################################
# One advantage/usage of this method is what we can call *dynamic attribute creation*.


TempUnitConverter = {
    "FAHRENHEIT": {
        "Fahrenheit": lambda fahrenheit: fahrenheit * 1.0,  # fahrenheit to Centigrade
        "Kelvin": lambda fahrenheit: (fahrenheit + 459.67) * 5/9,  # fahrenheit to kelvin
        "Centigrade": lambda fahrenheit: (fahrenheit - 32.0) / 1.8  # fahrenheit to Centigrade
    },
    "KELVIN": {
        "Fahrenheit": lambda kelvin: kelvin * 9/5 - 459.67,  # kelvin to fahrenheit
        "Kelvin": lambda k: k*1.0,     # Kelvin to Kelvin
        "Centigrade": lambda kelvin: kelvin - 273.15  # kelvin to Centigrade}
    },
    "CENTIGRADE": {
        "Fahrenheit": lambda centigrade: centigrade * 1.8 + 32,  # Centigrade to fahrenheit
        "Kelvin": lambda centigrade: centigrade + 273.15,  # Centigrade to kelvin
        "Centigrade": lambda centigrade: centigrade * 1.0}
}


class Temp(object):
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
                raise ValueError("output", self.__class__.__name__, out_unit, self.allowed)

            val = TempUnitConverter[self.input_unit][str(out_unit)](self.val)
            return val

    @property
    def allowed(self):
        return list(TempUnitConverter.keys())

    @property
    def input_unit(self):
        return self._input_unit

    @input_unit.setter
    def input_unit(self, in_unit):
        if in_unit.upper() == 'CELCIUS':
            in_unit = 'CENTIGRADE'
        if in_unit.upper() not in self.allowed:
            raise ValueError("Input", self.__class__.__name__, in_unit, self.allowed)
        self._input_unit = in_unit.upper()


temp = np.arange(10)
T = Temp(temp, 'Centigrade')

T.Kelvin

#%%

T.Fahrenheit

#%%

T.Centigrade

#%%
# Above we did not explicitly defined ``Kelvin``, ``Fahrenheit`` or ``Centigrade``
# attributes of the ``Temp`` class.
# but these attribtues are created after ``__getattr__`` method is called.