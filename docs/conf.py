
import sys
import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

CURDIR = os.path.abspath(os.path.dirname(__file__))

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
    'sphinx_search.extension',
    'hoverxref.extension',
    'sphinxemoji.sphinxemoji',
    'sphinxcontrib.contentui',
    'sphinxcontrib.httpdomain',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx_search.extension',
    'sphinx_tabs.tabs',
    ]

# -- hoverxref.extension configuration ----------------------
hoverxref_auto_ref = True
hoverxref_domains = ["py"]
hoverxref_roles = [
    "option",
    # Documentation pages
    # Not supported yet: https://github.com/readthedocs/sphinx-hoverxref/issues/18
    "doc",
    # Glossary terms
    "term",
]
hoverxref_role_types = {
    "mod": "modal",  # for Python Sphinx Domain
    "doc": "modal",  # for whole docs
    "class": "tooltip",  # for Python Sphinx Domain
    "ref": "tooltip",  # for hoverxref_auto_ref config
    "confval": "tooltip",  # for custom object
    "term": "tooltip",  # for glossaries
}

# -- sphinxemoji configuration -------------------------------
sphinxemoji_style = 'twemoji'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = {
   '.rst': 'restructuredtext',
   '.txt': 'markdown',
    '.md': 'markdown',
}

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# Project information. Label goes into left nav title block
project = 'Stripe Systems'
copyright = '2023, Ontomatica'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the built documents.
# The short X.Y version.
version = '0.1'

# The full version, including alpha/beta/rc tags.
release = 'a'

# Turns on numbered figures for HTML output
number_figures = True

# There are two options for replacing |today|: either, you set today to some non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%d %B %Y'


# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    '_link-gn-10.rst',
]

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

# make rst_epilog a variable, so you can add other epilog parts to it
rst_epilog =""

# Read link all targets from file
with open('_link-gn-10.rst') as f:
     rst_epilog += f.read()

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages. See the documentation for a list of built-in themes.
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a theme further.
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
# Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,
    'body_max_width': 'none'
}

# The name for this set of Sphinx documents. Appears in browser tab.
# If None, it defaults to "<project> v<release> documentation".
html_title = "project"

# A shorter title for the navigation bar. Default is the same as html_title.
html_short_title = 'Stripe'

# The name of an image file (relative to this directory) to place at the top of the sidebar.
#html_logo = 'Ontomatica.png'

# The name of an image file (within the static path) to use as favicon of the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
html_favicon = "_images/onto-shortcut-w252-h252-color-ffffff-bgnd-1f64ff.svg"

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
# They are copied after the built-in static files, so a file named "default.css" will overwrite the built-in "default.css".

html_static_path = [
    '_content',
    '_images',
    '_static',
]

# These paths are either relative to html_static_path or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
    'css/lightbox.css',
]

html_js_files = [
    'https://cdn.ampproject.org/v0.js',
    'https://cdn.ampproject.org/v0/amp-bind-0.1.js',
    'https://cdn.ampproject.org/v0/amp-form-0.1.js',
    'https://cdn.ampproject.org/v0/amp-image-lightbox-0.1.js',
    'https://cdn.ampproject.org/v0/amp-list-0.1.js',
    'https://cdn.ampproject.org/v0/amp-lightbox-gallery-0.1.js',
    'https://cdn.ampproject.org/v0/amp-mustache-0.2.js',
    'https://cdn.ampproject.org/v0/amp-selector-0.1.js',
]

# If not '', a 'Last updated on:' time-stamp is inserted at every page bottom, using the given strftime format.
html_last_updated_fmt = '%d %b %Y'

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright Ontomatica" is shown in the HTML footer. Default is True.
html_show_copyright = False


html_file_suffix = '.html'
html_search_language = 'en'
htmlhelp_basename = 'stripe'
html_use_smartypants = False
html_add_permalinks = '¶'
html_secnumber_suffix = '. '
html_context = {}
html_copy_source = False
