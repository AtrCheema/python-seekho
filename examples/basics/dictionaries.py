"""
=============
6. dictionary
=============
"""


# %% md
# Intro
#=======
# Dictionaries are data containers to keep the data where each data is associated with a `key`.Also known
# as associative arrays, dictionaries are data types consisting of key and value pairs.Each
# value in a dictionary is associated with a key, and every key has a value associated with it.

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

type(man)

# %% md
# Each key and value pair must be separated by comman.We can access data from a dictionary as following.

# %%

man["name"]

# %%

man["citizenship"]

#%%

# uncomment following line
# man["city"]  # KeyError

#%% md
# The dictionary ``man`` does not have a key named `city`, so does the error suggests.

#%%
# The key must be the same object as when it was defined.We can not use indexing for keys such as

#%%

# uncomment followingline
# man[0]  # KeyError

# %% md
# We can add a new key, value pair in an existing dictionary as following

# %%

man["city"] = "Baghdad"

print(man)

# %% md
# Thus we can start with an empty dictionary and populate it later on


# %%

man = {}

man

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
man["burial_place"] = "Baghdad"

print(man)

# %% md
# But we can not have a dictionary with two or more same keys.If we add a new
# key with same name, the original key, value will be replaced.

# %%

man["died"] = 1980
print(man)

# %% md
# `type` of keys and values
#==========================
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
## Makind a real practical dictionary

# %%

ur_per = {"admi": "mard", "aurat": "zan", "bacha": "tefl", "paighambar": "paighambar"}
per_ar = {"mard": "rojol", "zan": "nissa", "tefl": "tefl", "paighambar": "paighambar"}

print("The Arabic word for aurat is: " + per_ar[ur_per["aurat"]])

# %% md
## Operations on dictionaries

# `len`, `
# del ` and ` in `

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

len(man)

# %%

"died" in man

# %%

del man["died"]
"died" not in man

# %% md
# Repeating the above code will result in error.

# %%

"city" not in man

# %% md

## `pop`

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

man.pop("died")

# %%

man

# %%

# uncomment following line
# man.pop("died")  # KeyError

# %%

man.pop("died", 1980)

# %% md
# We can use this method to avoid the error of removing the key from a dictionary
# if the key is not present in dictionary.

# %%

man.pop("died", None)

# %%

man

# %% md

## `poopitem`

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

man.popitem()

# %%

man

# %%

man.popitem()

# %%

man

# %% md
## ``get``
# `get` method can also be used for accessing the values in dictionary.It returns
# `None` if the key is not present and we can set the default value for a key
# if the value is not already present.

# %%

man = {"name": "Baqir -al- Sadr",
       "born": 1935,
       "citizenship": "Iraq",
       "died": 1979}

man.get("city")

# %%

man.get("city", "Baghdad")

# %% md
# ``copy``
#==========
# Simple object assignment with ``=`` makes a shallow copy.

# %%

man1 = {"name": "Baqir -al- Sadr",
        "born": 1935,
        "citizenship": "Iraq",
        "died": 1979}

man2 = man1
man2["name"] = "Mutahri"

print(man1)

#%%

print(man2)

#%% md
# so even though we changed the ``name`` of ``man2``, but ``name`` of ``man1``
# is also changed.

#%%


man1 = {"name": "Baqir -al- Sadr",
        "born": 1935,
        "citizenship": "Iraq",
        "died": 1979}

man2 = man1.copy()

man2["name"] = "Mutahri"

#%%

print(man1)
print(man2)

#%%
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
# Same is true for `list` in the dictioanrys

# %%

books1 = {"AlSadr": ["Our Philosophy", "Our Economy"],
          "Mutahri": ["Divine Justice", "Man and Destiny"]}

books2 = books1.copy()

books2["Mutahri"][1] = "The goal of life"
print(books1)
print(books2)

#%% md
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

#%%
# if we iterate through each key, value pair of dictionay and copy
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

#%% md
# but what if dictioary inside the dictionary further contains dictionaries


men1 = {1: {"iraq": {'person1': {'name': 'sadr'}, 'person2': {'name': 'hakim'}},
            "iran": {'person1': {'name': 'mutahri'}, 'person2': {'name': 'shariati'}}}}

men2 = copy_dict(men1)

men2[1]["iraq"]['person1']['name'] = "baqir al sadr"

print(men1)
print(men2)

#%%
# although we canged ``name`` of ``person1`` in ``men2`` but it is also changed in ``men1``.

#%%
# we can acheive this by calling the parent function again every
# time the value is a dictionay i.e. calling ``copy_dict`` function inside ``copy_dict`` function.

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


# %% md
# ``update``
#==========

# %%

books = {"AlSadr": ["Our Philosophy", "Our Economy"],
         "Mutahri": ["Divine Justice", "Man and Destiny"]
         }

new_books = {"Legenhausen": ["Religious pluralism", "Hegel's ethics"]}

books.update(new_books)

print(books)

# %% md
# Merging dictionaries
#======================
# The update merges one dictionary into other. If we want to keep both dictionaries intact and create
# a new one by merging them together, we can do them as following(starting from python 3.5)

# %%

old_books = {"AlSadr": ["Our Philosophy", "Our Economy"],
             "Mutahri": ["Divine Justice", "Man and Destiny"]
             }

new_books = {"Legenhausen": ["Religious pluralism", "Hegel's ethics"]}

books = {**old_books, **new_books}

print(books)

# %%

print(old_books)

print(new_books)

# %%

books = {**old_books, "Iqbal": "reconstruction", **new_books}

print(books)

# %% md
# Double asterik ``**``, actually just unpacks the dictionary.

# %%

{'x': 1, **{'y': 2}}

# %% md
# For backup compatability, we can use the method that can run on versions before 3.5 as follows

# %%

books = old_books.copy()
books.update(new_books)
print(books)

# %% md

## Keys and Values

# %%

keys = books.keys()

print(type(keys))

#%%

print(keys)

# %%
# We can convert keys of a dictionary into ``list`` type as follows

keys = list(keys)
print(type(keys))

#%%

print(keys)

# %%
# similarly we can convert values of a dictionary into ``list`` type as follows

values = books.values()

values = list(values)
print(type(values))

#%%

print(values)

# %%

books_as_list = list(books.items())

books_as_list

# %%

print(type(books_as_list[0]))

#%%

print(books_as_list[0])

# %% md
# dictionaries from lists

# %%

captials = ["Quetta", "Karachi", "Peshawar", "Lahore"]
provinces = ["Balochistan", "Sindh", "KPK", "Punjab"]

provinces_captials_iterator = zip(provinces, captials)

provinces_captials_iterator

# %%

provinces_captials = list(provinces_captials_iterator)
print(provinces_captials)

# %%

provinces_captials_dict = dict(provinces_captials)
print(provinces_captials_dict)

# %%

dict(zip(provinces, captials))

# %%

captials = ["Quetta", "Karachi", "Peshawar", "Lahore"]
provinces = ["Balochistan", "Sindh", "KPK", "Punjab", "FATA"]

dict(zip(provinces, captials))

# %%

provinces_captials_dict = dict(
    list(zip(["Balochistan", "Sindh", "KPK", "Punjab"], ["Quetta", "Karachi", "Peshawar", "Lahore"])))

print(provinces_captials_dict)

#%% md
# We can now merge two dictionaries with another method.

# %%

old_books = {"AlSadr": ["Our Philosophy", "Our Economy"],
             "Mutahri": ["Divine Justice", "Man and Destiny"]}

new_books = {"Legenhausen": ["Religious pluralism", "Hegel's ethics"]}

books = dict(list(old_books.items()) + list(new_books.items()))
books

# %%
# if we wish to check that whether a python object is key or value, we can
# achieve this as following

from collections.abc import KeysView, ValuesView
isinstance(books.keys(), KeysView)  # -> True

#%%
# similarly for dictionary values
isinstance(books.values(), ValuesView)  # -> True

