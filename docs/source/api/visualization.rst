Visualisation (static)
======================

.. currentmodule:: masknmf

Static plotting helpers that emit HTML / PNG output and are safe to run on a
headless server.  Interactive widgets (e.g. :class:`PMDWidget`) are
preserved as stubs that raise :exc:`NotImplementedError` when constructed -
see :doc:`/headless` for details.

Plot helpers
------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    plot_ith_roi
    construct_index
    plot_pmd_vs_raw_stack_diagnostic
    generate_raw_vs_resid_plot_folder
    roi_compare_pmd_raw
    pmd_temporal_denoiser_trace_plot

Widget stubs (no-op in headless build)
--------------------------------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    PMDWidget
    signal_space_demixing
    stack_comparison_interface
    get_correlation_widget
    make_demixing_video
    visualize_superpixels_peaks
    quantile_segregated_signal_gui
