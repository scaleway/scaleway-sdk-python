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
import re

# sys.path.insert(0, os.path.abspath('../scaleway'))
# sys.path.insert(0, os.path.abspath('../scaleway-async'))
# sys.path.insert(0, os.path.abspath('../scaleway-core'))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "autoapi.extension"
]

templates_path = ["_templates"]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

autoapi_type = "python"
autoapi_dirs = [
    os.path.abspath('../scaleway'),
    os.path.abspath('../scaleway-async'),
    os.path.abspath('../scaleway-core'),
]
autoapi_template_dir = "_templates/autoapi"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]
autoapi_generate_api_docs = True

def contains(seq, item):
    """Jinja2 custom test to check existence in a container.

    Example of use:
    {% set class_methods = methods|selectattr("properties", "contains", "classmethod") %}

    Related doc: https://jinja.palletsprojects.com/en/3.1.x/api/#custom-tests
    """
    return item in seq


def prepare_jinja_env(jinja_env) -> None:
    """Add `contains` custom test to Jinja environment."""
    jinja_env.tests["contains"] = contains


autoapi_prepare_jinja_env = prepare_jinja_env

# Custom role for labels used in auto_summary() tables.
rst_prolog = """
.. role:: summarylabel
"""


# autodoc_default_options = {
#     "show-inheritance": True,
#     "members": True,
#     "undoc-members": False,
# }



def skip_submodules(app, what, name, obj, skip, options):
    if re.search("marshal*", name) or re.search("unmarshal*", name) or re.search("test*", name) or re.search("utils", name):
        print("value of name: ", name, " obj: ", obj, "what: ", what)
        skip = True
    return skip


def setup(sphinx):
    sphinx.connect("autoapi-skip-member", skip_submodules)


