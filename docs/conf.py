# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Scaleway SDK Python'
copyright = '2025, Scaleway'
author = 'Scaleway'
release = '2.7.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys

sys.path.insert(0, os.path.abspath('../scaleway'))
sys.path.insert(0, os.path.abspath('../scaleway-async'))
sys.path.insert(0, os.path.abspath('../scaleway-core'))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

autoapi_dirs = [
    os.path.abspath('../scaleway'),
    # os.path.abspath('../scaleway-async'),
    # os.path.abspath('../scaleway-core'),
]

autoapi_generate_api_docs = True


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**/marshalling*']

autodoc_default_options = {
    "show-inheritance": True,
    "members": True,
    "undoc-members": False,
}

source_suffix = ".rst"

master_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']


