"""
=====================
7.8 testing your code
=====================

This lesson describes unit testing in python.
"""

# %% md
# If you are writing a code which you think will not be used by you or
# anyone else in the future, then you can skip this lesson. However, if
# you intend to write a code, which will used by you and others in future
# then you must write tests for your code, so that your code is reliable.
# The purpose of writing tests is **to make sure that the code works and
# will keep on working the way it should work**.
#
# Consider the following function which adds two numbers
#
def add(a,b):
    return a+b

# %%
# Now if we want to write a test for this function, it will look something like below

summation = add(2,2)
assert summation==4

# %%
# Above we are testing the ``add`` function. But we have tested it only with integers
# as input. We should probably check it with float or other types as well.

assert add(2.0, 2.0)==4.0
