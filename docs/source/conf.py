from os.path import abspath
from sys import path

path.insert(0, abspath("../.."))

project = "docmerge"
copyright = "2023, Marcos Bressan"
author = "Marcos Bressan"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "both",
    "style_external_links": True,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "white",
    # Toc options
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": -1,
    "includehidden": True,
    "titles_only": False,
}

# Napoleon settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# autosummary
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
# If no class summary, inherit base class summary
autodoc_inherit_docstrings = True
autodoc_typehints_format = "short"
autodoc_preserve_defaults = True
# Remove 'view source code' from top of page (for html, not python)
html_show_sourcelink = True