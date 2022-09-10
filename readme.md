
[![Documentation Status](https://readthedocs.org/projects/python-seekho/badge/?version=latest)](https://python-seekho.readthedocs.io/en/latest/?badge=latest)

A book for python-learners to learn the language by practicing it.

## Purpose
The purpose of this book is to provide the prospective learners a self-taught material 
with executable notebooks. This book can be considered as practical code exercises when the 
(python) infrastructure is available. However, the [pdf version](https://python-seekho.readthedocs.io/_/downloads/en/latest/pdf/) 
of it can also be used as ebook. The book is more closely related to python section of [tutorialspoint.com](https://www.tutorialspoint.com/python/index.htm)
website. However, this book covers many topics which are not discussed there. More importantly, the code examples
here can be downloaded as either jupyter notebook or .py files. Therefore, the user can access the complete material
which is more helpful for practical purposes.

## Who should read this book
This book is intended for absolute beginners, those who have no knowledge of python.
A very little knowledge of programming can be helpful for the readers. The advanced
python users may find advanced topics within each chapter in this book useful.

## Installation
If you have internet connection, you have two options
    
- Download the ipython notebook of a lesson and upload it on any cloud servers such
      as [colab](https://colab.research.google.com/), [binder](https://mybinder.org/) or [studiolab](https://studiolab.sagemaker.aws/).
    
- click on launch binder button and start running the code, cell by cell.

For offline users; first install python, the libraries mentioned in requirements.txt
file and jupyter. Then the user can run any jupyter notebook which again can be downloaded
all at once from [website](https://python-seekho.readthedocs.io).

## How to read this book?
This book consists of jupyter notebooks. Each jupyter notebook consists of multiple cells.
Each cell consists of code snippets. The best way to get maximum out of this book is to
follow following two tips

1) Predict the output from a cell before running the cell, then run the cell and see whether
your prediction matches with the output of the cell or not!
   
2) Change the contents of the cell and predict the output and then run the cell and compare your
prediction with actual output.
   
3) Answer the questions in the lessons.

## Conventions
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
   

## Note
This is a living book which is currently being maintained actively on its GitHub repository.
You can expect improvement in the book with time.