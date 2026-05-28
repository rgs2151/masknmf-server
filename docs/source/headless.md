# Headless / CPU-only build

This page documents what was changed when stripping the GPU and widget
dependencies out of upstream `masknmf-toolbox`.

## What was removed

| Dependency | Reason for removal |
|------------|--------------------|
| `fastplotlib`, `pygfx`, `wgpu`, `glfw` | GPU-backed interactive plotting; require a display server and OpenGL/Vulkan drivers. |
| `imgui_bundle` | Immediate-mode GUI bound to `fastplotlib`. |
| `ipywidgets` | Jupyter-only; not useful on a headless worker. |
| `simplejpeg` | Pulled in by `fastplotlib[imgui,notebook]`. |
| `jupyterlab` | Editor stack — not a runtime dependency. |
| CUDA runtime (via PyTorch CUDA build) | Optional in this build — install the CPU-only `torch` wheel. |

## What was kept

* **All core processing**: motion correction, PMD compression, temporal
  denoiser training, signal demixing.
* **All pipelines**: `TwoPhotonCalciumPipeline`, `WidefieldSinglechannelPipeline`.
* **All static plotting helpers**: `plot_ith_roi`, `pmd_temporal_denoiser_trace_plot`,
  etc. — these use `matplotlib` (forced to `Agg` backend) and `plotly` and
  emit HTML / image files instead of opening windows.
* **The public API surface**, including the widget names. Widget classes are
  preserved as stubs that raise {exc}`NotImplementedError` when *called* so
  importing them never crashes, but invoking them tells the user the build
  has no GUI.

## `device=` parameters

Every public entry point that accepts `device="auto" | "cuda" | "cpu"` still
accepts those strings. `"cuda"` (and any `torch.device("cuda...")` object) is
coerced to `torch.device("cpu")` by {func}`masknmf.utils.torch_select_device`,
which emits a single user warning the first time it happens. Existing scripts
keep working unchanged.

```python
from masknmf.utils import torch_select_device

torch_select_device("auto")  # -> device(type='cpu')
torch_select_device("cuda")  # -> device(type='cpu') + UserWarning (once)
torch_select_device("cpu")   # -> device(type='cpu')
```

## Calls to `torch.cuda.empty_cache()`

All call sites are now guarded by `if torch.cuda.is_available()` so they
become no-ops on a CPU host instead of raising.

## Training the temporal denoiser

`train_total_variance_denoiser` previously used Lightning with
`accelerator="gpu"` and `precision="16-mixed"`. The CPU build switches to
`accelerator="cpu"` and `precision="32-true"` since mixed-precision is a
GPU-only feature.

## Running tests

The full test suite assumes the GPU build. On the headless build, skip the
visualisation / interactive tests:

```bash
pytest tests -k "not widget and not interactive"
```
