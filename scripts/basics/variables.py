"""
=============
1.1 variables
=============
This lesson introduces data types and variables in python.
"""

# %%
# A variable is a way to link some data to a memory location. The memory here, does not
# mean the storage such as hard drive or USB etc. rather memory such as RAM.
# The memory size which is allocated for a variable depends on the `kind` and
# the amount of data linked to that variable. For example, a variable consisting 10 integers will
# hold less memory as compared to a variable consisting of a million integers.
# Similarly, a variable holding an integer (e.g. 92) will have different amount/size of memory
# as compared to a variable holding a string say ``Ali``.
# When we define a variable in python, the python checks the type of the variable
# and allocates some memory for that variable.

# %%

a = 12

# %% md
# So what has been done above is that a variable named ``a`` is assigned a value
# of 12. Behind the scenes python created an ``object`` and the variable
# name ``a`` is a reference for that object.

# %%

a = 14

# %% md
# When the variable ``a`` is redefined, it means the location of memory which was
# holding the value 12 before, now holds 14. This means we have changed the contents of memory.

# %%

a = a + 12
print(a)

# %% md
# The ``print`` is a (builtin) function in python which we can use to `print the value
# of a variable`. This is not always true but more about it will come in
# :ref:`sphx_glr_auto_examples_basics_print_function.py` and :ref:`sphx_glr_auto_examples_oop_magical_methods.py`.
# The kind of object python creates, depends upon the type of data. We can check
# the `type` of a variable by using the command/function ``type(VariableName)``

# %%

print(type(a))

# %%
# A ``function`` is a different creature in python. We will cover more about it later in
# :ref:`sphx_glr_auto_examples_basics_functions.py` . At this point, just keep in mind that
# when some object is a function, we can `call` it by appending paranthesis ``()`` after its name
# Above we have called the ``print`` function. Don't worry if you don't understand the meaning
# of calling a function at this point.

# %%
# The function ``type`` is **the most important function in python**. Whenver you don't know about
# some object in python, the first thing you should do is to check its ``type`` using ``type(object)``
b = 30.0
print(type(b))

# %%
# **Question**
#
# Both ``a`` and ``b`` contained the value `thirty`, then why they had different types?

# %%

c = a + b
print(c, type(c))

# %%

d = a + a
print(d, type(d))

# %% md
# It is important to note that the python is able to change the type of new
# variable based on the kind of value assigned to it. If a float
# value is assigned to a variable, python will change the type
# of this variable to float.
#
# Another significant thing is that, we can assign any type of data to a variable.
# For example, we can assign ``int`` to variable ``a``, later we can assign ``float``
# to the variable ``a`` and then we can assign a completely different type like ``string``
# to the variable  ``a``.
#
# This is a blessing (in terms of ease of use) as well as a curse (in terms of its
# slow speed) of python and for python users.

# %%

a = 'Ali'
print(type(a))

# %%
# **Question**
#
# Find out 14 different ``types`` in python. We have already seen three types above
# i.e. ``str``, ``int`` and ``float``.

# %% md
# When we assign a value to a variable and then assign that variable to a new
# variable, then both of these variables actually refer to the same object.
# We can verify this using the function ``id(VariableName)``

# %%

a = 12
b = a
id(a), id(b)

# %%
# Above we have checked the identity of both ``a`` and ``b``. The identity of an object
# in python is the memory address of that object. It means the address in memory (RAM) where that
# objected is stored/put. Since both ``a`` and ``b`` refer to the same object,
# they have the same memory address. We can also say that since both ``a`` and ``b`` have
# the same memory address, that means they are same objects.

# %%
b = 14
id(a), id(b)

# %% md
# So when we assigned a different data to ``b``, a new object was created and now ``b``
# refers to this new object and thus its identity (memory address) changes now.
#
# Just as there are conventions for naming people in a society, there is convention
# and rules for naming variables in python. The name of a variable can be any alpha-numeric
# combination with some exceptions. Following are valid variable names

# %%

ali9 = 12
Ali9 = 14
아타르 = 2
print(아타르)

# %% md
# A variable name must not start from a number.

# %%

# uncomment following line
# 1_ali = 29

# %%
# **Question:**
# Explain the error which will result from the above code.

# %% md
# We can not name certain keywords as variable names. These keywords can
# be seen official python docs website [1]_

# %%
# Data Types
# ==========
# Data type signifies the type of operation that can be performed on that
# data. The three common data types in python are as follows
#    * numeric
#    * sequence
#    * boolean

# %% md
# Numbers
# -----------
# To represent numerical values, python has three types
#    * integer
#    * float
#    * complex

# %%

a = 1
b = 0b101   # binary with base 2
x = 0o14  # octal with base 8
y = 0xe     # hexadecimals with base 16

print(a, type(a))
print(b, type(b))
print(x, type(x))
print(y, type(y))

# %%
# `0b101`, `0o14` and `0xe` are examples of integers represented in binary, octal and hexadecimal
# bases respectively. We can convert a number to binary, octal and hexadecimal using
# the functions ``bin``, ``oct`` and ``hex`` respectively as follows

print(bin(5))
print(oct(12))
print(hex(14))

# %%
# However, if you don't understand the meaning of binary, octal and hexadecimal bases, don't worry.
# This is not important at this point. Just keep in mind that we can represent numbers in different
# bases in python.

a = 12.5e3
print(type(a))

# %%
# Since the value of ``a`` is a float, the type of ``a`` is float. The value of ``a`` is
# 12.5 times 10 raised to the power 3. This is called scientific notation. We can also
# represent a number in scientific notation as follows

a = 12.5e-3

# %%
# **Question**
# What is the value of ``a`` in the above code?

# %%
# **Question:**
#
# Define variables to store the information on your ID card and print each of them.
# The variables should not be of same type.

# %%

x = 3 + 4j  # consist of real and imaginary part
print(type(x))

# %%

coke = False
water = True
print(type(coke))

# %%
# **Question**
# What will the suitable data type to store currency values? Explain your reasoning.

# %%
# Sequence
# ---------

# %%
# boolean
# --------

# %%
#
# .. [1] `<https://docs.python.org/2.5/ref/keywords.html>`_
