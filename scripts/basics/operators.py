"""
================
1.2 operators
================
This lesson describes Basic operators in python.

.. important::
  This lesson is still under development.
"""

# %%
# Basic operations
# ---------------------
# ``+`` is used for addition

#########################################

a = 10 + 20
print(a)

#########################################

a += 10
print(a)

#########################################
# ``-`` is used for subtraction

#########################################

a = 20 - 10
print(a)

#########################################

a -= 5
print(a)

#########################################
# ``*`` for multiplication

#########################################

a = 2*10
print(a)


#########################################

a *= 2
print(a)

#########################################
# ``%`` modulo

# returns remainder

#########################################


print(14 % 5)

#########################################
# If one of the value is float, result will be float.

#########################################


print(17 % 5.0)

#########################################
# The sign of the result will be same as sign of divider.

#########################################

print(17 % -5.0)

#########################################
# ``/`` for division

#########################################


a = 20/6
print(a)

#########################################
# ``//`` is used for truncated division

#########################################

print(20//6)

#########################################

print(20//6.0)

#########################################
# If the answer of the truncated division is negative, the answer is rounded to
# the next smallest integer (greater negative)

#########################################

print(20//-6.0, -20//6.0)

#########################################

-20 // -6.0

#########################################
# `**`  is used for exponentiation

#########################################

2**3

#########################################
# Comparisons
# --------------------------

#########################################

print(2 == 3)

#########################################

print(2 ==2)

#########################################

2.2 == 1.1 + 1.1

#########################################
# 1.1 + 2.2 results in an approximated answer so we avoid comparing floats.

#########################################

3.3 == 1.1 + 2.2

#########################################

abs((1.1 + 2.2) - 3.3) < 1e-15

#########################################
# Check if a number lies between two numbers

#########################################

8<10<12

#########################################

capitalism = 'a system based on individualism'

capitalism != 'justice'

#########################################
# Logical operators
# --------------------------------
# ``not`` results in opposite to what comes after it.

#########################################

not True

#########################################

not False

#########################################

x = 5.2
not x <= 10

#########################################

capitalism = False
communism = False
justice = True
capitalism and communism

#########################################

capitalism or communism


#########################################

capitalism and justice

#########################################

capitalism or justice

#########################################

capitalism is not justice

#########################################
# Default values
# ------------------------

#########################################

food = 'bread'
lunch = food or 'curry'
print(lunch)

#########################################

food = None
lunch = food or 'curry'
print(lunch)

#########################################
# If the first argument before ``or`` is ``True``, the value after ``or`` is discarded.

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
# thus and answer

#########################################

print(a is b)

#########################################
# However, python already stores some commonly used smaller numbers in memory, so
# when they are created, python refers to that same memory location and does not
# really create them. Thus for smaller numbers (from -5 to 256 integers) `is` returns True.

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

feudalism is capitalism

#########################################
# Order of operations
# ------------------------------------

#########################################

20 + 4 * 10

#########################################

2 * 3 ** 4 * 5

#########################################
# Complete order of precedence of operators in python can be found from
# :ref:`here <https://docs.python.org/3/reference/expressions.html#operator-precedence>` .
