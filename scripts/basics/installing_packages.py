"""
=========================
1.20 installing packages
=========================

"""

def foo():
    pass

foo()

# %%
# Above we used the function `foo` which was defined above in the same file where it was called.
# However, if the `foo` was defined not in the same file, but in some other file, we would have
# to ``import`` the `foo` function from that file. That file containing `foo` function can be
# located anywhere in the hard drive/storage. If python is able to 'see' that file and consequently
# the foo function in that file, you can import foo from that file. But if python is not able
# to see that file, even if it is located somewhere in your computer, you can not import
# that function. This applies not only to functions by to every python object like variables, classes etc.
# The process of putting the required files in required format at the required location can be
# termed as installing a library/module/package in python. When we say that we want to install
# a library say ``numpy`` in python, it means we want all the files of this library at place
# in our computer so that python can see it. Moreover, the files should be in such a form
# that we can import our desired functions from them.

# putting module in cwd
# ---------------------

# using site
#-----------------------

import site

# pip
#-------

# conda
#--------

# -e .
