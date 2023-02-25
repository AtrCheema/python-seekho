"""
==================
6.0 Introduction
==================

.. currentmodule:: easy_mpl

This lesson introduces basics of plotting in python.
"""

# %% md
# Pure python does not contain a built-in module for plotting. Fortunately, other people
# have developed many awesome tools for plotting in python. However, since these
# tools do not come together with python, it means we have to install them.
# One such tool is `matplotlib <https://matplotlib.org/>`_. Once the matplotlib is installed, we can
# import it as below:

import matplotlib

# %%
# the pyplot sub-module of matplotlib as

import matplotlib.pyplot as plt

# %%
# It was developed to replicate MATLAB
# in python. It is a very comprehensive and probably the most widely used plotting
# library in python. matplotlib provides great flexibility to the user to accomplish
# data visualization in python. However, this flexibility comes with a price. Suppose
# if you want to build a house, you have a choice either to make walls, doors
# windows, etc yourself or you can get these ready-to-use materials and then join them
# together. Using the first approach is more cumbersome and time consuming because you will only
# have raw material (wood, rocks, soil, water) to start with. However, it provides you the flexibility
# which you will not have if you use the second approach. The same is true for matplotlib.
# There are two APIs in matplotlib, the functional and object oriented. Following example
# shows drawing a plot using object oriented API of matplotlib.

fig, axes = plt.subplots()
axes.plot([1,2,3])
plt.show()

# %%
# If we want to add the legend, we have to add another line as below

_, axes = plt.subplots()
axes.plot([1,2,3], label="a line")
plt.legend()
plt.show()

# %%
# Above we first cretae the `axes <https://matplotlib.org/stable/api/axes_api.html>`_
# and then use it plot the list of values.
# We have to call ``plt.show()`` to see the plot. Once the plot is shown, the axes
# is `exhausted <https://matplotlib.org/stable/tutorials/introductory/lifecycle.html>`_.
# This means we can not work on it any further. We have to create
# a new axes if we want to plot a new line. Above we have created the plot
# using objected oriented API of matplotlib. There is also a functional API
# in matplotlib. To accomplish above using functional API, we can do as below

plt.plot([1,2,3], label="a line")
plt.legend()
plt.show()

# %%
# As we can notice that, the functional API will fall short to our requirements most
# of the times. But the objected oriented API seems too verbose. What if we could do
#
# .. code-block:: python
#
#    plot([1,2,3], label="a line")
#
# and we would be able to see the plot. This necessity gave rise to `easy_mpl <https://easy-mpl.readthedocs.io>`_ library.
# The purpose of easy_mpl is to ease the use of
# matplotlib while keeping the flexibility of object oriented programming paradigm
# of matplotlib intact. Using these one liners will save the time and will not hurt.
# Moreover, you can swap most function of this library with that of matplotlib and
# vice versa. In this chapter, we will mainly use easy_mpl library for plotting.

# %%
# ``easy_mpl`` contains two kinds of functions, one which are just wrappers around their
# matplotlib alternatives. These include :func:`plot`, :func:`scatter`, :func:`bar_chart`, :func:`pie`,
# :func:`hist`, :func:`imshow` and :func:`boxplot`. As the name suggests, these are just alternatives
# to their matplotlib aliases. All of these functions take same input arguments as taken by
# corresponding matplotlib functions. If these functions are given same input arguments as to their
# matplotlib alternatives, then these functions return same output as returned by matplotlib. Therefore,
# we can consider them as alternative to matplotlib (for most cases). All these functions take three further input
# arguments. These are ``ax``, ``ax_kws`` and ``show``. The meanings of these three arguments are as below
#
# * ``ax`` stands for axes, the matplotlib axes object :obj:`matplotlib.axes`.
#   If ``ax`` argument is given, then the plots are drawn on this otherwise either a new
#   matplotlib axes is created or currently available axes is used.
# * ``ax_kws`` is a dictionary which includes the arguments to manipulate the x and y labels, ticklabels, title.
#   These arguments are passed to :func:`easy_mpl.utils.process_axes` function.
# * The ``show`` argument determines whether to draw the plot after the function or not.
#   If ``show`` is set to False, then the axes is not *exhausted*, which means, we can
#   manipulate it if required and call `plt.show` or `plt.draw` after manipulating the axes.
#   Otherwise, in default case (when ``show`` is True), the plot is drawn immediately after
#   calling the corresponding function.
#

# %%
# Moreover these wrapper functions also take some auxiliary input arguments
# which can be used for further manipulation of these plots. For example the
# :func:`imshow` function takes the ``grid_params`` argument. The second
# kinds of functions in this library are helper functions for data visualization and analysis.
# These include :func:`regplot`, :func:`dumbbell_plot`, :func:`ridge`, :func:`parallel_coordinates`,
# :func:`taylor_plot`, :func:`lollipop_plot`, :func:`circular_bar_plot`,
# :func:`violin_plot` and :func:`spider_plot` . Thus easy_mpl is not a replacement to matplotlib
# in all the cases but it can be your go to tool for the plots given in examples and API in most
# of the cases.

# %%
# Although we will use easy_mpl in this chapter but some concepts of matplotlib will be introduced
# along the way. Each chapter contains comprehensive list of examples so that they can be adopted
# by the user. For complex examples, the user will notice switching to matplotlib by using native
# matplotlibl functions directly.
