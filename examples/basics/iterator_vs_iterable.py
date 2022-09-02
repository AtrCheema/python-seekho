"""
=========================
16. iterator vs iterable
=========================
"""

#%% md
# An ``iterable`` is any object which can be looped over. An
# ``iterable`` can be turned into ``iterator`` after applying ``iter`` function on
# it. An ``iterator`` is an object upon which ``next`` method can be applied.
# (Note: This is not a complete definition but without OOP, I suppose this will work)

#%%

provinces = ["Sindh", "Balochistan", "Janubi Pubjab", "Hazara", "Pakhtunkhwa"]
for prov in provinces:
    print(prov)

#%%

# uncomment followig line
# next(provinces)  # -> TypeError: 'list' object is not an iterator

#%% md
# As the error explicitly states, ``provinces`` is not ``iterator``. so we can
# not apply ``next`` method on it.
#
# However, we can convert it into ``iterator`` after applying ``iter`` method on it.

#%%

prov_iterator = iter(provinces)
next(prov_iterator)

#%% md
# but what is ``next`` good for?

#%%

# uncomment following 2 lines

#for i in range(len(provinces)):
#    print(next(prov_iterator))

#%%
# we get ``StopIteration`` exception after we have iterated through all the iterms of list

#%% md
# Let's create the iterator again and run this code.

#%%

prov_iterator = iter(provinces)
for i in range(len(provinces)):
    print(next(prov_iterator))

#%% md
# Now try `next` on `prov_iterator` once again

#%%

# uncomment following line
# next(prov_iterator)

#%% md
# So we can get next item from an iterator until it has returned all items
# from the iteraable.

#%%

print(type(prov_iterator))

#%% md
# Let's create an iterator from `tuple`

#%%

provinces = ("Sindh", "Balochistan", "Janubi Pubjab", "Hazara", "Pakhtunkhwa")
prov_iterator = iter(provinces)
print(type(prov_iterator))

#%% md
# Do we need a better way to check if an object is iterator or not?

#%% md
## `isinstance`
# can also be used if some object is of a particular type or not.

#%%

isinstance(2.5, float)

#%%

isinstance(2.5, str)

#%%

from collections.abc import Iterator, Iterable
isinstance(prov_iterator, Iterable)

#%%

isinstance(prov_iterator, Iterator)

#%%

sequences = {
             list: ["Islamabad", "Tehran", "Istambul"],
             str: "Islamabad",
             tuple: ("Islamabad", "Tehran", "Istambul"),
             dict: {"Islamabad": '', "Tehran": '', "Istambul": ''},
             int: 2,
             float: 2.5
}

for _type, obj in sequences.items():
    print(isinstance(obj, _type))

#%%

for obj in sequences.values():
    print(isinstance(obj, Iterable), isinstance(obj, Iterator))

#%%

for obj in sequences.values():
    if isinstance(obj, Iterable):
        obj = iter(obj)
        print(isinstance(obj, Iterable), isinstance(obj, Iterator))
    else:
        print("{} can not be converted into iterator because it is not iterable".format(obj))

#%% md
# The key takeaways from above two cells are following:
#
# * So ``list``, ``str``, ``tuple`` and ``dict`` are iterables as such and not iterators.
# However they can be converted into ``iterators`` after applying `next` method on it.
#
# * Every ``iterator`` is also and ``iterable`` but all iterables are not iterators.
#
# * In order to be able to create ``iterator`` from an object, it must be ``iterable``
# first. Floats and integers are not iterable so can not be converted into iterators as well.
#

#%% md
# As an ``iterator`` is also ``iterable`` so it can also be used on right side of ``for`` loop.

#%%

for prov in prov_iterator:
    print(prov)

#%% md
# If you run the above cell again, it will not print anything because the iterator
# is already exhausted.
#
# Not all methods that can be applied on an ``iterable`` can also be applied on
# ``iterator``. For example the ``len`` method can not be applied on `iterator`.

#%%

# uncomment following line
# len(prov_iterator)

#%% md
# we can however find the number of items in an iterator after converting it into list

#%%

prov_iterator = iter(provinces)
len(list(prov_iterator))

#%% md
# The methods ``next`` and ``iter`` for iterator and iterable actually come from
# ``__next__`` and ``__iter__`` methods which reside inside corresponding class.
# Since OOP concepts are not discussed in this course, so these methods are also not discussed.
