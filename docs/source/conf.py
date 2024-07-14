# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
from sphinx_gallery.sorting import ExampleTitleSortKey, ExplicitOrder
import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'phthon-seekho'
copyright = '2024, Ather Abbas'
author = 'Ather Abbas'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.todo',
'sphinx.ext.viewcode',
'sphinx.ext.autodoc',
'sphinx.ext.autosummary',
'sphinx.ext.doctest',
'sphinx.ext.intersphinx',
'sphinx.ext.imgconverter',
'sphinx_issues',
'sphinx.ext.mathjax',
'sphinx.ext.napoleon',
'sphinx.ext.githubpages',
'sphinx_toggleprompt',
'sphinx_copybutton',
"sphinx-prompt",
"sphinx_gallery.gen_gallery",
'sphinx.ext.ifconfig',
"sphinx_thebe"
]

# specify the master doc, otherwise the build at read the docs fails
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# intersphinx configuration
intersphinx_mapping = {
    'python': ('https://docs.python.org/{.major}'.format(
        sys.version_info), None),
    'numpy': ('https://docs.scipy.org/doc/numpy/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None),
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
}

class ExampleTitleSortKeyWithNumber(ExampleTitleSortKey):
    """Sort examples in src_dir by example title considering that the title
    starts with a number followed by space
    """

    def __call__(self, filename):
        """extract the title and convert numbers before "." ("dot) to integer
        1.1 FirstTitle  -> 11
        """
        title = super().__call__(filename)
        number = title.split(' ')[0]
        return int(number.replace('.', ''))


examples_dirs = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'scripts')

sphinx_gallery_conf = {
    'backreferences_dir': 'gen_modules/backreferences',
    # 'doc_module': ('sphinx_gallery', 'numpy'),
    'reference_url': {
        'sphinx_gallery': None,
    },
    'examples_dirs': os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'scripts'),
    'gallery_dirs': 'auto_examples',
    'compress_images': ('images', 'thumbnails'),
    # 'subsection_order': SubSectionTitleOrder(examples_dirs),
    'filename_pattern': '',
    # 'line_numbers': False,

    'binder': {'org': 'AtrCheema',
               'repo': 'python-seekho',
               'branch': 'master',
               'binderhub_url': 'https://mybinder.org',
               'dependencies': os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.binder', 'requirements.txt'),
               'notebooks_dir': 'notebooks',
               'use_jupyter_lab': True,
               },
    # 'show_memory': True,
    # 'junit': os.path.join('sphinx-gallery', 'junit-results.xml'),
    # capture raw HTML or, if not present, __repr__ of last expression in
    # each code block
    'capture_repr': ('_repr_html_', '__repr__'),
    'matplotlib_animations': True,
    'image_srcset': ["2x"],

    'within_subsection_order': ExampleTitleSortKeyWithNumber,
    # 'examples_dirs': ['../scripts', '../tutorials'],
    'subsection_order': ExplicitOrder(['../../scripts/basics',
                                       '../../scripts/builtin_modules',
                                       '../../scripts/oop',
                                       '../../scripts/numpy',
                                       '../../scripts/pandas',
                                       '../../scripts/plotting',
                                       '../../scripts/advanced',
                                       ]),
    # 'expected_failing_examples': ['../scripts/oop/descriptors.py']
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_logo = "logo.jpg"
html_favicon = "logo.jpg"

html_theme_options = {
    "repository_url": "https://github.com/AtrCheema/python-seekho",
    # add a link to your repository
    "use_repository_button": True,
    # To convert your footnotes to instead be sidenotes/marginnotes
    "use_sidenotes": False,
    "use_download_button": True,
    # add a button to open an issue about the current page
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'docs'),
    "repository_branch": "master",
    #  add the landing page of your site to the table of contents
    "home_page_in_toc": True,
    # remove the site title below the logo
    "logo_only": True,
    "launch_buttons": {
        "thebe": True,
        "notebook_interface": "jupyterlab",
        "colab_url": "https://colab.research.google.com",
    }
}

thebe_config = {
   "always_load": True,
   "repository_url": "<https://github.com/AtrCheema/python-seekho>",
   "repository_branch": "<master>",
}

html_title = "python-seekho"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
