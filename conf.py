# -*- coding: utf-8 -*-
#
import os
import sys
try:
    import sphinx_rtd_theme
except Exception as err:
    print "Building without template."

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'D2Moddin'
copyright = u'2014, D2Modd.in'
version = '1.0'
release = '1.0'
exclude_patterns = ['_build']
default_role = 'obj'
pygments_style = 'sphinx'
# This doesn't exist since we aren't shipping any static files ourselves.
#html_static_path = ['_static']
htmlhelp_basename = 'D2Moddindoc'
latex_documents = [
    ('index', 'D2Moddin.tex', u'D2Moddin Documentation',
     u'Christian Stewart', 'manual'),
]
man_pages = [
    ('index', 'd2moddin', u'D2Moddin Documentation',
     [u'Christian Stewart'], 1)
]

exclude_patterns = [
    #'api' # needed for ``make gettext`` to not die.
]

language = 'en'

locale_dirs = [
    'locale/',
]
gettext_compact = False
