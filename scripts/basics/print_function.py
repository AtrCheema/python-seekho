"""
============
1.11 print
============
.. important::
  This lesson is still under development.
"""

#%% md
# ``print`` is a function in python 3. In general it will print any value given to it as
# inside argument. If we use two print statements, the next statement is printed on next line.
#
# Print function converts input to string (if it is not already a string) and adds a
# space at its start if it is not start of newline and puts new line at its end.

#%%

name = " Ali"
print(1)
print('printing' + name)

#%% md
# similar thing happens withing loops. When we put a print function in loop, each
# print statement is printed on next line.

#%%

for i in range(5):
    print('printing', i)

#%% md
# but what if we don't want to print at next line. We can do this by making use
# of `end` keyword in print function.

#%%

for i in range(5):
    print(i, end=', ')

#%% md
# The default value of argument ``end`` is ``end=\n``. The print function can take more
# than one argument to print, and we can separate these arguments by a custom separator
# using the argument ``sep``.

#%%

print('Iqbal was born in', 1877, sep=': ')

#%% md

# format
# We can format the output inside print statement by either ``%`` or ``format``. While `%`
# can work both in python 2 and python 3, however, here only `format` is discussed.

#%%

print('Allama Iqbal was born in {} in year {}'.format('Sialkot', 1877))

#%%

rivers = {
    "Indus ": [3180000.525, 'Meters'],
    "Chenab ": [760000.850001004, "Meters"],
    "Jhelum": [132.00001245, "KiloMeters"]
}

for river, paras in rivers.items():
    print('River {} is {}  {} long'.format(river, paras[0], paras[1]))

#%% md
# The number of ``{}`` must be ``<=`` number of arguments in ``format``. The ordering of
# arguments in ``format`` can be customized as shown below.

#%%

rivers = {
    "Indus ": [3180000.525, 'Meters'],
    "Chenab ": [760000.850001004, "Meters"],
    "Jhelum": [132.00001245, "KiloMeters"]
}

for river, paras in rivers.items():
    print('River {1} is {0}  {2} long'.format(paras[0], river, paras[1]))

#%% md
# By default ``{}`` gets as much space as required by it, but we can fix the space used
# by a particular ``{}``. The number of spaces must be defined after ``:`` inside ``{}``.

#%%

for river, paras in rivers.items():
    print('River {0:20} is {1:15}  {2:15} long'.format(river, paras[0], paras[1]))

#%% md
# To define the format of the incoming argument in ``{}``. For example we can use `f` for
# fractional numbers (as done below). If we don't want fractional part, we can use `d`.
# For right alignment, we can use ``<``.

#%%

for river, paras in rivers.items():
    print('River {0:<20} is {1:<15.2f}  {2:<15} long'.format(river, paras[0], paras[1]))

#%% md
# To left align we can use ``>``. ``e`` can be used to show numbers in scientific notation.

#%%

for river, paras in rivers.items():
    print('River {:>20} is {:>15.3e}  {:>15} long'.format(river, paras[0], paras[1]))

#%% md
# We probably would have wished to print it like following

#%%

for river, paras in rivers.items():
    print('River {:<10} is {:^15.1f}  {:<10} long'.format(river, paras[0], paras[1]))

#%% md
# ``^`` is used for center alignment.
# We can truncate long strings as following. If we don't truncate and if incoming
# string in ``{}`` is larger than the space specified, then additional space will be
# assigned to that ``{}``.

#%%

print('{:.12}'.format('Khayber Pakhtun Khwa'))

#%% md
# printing list
# ---------------

#%%

l = [8.364, 0.37, 0.09303, 7.084999, 9.46999999, 0.28600003,
     0.229, 1e-06, 9.414, 0.986001, 2.153005]

print(l)

#%%

print(*l, sep=', ')

#%% md
# ``*`` unpacks the list `l`

#%%

for p in l: print("{:8.5f}".format(p), end=', ')

#%% md
# dynamic printing
# ------------------

#%%

import time

for i in range(10):
    print('.', end='')
    time.sleep(0.3)

#%% md
# ``\r`` removes/deletes what is present on its left side.

#%%

print('Salam \r alaikum')

#%% md
# This can be used for more dynamic printing as following

#%%

a = 0
for x in range (0,10):
    a = a + 1
    b = ("Loading" + "." * a)
    # `b` is printed on top of the previous line.
     # sys.stdout is also called when we use print function
    #sys.stdout.write('\r'+b)
    print('\r'+b, end='')
    time.sleep(0.3)
print ('complete')

#%% md
# Following parts of this tutorial are not really necessary and are hardly used but they
# are mentioned just for the sake of completion.

#%% md
# Customizing print function
# --------------------------

# We can also add additional features to print function if we wish, by redefining print
# function, though it will hardly be required.

#%%

import builtins as _builtins

def MyPrint(*args, **kwargs):
    """My custom print() function."""
    # Adding new arguments to the print function signature
    # is probably a bad idea.
    # Instead consider testing if custom argument keywords
    # are present in kwargs
    _builtins.print('Customized print function')
    return _builtins.print(*args, **kwargs)

#%%

MyPrint('Salam')

#%% md
# Colored printing
# -----------------

#%%

print('Normal' + '\033[91m' + ' Red' + '\033[93m' + 'yellow' + '\033[94m' + ' Blue')

#%%

COLOR = {
    'Bold'       : "\033[1m",
    'Underlined' : "\033[4m",

    'ResetBold'       : "\033[21m",
    'ResetUnderlined' : "\033[24m",

    'Default'      : "\033[39m",
    'Black'        : "\033[30m",
    'Red'          : "\033[31m",
    'Green'        : "\033[32m",
    'Yellow'       : "\033[33m",
    'Blue'         : "\033[34m",
    'Magenta'      : "\033[35m",
    'Cyan'         : "\033[36m",
    'LightGray'    : "\033[37m",
    'DarkGray'     : "\033[90m",
    'LightRed'     : "\033[91m",
    'LightGreen'   : "\033[92m",
    'LightYellow'  : "\033[93m",
    'LightBlue'    : "\033[94m",
    'LightMagenta' : "\033[95m",
    'White'        : "\033[97m",

    'BackgroundDefault'      : "\033[49m",
    'BackgroundBlack'        : "\033[40m",
    'BackgroundRed'          : "\033[41m",
    'BackgroundGreen'        : "\033[42m",
    'BackgroundYellow'       : "\033[43m",
    'BackgroundBlue'         : "\033[44m",
    'BackgroundMagenta'      : "\033[45m",
    'BackgroundCyan'         : "\033[46m",
    'BackgroundLightGray'    : "\033[47m",
    'BackgroundDarkGray'     : "\033[100m",
    'BackgroundLightRed'     : "\033[101m",
    'BackgroundLightGreen'   : "\033[102m",
    'BackgroundLightYellow'  : "\033[103m",
    'BackgroundLightBlue'    : "\033[104m",
    'BackgroundLightMagenta' : "\033[105m",
    'BackgroundLightCyan'    : "\033[106m",
    'BackgroundWhite'        : "\033[107m",
    }

last_color = '\033[91m'
for color, cc in COLOR.items():
    print(last_color + cc)
    last_color = color

#%%

print('ali')

#%% md
# printing special characters

#%%

print("\N{COPYRIGHT SIGN}")

#%% md
# A complete code for special characters can be found here [1]_

#%%

special_characters = {
"NULL": "\N{NULL}",
"SECTION SIGN": "\N{SECTION SIGN}",
"COPYRIGHT SIGN": "\N{COPYRIGHT SIGN}",
"REGISTERED SIGN": "\N{REGISTERED SIGN}",
"INVERTED QUESTION MARK": "\N{LATIN CAPITAL LETTER O WITH STROKE}",
"LATIN CAPITAL LETTER O WITH STROKE": "\N{LATIN CAPITAL LETTER O WITH STROKE}",
"LATIN CAPITAL LETTER SCHWA": "\N{LATIN CAPITAL LETTER SCHWA}",
"LATIN CAPITAL LETTER OPEN E": "\N{LATIN CAPITAL LETTER OPEN E}",
"LATIN SMALL LETTER N WITH LONG RIGHT LEG": "\N{LATIN SMALL LETTER N WITH LONG RIGHT LEG}",
"LATIN CAPITAL LETTER O WITH MIDDLE TILDE": "\N{LATIN CAPITAL LETTER O WITH MIDDLE TILDE}",
"LATIN CAPITAL LETTER ESH": "\N{LATIN CAPITAL LETTER ESH}",
"LATIN SMALL LETTER T WITH HOOK": "\N{LATIN SMALL LETTER T WITH HOOK}",
"LATIN CAPITAL LETTER T WITH RETROFLEX HOOK": "\N{LATIN CAPITAL LETTER T WITH RETROFLEX HOOK}",
"LATIN CAPITAL LETTER UPSILON": "\N{LATIN CAPITAL LETTER UPSILON}",
"LATIN SMALL LETTER SCHWA": "\N{LATIN SMALL LETTER SCHWA}",
"LATIN SMALL LETTER ESH": "\N{LATIN SMALL LETTER ESH}",
"LATIN LETTER BILABIAL CLICK": "\N{LATIN LETTER BILABIAL CLICK}",
"GREEK CAPITAL LETTER OMEGA WITH TONOS": "\N{GREEK CAPITAL LETTER OMEGA WITH TONOS}",
"GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS": "\N{GREEK SMALL LETTER IOTA WITH DIALYTIKA AND TONOS}",
"GREEK CAPITAL LETTER DELTA": "\N{GREEK CAPITAL LETTER DELTA}",
"GREEK CAPITAL LETTER THETA": "\N{GREEK CAPITAL LETTER THETA}",
"GREEK CAPITAL LETTER LAMDA": "\N{GREEK CAPITAL LETTER LAMDA}",
"GREEK CAPITAL LETTER PI": "\N{GREEK CAPITAL LETTER PI}",
"GREEK CAPITAL LETTER SIGMA": "\N{GREEK CAPITAL LETTER SIGMA}",
"GREEK CAPITAL LETTER PHI": "\N{GREEK CAPITAL LETTER PHI}",
"GREEK CAPITAL LETTER PSI": "\N{GREEK CAPITAL LETTER PSI}",
"GREEK CAPITAL LETTER OMEGA": "\N{GREEK CAPITAL LETTER OMEGA}",
"GREEK SMALL LETTER ETA WITH TONOS": "\N{GREEK SMALL LETTER ETA WITH TONOS}",
"GREEK SMALL LETTER IOTA WITH TONOS": "\N{GREEK SMALL LETTER IOTA WITH TONOS}",
"GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS": "\N{GREEK SMALL LETTER UPSILON WITH DIALYTIKA AND TONOS}",
"GREEK SMALL LETTER ALPHA": "\N{GREEK SMALL LETTER ALPHA}",
"GREEK SMALL LETTER BETA": "\N{GREEK SMALL LETTER BETA}",
"GREEK SMALL LETTER GAMMA": "\N{GREEK SMALL LETTER GAMMA}",
"GREEK SMALL LETTER DELTA": "\N{GREEK SMALL LETTER DELTA}",
"GREEK SMALL LETTER EPSILON": "\N{GREEK SMALL LETTER EPSILON}",
"GREEK SMALL LETTER ZETA": "\N{GREEK SMALL LETTER ZETA}",
"GREEK SMALL LETTER ETA": "\N{GREEK SMALL LETTER ETA}",
"GREEK SMALL LETTER THETA": "\N{GREEK SMALL LETTER THETA}",
"GREEK SMALL LETTER LAMDA": "\N{GREEK SMALL LETTER LAMDA}",
"GREEK SMALL LETTER MU": "\N{GREEK SMALL LETTER MU}",
"GREEK SMALL LETTER NU": "\N{GREEK SMALL LETTER NU}",
"GREEK SMALL LETTER XI": "\N{GREEK SMALL LETTER XI}",
"GREEK SMALL LETTER PI": "\N{GREEK SMALL LETTER PI}",
"GREEK SMALL LETTER SIGMA": "\N{GREEK SMALL LETTER SIGMA}",
"GREEK SMALL LETTER TAU": "\N{GREEK SMALL LETTER TAU}",
"GREEK SMALL LETTER CHI": "\N{GREEK SMALL LETTER CHI}",
"GREEK SMALL LETTER PSI": "\N{GREEK SMALL LETTER PSI}",
"GREEK SMALL LETTER OMEGA": "\N{GREEK SMALL LETTER OMEGA}",
"GREEK PHI SYMBOL": "\N{GREEK PHI SYMBOL}",
"GREEK SMALL LETTER ARCHAIC KOPPA": "\N{GREEK SMALL LETTER ARCHAIC KOPPA}",
"GREEK CAPITAL THETA SYMBOL": "\N{GREEK CAPITAL THETA SYMBOL}",
"GREEK LUNATE EPSILON SYMBOL" : "\N{GREEK LUNATE EPSILON SYMBOL}"
}

for sp, val in special_characters.items():
    print("{:52} {:>5}".format(sp, val))

#%%
#
# .. [1] `<http://www.fileformat.info/info/charset/UTF-16/list.htm>`_