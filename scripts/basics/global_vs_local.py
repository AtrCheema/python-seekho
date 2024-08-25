"""
======================
1.14 global vs local
======================
"""
# %%
# It is very important to understand the difference between global scope and local
# scope of a variable/object in python. A variable defined outside a function has global
# scope while a variable defined inside a function has local scope. 

# %%
var = 1
def foo():
    return

# %%
# Above the variable ``var`` has global scope. We can access it from anywhere in the
# script. 


# %%
def foo():
    var1 = 1
    return

# %%
# The variable ``var1`` has local scope. We can access, use and modify it only 
# insdie the function ``foo``. We can not access it from outside the function
# ``foo``. If we try to access it, python will give us an error. Hence the variable
# ``var`` has local scope.

#%%
# If a variable is defined outside the function and a variable with same name is
# defined and(or) being modified inside a function, then that definition inside
# the function will have no effect on the variable outside the function.

#%%

var = 1

def foo(n):
    var = n
    print(var, 'inside foo')
    return

foo(10)

print(var, 'outside foo')

#%% md
# `var` inside the `foo` is different than the `var` outside the `foo`.
# If we try to access value of variable which is defined only outside the
# function, it will result in error.

#%%

var = 1

def foo(n):
    print(n)
    var = var + n
    return var

# %%
# uncomment follwoing line
# foo(10)  # UnboundLocalError

#%% md
# Read and try to make sense of the error message as understanding error messages
# is one of the best ways to master a programming language.
# So the variable `var` which is defined outside `foo` can not be accessed (actually
# it can be accessed but not changed/reassigned, discussion follows) inside `foo`.
# If we want to do so, we need to use the keyword ``global``.

#%%


var = 1

def foo(n):
    global var
    print(n)
    var = var + n
    return var

foo(10)

#%% md
# By making use of ``global`` statement, we are saying that the variable `var`
# inside the function is same object as the variable `var` outside the function `foo`.
# Similarly if a variable is defined inside the function, we can not access that
# variable outside the function.

#%%

def foo(n):
    var1 = n+2
    return

foo(10)

# %%

# uncomment following line

# print(var1) NameError

#%% md
# variable `var1` is defined inside the function and is removed from memory as soon
# as the function execution finishes at `return` statement. (Why I used `var1`
# instead of `var` for this example?)
# If we want to access a variable -which is defined inside the function- outside the
# function, we have to make this variable global by declaring the it.

#%%

def foo(n):
    global var1
    var1 = n+2
    return

foo(10)

# %%

# uncomment following line
# print(var1)

#%% md
# when python finds a variable is local

#%%

var = 1

def foo(n):
    print(var)

foo(10)

#%% md
# The above code shows we are able to access/employ/use/read the value of variable
# `var` inside `foo` without making it `global`.

#%%

var = 1

def foo(n):
    print(var)
    var = 0

# %%

# uncomment following line
# foo(10)  # UnboundLocalError

#%% md
# So untill we defined the variable `var` inside `foo` by `var=0`, python did not create
# the local variable `var`. Until that point if we use/access the value of `var`,
# python will give us the value of `var` from outer scope. But as soon as we
# defined `var` inside the function `foo`, then python knows that this `var` is a
# local variable and is different than `var` outside the `foo`. Python then creates
# the local variable `var`. At this point python makes the variable `var`, **local**.
# (You can say, python forgets what `var` in outer scope is). As we tried to use
# `var` before declaring it, hence the error message.

#%%

var = 1

def foo(n):
    global var
    var = n  # modifying global copy of var

def print_var():
    print(var)  # prints global value of var

print(var)
foo(10)
print_var()

#%% md
# **Takeaway:** We need to declare a variable as `global` in a function which assigns
# a value of it. If we want to ONLY USE a global variable in local scope, we can
# do this without declaring it global.

#%% md
# *alternative to global*
# =======================
# If we want to share a variable between two functions, and the outer scope, we
# have to make use of `global` statement in both functions.

#%%

var = 0   # The initial value of x, with global scope

def foo2():
    global var
    var = var + 5

def main():
    global var   # So we can change the value of var inside main
    print(var)    # first check the var inside main
    var = 10
    print(var)
    foo2()
    print(var)

main()

#%% md
# We should normaly avoid sharing variables among different functions with the
# help of ``global``. The alternative to do this, is to make use of functions with ``return``.

#%%

def foo1(parameter):
    return parameter + 5

def main():
    var = 10
    print(var)
    var = foo1(var)
    print(var)

main()

#%% md
# existence of a vriable
# =======================
# Now the variable `var` exists in memory. We can print its value.

#%%

var

#%% md
# We can delete the variable from memory by making use of `del` statement.

#%%

del var

#%% md
# Now if we try to print the value of `var` again, python says it does not know
# what is `var`, since we removed it from memory.

#%%

# uncomment following line
# var  # NameError

#%% md
# If we want to safely remove/delte a variable, we can first check whether it is
# present in memory or not and delete it only if it is present.

#%%

_all = locals().copy()
_all.update(globals())
if 'var' in globals():
    del var
    print('var removed')
else:
    print('it was not in memory')

#%% md
# We can create the variable `var` once again and try to remove it using the above
# method to validate it.

#%%

var = 3
var

#%%

if 'var' in globals():
    del var
    print('var removed')
else:
    print('it was not in memory')

#%% md
# ``globals()`` returns a dictionary of all global variables while ``locals()`` returns a
# dictionary of all local variables. The names of variables are keys of these
# dictionaries and values of these variables are values of these keys in these dictionaries.

#%%
#
# .. code-block:: python
#
#    for k,v in locals().items():
#        print(k)#, v)  # not printing values for brevity
#
#

#%%
#
# .. code-block:: python
#
#    for k,v in globals().items():
#        print(k)
#

#%% md
# calling a function by its string name
# With the help of `globals()` function, we can call a method by its string name.

#%%

def qatal(a):
    print(a + ' sanaullah')

func_as_string = 'qatal'

globals()[func_as_string]('rana') # qatal().

#%% md
# Normally global variables are considered bad see this [1]_  and this [2]_ .
# In python, by convention, global is used for constants and variables
# are seldom used as global. Technically in python there is no
# difference between variables and constants, however it is a convention
# to capitalize GLOBAL CONSTANTS and not global_variables. It is recommende
# that you explicitly declare global inside a function when you
# are using a global variable even though if it is not required.

#%% md
# modifying global variable with same name as local
# If there is a local variable with same name as global variable and we want to modify
# global variable, we can make use of `globals()`.

#%%

thug = 'showbaz'

def commision(accused):
    thug = 'nawaz'
    print('internal thug: ', thug)
    globals()['thug'] = accused
    print('internal thug: ', thug)
    return

print('global thug before: ', thug)
commision('bajwa')
print('global thug later:', thug)

#%% md
# Mutable objects
# ===============
# We can change/modify the values of mutable objects such as that of dictionaries
# from inside the function without declaring them global.

#%%

thug = {'name': ' '}

def commision(thug_name):
    thug['name'] = thug_name

print(thug)
commision('showbaz')
print(thug)

#%%

thugs = ['musharaf', 'zardari']

def commision(accused):
    thugs.append(accused)

commision('nawaz')
thugs

#%%

thugs = set(thugs)

def commision(accused):
    thugs.add(accused)

commision('bajwa')
thugs

#%% md
# Although tuples are immutable, thus they can not be modified but they can contain
# mutable objects such as lists, thus we can change/modify such contents of
# tuples from inside the function without using the keyword `global`.

#%%

thugs_tuple = (list(thugs),)

def commision(accused):
    thugs_tuple[0].append(accused)

print(thugs_tuple)
commision('pervailz elahi')
print(thugs_tuple)

#%% md
# What will happen if we do assignment to a global variable inside function/local
# scope. The variable inside the local scope will be new created while the
# immutable object outside the function will remain same.

#%%

thugs = ['musharaf', 'zardari']

def commision(accused):
    thugs = [accused]
    print(thugs, 'inside')
    return

print(thugs, 'outside')
commision('nawaz')
print(thugs, 'outside')

#%% md
# However, as said earlier, if we used the keyword `global`, this will affect
# the variable from global scope.

#%%

thugs = ['musharaf', 'zardari']

def commision(accused):
    global thugs
    thugs = [accused]
    print(thugs, 'inside')
    return

print(thugs, 'outside')
commision('nawaz')
print(thugs, 'outside')

#%% md
# In general: variables in python are local unless declared otherwise.

# %%
# Questions
# =========
# Answer the following questions without running the code above them.

def foo():
    number = 2
    return number

# %%
# **Question:** What value will be printed by the following code?
#
# .. code-block:: python
#
#    foo()
#    print(number)

# %%
# **Question:** Did you get any error in the above code? If yes, then explain the error?

# %%

num = 1

def add_something(var):
    return var + num

def multipy_something(var):
    return var * num

a = add_something(5)
b = multipy_something(a)

# %%
# **Question:** What will be the value of ``b`` in above code?


# %%
num = 1

def add_something(var):
    return var + num

def multipy_something(var):
    return var * num

a = add_something(5)
num = 12
b = multipy_something(a)

# %%
# **Question:** What will be the value of ``b`` in above code and why?

# %%

num = 1

def add_something(var):
    num = 14
    return var + num

def multipy_something(var):
    return var * num

a = add_something(5)
num = 12
b = multipy_something(a)

# %%
# **Question:** What will be the value of ``b`` in above and why?

# %%
num = 1

def add_something(var):
    global num
    num = 14
    return var + num

def multipy_something(var):
    return var * num

a = add_something(5)
b = multipy_something(a)

# %%
# **Question:** What will be the value of ``b`` in above code and why?

# %%
num = 1

def add_something(var):
    global num
    num = 14

def multipy_something(var):
    return var * num

add_something(5)
b = multipy_something(12)

# %%
# **Question:** What will be the value of `b` in above code and why?

# %%

num = 1

def add_something(var):
    global num
    num = 14

def multipy_something(var):
    num = 12
    return var * num

add_something(5)
num = num + 92
multipy_something(12)

# %%
# **Question:** What will be the value of ``num`` in above code and why?

# %%
num = 1

def add_something(var):
    global num
    num = 14

def multipy_something(var):
    global num
    num = num * var

add_something(5)
num = num + 92
multipy_something(12)

# %%
# **Question:** What will be the value of ``num`` in above code and why?

# %%
book = "black"

def change_book1():
    book = "white"
    return

def change_book2():
    global book
    book = book + " white"

change_book1()
book = book + " skin"
change_book2()
book = book + " masks"

# %%
# **Question:** What will be the value of `book` and why?

# %%
book = {'name': 'black skin white masks'}

def add_info():
    book['author'] = 'frantz fanon'
    return

def change_info():
    book['name'] = 'white skin black masks'
    return

add_info()
change_info()

# %%
# **Question:** What will be the value of ``book['name']`` and why?

#%% md
# .. [1] `<http://wiki.c2.com/?GlobalVariablesAreBad>`_
# .. [2] `<https://en.wikipedia.org/wiki/Side_effect_(computer_science)>`_
