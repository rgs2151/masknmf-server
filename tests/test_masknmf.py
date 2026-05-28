"""Headless / CPU-only smoke tests."""

from __future__ import annotations

import warnings

import numpy as np
import pytest
import torch

import masknmf
from masknmf.utils import torch_select_device, cuda_empty_cache


# ---------------------------------------------------------------------------
# Device coercion
# ---------------------------------------------------------------------------


def test_torch_select_device_auto_returns_cpu():
    assert torch_select_device("auto").type == "cpu"


def test_torch_select_device_cpu_returns_cpu():
    assert torch_select_device("cpu").type == "cpu"


def test_torch_select_device_cuda_is_coerced_to_cpu():
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        dev = torch_select_device("cuda")
    assert dev.type == "cpu"
    assert any("CPU/headless" in str(w.message) for w in caught)


def test_torch_select_device_rejects_non_str():
    with pytest.raises(TypeError):
        torch_select_device(123)  # type: ignore[arg-type]


def test_cuda_empty_cache_is_safe_on_cpu_host():
    # Must not raise on a host without CUDA.
    cuda_empty_cache()


# ---------------------------------------------------------------------------
# Widget stubs preserve API, raise on use
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "name",
    [
        "PMDWidget",
        "signal_space_demixing",
        "stack_comparison_interface",
        "get_correlation_widget",
        "make_demixing_video",
        "visualize_superpixels_peaks",
        "quantile_segregated_signal_gui",
    ],
)
def test_widget_stub_raises(name):
    obj = getattr(masknmf, name)
    with pytest.raises(NotImplementedError, match="headless"):
        obj()


# ---------------------------------------------------------------------------
# Motion correction (CPU)
# ---------------------------------------------------------------------------


@pytest.fixture
def synthetic_movie():
    rng = np.random.default_rng(0)
    return (rng.random((4, 32, 32)) * 4096).astype(np.int16)


def test_rigid_motion_correction(synthetic_movie):
    rigid = masknmf.RigidMotionCorrector(max_shifts=(3, 3))
    rigid.compute_template(synthetic_movie)
    out = masknmf.RegistrationArray(synthetic_movie, rigid)[:]
    assert out.shape == synthetic_movie.shape


def test_motion_corrector_device_is_always_cpu():
    rigid = masknmf.RigidMotionCorrector(device="cuda")
    assert isinstance(rigid.device, torch.device)
    assert rigid.device.type == "cpu"
