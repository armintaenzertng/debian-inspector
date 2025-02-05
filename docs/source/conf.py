# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.

import pathlib
import sys

srcdir = pathlib.Path(__file__).resolve().parents[2].joinpath('src')
sys.path.insert(0, srcdir.as_posix())


# -- Project information -----------------------------------------------------

project = "debian_inspector"
copyright = "nexB Inc. and others."
author = "AboutCode.org authors and contributors"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinxcontrib.apidoc",
]

# Setting for sphinxcontrib.apidoc to automatically create API documentation.
apidoc_module_dir = srcdir.joinpath('debian_inspector').as_posix()
apidoc_separate_modules=True
apidoc_module_first = True

# Reference to other Sphinx documentations
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

master_doc = "index"

html_context = {
    "display_github": True,
    "github_user": "nexB",
    "github_repo": "debian-inspector",
    "github_version": "main",  # branch
    "conf_py_path": "/docs/source/",  # path in the checkout to the docs root
}

html_css_files = ["_static/theme_overrides.css"]


# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# Define CSS and HTML abbreviations used in .rst files.  These are examples.
# .. role:: is used to refer to styles defined in _static/theme_overrides.css and is used like this: :red:`text`
rst_prolog = """
.. |psf| replace:: Python Software Foundation

.. # define a hard line break for HTML
.. |br| raw:: html

   <br />

.. role:: red

.. role:: img-title

.. role:: img-title-para

"""
