"""
Interactive widget surface for ``masknmf``.

The CPU/headless build of ``masknmf`` ships **without** the heavy interactive
visualisation stack (``fastplotlib``, ``imgui_bundle``, ``pygfx``,
``ipywidgets``, ``glfw``).  These dependencies require a GPU and a display
server and are unsuitable for a headless processing pipeline.

To keep the public import surface stable, the widget entry points are
re-exposed here as lazy stubs that raise :class:`NotImplementedError` with a
clear message the moment they are *called* (importing them is fine).  Users
that need the GUIs should install the upstream
``masknmf-toolbox`` distribution which keeps the optional ``[viz]`` extras.
"""

from __future__ import annotations

_REASON = (
    "Interactive GUI widgets are not available in the CPU/headless build of "
    "masknmf. This build intentionally drops fastplotlib / imgui / glfw / "
    "ipywidgets so it can run on a headless CPU-only server. Install the "
    "full masknmf-toolbox distribution if you need interactive widgets."
)


class _HeadlessWidget:
    """Placeholder that mimics a widget class but cannot be instantiated."""

    def __init__(self, *args, **kwargs):
        raise NotImplementedError(_REASON)


def _headless_callable(name: str):
    def _stub(*args, **kwargs):
        raise NotImplementedError(f"{name}: {_REASON}")

    _stub.__name__ = name
    _stub.__qualname__ = name
    return _stub


class PMDWidget(_HeadlessWidget):
    """Stub for the PMD diagnostic widget (unavailable in the headless build)."""


signal_space_demixing = _headless_callable("signal_space_demixing")
stack_comparison_interface = _headless_callable("stack_comparison_interface")
get_correlation_widget = _headless_callable("get_correlation_widget")
make_demixing_video = _headless_callable("make_demixing_video")
visualize_superpixels_peaks = _headless_callable("visualize_superpixels_peaks")
quantile_segregated_signal_gui = _headless_callable("quantile_segregated_signal_gui")


__all__ = [
    "PMDWidget",
    "signal_space_demixing",
    "stack_comparison_interface",
    "get_correlation_widget",
    "make_demixing_video",
    "visualize_superpixels_peaks",
    "quantile_segregated_signal_gui",
]
