"""
==================================
3.8 class vs  instance attributes
==================================
"""


class Insan:
    ethnicity = "Balochi"


x = Insan()
y = Insan()

print(x.ethnicity)

# %%

print(y.ethnicity)

# %%

print(Insan.ethnicity)

# %%

x.ethnicity = "muhajir"
y.ethnicity

# %%

Insan.ethnicity

# %%

Insan.ethnicity = "Insaniyat"
Insan.ethnicity

# %%

y.ethnicity

# %%

x.ethnicity

# %% md
# Because the attribute was changed for class and instance ``x`` was created before
# this change so ``x`` still has old attribute value.

# %%

x.__dict__

# %%

print(y.__dict__)

# %% md
# Because `y` itself does not have attribute ``ethnicity`` so it looked for the
# attribute value in class `Insan` and used that value for itself.

# %%

print(Insan.__dict__)

# %% md
# So class attributes and instance attributes can have different values. We can
# find out attributes of ``class`` of an ``instance`` from the `instance` using following code

# %%

print(x.__class__.__dict__)


# %%


class philosopher:
    Quotes = (
        """What cannot be imagined cannot even be talked about.""",
        """Philosophy is a battle against the bewitchment of our intelligence by means of language.,""",
        """The limits of my language means the limits of my world."""
    )

    def __init__(self, name='Wittgenstein', dob=1889):
        self.name = name
        self.build_year = build_year

    # other methods as usual


# %%

for number, quote in enumerate(philosopher.Quotes):
    print(str(number + 1) + ":\n" + quote)


# %% md
# Counting instances of a class
# -------------------------------

# %%

class Insan:
    counter = 0

    def __init__(self):
        # every time a new instance is created the attribute 'counter' of 'Insan' increases by 1
        type(self).counter += 1

    def __del__(self):
        # every time an instance of `Insan` is deleted, the attribute 'counter' of 'Insan' decreases by 1
        type(self).counter -= 1


x = Insan()
print("Population count is: : " + str(Insan.counter))
y = Insan()
print("Population count is: : " + str(Insan.counter))
del x
print("Population count is: : " + str(Insan.counter))
del y
print("Population count is: : " + str(Insan.counter))

# %% md
# ``type(self)`` is evaluated back to `Insan`
