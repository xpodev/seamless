import sys

sys.path.insert(0, "..")
from seamless import __version__

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Seamless"
copyright = "2024, Xpo Development"
author = "Xpo Development"
version = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "pydata_sphinx_theme",
    "sphinx_substitution_extensions",
    "autoapi.extension",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "_templates", "Thumbs.db", ".DS_Store"]

autoapi_dirs = ["../seamless"]
autoapi_ignore = ["*/internal/*"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "special-members",
    "imported-members",
]
autoapi_root = "api-reference"
autoapi_keep_files = True
autoapi_generate_api_docs = True
autoapi_add_toctree_entry = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = "_static/images/favicon.ico"
html_logo = "_static/images/favicon.svg"
html_static_path = ["_static"]
html_theme = "pydata_sphinx_theme"
html_title = "Seamless Documentation"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/xpodev/seamless",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/python-seamless",
            "icon": "fa-brands fa-python",
        },
    ],
    "logo": {
        "alt_text": "Seamless",
        "text": "Seamless",
    },
}

html_css_files = [
    "css/custom.css",
]

rst_prolog = f"""
.. |version| replace:: {version}
.. |br| raw:: html

   <br />
"""
