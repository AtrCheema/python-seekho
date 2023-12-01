Foreword
**********

A self-paced beginner-level book for python-learners.

Background
===========
I must confess that I do not consider myself an expert capable of writing an entire book on Python. 
As I embarked on my journey to learn Python through online resources, 
I encountered a wealth of materials readily available on the internet. 
Whenever I stumbled upon a particularly insightful example that helped clarify a concept, 
I copied and saved that code snippet in a centralized location. Slowly, this copied material grew larger, and I started organizing
it so that other people could also benefit from the code snippets which I found
useful and which were scattered here and there. Moreover, as I was learning python,
I discovered that hands-on practice is the most effective approach. However, there are
very few resources which offer their code material for download. This led to the creation
of the resource that you have in your hand or on your screen right now!

Purpose
==========
The purpose of this book is to provide prospective learners a self-taught material
with executable notebooks. You can consider this book as a collection of practical code exercises when the
(python) infrastructure is available. However, the pdf_ version
of it can also be used as an ebook. The book is more closely related to the python section of the tutorialspoint_
website. However, this book covers many topics which are not discussed there. More importantly,  the user can download the code examples
here as either Jupyter notebook or as .py files. Therefore, the user can access the complete material
which is more helpful for practical purposes.

Who should read this book
============================

This book is intended for absolute beginners, those who have no background in python.
A very little knowledge of programming can be helpful for the readers. The advanced
python users may find advanced topics within each chapter in this book useful.

Installation
================
If you have internet connection, you can download the ipython notebook of a
lesson and upload it on any cloud servers such as colab_  , binder_ or studiolab_ .

For offline users; first install python, then install all the libraries mentioned in requirements_
file as well as jupyter. Then the user can run any jupyter notebook which again can be downloaded
from website_ .

How to read this book?
==========================
This book consists of Jupyter notebooks. Each Jupyter notebook consists of multiple cells.
Each cell consists of code snippets. The best way to get the maximum out of this book is to
follow following two tips

1) Predict the output from a cell before running the cell, then run the cell and see whether your prediction matches with the output of the cell or not!

2) Change the contents of the cell and predict the output and then run the cell and compare your prediction with actual output.

3) Answer the questions asked in the lessons.


Conventions
===============
Since this is an executable book, which means all the code in this book is executed
during the creation of the book. There is some code in the book which throws errors and
has been commented out. The code which raises errors is only for demonstration purpose
and does not represent a bug in the book. The readers are explicitly advised
to uncomment those lines and run the code to see and understand the error. For example, the following code
illustrates the working of ``TypeError``. However, the code which
raises the ``TypeError`` is commented out. When the user uncomments the line and runs it,
he/she can see the error.

.. code-block:: python

    >>> a = 2

    >>> # uncomment following line
    >>> # a + 'a'  # -> TypeError, we can not add integer and string types


Note
========
This is a living book which is currently being maintained actively on its GitHub repository.
You can expect improvement in the book with time.

.. _colab:
    https://colab.research.google.com/

.. _binder:
    https://mybinder.org/

.. _studiolab:
    https://studiolab.sagemaker.aws/

.. _website:
    https://python-seekho.readthedocs.io

.. _pdf:
    https://python-seekho.readthedocs.io/_/downloads/en/latest/pdf/

.. _tutorialspoint:
    https://www.tutorialspoint.com/python/index.htm

.. _requirements:
    https://github.com/AtrCheema/python-seekho/blob/master/requirements.txt