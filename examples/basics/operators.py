"""
================
1.2 operators
================
This notebook describes Basic operators in python
"""

#%%
# ``+`` for addition

#########################################

a = 10 + 20
print(a)

#########################################

a +=10
print(a)

#########################################
# ``-`` for subtraction

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


14 % 5

#########################################
# If one of the value is float, result will be float.

#########################################


17 % 5.0

#########################################
# The sign of the result will be same as sign of divider.

#########################################


17 % -5.0

#########################################
# ``/`` for division

#########################################


a = 20/6
print(a)

#########################################
# `//` for truncated division

#########################################

20//6

#########################################
20//6.0

#########################################
# If the answer of the truncated division is negative, the answer is rounded to
# the next smallest integer (greater negative)

#########################################

20//-6.0, -20//6.0

#########################################

-20 // -6.0

#########################################
# `**` for exponentiation
#------------------------------

#########################################

2**3

#########################################
# Comparisons
#--------------------------


#########################################

2 == 3


#########################################

2 ==2

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
#---------------------------------
# `not` results in opposite to what comes after it.

#########################################

not True

#########################################

not False

#########################################

x = 5.2
not x<=10

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
#------------------------

#########################################

food = 'bread'
lunch = food or 'curry'
lunch

#########################################

food = None
lunch = food or 'curry'
lunch

#########################################
# If the first argument before ``or`` is ``True``, the value after ``or`` is discarded.

#########################################

food = None
lunch = 'currey' or food
lunch

#########################################

food = 'bread'
lunch = 'currey' or food
lunch

#########################################
# Identity
#---------------------

# ``is`` operator compares whether both variables on its right and left side refer
# to same memory location or not.

#########################################

a = 257
b = 257
a == b

#########################################

id(a), id(b)

#########################################
# Because ali and hasan are stored at different location at different location,
# thus and answer

#########################################

a is b

#########################################
# However, python already stores some commonly used samaller numbers in memory, so
# when they are created, python refers to that same memory location and does not
# really create them. Thus for smaller numbers (from -5 to 256 integers) `is` returs True.

#########################################

a = 256
b = 254 + 2
a is b

#########################################

id(a), id(b)

#########################################

feudalism = 'slavery'
capitalism = 'slavery'

feudalism is capitalism

#########################################

feudalism = 'a system of slavery'
capitalism = 'a system of slavery'

feudalism is capitalism

#########################################
# Order of operations
#------------------------------------

#########################################

20 + 4 * 10


#########################################

2 * 3 ** 4 * 5


#########################################
# Complete order of precedence of operators in python can be found from
# :ref:`here <https://docs.python.org/3/reference/expressions.html#operator-precedence>` .
