"""
=================
2. creating class
=================
"""

#%% md
# Creating Classes
#-----------------
#
# We can define a minimal class as follows

#%%

class Insan:
    pass

#%% md
# class consists of two parts
# * header: keyword ``class`` and name of class and then listing of other classes from
# which this class inherits i.e. superclasses. 3rd argument is optional
# * body: indented statements, we have only one statement i.e. ``pass``


#%% md
# Using classes
#--------------
# We can use this simple class as following

#%%

ali = Insan()
husain = Insan()

#%% md
# we have created two objects/instances of class ``Insan`` namely ``ali`` and ``husain``.
# if we check the type of these instances we can confirm it.

#%%

type(ali), type(husain)

#%%

shabir = husain

#%%

print(husain == shabir)

#%%

print(husain == ali)

#%% md
# So ``husain`` and ``ali`` are different although they are instances of
# same class but they are different because they are different instances of the class ``Insan``.
