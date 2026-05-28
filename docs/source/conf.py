"""
Sphinx configuration for the CPU/headless masknmf build.

This config intentionally avoids importing fastplotlib / pygfx / glfw so the
docs can be built on any CPU-only CI runner (e.g. GitHub Actions
``ubuntu-latest``).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# Force matplotlib into a non-interactive backend; some autodoc traversals
# transitively import visualisation helpers.
os.environ.setdefault("MPLBACKEND", "Agg")

ROOT_DIR = Path(__file__).parents[2].resolve()  # repo root
sys.path.insert(0, str(ROOT_DIR))

import masknmf  # noqa: E402

# -- Project information -----------------------------------------------------
project = "masknmf"
copyright = "2025, Amol Pasarkar"
author = "Amol Pasarkar"
release = masknmf.__version__
version = release

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "sphinx_design",
    "myst_parser",
]

autosummary_generate = True
autosummary_ignore_module_all = False

# Skip importing optional / heavy modules at build time so the docs job
# stays CPU-only.  These objects are documented as best-effort by their
# docstrings only.
autodoc_mock_imports = [
    "fastplotlib",
    "pygfx",
    "imgui_bundle",
    "ipywidgets",
    "glfw",
    "simplejpeg",
    "wgpu",
]

templates_path = ["_templates"]
exclude_patterns: list[str] = []

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- HTML output -------------------------------------------------------------
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_title = f"masknmf v{release}"

html_theme_options = {
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/apasarkar/masknmf-toolbox",
            "icon": "fa-brands fa-github",
        },
    ],
    "show_prev_next": True,
    "use_edit_page_button": False,
    "collapse_navigation": False,
    "navigation_depth": 3,
}

html_context = {
    "default_mode": "auto",
}

# -- Autodoc -----------------------------------------------------------------
autodoc_member_order = "groupwise"
autoclass_content = "both"
add_module_names = False

autodoc_typehints = "description"
autodoc_typehints_description_target = "documented_params"
autodoc_preserve_defaults = True

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False

# -- Intersphinx -------------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "torch": ("https://docs.pytorch.org/docs/stable/", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
}

# -- MyST --------------------------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "tasklist",
]

# -- Suppress noisy warnings from autosummary for stub widget objects --------
suppress_warnings = ["autosummary.import_cycle"]
