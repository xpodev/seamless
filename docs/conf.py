import importlib.util
import pathlib, importlib

HERE = pathlib.Path(__file__).parent

# Import the package to get the version
spec = importlib.util.spec_from_file_location(
    "seamless", str(HERE.parent / "seamless" / "version.py")
)
seamless = importlib.util.module_from_spec(spec)
spec.loader.exec_module(seamless)

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Seamless"
copyright = "2024, Xpo Development"
author = "Xpo Development"
version = seamless.version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_rtd_theme",
    "sphinx_substitution_extensions",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_favicon = "favicon.ico"
html_title = "Seamless Documentation"

rst_prolog = f"""
.. |version| replace:: {version}
.. |br| raw:: html

   <br />
"""