
[![Documentation Status](https://readthedocs.org/projects/python-seekho/badge/?version=latest)](https://python-seekho.readthedocs.io/en/latest/?badge=latest)
![GitHub last commit](https://img.shields.io/github/last-commit/AtrCheema/python-seekho)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/AtrCheema/python-seekho)

A book for python-learners to learn the language by practicing it.

# Purpose
The purpose of this book is to provide the prospective learners a self-taught material 
with executable notebooks. This book can be considered as practical code exercises when the 
(python) infrastructure is available. However, the [pdf version](https://python-seekho.readthedocs.io/_/downloads/en/latest/pdf/) 
of it can also be used as ebook. The book is more closely related to python section of [tutorialspoint.com](https://www.tutorialspoint.com/python/index.htm)
website. However, this book covers many topics which are not discussed there. More importantly, the code examples
here can be downloaded as either jupyter notebook or .py files. Therefore, the user can access the complete material
which is more helpful for practical purposes.

# Who should read this book
This book is intended for absolute beginners, those who have no knowledge of python.
A very little knowledge of programming can be helpful for the readers. The advanced
python users may find advanced topics within each chapter in this book useful.

# Installation
If you have internet connection, you have two options
    
- Download the ipython notebook of a lesson and upload it on any cloud servers such
      as [colab](https://colab.research.google.com/), [binder](https://mybinder.org/) or [studiolab](https://studiolab.sagemaker.aws/).
    
- click on launch binder button and start running the code, cell by cell.

For offline users; first install python, the libraries mentioned in requirements.txt
file and jupyter. Then the user can run any jupyter notebook which again can be downloaded
all at once from [website](https://python-seekho.readthedocs.io).

# How to read this book?
This book consists of jupyter notebooks. Each jupyter notebook consists of multiple cells.
Each cell consists of code snippets. The best way to get maximum out of this book is to
follow following two tips

1) Predict the output from a cell before running the cell, then run the cell and see whether
your prediction matches with the output of the cell or not!
   
2) Change the contents of the cell and predict the output and then run the cell and compare your
prediction with actual output.
   
3) Answer the questions in the lessons.

# Conventions
Since this is an executable book, which means all the code in this book is executed
during the creation of the book. There is some code in the book which throws errors and
has been commented out. The code which raises errors is for demonstrative purpose
only and does not mean that it is a bug in the book. The readers are explicitly advised
to uncomment those lines and run the code to see the error. For example, following code
illustrates the working of `TypeError`. However, the code which actually
raises the `TypeError` is commented out. When the user uncomment the line and runs it,
he/she can see the error.

```python
a = 2

# uncomment following line
# a + 'a'  # -> TypeError, we can not add integer and string types
```
   

# Note
This is a living book which is currently being maintained actively on its GitHub repository.
You can expect improvement in the book with time.

# Chapters

## Chapter 1. Basics

### 1.1 [Variables](scripts/basics/variables.py)
### 1.2 [operators]()
### 1.3 [sequential data]()
### 1.4 [lists]()
### 1.5 [copying lists]()
### 1.6 [dictionary]()
### 1.7 [sets]()
### 1.8 [conditional statements]()
### 1.9 [while loops]()
### 1.10 [for loops]()
### 1.11 [print]()
### 1.12 [functions]()
### 1.13 [args and kwargs]()
### 1.14 [global vs local]()
### 1.15 [nested functions]()
### 1.16 [iterator vs iterable]()
### 1.17 [read/write operations]()
### 1.18 [Exceptions]()
### 1.19 [generators]()
### 1.20 [installing packages]()
### 1.21 [builtin functions]()


## Chapter 2. Builtiin modules

### 2.1 [os](scripts/builtin_modules/_os.py)
### 2.2 [sys]()
### 2.3 [time and dateandtime ]()
### 2.4 [copy]()
### 2.5 [collections]()
### 2.6 [types and typing]()
### 2.7 [math]()
### 2.8 [pathlib]()
### 2.9 [warnings]()
### 2.10 [random]()
### 2.11 [csv]()
### 2.12 [itertools]()


## Chapter 3. Object Oriented Programming

### 3.1 [Introduction](scripts/basics/variables.py)
### 3.2 [creating class]()
### 3.3 [Attributes]()
### 3.4 [methods]()
### 3.5 [init method]()
### 3.6 [str and repr methods]()
### 3.7 [public vs private attributes]()
### 3.8 [class vs instance attributes]()
### 3.9 [static methods]()
### 3.10 [class methods]()
### 3.11 [property]()
### 3.12 [descriptors]()
### 3.13 [Inheritance]()
### 3.14 [__call__]()
### 3.15 [__getattr__]()
### 3.16 [magic methods]()
### 3.17 [getattr vs setattr]()


## Chapter 4. numpy

### 4.1 [understanding dimension/axis](scripts/numpy/dimensions_axis.py)
### 4.2 [stacking vs concatenating]()
### 4.3 [quantile and digitize]()


## Chapter 5. Pandas

### 5.1 [Introduction](scripts/pandas/dataframe_vs_series.py)
### 5.2 [indexing and slicing]()
### 5.3 [working with time series]()
### 5.4 [reading/writing]()
### 5.5 [apply]()
### 5.6 [groupby]()
### 5.7 [multi-indexing]()
### 5.8 [efficient pandas]()


## Chapter 6. Plotting

### 6.1 [Introduction](scripts/plotting/intro.py)
### 6.2 [basic plot]()
### 6.3 [scatter plot]()
### 6.4 [bar plot]()
### 6.5 [heatmap]()
### 6.6 [regression plot]()
### 6.7 [lollipop plot]()
### 6.8 [dumbell plot]()
### 6.9 [circular bar plot]()
### 6.10 [histogram]()
### 6.11 [ridge plot]()
### 6.12 [contour plot]()
### 6.13 [pie chart]()
### 6.14 [spider plot]()
### 6.15 [parallel coordinates]()
### 6.16 [taylor plot]()
### 6.17 [boxplot]()
### 6.17 [violin plot]()
### 6.18 [Adding Marginal Plots]()


## Chapter 7. Advanced Topics

### 7.1 [Parallel Processing]()
### 7.2 [cython]()
### 7.3 [interfacing with C]()
### 7.4 [interfacing with C++]()
### 7.5 [interfacing with FORTRAN]()
### 7.6 [interfacing with matlab]()
### 7.7 [testing]()
### 7.8 [Regular Expressions](scripts/basics/variables.py)
