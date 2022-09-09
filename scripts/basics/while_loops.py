"""
=================
1.9 while loops
=================
"""

#%% md
# Suppose we have a list of names of people who have ruled Pakistan with one name
# in it who has not been the ruler and we want to find out at which psition the
# name of this person is located. One way to solve this problem is to use while loops.

#%%

looters = ['sikandar mirza', 'ayub khan', 'yahya khan', 'zulfiqar bhutto', 'shahid afridi', 'zia-ul-haq',
           'benazir', 'nawaz sharif', 'musharaf',   'zardari']

acc_id = 0
while acc_id<len(looters):   # this condition must become False at some point.
    if looters[acc_id] == 'shahid afridi':
        print('Found a normal person at position', acc_id)
    else:
        print(looters[acc_id], 'was a thug')
    acc_id += 1

#%% md
# The basic syntax of while statement in python is:
#
# .. code-block:: python
#
#    while (condition):
#        do something
#
# The condition after `while` must become `False` after some time otherwise the
# loop will continute indefinitely. Consider not increasing thte value of `acc_id`
# in upper example and the print statement will continute forever until we have
# to stop it forcefully by terminating the program. (In case you do do this,
# you can stop this by going to `Runtime` --> `Interrupt execution`.)

#%% md
# while with else
#
# .. code-block:: python
#
#  while condition:
#    do something
#  else:
#    do something at last
#

#%%

looters = ['sikandar mirza', 'ayub khan', 'yahya khan', 'zulfiqar bhutto', 'shahid afridi', 'zia-ul-haq',
           'benazir', 'nawaz sharif', 'musharaf', 'zardari']

acc_id = 0
while acc_id<len(looters):
    if looters[acc_id] == 'shahid afridi':
        print('Found a normal person at position', acc_id)
    else:
        print(looters[acc_id], 'was a thug')
    acc_id += 1
else:
    print("Search finished from the whole list of 'looters'")

#%%

looters = ['sikandar mirza', 'ayub khan', 'yahya khan', 'zulfiqar bhutto', 'shahid afridi', 'zia-ul-haq',
           'benazir', 'nawaz sharif', 'musharaf', 'zardari']

acc_id = 0
while acc_id<len(looters):
    if looters[acc_id] == 'shahid afridi':
        print('Found a normal person at position ', acc_id)
    else:
        print(looters[acc_id], 'was a thug')
    acc_id += 1

print("Search finished from the whole list of 'looters'")

#%% md
# We may think `what is the use of else statement`? Ofcouse we can achieve same
# thing by just placing the code inside `else` statement, without making use of `else`.

#%% md
# Wouldn't it be better if we just stop the search after we found the thief.
# Here comes the benefit of `break` statement along with `else` keyword.

#%%

looters = ['sikandar mirza', 'ayub khan', 'yahya khan', 'zulfiqar bhutto', 'shahid afridi', 'zia-ul-haq',
           'benazir', 'nawaz sharif', 'musharaf', 'zardari']

acc_id = 0
while acc_id<len(looters):
    if looters[acc_id] == 'shahid afridi':
        print('Found a normal person at position', acc_id, '. No need to continute searching anymore')
        break
    else:
        print(looters[acc_id], 'was a thug')
    acc_id += 1
else:
    print("Search finished from the whole list of 'looters'")
