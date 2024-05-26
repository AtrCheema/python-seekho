"""
================
1.3 operators
================
This lesson describes Basic operators in python.

The traiditional mathematical operations can be performed
on python objects just by using their symbels. This means addition, subtraction,
multiplication and divitsion can be perfomred just by using ``+``, ``-``, ``*`` and
``/`` symbols/operators between two objects respectively.
"""

# %%
# Basic operations
# ---------------------
# ``+`` is used for addition

#########################################

a = 5 + 12
print(a)

#########################################
# If we want to add something to variable 'a', one way of doint it is using ``+=``.
a +=14
print(a)

#########################################
# Above we added 10 to `a` and assigned the new value again to `a`. In this way, the
# value of `a` is updated.


#########################################
# Similarly we can use ``-`` for subtracting one object from another\

a = 14 - 12
print(a)

#########################################

a -= 5
print(a)

#########################################
# ``*`` is used for for multiplication

#########################################

a = 2*12
print(a)


#########################################

a *= 2
print(a)

#########################################
# The modulo operator ``%`` returns remainder

#########################################


print(14 % 5)

#########################################
# If one of the value is float, result will be a float.

#########################################

print(17 % 5.0)

#########################################
# Above `17` was integer and `5.0` was float. Since one value was float, the result
# is also a float
#
# The sign of the result will be same as sign of divider.

#########################################

print(17 % -5.0)

#########################################
# ``/`` is used for division

#########################################


a = 20/6
print(a)

#########################################
# `//` is used for truncated division

#########################################

print(20//6)

#########################################

print(20//6.0)

#########################################
# If the answer of the truncated division is negative, the answer is rounded to
# the next smallest iteger (greater negative)

#########################################

print(20//-6.0, -20//6.0)

#########################################

print(-20 // -6.0)

# %%
# **Question**
# What is the output of the following code
#
# .. code-block:: python
#
#    print(20//-6.0, -20//6.0)

# %%
# **Question**
# What is the output of the following code
#
# .. code-block:: python
#
#    print( 20//60, 20/60)

#########################################
# ``**`` is used for exponentiation i.e. to raise one object over another.
# For example two to the power of three can be done as below

print(2**3)

# %%
# The application of basic mathematical operators is not limited to floats or integers.
# We can also apply ``+`` to strings in python

a = "Materialism leads to "
b = "injustice."
print(a + b)

# %%
# However we can not do same for ``-`` operator. This means we can
# not subtract two strings.

# %%

# uncomment following line
# a - b # -> TypeError

# %%
# But when we multiply a ``string`` by an ``integer``, the
# string is repeated.
print(a * 2)

# %%
# Above we are multiplying a string with an integer because `a` is a string and `2` is integer.
# If however, we do ``a +2``, we will again get ``TypeError``.
#
# What kind of mathematical operations can be applied on an object or between two objects,
# depends purely upon the objects. To our surprise, we can even modify the behavior of these
# mathematical operators in python. More about this will come later in
# :ref:`sphx_glr_auto_examples_oop_magical_methods.py`.

#########################################
# Comparisons
# --------------------------
# If we want to compare one object with another and tell whether both are
# equal or not, we make use of ``==`` operator.

#########################################

print(2 == 3)

#########################################
# The ``==`` operator returns either True or False depending upon the values being compared.
print(2 ==2)

#########################################

print(2.2 == 1.1 + 1.1)

#########################################
# However, we should avoid comparing floats in this way. This is because
# `computers can not represent accurate values of floats <https://stackoverflow.com/q/21895756/14411830>`_.
# 1.1 + 2.2 results in an approximated answer, so we better avoid comparing floats.

# %%
# **Question**
# Find out the type of the output returned by ``==`` operator.
# type(2==3)
#########################################

print(3.3 == 1.1 + 2.2)

#########################################

print(abs((1.1 + 2.2) - 3.3) < 1e-15)

#########################################
# ``>`` can be read as `greater than` or `smaller than`` depending upon its direction.
#
# If we want to check whether a numerical value lies between two numbers or not
# we can make use of ``<`` or ``>`` operators twice.

#########################################

print(8<10<12)

#########################################
# ``!=`` can be considered as opposite of ``==`` and can be read as `not equal to`

capitalism = 'a system based on individualism'

print(capitalism != 'justice')

#########################################
# Logical operators
# --------------------------------
# ``not`` results in opposite to what comes after it.

#########################################

print(not True)

#########################################

print(not False)

#########################################

x = 5.2
print(not x<=10)

#########################################

capitalism = False
communism = False
justice = True
print(capitalism and communism)

#########################################


print(capitalism or communism)

#########################################

print(capitalism and justice)

#########################################
# Above, since one statement on left side of ``and`` is
# False, the output is False. For ``and`` to return True, both statements/expressions
# on its right and left side, must return True. If one is True and one is False, the
# output will be False. However, for ``or``, even if one side evaluates to True, the
# output is True. This becomes clear if you understand, why the output of below
# code is True.

print(capitalism or justice)

#########################################

print(capitalism is not justice)

# %%
# **Question**
# The above code ``print(capitalism is not justice)`` printed
# True. This is because ``justice`` was True and thus ``not justice``
# becomes False. Therefore, what we are implicitly saying `False is False`, which is True.
# Now reset the values of variables `capitalism` and `justice` in such a way
# that the code ``print(capitalism is not justice)`` should return False.
# This is shown below
#
# .. code-block:: python
#
#    capitalism =
#    justice =
#    print(capitalism is not justice)  # must print False

#########################################
# Default values
# ------------------------

#########################################

food = 'bread'
lunch = food or 'curry'
print(lunch)

#########################################
# The statement on left of ``or`` was not False/None, therefore, variable `lunch`
# became `bread` .

food = None
lunch = food or 'curry'
print(lunch)

#########################################
# If the first argument before ``or`` is ``True`` or not None, the value after ``or`` is discarded.

#########################################

food = None
lunch = 'currey' or food
print(lunch)

#########################################

food = 'bread'
lunch = 'currey' or food
print(lunch)

#########################################
# Identity
# ---------------------
# ``is`` operator compares whether both variables on its right and left side refer
# to same memory location or not.

#########################################

a = 257
b = 257
print(a == b)

#########################################

id(a), id(b)

#########################################
# Because ali and hasan are stored at different location at different location,
# thus the answer is False

#########################################

print(a is b)

#########################################
# **Note**
# If the above code prints ``True``, it could be that the python
# version that you are using saves even large integers in memory.
#
# Actually, python already stores some commonly used smaller numbers in memory, so
# when they are created, python refers to that same memory location and does not
# really create them. Thus, for smaller numbers (from -5 to 256 integers) `is` returns True.

#########################################

a = 256
b = 254 + 2
print(a is b)

#########################################

print(id(a), id(b))

#########################################

feudalism = 'slavery'
capitalism = 'slavery'

print(feudalism is capitalism)

#########################################

feudalism = 'a system of slavery'
capitalism = 'a system of slavery'

print(feudalism is capitalism)

#########################################
# Order of operations
# ------------------------------------

#########################################
# The multiplication ``*`` is performed before addition ``+`` even if ``+`` appears
# before ``*``.
print(20 + 4 * 10)

#########################################
# Similarly `exponentiation` (``**``) is performed before multiplication.
print(2 * 3 ** 4 * 5)

# %%
# **Question:**
# Write the code to convert 1000 seconds into hours.

# %%
# **Question:**
# Why the output of ``2/3+4`` and ``2/(3+4)`` is different?

#########################################
# Complete order of precedence of operators in python can be found from
# :ref:`here <https://docs.python.org/3/reference/expressions.html#operator-precedence>` .
