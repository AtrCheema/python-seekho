"""
=========================
1.20 installing packages
=========================

"""

# %%
# What is meaning of installing a python package?

def foo():
    pass

foo()

# %%
# Above we used the function `foo` which was defined above in the same file where it was called.
# However, if the `foo` was defined not in the same file, but in some other file, we would have
# to ``import`` the `foo` function from that file. That file containing `foo` function can be
# located anywhere in the hard drive/storage of our machine/computer. If python is able to 'see' that file and consequently
# the foo function in that file, you can import foo from that file. But if python is not able
# to see that file, even if it is located somewhere in your computer, you can not import
# that function. This applies not only to functions by to every python object like variables, classes etc.
# The process of putting the required files in required format at the required location can be
# termed as installing a library/module/package in python. When we say that we want to install
# a library say ``numpy`` in python, it means we want all the files of this library at a place
# in our computer so that python can see it. Moreover, the files should be in such a form
# that we can import our desired functions from them.

# %%
# putting module in cwd
# ---------------------
# A simpler solution of installing a package/library is to simply put in our
# current working directory. This is because if we print ``sys.path``,
# the first directory is the current working directory. This means, whenever
# we try to import something, python will look into current working directory.
# Therefore, if we put some file/package/library in our current working directory,
# we can simply import that library without any problem.

# %%
# using site
# -----------------------
# Putting a lot of libraries/packages in our current working library can clutter
# current working direcotry. This is because we may need hundred of libraries to work with.
# One solution is to place those packages at any place in our desired location in our machine,
# and then import that package from that location. We can add the location of that package
# into python's ``path`` during runtime using ``site.addsitedir`` function.

import site
site.addsitedir('path/to/my/package')

# %%
# pip
# -------
# An easy and one of the most commonly used tool to install a package is using
# ``pip``. We can do this in the command prompt. Remember that ``pip`` installs
# the package in ``site_packages`` directory of python.

#  pip install mypackage

# pip install mypackage==0.1

# pip install -update mypackage

# pip install mypackage[InstallOptions]

# %%
# conda
# --------

# -e .
