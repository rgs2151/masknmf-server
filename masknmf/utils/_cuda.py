"""
Device selection for the CPU/headless build of ``masknmf``.

The original implementation auto-detected CUDA and warned if it was absent.
In this build all computations run on CPU.  The function is kept so the
public API (``device="auto" | "cuda" | "cpu"``) continues to work for callers
- a ``"cuda"`` request is silently coerced to ``"cpu"`` with a one-shot
warning so users running old scripts on a CPU-only host don't crash.
"""

from __future__ import annotations

from warnings import warn

import torch

_CUDA_WARNING_EMITTED = False


def torch_select_device(
    device: str | torch.device = "auto",
    log_warning: bool = True,
) -> torch.device:
    """
    Resolve a device spec to a :class:`torch.device`.

    Args:
        device: ``"auto"``, ``"cpu"``, ``"cuda"`` (legacy, coerced to CPU), or
            an explicit :class:`torch.device`.
        log_warning: When ``True`` (default), emit a one-shot warning if the
            caller requested ``"cuda"`` on a build that no longer supports it.

    Returns:
        Always a CPU ``torch.device`` in this build.
    """
    global _CUDA_WARNING_EMITTED

    if isinstance(device, torch.device):
        if device.type != "cpu" and log_warning and not _CUDA_WARNING_EMITTED:
            warn(
                "masknmf is running in CPU/headless mode; the requested "
                f"device {device!r} is being coerced to 'cpu'.",
                stacklevel=2,
            )
            _CUDA_WARNING_EMITTED = True
        return torch.device("cpu")

    if not isinstance(device, str):
        raise TypeError(
            f"device must be a str or torch.device, got {type(device).__name__}"
        )

    if device.startswith("cuda") and log_warning and not _CUDA_WARNING_EMITTED:
        warn(
            "masknmf is running in CPU/headless mode; 'cuda' is coerced to "
            "'cpu'. Install the full GPU build of masknmf-toolbox to use a "
            "GPU.",
            stacklevel=2,
        )
        _CUDA_WARNING_EMITTED = True

    return torch.device("cpu")


def cuda_empty_cache() -> None:
    """No-op replacement for ``torch.cuda.empty_cache()`` (CPU-only build)."""
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
