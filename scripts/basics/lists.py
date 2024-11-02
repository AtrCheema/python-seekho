"""
===========
1.4 lists
===========
This lesson describes the concept of `list` in python.

"""

# %%
# A list can be defined as a collection of objects or a container in which we
# hold different objects.

mylist = []

# %%
# Above we defined an empty list. How do we know that it is list? We can always check
# the type of object in python as below.

print(type(mylist))

# %%
# We can also make a list which is not empty as below

imperialists = ['Bush', 'Obama', 'Trump', 'Zuckerberg', 'Bezos', 'coca cola']
print(type(imperialists))

# %%
# In above-mentioned list, all of its (6) elements are strings. However, the elements/members
# a list are not required to be of same `type`.

# %%
imperialists = ["Bush", {"years": 8}, 2000, (2000, 2008)]
print(type(imperialists))

# %%
# In above list, the first member is ``string``, the second member is ``dictionary``,
# the third member is ``integer`` and the fourth member is a ``tuple``. We will
# study about string, dictionary, integer and tuple in upcoming lessons.
#
# There are two ways to convert a python object into list
#    * using ``[]``
#    * usnig ``list`` function

# %%
a = 1,2
print(type(a))
a_as_list_using_slice_op = [a]
print(type(a_as_list_using_slice_op))

# %%
a_as_list_using_list_fn = list(a)
print(type(a_as_list_using_list_fn))

# %%
# However there is a major difference in these two. ``[]`` converts the whole object *as it is*
# into a list. On the other hand, ``list`` function is more like `element wise` operator.
# This can be verified by printing the converted lists created above.

print(a_as_list_using_slice_op)
print(a_as_list_using_list_fn)

# %%
# `a_as_list_using_list_fn` is a list with two members while `a_as_list_using_slice_op` is a list
# with only one member. This can be verified by checking the length of both lists.

print(len(a_as_list_using_slice_op))
print(len(a_as_list_using_list_fn))

# %%
# Then length of list which is created using slice operator ``[]`` is always 1, while
# the length of list created using ``list`` function depends upon the number of values
# in the object. The slice operator is creating a list with one member and that one member
# is a tuple in this case.
# 
# Spend some minutes on understanding the difference between these two ways of creating a list.
# Try with different objects and see the difference.

# %%
# **Question**
# Write code to prove the above statement.

# %%
# slicing a list
# ===============
# Since the list is a sequence, we can slice it as well. The slicing of a list
# can be done using the slice operator ``[]``.
# Consider the following list

imperialists = ['Bush', 'Obama', 'Trump', 'Zuckerberg', 'Bezos', 'coca cola']
print(imperialists[0])

# %%
print(imperialists[2])

# %%
print(imperialists[-1])

# %%
# The ``:`` operator/symbol is used to slice a list. The syntax is as follows
# ``list[start:stop:step]``. The default value of ``start`` is 0, of ``stop`` is
# length of list and of ``step`` is 1.

print(imperialists[2:4])

# %%
# **Question:**
# What will be the output of the following code
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    a[2] = 12
#    print(a)


# %%
# Operations on a list
# =====================
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

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    a.append(12)
#    print(a[-1])

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

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    a.pop(2)
#    print(len(a))  # ??
#    a.pop(2)   # ??

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

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    b = [2, 3]
#    print(len(a.extend(b)))  # ?

##############################################
# using ``+`` operator
# ---------------------------------------------
# We can also append lists using the `+` operator.

##############################################

media_houses = ['bbc', 'cnn', 'reuters', 'springer']
print(imperialists + media_houses)

##############################################
# So when we use `+` operator between two lists, a new list is created which
# contains all the members of both lists. The original lists remain unchanged.

print(imperialists)

##############################################

imperialists = imperialists + media_houses
print(imperialists)

##############################################
# Above we are recreating the list `imperialists` by adding `media_houses` to it.

morons = ['sam haris', 'richard dawkins', 'baghdadi', 'bin ladan']
imperialists += morons
print(imperialists)

# %%
# `+=` operator means that the list on the left side of `+=` operator is updated
# by adding the list on the right side of `+=` operator.

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    b = [2, 3]
#    print(len(a + b))  # ?


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

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    a.insert(2, 12)
#    print(a)  # ?

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

# %%
# **Question:**
# What will be the output of the following code?
#
# .. code-block:: python
#
#    a = [1,5, 7,14]
#    a.reverse()
#    print(a)  # ?

##############################################
# sort
# ----------------------------
# We can sort the list using the `sort` function. 
# If the contents of the list strings, then the list will be sorted in
# lexicographical order. If the contents are numbers, then the list will be
# sorted in ascending order.
##############################################

print(imperialists)

##############################################
# The function does not return anything itself but the original list is sorted.

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

# %%
# **Question**
# What will be the output of the following code
#
# .. code-block:: python
#
#    x = [1,2]
#    y = [3,4, 5]
#    print(len(x + y))

# %%
# ``*``
# ---------
a = ['Najaf']
print(a * 3)

# %%

a = ['Najaf', '->', 'Karbala']
print(a * 3)

##############################################
# Notes
# ============================================
# I have been using the word function for ``append``, ``sort`` etc. However, in
# Object-Oriented Programming, it can be seen that they are actually called `methods`.
#
# There are a lot more powerful list manipulations which can be done by combining
# conditional and looping statements. We will come back to them once looping and
# conditioning statements are covered.
