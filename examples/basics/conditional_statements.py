"""
=========================
8. conditional statements
=========================
"""

#%%
# The basic syntax of if statement in python is:
#
# .. code-block:: python
#
#    if (condition):
#        do something
#
#

###################################

name = "zardari"

if name == 'zardari':
    print('chor')

###################################

name = 'Zardari'
if name == 'zardari' or name == 'Zardari':
    print('chor')

###################################

name = 'nawaz'
if name == 'zardari' or name == 'Zardari':
    print('chor')
if name == 'nawaz' or name == 'Nawaz':
    print('chor')


#%%
# Similarly the syntax for `if` and `elif` statement is
#
# .. code-block:: python
#
#  if (cnodition):
#    do something
#  elif (condition):
#    do something
#  else:
#    do something
#

###################################

name = 'edhi'
if name == 'zardari' or name == 'Zardari':
    print(name, ' is chor')
elif name == 'nawaz' or name == 'Nawaz':
    print(name, ' is chor')
else:
    print(name, ' is not chor')

###################################
# ``elif`` vs multiple ``if``
#-------------------------------
#
# Mutiple ifs means, the all the ifs will be checked, while with elif, the code will stop if one of the if is True.

###################################

age = 14

if age < 16:
    print("You are a child")
if age >= 16: #Greater than or equal to
    print("You are an adult")
else:   #Handle all cases where 'age' is negative
    print("The age must be a positive integer!")

###################################

age = 14

if age < 16:
       print("You are a child")
elif age > 16:
       print("You are an adult")
else:   #Handle all cases where 'age' is negative
       print("The age must be a positive integer!")

###################################
# ``in``
#--------
# We can use `in` statement to compare a variable against multiple variables.

###################################

name = 'zardari'
if name in ['zardari', 'nawaz', 'chaudhrys', 'mqm']:
    print(name, ' was democratic thug')
elif name in ['zia', 'yahya', 'musharaf', 'ayub']:
    print(name, ' was non-democratic thug')
else:
    print(name, ' is not chor')

###################################

name = 'Zia'
if name.upper() in ['ZARDARI', 'NAWAZ', 'CHAUDHRYS', 'MQM']:
    print(name, ' was a democratic chor')
elif name.upper() in ['ZIA', 'YAHYA', 'MUSHARAF', 'AYUB']:
    print(name, ' was a non-democratic is chor')
else:
    print(name, ' is not chor')

###################################
# comparing numbers
#-------------------

###################################

year = 2009

if 2007>year>2000:
    print('Non-democratic thug ruled Pakistan')
elif 2020>year>=2007:
    print('democratic thug ruled Pakistan')
else:
    print('not considering')

###################################

year = 2012

if 2007>year>2000:
    print('Non-democratic thug ruled Pakistan')
elif 2020>year>=2007:

    if 2013>year>=2007:
        print('democratic thug zardari ruled Pakistan')
    elif 2018>year>=2013:
        print('democratic thug Nawaz ruled Pakistan')
    else:
        print('It seems the ruler is incapable')
else:
    print('not considering')

###################################
# One liner

###################################

day = "14 aug"

if day == '14 aug':  print('This is independence day not partition day.')

###################################

oil = True
us_presence = 1 if oil else 0

print(us_presence)

###################################
# We can use such one liners to set default values to a variable.

###################################

human = {"arms": 2,
         "legs": 2,
         "head": 1}

default_age = 14

age = human["age"] if "age" in human else default_age
print(age)

###################################

provinces = 4
capital = "Kathmandu"
pm = "unknown"

if provinces == 4 and capital == "Islamabad" or pm == "Imran Khan":
    print("This is Pakistan")

###################################

provinces = 4
capital = "unknown"
pm = "Imran Khan"

if provinces == 4 and capital == "Islamabad" or pm == "Imran Khan":
    print("This is Pakistan")

###################################
# ``if not`` vs ``!=``
#---------------------
# Inner working is different but the output is same however `not` is preferred.

###################################

day = "Thursday"
if day != 'Friday':
    print('no jumma prayer')

###################################

day = "Thursday"
if not day == 'Friday':
    print('no jumma prayer')

###################################

if day == 'Friday':
    pass
else:
    print("no jumma prayer")

###################################
# ``any`` vs ``all``
#-------------------

###################################

a = [False, 2>4, 2!=1]
if any(a):
    print('go ahead')

###################################

a = [False, 2>4, 2!=1]
if all(a):
    print('go ahead')
