"""
=====================
1.3 sequential data
=====================
"""

# %%
# A sequential data is the data type with one or more than one value/object in it.
#
# Four major sequential data types
#    * Strings
#    * Lists
#    * Tuple
#    * Range

# %%
# Since a sequential data type consists of more than one value, we can check the length
# of a sequential data using ``len`` function.

# %%
# Lists
# =========
# Lists are array likes, enclosed by square brackets.

# %%

a = [1, 2, 3, 4]
print(a)

# %% md
# we can verify that variable ``a`` is of `list` type

# %%

type(a)

# %% md
# But ``a`` is not just an array like in `Fortran` programming language. It is rather, much more than that.
# It is a collection of objects.

# %%

type(a[0]), type(a[1])

# %% md
# All elements in above list were of type `int` but a list can hold any kind of
# objects all in same list. The following list contains, `int`, `float`, `str`
# and a `list` type in it. Yes a list can have a list inside it as well. That
# is why it is called a **collection of objects**.

# %%

a = [1, 2.0, '3', [4, 5]]
type(a[0]), type(a[1]), type(a[2]), type(a[3])

# %% md
# as we have seen above that we can index list elements as well. However, if
# we try to access for an index in a list which is not present, it will result
# in error. For example above list contains four elements. If we try to access a[4]
# (which means element at 4th index or 5th element), it will result in error.

# %%

# uncomment following line
# a[4]  # IndexError

# %% md
# We have also seen that list is an ordered collection of objects. If we print
# list `a`, it will print its elements in same sequence as they are originally.

# %%

print(a)

# %% md
# We can change contents of lists using indexing.

# %%

a[3] = 'a new element'
print(a)

# %% md
# We can replace a sequence of elements in a list with a new sequence and the new
# sequence does not have to be of same length and type as old sequence.

# %%

print(a[0:3])

a[0:3] = [2.0, 2]
print(a)

# %% md
# So we see the size of list is changed automatically/dynamically.

# %% md
# nested lists
# --------------
# A list can contain several lists and every list in side a list further sublists
# and so on.

# %%

pakistan = [[['Nawakali', 'Alamdar Road', 'Killi Ismail', 'Kharotabad'],
             'Kallat', 'Ziarat', 'Gawadar'],
            ['Sukkur', 'Rohri', 'Hayderabad', 'Karachi'],
            ['Peshawar', 'Hangue', 'Mardan', 'Charsadda'],
            ['Lahore', ['ugoki', 'sambrial', 'pasrur', 'daska'], 'Sadiqabad', 'Multan']]

len(pakistan)

# %% md
# Finding length of `pakistan` will give length of outermost list. We can find
# out lengths of inner lists as well.

# %%

len(pakistan[0]), len(pakistan[1]), len(pakistan[2]), len(pakistan[3])

# %%

print(pakistan[0][0][0:])

# %%

print(pakistan[3][0][:])

# %%

print(pakistan[3][1][-3:])

# %%

print(pakistan[3][1][3][3:])

# %%

enigma = 'IRtu diysa rtdo oK icpolnivnegn iweanst  at ow hbiet ea  sluipbeerrmaalc!i s t'
print(enigma[::2])

# %%

print(enigma[1::2])

# %% md
# concatenation
# ---------------
# List concatenation works same as that of strings.

# %%

provinces = ['sind', 'balochistan', 'kpk', 'punjab'] + ['janubi punjab', 'kashmir', 'potohar']
print(provinces)

# %%

provinces += ['hazara', 'karachi']
print(provinces)

# %% md
# Tuples
# ==========
# In contrast to lists, tuples are immutables which means, once they are created,
# we can not change/modify their content.

# %%

a = (1, 2, 3)
type(a)

# %%
# Just like lists, the contents of tuples can also be of different types.
a = (1, 2.0, 'a', pakistan)
print(a)

# %% md
# We can not change a value in a tuple.

# %%

# uncomment following line
# a[2] = 'last'  # TypeError

# %% md
# Tuples are used to store data where we know it will not change. This also
# makes sure that we don't change the data accidentally.

# %% md
# `in`
# -------
# The `in` keyword is used to check whether an element is present in a
# sequence or not.

# %%

print("Bahawalpur" in provinces)

# %%

print("Multan" not in provinces)

# %%

print("pubjab" in provinces)

# %%

print('a' in a)

# %%

print('at' in enigma)

# %% md
# Repetition
# -----------

# %%

text = ["Gaza is an open air prison. "]
t = [text] * 3
print(t)

# %% md
# Caveat

#%%

print(t[0][0])

# %%

t[0][0] = "Yemen is an open air prison. "
print(t)

# %% md
# Indexing
# ---------

# %%

# a = ['Makran',' coastal', 'highway', 'in', 'Balochistan', 'is', 'stunning']
a = "Lasbela and Loralai!"
# a = ('Makran',' coastal', 'highway', 'in', 'Balochistan', 'is', 'stunning')

start = 2
stop = 7
print(a[start:stop])  # items start through stop-1
print(a[start:])      # items start through the rest of the array
print(a[:stop])       # items from the beginning through stop-1
print(a[:])           # every item in sequence

# %%

print(a[-1])    # last item in the sequence
print(a[-2:])   # last two items in the sequence
print(a[:-2])   # whole sequence

# %%

print(a[::-1])    # all items in the sequence, reversed
print(a[1::-1])   # the first two items, reversed
print(a[:-3:-1])  # the last two items, reversed
print(a[-3::-1])  # everything ex
