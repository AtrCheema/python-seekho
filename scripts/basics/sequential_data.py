"""
=====================
1.2 sequential data
=====================
"""

# %%
# A sequential data is the data type with one or more than one value/object in it.
#
# There are four major built-in sequential data types in python
#    * Strings
#    * Lists
#    * Tuple
#    * Range

# %%
# Since a sequential data type consists of more than one value, we can check the length
# of a sequential data using ``len`` function.

# %%
# Strings
# =======
# In python, a string is a data type which does not have a numeric value and
# is therefore treated as a text.

s = 'Ali'
print(type(s))

# %%
# The value/data of string need not to be only English language characters. They
# can be anythin such as numbers unless they are defined as string.
s = '12'
print(type(s))

# %%
# Although, ``12`` above is a numeric value, but since is enclosed inside quotation marks
# ``''``, python considers it a string and not a number.
#
# There are four common ways to define a string in python:
#    * single quotation ``'The wretched of the earth'``
#    * double quotation ``"The wretched of the earth"``
#    * triple doubel quotations ``"""The wretched of the earth"""``
#    * triple quotation  ``'''The wretched of the earth'''``

s1 = 'Only persons really changed history those who changed men`s thinking about themselves'
s2 = "Only persons really changed history those who changed men's thinking about themselves"
s3 = """Only persons really changed history those who changed men's thinking about themselves"""
s4 = '''Only persons really changed history those who changed men's thinking about themselves'''
print(type(s1), type(s2), type(s3), type(s4))

# %%
# A string can be as long as we wish!

s = 'What is the first question that should come to our mind in this life?'
s2 = "Should Immanuel Kant be condemned for his racist views?"

print(type(s), type(s2))

# %%
s3 = 'Why the colonization isn\'t considered a crime?'
print(s3)

# %%

s3 = "Why the colonization isn't considered a crime?"
print(s3)

# %% md
# If we want to quote something with double strings inside a double quoted string,
# we can do it as following.

# %%

txt = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
print(txt)

# %%

txt = '''Baqir al sadr was an Iraqi scholar.
He was born in 1935 and wrote his famous book "our philosophy" just at the age of 25.
He was killed at the age of 45 by Saddam Husain.'''
print(txt)

# %%
# **Question:**
# Print the following sentence including the double quotations.
#
# "The one who controls his desires is a free man. Ali ibn Abi Talib"

# %% md
# Indexing
# ------------
# Indexing refers to selecting a value at a certain position from a sequential data.
# It shhould be noted that in python, the indexing starts from 0 and not from 1. This
# means, 0 refers to 1st position and 1 refers to second position. The slice operator ``[]``
# is used to index a sequential data.
# %%

s = "Assalam o alaikum"
print(s[0])

# %%
# Above we have selected the first character of the string ``s``. We can select any
# character by changing the index in the slice operator.

print(s[7])

# %%
# We can find the length of a sequence object in python using the function `len`.
# For strings, we can check the number of characters ``len``.
# The length of a string is the number of characters in it including the empty spaces if they are present.
# When we check the length of a string using ``len`` function, it returns an integer.

len(s)

# %%
# We can also select the last character of a string using negative indexing.

print(s[len(s)-1], s[-1])

# %%
# **Question:**
#
# Explain the difference between ``s[len(s)-1]`` and ``s[-1]``.
#
# Select the last character of the string ``s`` using positive indexing.

# %% md
# Slicing
# --------
# We can select a sequence of characters from a string using slice ``:`` operator.

# %%
print(s[-3:], s[5:8], s[8:])

# %%
# Above we are selecting and printing three three different slices of the string ``s``.
# In the first slice, we have selected the last three characters of the string ``s`` using negative indexing.
# In the second slice, we have selected the characters from 6th to 8th position of the string ``s`` using positive indexing.
# In the third slice, we have selected the characters from 9th position to the end of the string ``s`` using positive indexing.

# %% md
# Concatenation
# --------------
# Concatenation in strings string refers to joining two or more strings together. This can be done using
# the ``+`` operator.

# %%

a = " Assalam" + " o" " alaikum"
print(a)


# %%
# **Question:**
#
# Write a code so that following two lines become a single sentence.
# 
# "The one who controls his desires"
# 
# "is a free man"

# %% md
# Repetition
# ---------------

# %%

b = a*3
print(b)

# %%
# **Question:**
# Print the following string 10 times by making use of ``*``.
# 
# "Black skin, white masks. "

# %% md
# immutability
# ----------------

# %%

# uncomment following line
# a[-1] = ". "  # TypeError

# %%

a = "Muhammad"
b = "Muhammad"
print(a is b)

# %%
# This above line uses the ``is`` operator to check if the two variables ``a`` 
# and ``b`` refer to the same object in memory. The ``is`` operator returns 
# True if they do and False otherwise.

print(a == b)

# %%
# In the above line, we are using the ``==`` operator to check if the two variables
# ``a`` and ``b`` have the same value. The ``==`` operator returns True if they do
# and False otherwise.

a = "Muhammad!"
b = "Muhammad!"
print(a is b)

# %%

print(a == b)

# %%

a = "Muhammad1"
b = "Muhammad1"
print(a is b)

#%%

print(a == b)

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
# We can change contents of lists using indexing operator ``[]``.
# We have already seen that teh ``[]`` operator is used to create a list.
# It is also used to index a list and to change its contents.

# %%

a[3] = 'a new element'
print(a)

# %% md
# Above we have replaced the 4th element of list `a` with a new element. 
# If you have not understoop this, don't worry, more of this wil come 
# in the chapter of :ref:`sphx_glr_auto_examples_basics_lists.py`.
#
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

panjtan = (1,2,3,4,5)
type(panjtan)

# %%
# Just like lists, the contents of tuples can also be of different types.
panjtan = (1, 2, 'three', 4.0, [5])
print(panjtan)

# %% md
# We can not change a value in a tuple.

# %%

# uncomment following line
# panjtan[2] = 'Musa'  # TypeError

# %% md
# **Question:**
#
# Explain what were trying to acheive by ``panjtan[2] = 'Musa'`` and why it resulted in error.
# On the otherhand, if we do ``panjtan[2]``, why it will not result in error?

# %% md
# Tuples are used to store data where we know it will not change. This also
# makes sure that we don't change the data accidentally.

# %% md
# `in`
# =====
# The `in` is a buil-tin keyword which is used to check whether an element is present in a
# sequence or not.

# %%

print("Bahawalpur" in provinces)

# %%
# We had created a list `provinces` above. We are checking if "Bahawalpur" is 
# present in it or not in the above code.
# The output from above code will be `False` because "Bahawalpur" is not present
# in the list `provinces`. 

print("Multan" not in provinces)

# %%

print("pubjab" in provinces)

# %%
# We are checking if "pubjab" is present in the list `provinces` or not.
#
# We can also use `in` to check if a string is present in a tuple or not.
print('three' in panjtan)

# %%
# Similarly we can use `in` to check if a string is present in a string or not.
print('at' in enigma)

# %%
# **Question:**
# Consider the following python list.
#
# ``
# scoundrels = ['asim', 'kakar', 'mohsin']
# ``
#
# Write code to using `in` to check if `bajwa` is a scoundrel or not?.

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



# %% md
# Range
# ======
# It gives immutable sequence. We will further study its use later during in
# :ref:`sphx_glr_auto_examples_basics_for_loops.py`.

# %%

a = range(4)
print(a)

# %%

print(type(a))