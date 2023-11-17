# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
# 
import os
import sys
import time

# autodoc required
sys.path.insert(0, os.path.abspath('../../easyclimate/src'))  # Source code dir relative to this file

# get year
localtime = time.localtime(time.time())
str_year = str(localtime[0])

project = 'Easy Climate'
copyright = str_year + ', shenyulu（深雨露）'
author = 'shenyulu'
release = 'v2023.11.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark', 
    'sphinx_markdown_tables', 
    'sphinx.ext.mathjax', 
    'sphinxcontrib.jupyter',
    # 'sphinx_tabs.tabs', 
    "sphinx_inline_tabs", # Add inline tabbed content to your Sphinx documentation

    # 'nbsphinx',  # 避免 ipynb, py, rst 重名识别错误
    'sphinx_gallery.gen_gallery', # Add inline tabbed content to your Sphinx documentation
    # 'sphinx_copybutton' # Add a convenient copy button to code blocks 目前有错误

    #  Sphinx autodoc 方法
    # 'sphinx.ext.autodoc',  # Core library for html generation from docstrings
    # 'sphinx.ext.autosummary',  # Create neat summary tables

    # Sphinx AutoAPI 方法
    'autoapi.extension',

    # 链接到其他项目的文档
    'sphinx.ext.intersphinx',
    # copy button
    'sphinx_copybutton',

    'sphinx.ext.githubpages',

]

templates_path = ['_templates']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'changes/*.rst']


# -- Options for AutoAPI extension -------------------------------------------
autoapi_type = 'python'
autoapi_dirs = ['../../easyclimate/src']
autoapi_add_toctree_entry = False
autoapi_root = 'technical/api'

# autodoc_typehints = 'description'
# autosummary_generate = True  # Turn on sphinx.ext.autosummary

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'furo'
html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

# Theme
html_theme_options = {
    "sidebar_hide_name": True,
    "top_of_page_button": "edit",
    "announcement": "🚨 This package is still undergoing rapid development. 🚨",
}

# Logo
html_logo = "_static/easyclimate-logo.svg"

# 添加编辑按钮
html_theme_options = {
    # furo
    # "source_repository": "https://github.com/shenyulu/easyclimate/",
    # "source_branch": "main",
    # "source_directory": "docs/",

    # book
    "repository_url": "https://github.com/shenyulu/easyclimate",
    "use_repository_button": True,
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
}

sphinx_gallery_conf = {
     'examples_dirs': './dynamic_docs',   # path to your example scripts
     'gallery_dirs': './auto_gallery_output',  # path to where to save gallery generated output
     'image_scrapers': ('matplotlib', ),
     'compress_images': ('images', 'thumbnails'),   # require install `optipng`, download from http://optipng.sourceforge.net/
     'line_numbers': False,  # 代码行号
     'promote_jupyter_magic': True,
     #  Controlling what output is captured
     'capture_repr': ('_repr_html_', '__repr__', '__str__'),

     'run_stale_examples': True,
     
     'min_reported_time': False,
     'download_all_examples': False,

    #  'show_memory': True,
     'show_signature': False,
}

# 链接文档
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_mapping
# https://pydoctor.readthedocs.io/en/latest/sphinx-integration.html
# e.g., https://docs.python.org/3/objects.inv
intersphinx_mapping = {'scipy': ('https://docs.scipy.org/doc/scipy/', None),
                       'numpy': ('https://numpy.org/doc/stable', None),
                       'xarray': ('https://docs.xarray.dev/en/stable', None),
                       'geocat-viz': ('https://geocat-viz.readthedocs.io/en/latest', None),
                       'geocat-comp': ('https://geocat-comp.readthedocs.io/en/latest/', None),
                       'dask': ('https://docs.dask.org/en/latest', None),
                       'python': ('https://docs.python.org/3', None),
                       'pandas': ('https://pandas.pydata.org/pandas-docs/stable', None),
                       'matplotlib': ('https://matplotlib.org/stable', None),
}