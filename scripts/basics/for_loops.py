"""
=================
1.10 for loops
=================

This lesson introduces ``for`` loops in python.
"""

# %%
# Just like while loops, `for` loops allow an instruction to be executed
# a certain number of times. How many times? It depends upon iterator.
# As per wikipedia 11 people have received Nishan-e-Haider [1]_
# award in Pakistan. Let's say we want to iterate over this list.

NH_receivers = ['Saif Ali Janjua', 'Muhammad Sarwar', 'Tufail Muhammad',
                'Aziz Bhatti', 'Rashid Minhas', 'Muhammad Akran',
                'Shabbir Sharif', 'Muhammad Husain Janjua', 'Muhammad Mahfuz',
                'Sher Khan', 'Lalak Jan']

for shaheed in NH_receivers:
    print(shaheed)

# %% md
# In above example, a list is acting as an iterator. In fact it can be a tuple,
# string or any other sequence. The basic syntax of for loop in python is:
#
# .. code-block:: python
#
#    for variable in sequence:
#        do something
#
# The `variable` in above syntax is assigned a new new value from `sequence` upon every iteration.

# %%

for podcast in ("Hujjat", "The east is the podcast", "Philosophise this", "Lex Friedman"):
    print("I am listening to: ", podcast)

# %%

scholars = {
    "Baqir al sadr": 1980,
    "Murtaza Mutahri": 1979,
    "Allama Iqbal": 1938,
    "Jamal ul din Afghani": 1897,
    "Ali Shariati": 1977,
    "Moh Husain Tabatabai": 1981
}

for scholar, date_of_death in scholars.items():
    print(scholar, "died in ", date_of_death)

# %% md
# `for` with else
# Just like `while` loops, the code under else gets executed if everything
# goes well within `for` loop. If let's say, we are running for loop to
# search an item in the iterator, and when we find the item, there is not
# point in continuing the `for` loop further. Hence we `break` out of for loop.
# In such a case code under `else` will not be executed.
#
# .. code-block:: python
#
#    for variable in sequence:
#        do something
#    else:
#        do at last
#

# %%

for shaheed in NH_receivers:
    if shaheed == 'Rashid Minhas':
        print("Person from air force found")
        break
else:
    print('Search completed')

# %% md

# range

# %%

range(5)

# %%

for i in range(5):
    print(i)

# %% md
# We can alo iterate over a list using range.

# %%

for i in range(5):
    print(NH_receivers[i])

# %%

for i in range(2, 5):
    print(NH_receivers[i])

# %% md
# Skipping every nth value in iterator

# %% md
# We can also include step argument in range, which decides how big the jump/step
# we want to have in our iterator.

# %%

for i in range(2, 8, 2):
    print(NH_receivers[i])

# %% md
# We can also go backwards in the iterator

# %%

for i in range(8, 2, -1):
    print(NH_receivers[i])

# %%

for i in range(8, 0, -2):
    print(NH_receivers[i])

# %% md
# accessing index
# If we want to access index itself, we can do this by using `enumerate`.

# %%

for index, item in enumerate(NH_receivers, start=0):  # default value of start is zero.
    print(item, ' is Nishan - Haider receiver number ', index)

# %% md
# which is equivalent to

# %%

index = 0
for item in NH_receivers:
    print(item, ' is Nishan - Haider receiver number ', index)
    index += 1

# %% md
# This is another way to keep track that how many times the loop has been executed.
#
# Iterating over more than one sequence

# %%

scholars = ['Baqir al sadr', 'Murtaza Mutahri', 'Allama Iqbal', 'Jamal ul din Afghani', 'Ali Shariati',
            'Moh Husain Tabatabai']
date_of_death = [1980, 1979, 1938, 1897, 1977, 1981]

for scholar, dod in zip(scholars, date_of_death):
    print(scholar, ' died in year ', dod)

# %%

date_of_birth = [1935, 1919, 1877, 1838, 1933, 1904]
for scholar, dod, dob in zip(scholars, date_of_death, date_of_birth):
    print(scholar, ' was born in ', dob, ' and died in year ', dod)

# %% md
# But what if lengths of lists are not equal.

# %%

scholars = ['Baqir al sadr', 'Murtaza Mutahri', 'Allama Iqbal', 'Jamal ul din Afghani', 'Ali Shariati',
            'Moh Husain Tabatabai']
date_of_death = [1980, 1979, 1938, 1897, 1977, 1981, 1989]

print(len(scholars), len(date_of_death))

for scholar, dod in zip(scholars, date_of_death):
    print(scholar, ' died in year ', dod)

# %% md
# Simple `zip` will iterate over the point when all lists are equal and
# ignore if any sequence is larger than the others. If we want to iterate
# until the longest sequence, we have to use `zip_longest` from `itertools`

# %%

from itertools import zip_longest

scholars = ['Baqir al sadr', 'Murtaza Mutahri', 'Allama Iqbal', 'Jamal ul din Afghani', 'Ali Shariati',
            'Moh Husain Tabatabai']
date_of_death = [1980, 1979, 1938, 1897, 1977, 1981, 1989]

for scholar, dod in zip_longest(scholars, date_of_death):
    print('name: ', scholar, ' date of death: ', dod)

# %% md
# notice the last printed line.
# accessing previous and next value
# we must start from 1 and end before last item in order to print correct values

for i in range(1, len(NH_receivers) - 1):
    print(NH_receivers[i], ' came before ', NH_receivers[i + 1], ' and after ', NH_receivers[i - 1])

# %% md
# changing loop variable inside loop
# Let's say we want to iterate over sequence from 0 to 10
# i.e `0,1,2,3,4,5,6,7,8,9` but after `5` we wan to jump to `8` and
# then carry on. It means we should change the loop variable inside
# the loop. A naive mind might thing following approach would work
# %%

for i in range(10):
    if i == 5:
        i += 3
    print(i)

# %% md
# But we had wished the output as `0,1,2,3,4,5,8,9`.
# The reasons is, for loop iterated over `0,1,2,3,4,5,6,7,8,9` and if
# we changed current value of `i`, it will not affect next value of
# `i` at next iteration. We have to use `while` loop in such a scenario.

# %%

i = 0
while i < 10:
    if i == 5:
        i += 3
    print(i)
    i += 1

# %% md
# Flattening a list of lists
#
# If we have a list of lists, and we want to flatten all the elements of that
# list into one list, we can use a nested for loop to achieve this.

# %%

prime_miniters = [['zafrullah jamali', 'chaudhry shujaat', 'shaukat aziz'],
                  ['yousuf raza gilani', 'raja pervaiz ashraf'],
                  ['nawaz sharif', 'shahid khaqan']]

print(len(prime_miniters))

all_pms = []
for era in prime_miniters:
    for pm in era:
        all_pms.append(pm)

print(all_pms)

# %%

print(len(all_pms))

# %%
# If you want to dig deep into how the ``for`` loops work in python,
# you go jump to :ref:`sphx_glr_auto_examples_oop_magical_methods.py`.

# %%
#
# .. [1] `<https://en.wikipedia.org/wiki/Nishan-e-Haider>`_
