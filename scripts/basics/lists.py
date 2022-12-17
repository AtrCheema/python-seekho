"""
===========
1.4 lists
===========
This lesson describes `lists` in python.

.. important::
  This lesson is still under development.
"""

# %%
# A list can be defined as a collection of objects or a container in which we
# hold different objects.

mylist = []

# %%
# Above we an empty list. How do we know that it is list? We can always check
# the type of an object in python as below.

print(type(mylist))

# %%
# We can also make a list which is not empty as below

imperialists = ['Bush', 'Obama', 'Trump', 'Zuckerberg', 'Bezos', 'coca cola']
print(type(imperialists))

# %%
# In above mentioned list, all of its (6) elements are strings. However, the elements/members
# a list need not to be of same type.

# %%
imperialists = ["Bush", {"years": 8}, 2000, (2000, 2008)]
print(type(imperialists))

# %%
# In abvoe list, the first member is ``string``, the second member is ``dictionary``,
# the third member is ``integer`` and the fourth member is a ``tuple``. We will
# study about string, dictionary, integer and tuple in upcoming lessons.

# Once we have a list, we can perform different operations on it. Some of them
# are given below.

##############################################
# append
# --------------------------------------------


imperialists = ['Bush', 'Obama', 'Trump', 'Zuckerberg', 'Bezos', 'coca cola']
print(imperialists)

##############################################

imperialists.append('clinton')
print(imperialists)


##############################################
# `append` changes the original list and it itself returns `None`.

##############################################

new_imperialists = imperialists.append('netanyahu')
print(new_imperialists)

##############################################

print(imperialists)


##############################################
# If we add a similar but new element in list, then the list will have 2 such
# elements as its member.


##############################################

imperialists.append('netanyahu')
print(imperialists)


##############################################
# pop
# --------------------------------------------

##############################################

last_element = imperialists.pop(-1)
print(imperialists)

##############################################

print(last_element)

##############################################

# uncomment following 1 line
# imperialists.pop(8)

##############################################

imperialists.pop()

##############################################

print(imperialists)

##############################################

# uncomment following 1 line
# imperialists.pop('Bush')

##############################################
# extend
# ---------------------------------------------
# If we want to add multiple elements to a list, using `append` will put a new
# list in the previous list

##############################################

imperialists = ['Bush', 'Obama', 'Trump', 'Zuckerberg', 'Bezos', 'coca cola', 'clinton']
uk_imperialists = ['churchil', 'Tony Blair', 'BBC']
imperialists.append(uk_imperialists)
print(imperialists)

##############################################

imperialists = ['Bush', 'Obama', 'Trump', 'Zuckerberg', 'Bezos', 'coca cola', 'clinton']
imperialists.extend(uk_imperialists)
print(imperialists)

##############################################
# ``extend`` actually takes any sequence as input. It must not be a list. It can
# be a string or tuple.

##############################################

new_one = "Murdoch"
imperialists.extend(new_one)
print(imperialists)

##############################################

imperialists = ['Bush', 'Obama', 'Trump', 'clinton']
capitalists = ('Zuckerberg', 'Bezos', 'coca cola')
imperialists.extend(capitalists)
print(imperialists)

##############################################
# using ``+`` operator
# ---------------------------------------------
# We can also append lists using the `+` operator.

##############################################

media_houses = ['bbc', 'cnn', 'reuters', 'springer']
print(imperialists + media_houses)

##############################################

print(imperialists)

##############################################

imperialists = imperialists + media_houses
print(imperialists)

##############################################

morons = ['sam haris', 'richard dawkins', 'baghdadi', 'bin ladan']
imperialists += morons
print(imperialists)

##############################################
# remove
# ---------------------------------------------

##############################################

imperialists.remove('springer')
print(imperialists)

##############################################
# If we repeat the above operation, it will result in error because
# `springer` has already been removed from the list `imperialists`.

##############################################

# uncomment following 2 line
# imperialists.remove('springer')
# print(imperialists)

##############################################
# insert
# --------------------------------------------
# puts an the value before the index

##############################################

imperialists.insert(-1, 'DW')
print(imperialists)

###############################################
# Finding position/index of a member of a list
# -----------------------------------------------

##############################################

imperialists.index('bbc')

##############################################

# uncomment following 1 line
# imperialists.index('bbc', 8)

##############################################

# uncomment following 1 line
# imperialists.index('bbc', 3, 6)

##############################################
# if an element is present in a list twice, index of its first position is returned.

##############################################

last_value = imperialists[-1]
imperialists.insert(2, last_value)
print(imperialists)

##############################################

imperialists.index(last_value)

##############################################
# reverse
# --------------------------------------------

##############################################

imperialists = ['bbc', 'cnn', 'reuters', 'springer', 'voa']
imperialists.reverse()

##############################################
# The function does not return anything itself but the original list is reversed.

##############################################

print(imperialists)

##############################################
# sort
# ----------------------------

##############################################

print(imperialists)

##############################################

imperialists.sort()

##############################################

print(imperialists)

##############################################

imperialists.sort(reverse=True)
print(imperialists)

##############################################

numbers = [4,3,6,2]
numbers.sort()
print(numbers)

##############################################

# uncomment following 2 line
# imperialists = ['bbc', 1, 'cnn', 3, 'voa', 2]
# imperialists.sort()

##############################################
# Notes
# --------------------------------------------
# I have been using the word function for ``append``, ``sort`` etc, however in Object
# Oriented Programming, it can be seen that they are actually called `methods`.
#
# There are a lot more powerful list manipulations which can be done by combining
# conditional and looping statements. We will come back to them once looping and
# conditioning statements are covered.
