"""
=====================
1.3 sequantial data
=====================
"""

# Sequential data types
#
# * Strings
# * Lists
# * Tuple
# * Range

#%%
## Lists

# Lists are array likes, enclosed by square brackets.

#%%

a = [1,2,3,4]
a

#%% md
# we can verify that a is a fo `list` tyep

#%%

type(a)

#%% md
# But a is not just an array like `Fortran` rather it is much more than that.
# It is a collection of objects.

#%%

type(a[0]), type(a[1])

#%% md
# All elements in above list were of type `int` but a list can hold any kind of
# objects all in same list. The following list cnotains, `int`, `float`, `str`
# and a `list` type in it. Yes a list can have a list inside it as well. That
# is why is called a **collection of objects**.

#%%

a = [1,2.0, '3', [4,5]]
type(a[0]), type(a[1]), type(a[2]), type(a[3])

#%% md
# as we have seen above that we can index list elements as well. However, if
# we try to access for an index in a list which is not present, it will result
# in error. For example above list contains 4 elements. If we try to access a[4]
# (which means element at 4rth index or 5th element), it will result in error.

#%%

# uncomment following line
# a[4]  # IndexError

#%% md
# We have also seen that list is an ordered collection of objects. If we print
# list `a`, it will print its elements in same sequence as they are originally.

#%%

a

#%% md
# Unlike strings, we can change contents of lists using indexing.

#%%

a[3] = 'a new element'
a

#%% md
# We can replace a sequence of elements in a list with a new sequence and the new
# sequence does not have to be of same length and type as old sequence.

#%%

print(a[0:3])

a[0:3] = [2.0,2]
a

#%% md
# So we see the size of list is changed automatically

#%% md
### nested lists

# A list can contain several lists and every list in side a list further sublists
# and so on.

#%%

pakistan = [[['Nawakali', 'Alamdar Road', 'Killi Ismail', 'Kharotabad'],
             'Kallat', 'Ziarat', 'Gawadar'],
            ['Sukkur', 'Rohri', 'Hayderabad', 'Karachi'],
            ['Peshawar', 'Hangue', 'Mardan', 'Charsadda'], ['Lahore', ['ugoki', 'sambrial', 'pasrur', 'daska'], 'Sadiqabad', 'Multan']]

len(pakistan)

#%% md
# Finding length of `pakistan` will give length of outmost list. We can find
# out lengths of inner lists as well.

#%%

len(pakistan[0]), len(pakistan[1]), len(pakistan[2]), len(pakistan[3])

#%%

pakistan[0][0][0:]

#%%

pakistan[3][0][:]

#%%

pakistan[3][1][-3:]

#%%

pakistan[3][1][3][3:]

#%%

enigma = 'IRtu diysa rtdo oK icpolnivnegn iweanst  at ow hbiet ea  sluipbeerrmaalc!i s t'
enigma[::2]

#%%

enigma[1::2]

#%% md

### concatenation

# List concatenation works same as thaat of strings.

#%%

provinces = ['sind', 'balochistan', 'kpk', 'punjab'] + ['janubi punjab', 'kashmir', 'potohar']
provinces

#%%

provinces += ['hazara', 'karachi']
provinces

#%% md

## Tuples

# In contrast to lists, tuples are immutables.

#%%

a = (1,2,3)
type(a)

#%%

a = (1,2.0,'a', pakistan)
a

#%% md
# We can not change a value in a tutple.

#%%

# uncomment following line
# a[2] = 'last'  # TypeError

#%% md
# Tuples are used to store data where we know it will not change. This also
# makes sure that we don't change the data accidently.

## `in`

# The `in` keyword is used to check whether an element is present in a
# sequence or not.

#%%

"Bahawalpur" in provinces

#%%

"Multan" not in provinces

#%%

"pubjab" in provinces

#%%

'a' in a

#%%

'at' in enigma

#%% md

### Repeatition

#%%

text = ["Gaza is an open air prison. "]
t = [text] * 3
t

#%% md

#### Caveat

#%%

t[0][0]

#%%

t[0][0] = "Yemen is an open air prison. "
t

#%% md

## Indexing

#%%

#a = ['Makran',' coastal', 'highway', 'in', 'Balochistan', 'is', 'stunning']
a = "Lasbela and Loralai!"
#a = ('Makran',' coastal', 'highway', 'in', 'Balochistan', 'is', 'stunning')

start = 2
stop = 7
print(a[start:stop])  # items start through stop-1
print(a[start:])      # items start through the rest of the array
print(a[:stop])       # items from the beginning through stop-1
print(a[:])           # every item in sequence

#%%

print(a[-1])    # last item in the sequence
print(a[-2:])   # last two items in the sequence
print(a[:-2])   # whole sequence

#%%

print(a[::-1])    # all items in the sequence, reversed
print(a[1::-1])   # the first two items, reversed
print(a[:-3:-1])  # the last two items, reversed
print(a[-3::-1])  # everything ex
