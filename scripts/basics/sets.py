"""
==========
1.7 sets
==========
.. important::
  This lesson is still under development.
"""


#%% md
# A set is a collection of objects just like lists with the exception that it
# is unordered, does not contain same objects more than once, and can not
# contain immutable objects like lists.
#
# A set can be created from an existing sequence object such as a string,
# list or tuple.

#%%

urdu = set("National language of Pakistan")

print(type(urdu))

print(urdu)

#%%

pak_langs = set(["Balochi", "Barohi", "Sindhi", "Balti"])
print(pak_langs)

#%% md
# If our sequence contains repeating objects, only one instance of those repeating
# objects will be included in the list.

#%%

pak_langs = set(("Balochi", "Barohi", "Sindhi", "Balti", "Balochi"))
print(pak_langs)

#%% md
# Although, we can create sets from lists, but a set can not contain a list as an object.

#%%

pak_langs = set((("Balochi", "Barohi"), ("punbabi", "siraiki")))
print(pak_langs)

#%%

# uncomment following line
# pak_langs = set((["Balochi", "Barohi"], ["punbabi", "siraiki"]))
print(pak_langs)

#%% md
# In second case above, we want our set to have two lists as objects, so the error was prompted.
# Sets are mutable i.e. they can be changed. We can add new objects in sets as following

#%%

pak_langs = set(["Balochi", "Barohi", "Sindhi"])
pak_langs.add("Pashto")
print(pak_langs)

#%% md
# There are immutable sets as well with the name `frozenset`.

#%%

balochistan_langs = frozenset(["Balochi", "Barohi", "Pashto"])

# uncomment following line
# balochistan_langs.add("punjabi")

#%% md

# Operations on sets



#%% md
# adding elements
# -----------------
# We saw, how to add objects in sets with the method `add`. We can not violate
# aforementioned rules using `add` method.

#%%

imperialists = {"bbc", "cnn"}

# uncomment following line
# imperialists.add(["voa","dw"])  # TypeError

#%%

imperialists.add('bbc')
print(imperialists)

#%%

imperialists.update(["voa","dw"])
print(imperialists)

#%%

imperialists = {"bbc", "cnn"}

# uncomment following line
# imperialists.update([["voa","dw"]])  # TypeError
print(imperialists)

#%% md
# ``|`` operator can also be used to add/concatenate two sets

#%%

imperialists = {"bbc", "cnn"}

imperialists | {"voa", "dw"}

#%%

imperialists = {"bbc", "cnn"}

imperialists |= {"voa", "dw"}

print(imperialists)

#%% md
# `clear`
# ----------
# We can clear the contents of a set by using the method `clear` on a set.

#%%

dakus = {"musharaf", "nawaz", "benazir"}

dakus.clear()  # after NRO (https://en.wikipedia.org/wiki/National_Reconciliation_Ordinance)
print(dakus)

#%% md
# Copy
# ------
# The assignment operation ``=`` does not create a new set.

#%%

more_dakus = {"pervaiz elahi", "altaf husain"}
dakus_backup = more_dakus
more_dakus.clear()
print(dakus_backup)

#%% md
# ``copy`` method creates a shallow copy

#%%

more_dakus = {"pervaiz elahi", "altaf husain"}
dakus_backup = more_dakus.copy()
more_dakus.clear()
print(dakus_backup)

#%%

imperialists = {"BBC", "CNN", "VOA"}

more_imperialists = imperialists.copy()

more_imperialists.add("DW")

print(imperialists)

print(more_imperialists)

#%% md
# ``difference``
# ----------------

#%%

pml_q = {"zafrullah jamali", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pml_n = {"choi Nisar" , "umar ayyub", "khawaja Asif"}
pti = {"firdows ashiq", "umar ayyub", "asad umar", "fawad hussain"}

pml_q.difference(pti)


#%%

lotas_2013 = pml_q.difference(pml_q.difference(pml_n))
print(lotas_2013)

#%% md
# We can also make use of ``-`` operator

#%%

print(pml_q - pti)

#%% md
# `difference_update`
# -----------------------
# This makes change in original set. similar to `x-y` with the exception that `x`
# is itself changed.

#%%

pml_q = {"zafrullah jamali", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pml_n = {"choi Nisar" , "umar ayyub", "khawaja Asif"}
pti = {"firdows ashiq", "umar ayyub", "asad umar", "fawad hussain"}

pml_q.difference_update(pml_n)

print(pml_q)

#%%

pml_q.difference_update(pti)

print(pml_q)

#%% md
# ``discard``
# ---------------
# removes an element from set if it is present.

#%%

pml_q = {"zafrullah jamali", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pml_q.discard("zafrullah jamali")
print(pml_q)

#%%

pml_q.discard("choi nisar")
print(pml_q)

#%% md
# `ferdows ashiq` is not present in set `musharaf` but using `discard` did not
# raise an error.

## ``remove``
# Same as `discard` with the exception that an error is raised if the object is
# not present in set.

#%%

pml_q = {"zafrullah jamali", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pml_q.remove("zafrullah jamali")
print(pml_q)

#%%

# uncomment following line
# pml_q.remove("choi nisar")  # KeyError
print(pml_q)

#%% md
# ``pop``
# --------

#%%

pml_q = {"firdows ashiq", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pml_q.pop()
print(pml_q)

#%%

pml_q.pop()
print(pml_q)

#%% md
# Running the above cell multiple times will eventually raise an error when the
# set becomes empty.

# %%
# `union`
# -------------

#%%

pml_q = {"firdows ashiq", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pml_n = {"choi Nisar" , "umar ayyub", "khawaja Asif"}

pml_q.union(pml_n)

#%%

print(pml_q | pml_n)

#%% md

## `intersection`

#%%

pml_q = {"firdows ashiq", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pti = {"firdows ashiq", "umar ayyub", "asad umar", "fawad hussain"}

pml_q.intersection(pti)

#%% md
# We can also use ``&`` operator

#%%

print(pml_q & pti)

#%% md
# The original set `pml_q` remains unchanged.

#%%

print(pml_q)

#%% md
# However, if we use `intersection_update`, the original set is changed

#%%

pml_q.intersection_update(pti)
print(pml_q)

#%% md
# If we want to find out intersection between multiple sets, we can do it as following.

#%%

pml_q = {"firdows ashiq", "fawad hussain", "pervaiz elahi", "umar ayyub"}
pti = {"firdows ashiq", "umar ayyub", "asad umar", "fawad hussain"}
pml_n = {"choi Nisar" , "umar ayyub", "khawaja Asif"}

sets = [pml_q, pml_n, pti]
set.intersection(*sets)

#%% md
# or

#%%

sets = [pml_n, pti]
pml_q.intersection(*sets)

#%% md
# So we can say that [`umar ayyub`](https://en.wikipedia.org/wiki/Omar_Ayub_Khan)
# is the most consistent lota.

# %%
# `isdisjoint`
# --------------
# returns `True` if the intersection of two sets is not empty set.

#%%

ppp = {"firdows ashiq", "fawad hussain", "Amin Faheem", "umar ayyub"}
pti = {"firdows ashiq", "umar ayyub", "asad umar", "fawad hussain"}
ji = {"liaquat baloch", "siraj ul haq", "munawar hasan"}

ppp.isdisjoint(ji)

#%%

ppp.isdisjoint(pti)

#%% md

# `issubset`
# ------------
# ``<`` is used for proper subset and ``<=`` is used for subset checking.

#%%

pml_n = {"nawaz", "shahbaz", "pervaiz elahi", "mushahid husain"}
pml_q = {"pervaiz elahi", "mushahid husain"}

pml_q.issubset(pml_n)

#%%

print(pml_q <= pml_n)

#%%

print(pml_q < pml_q)

# %% md
# ``issuperset``
# --------------
# ``>`` is used for proper superset and ``>=`` is used for superset checking.

#%%

pml_n = {"nawaz", "shahbaz", "pervaiz elahi", "mushahid husain"}
pml_q = {"pervaiz elahi", "mushahid husain"}

pml_n.issuperset(pml_q)

#%%

print(pml_n >= pml_q)

#%%

print(pml_n > pml_n)

#%% md

# Since sets are unordered, the operation ``in`` is faster when applied to
# sets as compared to lists.

#%%

print("nawaz" in pml_n)

#%%

print("nawaz" not in pml_q)
