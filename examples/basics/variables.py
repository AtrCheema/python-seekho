"""
=============
1.1 variables
=============
This lesson introduces data types and variables in python.
"""

#%%
# A variable is a way to link some data to a memory location. The memory here, does not
# mean the storage such as hard drive or USB etc rather memory such as RAM.
# The memory size which is allocated for a variable depends on the kind and
# data linked to that variable. For example, a variable consisting 10 integers will
# hold less memory as compared to a variable consisting of a million integers.
# Similary a variable holding an integer will have different amount/size of memory
# as compared to a variable holding a string say ``Ali``.
# When we define a variable in python, the python checks the type of the variable
# and allocates some memory for that variable.

#%%

a = 10

#%% md
# So what has been done above is that a variable named ``a`` is assigned a value
# of 10. Behind the scenes python created an ``object`` and and the variable
# name ``a`` is a reference for that object.

#%%

a = 20

#%% md
# When the variable ``a`` is redefined, it means the location of memory which was
# holding the value 10 before, now holds 20. This means we have changed the contents of memory.

#%%

a = a + 10
print(a)

#%% md
# What kind of object python creates, depends upond the type of data. We can check
# the type of a variable by using the command ``type(VariableName)``

#%%

print(type(a))

#%%

b = 2.0
print(type(b))

#%%

c = a + b
print(c, type(c))

#%%

d = a + a
print(d, type(d))

#%% md
# It is significant to note that the python is able to change the type of new
# variable based on the kind of value assigned to it. If a float
# value is assinged to a variable, python will change the type
# of this variable to float.
#
# Another significant thing is that, we can assign any type of data to a variable.
# For example we can assign ``int`` to variable a, later we can assign ``float``
# to variable and then we can assign a completly different type like ``string`` to a.
#
# This is a blessing (in terms of ease of use) as well as a curse (in terms of its
# slow speed) of python and for python users.

#%%

a = 'Ali'
print(type(a))

#%% md
# When we assign a value to a variable and then assign that variable to a new
# variable, then both of these variables actually refer to the same object.
# We can verify this using the function ``id(VariableName)``

#%%

a = 12
b = a
id(a), id(b)

#%%

b = 14
id(a), id(b)

#%% md
# So when we assigned a differnt data to ``b``, a new object was created and now ``b``
# refers to this new object and thus its identity changes now.
#
# Following are valid variable names

#%%

ali9 = 12
Ali9 = 14
아타르 = 2
print(아타르)

#%% md
# A variable name must not start from a number.

#%%

# uncomment following line
# 1_ali = 29

# %% md
# We can not name certain keywords as variable names. These keywords can
# be seen official python docs website [1]_

#%%
# Data Types
# -------------
# Data types signifies the type of operation that can be performed on that
# data. Python has following data types

# %% md
# Numbers
# -----------
# To represent numerical values, python has three types
#    * integer
#    * float
#    * complex

#%%

a = 1
b = 0b101   # binary with base 2
x = 0o14 # octal with base 8
y = 0xe     # hexadecimals with base 16

print(a, type(a))
print(b, type(b))
print(x, type(x))
print(y, type(y))

#%%

print(bin(5))
print(oct(12))
print(hex(14))

#%%

a = 12.5e3
print(type(a))

#%%

x = 3 +4j  # consist of real and imagenary part
print(type(x))

#%%

coke = False
water = True
print(type(coke))

#%% md
# Sequence
#---------
#
# * strings
# * lists
# * tuple

#%%

s = 'What is the first question that should come to our mind in this life?'
s2 = "Should Immanual Kannt be condemned for his racist views?"

#%%

s3 = 'Why the colonization isn\'t considered a crime?'
print(s3)

#%%

s3 = "Why the colonization isn't considered a crime?"
print(s3)

#%% md
# If we want to quote something with double strings inside a double quoted string, we can do it as following.

#%%

txt = "He said: \"It doesn't matter, if you enclose a string in single or double quotes!\""
print(txt)

#%%

txt = '''Baqir al sadr was an Iraqi scholar.
He was born in 1935 and wrote his famour book "our philosophy" just at the age of 25.
He was kiiled at the age of 45 by Sadam Husain.'''
print(txt)

#%% md
# Indexing
#------------

#%%

s = "Assalam o alaikum"
s[0]

#%%

s[7]

#%%

len(s)

#%%

s[len(s)-1], s[-1]

#%% md
# Slicing
#--------

#%%

s[-3:], s[5:8], s[8:]

#%% md
# Concatenation
#--------------


#%%

a = " Assalam" + " o" " alaikum"
a

#%% md
# Repeatition
#---------------

#%%

b = a*3
b

#%% md
# We can find the length of a sequence object in python using the functin `len`.
# Since strings are also sequences, their length/size can also be found by `len`.

#%%

len(a), len(b)

#%% md
# immutability
#----------------

#%%

# uncomment following line
# a[-1] = ". "  # TypeError

#%%

a = "Muhammad"
b = "Muhammad"
a is b

#%%

a == b

#%%

a = "Muhammad!"
b = "Muhammad!"
a is b

#%%

print(a == b)

#%%

a = "Muhammad1"
b = "Muhammad1"
a is b

#%%

a == b

#%% md
# Range
#--------
# It gives immutable sequence. We will further study its use later during in
# :ref:`sphx_glr_auto_examples_basics_for_loops.py`.

#%%

a = range(4)
print(a)

#%%

print(type(a))

#%%
#
# .. [1] `<https://docs.python.org/2.5/ref/keywords.html>`_