"""
================
1.6 dictionary
================
This lesson describes a special data structure of python called ``dictionary``.
"""


# %% md
# Intro
# ========
# Dictionaries are data containers that store the data as key, value pairs.
# Each value in a dictionary is associated with a key, and threfore every key must have
# a value associated with it. Therefore, dictionaries are also sometimes known
# as associative arrays.

# %%
# We can define a dictionary using curly brackets "{}". Each key and value pair must
# be separated by a comma "," while a colon ":" is used to separate a key from its vlaue.

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979,
       "0": 0
       }

# %%
# We can verify that whether a python object is dictionary or not by checking its ``type``.
# A variable which is a dictionary has a ``dict`` type.

print(type(man))

# %% md
# We can access data from a dictionary by making
# use of slice operator ``[]``.

# %%

print(man["name"])

# %%
# Inside the square bracket, we can write any ``key`` which is present
# in the dicionary and we will get the value associated with it.
print(man["citizenship"])

#%%
# If we try to a access value whose corresponding key does not exist in the dictionary,
# we will get ``KeyError``.

# uncomment following line
# man["city"]  # -> KeyError

#%% md
# The error suggests that the dictionary ``man`` does not have a key named `city`.
#
# The key must be the same object as when it was defined. We can not use indexing for keys such as

# uncomment following line
# man[0]  # KeyError

# %%
# The ``man`` key does have a key with the name '0' but this is string type
# and we provide 0 as integer and threfore we got KeyError.

# %% md
# We can add a new key, value pair in an existing dictionary as following

# %%

man["city"] = "Baghdad"

print(man)

# %% md
# Thus we can start with an empty dictionary and populate it later on


# %%

man = {}

print(man)

# %%

man["city"] = "Baghdad"
man["name"] = "Baqir -al- Sadr"
man["born"] = 1935
man["citizenship"] = "Iraq"
man["died"] = 1979

print(man)

# %% md
# The values to different keys in a dictionary can be same.

# %%

man["birth_place"] = "Baghdad"
man["death_place"] = "Baghdad"

print(man)

# %% md
# But we can not have a dictionary with two or more same keys. If we add a new
# key with same name, the previous key, value will be replaced.

# %%

man["died"] = 1980
print(man)

# %% md
# `type` of keys and values
# ==========================
# The values in a dictionary can be of any type.

# %%

colonies = {"british": ["India", "Australia"],
            "french": "Libya",
            "polish": 0,
            "german": 3.5,  # most of their colonies are split and joined into new countires.
            "cuba": None}

print(colonies)

# %% md
# But the keys of a dictionary must be immutable.

# %%

persons = {1: "Adam",
           "Two": "Eva"}

print(persons)

# %%

# uncomment following line
# persons[[0, 1]] = ["Adam", "Eva"]  # TypeError

# %% md
# Making a real practical dictionary

# %%

ur_per = {"admi": "mard", "aurat": "zan", "bacha": "tefl", "paighambar": "paighambar"}
per_ar = {"mard": "rojol", "zan": "nissa", "tefl": "tefl", "paighambar": "paighambar"}

print("The Arabic word for aurat is: " + per_ar[ur_per["aurat"]])

# %% md
# ``keys`` and ``values`` methods
# ==================================
# We can get all the keys of a dictionary using ``.keys()`` method on dictionary.
# The dot "." here signifies that the ``keys()`` function comes from dictionary.
# This means any variable which is a dictionary, will have .keys() function in it.

# %%
books = {"AlSadr": ["Our Philosophy", "Our Economy"],
         "Mutahri": ["Divine Justice", "Man and Destiny"]
         }
keys = books.keys()

print(keys)

#%%
# Algthouh the printing keys look like ``list`` but in reality their time is not ``list``.
print(type(keys))

# %%
# We can convert keys of a dictionary into ``list`` type as follows

keys_as_list = list(keys)
print(type(keys_as_list))

#%%

print(keys_as_list)

# %%
# Similarly we can convert values of a dictionary into ``list`` type as follows

values = books.values()

values = list(values)

print(values)

print(type(values))

# %% md
# **Question:**
# Consider the following two dictionries:
#
# .. code-block:: python
#
#    a = {"Ali": 661, "Hassan": 670, "Hussain": 680, "Abid": 712, "Baqir": 733, "Jafar": 765}
#
#    b = {"Musa": 799, "Raza": 818, "Taqi": 835, "Naqi": 868, "Hassan": 874, "Hussain": None}
#
# Write the code which will return a single list of values from both dictionaries.

# %%
# The function ``items()`` when applied on a dictionay, returns both keys and values.

items = books.items()
print(items)

#%%
print(type(items))

#%%

books_as_list = list(books.items())

print(books_as_list)

# %%

print(type(books_as_list[0]))

#%%

print(books_as_list[0])

# %% md
# dictionaries from lists
# =======================
# We can convert a list into dictionary if each member in the list is a tuple.

# %%

capitals = ["Quetta", "Karachi", "Peshawar", "Lahore"]
provinces = ["Balochistan", "Sindh", "KPK", "Punjab"]

# %%
# We can make use of ``zip`` function to convert these two lists into
# a generator. More about generators and zip will come later.

provinces_capitals_iterator = zip(provinces, capitals)

print(provinces_capitals_iterator)

# %%

provinces_capitals = list(provinces_capitals_iterator)
print(provinces_capitals)

# %%
# Now we can convert `provinces_capitals` into dictionary by making use of ``dict`` function.

provinces_capitals_dict = dict(provinces_capitals)
print(provinces_capitals_dict)

# %%
# We can do all this in one step as follows

capitals = ["Quetta", "Karachi", "Peshawar", "Lahore"]
provinces = ["Balochistan", "Sindh", "KPK", "Punjab", "FATA"]

dict(zip(provinces, capitals))

# %%

provinces_capitals_dict = dict(
    list(zip(["Balochistan", "Sindh", "KPK", "Punjab"], ["Quetta", "Karachi", "Peshawar", "Lahore"])))

print(provinces_capitals_dict)

# %% md
# Operations on dictionaries
# ==========================
# Following examples show, how to apply different operations with
# dictionaries.

# %%
# ``len``
# -------
man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

len(man)

# %%

# %%
# ``in``
# -------
print("died" in man)

# %%

del man["died"]
print("died" not in man)

# %% md
# Repeating the above code will result in error.

# %%
# We can also combine ``in`` with ``not``
print("city" not in man)

# %% md
# ``pop``
# ---------

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

man.pop("died")

# %%

print(man)

# %%
# If we try to remove a non-existing key using ``pop``, it will throw KeyError.

# uncomment following line
# man.pop("died")  # KeyError

# %%
# However, we can avoid this error by supplying the default value that needs to
# be returned.
man.pop("dob", 19350101)

# %% md
# Therefore, we can use this method to avoid the error of removing the key from a dictionary
# if the key is not present in dictionary.

# %%

man.pop("died", None)

# %%

print(man)

# %% md
# ``poopitem``
# -------------

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

man.popitem()

# %%

print(man)

# %%

man.popitem()

# %%

print(man)

# %% md
# ``get``
# --------
# This method can also be used for accessing the values in dictionary. It returns
# `None` if the key is not present and we can set the default value for a key
# if the value is not already present.

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

print(man.get("city"))

# %%

man.get("city", "Baghdad")

# %%
# If a key is not present in a dictionary, and we try to access
# its value, we can avoid the KeyError by setting the default value
# of that key
print(man.get('age', 44))

# %% md
# ``copy``
# ---------
# Simple object assignment with ``=`` makes a shallow copy.

# %%

man1 = {"name": "Baqir -al- Sadr",
        "born": 1935,
        "citizenship": "Iraq",
        "died": 1979}

man2 = man1
man2["name"] = "Mutahri"

print(man1)

# %%

print(man2)

# %% md
# so even though we changed the ``name`` of ``man2``, but ``name`` of ``man1``
# is also changed.

# %%

man1 = {"name": "Baqir -al- Sadr",
        "born": 1935,
        "citizenship": "Iraq",
        "died": 1979}

man2 = man1.copy()

man2["name"] = "Mutahri"

# %%

print(man1)
print(man2)

# %%
# Now we don't see ``name`` of ``man1`` dictionary from getting changed.
# This is because we made a copy of ``man1`` and set this copy to ``man2``.
# After that we changed ``man2`` key.

# %%

men1 = {1: {"name": "Baqir -al- Sadr", "born": 1935, "citizenship": "Iraq", "died": 1980},
        2: {"name": "Mutahri", "born": 1919, "citizenship": "Iran", "died": 1979}}

men2 = men1.copy()

men2[2]["name"] = "Murtaza Mutahri"

print(men1)
print(men2)

# %% md
# Even though we made a copy of ``men1`` dictionary using ``copy`` method
# but its contents are still changed when we change ``men2``.
#
# This is because ``copy``  method still makes a shallow copy for dictionary
# inside the dictionary.
#
# Same is true for `list` in the dictionaries.

# %%

books1 = {"AlSadr": ["Our Philosophy", "Our Economy"],
          "Mutahri": ["Divine Justice", "Man and Destiny"]}

books2 = books1.copy()

books2["Mutahri"][1] = "The goal of life"
print(books1)
print(books2)

# %% md
# How to copy a dictionary which may contain several dictionaries?
#
# we can make use of ``copy`` by iterating over dictionary

import copy

men1 = {1: {"name": "Baqir -al- Sadr", "born": 1935, "citizenship": "Iraq", "died": 1980},
        2: {"name": "Mutahri", "born": 1919, "citizenship": "Iran", "died": 1979}}

men2 = copy.copy(men1)

men2[2]["name"] = "Murtaza Mutahri"

print(men1)
print(men2)

# %%
# if we iterate through each key, value pair of dictionary and copy
# it individually, we can avoid this shallow copying


def copy_dict(d: dict) -> dict:
    """makes deepcopy of a dictionary without cloning it"""
    assert isinstance(d, dict)

    new_dict = {}
    for k, v in d.items():
        new_dict[k] = copy.copy(v)
    return new_dict


men1 = {1: {"name": "Baqir -al- Sadr", "born": 1935, "citizenship": "Iraq", "died": 1980},
        2: {"name": "Mutahri", "born": 1919, "citizenship": "Iran", "died": 1979}}

men2 = copy_dict(men1)


men2[2]["name"] = "Murtaza Mutahri"

print(men1)
print(men2)

# %% md
# but what if dictionary inside the dictionary further contains dictionaries


men1 = {1: {"iraq": {'person1': {'name': 'sadr'}, 'person2': {'name': 'hakim'}},
            "iran": {'person1': {'name': 'mutahri'}, 'person2': {'name': 'shariati'}}}}

men2 = copy_dict(men1)

men2[1]["iraq"]['person1']['name'] = "baqir al sadr"

print(men1)
print(men2)

# %%
# although we changed ``name`` of ``person1`` in ``men2`` but it is also changed in ``men1``.

# %%
# we can achieve this by calling the parent function again every
# time the value is a dictionary i.e. calling ``copy_dict`` function inside ``copy_dict`` function.


def copy_dict(d: dict) -> dict:
    """makes deepcopy of a dictionary without cloning it"""
    assert isinstance(d, dict)

    new_dict = {}
    for k, v in d.items():
        if isinstance(v, dict):
            new_dict[k] = copy_dict(v)
        else:
            new_dict[k] = copy.copy(v)
    return new_dict


men1 = {1: {"iraq": {'person1': {'name': 'sadr'}, 'person2': {'name': 'hakim'}},
            "iran": {'person1': {'name': 'mutahri'}, 'person2': {'name': 'shariati'}}}}

men2 = copy_dict(men1)

men2[1]["iraq"]['person1']['name'] = "baqir al sadr"

print(men1)
print(men2)

# %%
# However, there is simpler solution to this problem. Instead of writting a function
# like `copy_dict`, which copies each object from dictionary one by one, we can simply
# use ``deepcopy`` function from ``copy`` module.
from copy import deepcopy

men1 = {1: {"iraq": {'person1': {'name': 'sadr'}, 'person2': {'name': 'hakim'}},
            "iran": {'person1': {'name': 'mutahri'}, 'person2': {'name': 'shariati'}}}}

men2 = deepcopy(men1)

men2[1]["iraq"]['person1']['name'] = "baqir al sadr"

print(men1)
print(men2)

# %% md
# ``update``
# ----------
# This method updates an existing dictionary.
# %%

books = {"AlSadr": ["Our Philosophy", "Our Economy"],
         "Mutahri": ["Divine Justice", "Man and Destiny"]
         }

new_books = {"Legenhausen": ["Religious pluralism", "Hegel's ethics"]}

# %%
# The method does not return anything. Only the original dictionary is changed.

books.update(new_books)

print(books)

# %% md
# Merging dictionaries
# ==========================
# The update merges one dictionary into other. If we want to keep both dictionaries intact and create
# a new one by merging them together, we can do this as following (starting from python 3.5)

# %%

old_books = {"AlSadr": ["Our Philosophy", "Our Economy"],
             "Mutahri": ["Divine Justice", "Man and Destiny"]
             }

new_books = {"Legenhausen": ["Religious pluralism", "Hegel's ethics"]}

books = {**old_books, **new_books}

print(books)

# %%
# We can verify that `old_books` and `new_books` dictionaries are intact.

print(old_books)

print(new_books)

# %%
# We can even provide a new key value pair.

books = {**old_books, "Iqbal": "reconstruction", **new_books}

print(books)

# %% md
# The double asterisk ``**``, in fact, just unpacks the dictionary into key value
# pairs and then we construct a new dictionary by putting the unpacked key value
# pairs inside curly brackets "{}".

# %%

print({'x': 1, **{'y': 2}})

# %% md
# For backup compatability, we better use the ``update`` method that can run on versions
# before 3.5 as follows

# %%

books = old_books.copy()
books.update(new_books)
print(books)

# %% md
# We can also merge two dictionaries with another method.

# %%

old_books = {"AlSadr": ["Our Philosophy", "Our Economy"],
             "Mutahri": ["Divine Justice", "Man and Destiny"]}

new_books = {"Legenhausen": ["Religious pluralism", "Hegel's ethics"]}

books = dict(list(old_books.items()) + list(new_books.items()))
print(books)

# %%
# **Question**
# Write the code to print the value of second key of the following dictionary i.e. "Hassan".
#
# .. code-block:: python
#
#    x = {1: "ali", 2: "hassan", 3: "hussain"}

# %%
# **Question**
# Write code to tell the date of bir and death of the 'Ali' from the following dictionary.
#
# .. code-block:: python
#
#    x = {"Ali": {"born": 600, "died": 661}, "Hassan": {"born": 625, "died": 670}, "Hussain": {"born": 626, "died": 680}}


# %%
# **Question**
# What will be output of following code?
#
# .. code-block:: python
#
#    x = {1: "ali", 2: "hassan", 3: "hussain"}
#    y = {1: "ali", 2: "hassan", 3: "hussain", 4: "Ali"}
#    print(x.get(4, y.get(4))

# %%
# **Question**
# Change the contents of dictionary `y` in such a way the following
# code throws ``KeyError``
#
# .. code-block:: python
#
#    x = {1: "ali", 2: "hassan", 3: "hussain"}
#    y = ??
#    print(x.get(4, y.get(4))  # should throw KeyError