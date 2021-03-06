# -*- coding: utf-8 -*-
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os, time, codecs, re

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('.'))

import podgen.version

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.4'

# Don't show warnings about the button images not being local
#suppress_warnings = ['image.nonlocal_uri']  # requires Sphinx >= 1.4

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
        'sphinx.ext.intersphinx',
        'sphinx.ext.coverage',
        'sphinx.ext.autodoc',
        'sphinx.ext.autosummary',
        'sphinx.ext.viewcode',
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'PodGen'
copyright = u'2014, Lars Kiesow. Modified work © 2016, Thorben Dahl'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = podgen.version.version_minor_str
# The full version, including alpha/beta/rc tags.
release = podgen.version.version_full_str

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

#html_style = 'lernfunk.css'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'fixed_sidebar': False,
    'page_width': "1000px",
    'sidebar_width': "225px",
    'body_text': "rgba(0, 0, 0, 0.8)",
    'footer_text': "rgba(0, 0, 0, 0.5)",
    'gray_1': "rgba(0, 0, 0, 0.9)",
    'gray_2': "rgba(0, 0, 0, 0.2)",
    'gray_3': "rgba(198, 198, 198, 0.9)",

    'github_user': 'tobinus',
    'github_repo': 'python-podgen',
    'github_banner': True,
    'logo_name': False,
    'logo': 'logo.png',
}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "PodGen Documentation"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "PodGen"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = '_static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'index': [
        'about.html',
        'navigation.html',
        'searchbox.html',
        'donate.html',
    ],
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
        'donate.html',
    ]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyPodGen'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'pyPodGen.tex', u'PodGen Documentation',
        u'Lars Kiesow and Thorben Dahl', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
latex_show_urls = "true"

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = False


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'pyPodGen.tex', u'PodGen Documentation',
        [u'Lars Kiesow', u'Thorben Dahl'], 1)
]

# If true, show URL addresses after external links.
man_show_urls = True


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'pyPodGen.tex', u'PodGen Documentation',
        u'Lars Kiesow, Thorben Dahl', 'Lernfunk3', 'One line description of project.',
        'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
                       'requests': ('http://docs.python-requests.org/en/master', None)}


# Ugly way of setting tabsize
import re

def process_docstring(app, what, name, obj, options, lines):
    '''
    spaces_pat = re.compile(r"(?<=        )( {8})")
    ll = []
    for l in lines:
        ll.append(spaces_pat.sub("   ",l))
    '''
    spaces_pat = re.compile(r"^ *")
    ll = []
    for l in lines:
        spacelen = len(spaces_pat.search(l).group(0))
        newlen = int((spacelen % 8) + (spacelen / 8 * 4))
        ll.append( (' '*newlen) + l.lstrip(' ') )
    lines[:] = ll


# Include the GitHub readme file in index.rst
r = re.compile(r'\[`*([^\]`]+)`*\]\(([^\)]+)\)')
r2 = re.compile(r'.. include-github-readme')
def substitute_link(app, docname, text):
    if docname == 'index':
        readme_text = ''
        with codecs.open(os.path.abspath('../readme.md'), 'r', 'utf-8') as f:
            readme_text = r.sub(r'`\1 <\2>`_', f.read())
        text[0] = r2.sub(readme_text, text[0])


def setup(app):
    app.connect('autodoc-process-docstring', process_docstring)
    app.connect('source-read', substitute_link)
