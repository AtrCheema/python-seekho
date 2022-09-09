"""
======================
1.12 args and kwargs
======================

"""


#################################################
# ``*args``
#---------
# If we want to our function to have variable number of input arguments, one way
# to do this is to put *args inside () when defining the function. This
# will allow us to have multiple unnamed input arguments.


#################################################

def add_nums(*args):
    print(type(args), len(args), args)


add_nums(5, 12.0)

#################################################
# ``*args`` returns a tuple. Inside the above function 2,3 is taken as `(2,3)`

#################################################

l = [2, 3, 4]
add_nums(l)

#################################################
# Inside the function `add_nums`, the input argument `[2,3,4]` which is a list,
# is taken as `([2,3,4],)` which is tuple.


#################################################

def do_add(*args):
    print(len(args), 'in do_add')
    for arg in args:
        print(arg)
    return


def add_nums(*args):
    # we get a tuple i.e. (12,14)
    print(len(args), 'in add_nums')

    # we pass the tuple (12,14) as input argument and NOT 12,14 as two input arguments
    return do_add(args)


add_nums(12, 14)


#################################################

def do_add(*args):
    print(len(args), 'in do_add')
    a = 0
    for arg in args:
        a += arg
    return a


def add_nums(*args):
    print(len(args), 'in add_nums')
    # we get a tuple i.e. (12,14) as input

    # we are again providing input as 2,3 which means we are providing two inputs
    return do_add(*args)


add_nums(12, 14)

#################################################
# Above: ``add_nums`` and ``do_add`` are called with exactly same kind of input arguments.

#################################################
# Following is example of misplaced return statement


#################################################

def do_add(*args):
    print(len(args), 'in do_add')
    a = 0
    for arg in args:
        a += arg
        return a


def add_nums(_a, *args):
    print(len(args), "in add_nums")
    return do_add(_a, *args)  # this asterik unpacks tuple args


add_nums(2, 12, 14)


#################################################

def do_add(a, *args):
    print(len(args), 'in do_add')

    for arg in args:
        a += arg
    return a


def add_nums(_a, *args):
    print(len(args), "in add_nums")
    return do_add(_a, *args)


add_nums(5, 12, 14)

#################################################
# ``a`` is the positional argument which takes 5, while while 12 and 14 are given
# as tuple to the function

#################################################


def add_nums(a, b, c):
    print(a, b, c)
    return


l = [1, 5, 12]
# if the list `l` contains more than 3 elements, passing it will raise error
add_nums(*l)

#################################################
# *Although* we can vary the number of arguments by using `*args` but we can not
# know the name of input args.

#################################################
# ``**kwargs``
#-----------------

#################################################

def add_nums(**kwargs):
    print(type(kwargs))


add_nums(a=5, b=12)  # we can not do add_nums(2,3) here


#################################################

def add_nums(**dictionary):
    print(type(dictionary), len(dictionary))


add_nums(a=5, b=12)


#################################################

def add_nums(**kwargs):
    print(type(kwargs))


a = 5
b = 12
dictionary = {'a': a, 'b': b}

# add_nums(a,b) is invalid, add_nums(dictionary) is invalid as well
add_nums(**dictionary)


#################################################

def add_nums(**kwargs):
    x = kwargs['a']
    y = kwargs['b']
    return x + y


a = 5
b = 12
dictionary = {'a': a, 'b': b}
add_nums(**dictionary)

#################################################
# Omitting ``**`` on both sides also serves the purpose.
# However, if we omit ``**`` in function definition, it would mean that
# function requires an input argument named ``kwargs``. If we ommit ``**`` when
# calling the function it means that we are giving a dicionary as it is as input argument.

#################################################


def add_nums(kwargs):
    x = kwargs['a']
    y = kwargs['b']
    return x + y


a = 5
b = 12
dictionary = {'a': a, 'b': b}
add_nums(dictionary)


#################################################

def add_nums(a=1, b=5):
    print(type(a))
    return a + b


d = {'a': 12, 'b': 14}
add_nums(**d)


#################################################

def add_nums(xx, **kwargs):
    x = kwargs['a']
    y = kwargs['b']
    return xx + x + y


dictionary = {'a': 5, 'b': 12}
add_nums(1, **dictionary)

#################################################
# ``xx`` is assigned the value of `1` when the function `add_nums` is called.
# We can put extra named arguments separately along with `**kwargs`.

#################################################


def add_nums(xx=1, **kwargs):
    _sum = 0.0
    for key, val in kwargs.items():
        _sum += val

    return _sum


dictionary = {'a': 5, 'b': 12}
add_nums(**dictionary)

#################################################
# The value of `xx` which is `1` is not added in the final answer.


#################################################

def add_nums(xx=1, yy=12, zz=14, **kwargs):
    _sum = 0.0
    for key, val in kwargs.items():
        _sum += val

    return _sum


add_nums(xx=114, yy=313, zz=7, a=1, b=5, c=12, d=14)

#################################################
# now ``kwargs`` contained ``a``, ``b``, ``c`` and ``d`` only. The above code
# can also be written as following.


#################################################

def add_nums(xx=1, yy=12, zz=14, **kwargs):
    _sum = 0.0
    for key, val in kwargs.items():
        _sum += val

    return _sum


additional_args = {
    "a": 1,
    "b": 5,
    "c": 12,
    "d": 14,

}
add_nums(xx=114, yy=313, zz=7, **additional_args)

#################################################
# A misplaced ``return`` can be a cause of many headachs, as in following case.


#################################################

def add_nums(xx=1, yy=12, zz=14,
             **kwargs):
    # if number of arguments are large, it is totally fine to go on
    # second line without any probelm

    _sum = 0.0
    for key, val in kwargs.items():
        _sum += val

        return _sum


additional_args = {
    "a": 114,
    "b": 5,
    "c": 12,
    "d": 14,

}
add_nums(xx=114, yy=313, zz=7, **additional_args)

#################################################
# Above, the function `add_nums` finishs execution just after first iteration of `for loop`.


#################################################

def cook_lunch_with_bread(raw_food):
    print('prepare lunch with break')


def cook_lunch_without_bread(raw_food):
    print('prepare lunch with {}, {} and without bread'.format(*raw_food.keys()))


def lunch(**raw_food):
    if 'bread' in raw_food:
        cook_lunch_with_bread(raw_food)
    else:
        cook_lunch_without_bread(raw_food)


lunch(rice='2', milk=1)

#################################################
# We can predefine/fix the number of positional arguments and keyword arguments
# that a function must take. Following code allows only 3 positional keyword
# arguments and 2 keyword arguments.

#################################################

def add_nums(a, b, c, *, d, e):
    print(a, b, c)

#%%
# we can not do add_num(2,3,4, 12, 14), as this would mean 5 positional
# arguments instead of 3.

add_nums(2, 3, 4, d=12, e=14)


#################################################

def add_nums(a, b, *args, **kwargs):
    _sum = a + b
    print(len(args), len(kwargs))
    for arg in args:
        _sum += arg
    for key, val in kwargs.items():
        _sum += val

    return _sum


add_nums(2, 3)

#################################################

add_nums(2, 3, 4, 5)

#################################################
# ``4`` and ``5`` goes to args

#################################################

add_nums(2, 3, 4, 5, 6, d=5, e=12)

#################################################
#
# ``4``, ``5`, ``6`` goes to args and ``d`` and ``e`` goes to kwargs
