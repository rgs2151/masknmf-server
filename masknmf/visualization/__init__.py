"""
Visualisation helpers for ``masknmf``.

This module is *headless-safe*: it forces the ``matplotlib`` backend to
``Agg`` on import so it can be used on a CPU-only server without a display.
The interactive widget API (``PMDWidget``, ``signal_space_demixing``,
``stack_comparison_interface``, ...) is preserved as stubs that raise a
descriptive :class:`NotImplementedError` if invoked - see
:mod:`masknmf.visualization.interactive_guis` for details.
"""

from __future__ import annotations

import os

# Force a non-interactive matplotlib backend before anything else imports it.
os.environ.setdefault("MPLBACKEND", "Agg")
import matplotlib  # noqa: E402  (must come after env var)

matplotlib.use("Agg", force=False)

from .interactive_guis import (  # noqa: E402
    PMDWidget,
    signal_space_demixing,
    stack_comparison_interface,
    get_correlation_widget,
    make_demixing_video,
    visualize_superpixels_peaks,
    quantile_segregated_signal_gui,
)
from .plots import (  # noqa: E402
    construct_index,
    plot_ith_roi,
    plot_pmd_vs_raw_stack_diagnostic,
    generate_raw_vs_resid_plot_folder,
    roi_compare_pmd_raw,
    pmd_temporal_denoiser_trace_plot,
)

__all__ = [
    "construct_index",
    "plot_ith_roi",
    "plot_pmd_vs_raw_stack_diagnostic",
    "generate_raw_vs_resid_plot_folder",
    "roi_compare_pmd_raw",
    "pmd_temporal_denoiser_trace_plot",
    "PMDWidget",
    "signal_space_demixing",
    "stack_comparison_interface",
    "get_correlation_widget",
    "make_demixing_video",
    "visualize_superpixels_peaks",
    "quantile_segregated_signal_gui",
]
