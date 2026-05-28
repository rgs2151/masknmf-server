# masknmf

CPU / headless build of the **maskNMF** pipeline for functional neuroimaging
data (calcium, voltage, glutamate). Params in &rarr; results out. No GPU, no
display server, no Jupyter widgets.

| | |
|---|---|
| **Source** | https://github.com/apasarkar/masknmf-toolbox |
| **Docs**   | https://apasarkar.github.io/masknmf-toolbox/ |
| **Paper**  | https://www.biorxiv.org/content/10.1101/2023.09.14.557777v1 |

## What this build is

A stripped, server-friendly fork of `masknmf-toolbox` that keeps the full
processing API (`TwoPhotonCalciumPipeline`, `WidefieldSinglechannelPipeline`,
`RigidMotionCorrector`, `PMDArray`, `SignalDemixer`, ...) and drops every
dependency that needs a GPU or a display:

- removed: `fastplotlib`, `pygfx`, `wgpu`, `glfw`, `imgui_bundle`,
  `ipywidgets`, `simplejpeg`, `jupyterlab`
- coerced: every `device="cuda"` / `torch.device("cuda")` to CPU at the
  device-selector boundary (one-shot warning, no crash)
- guarded: `torch.cuda.empty_cache()` behind `torch.cuda.is_available()`
- forced: `matplotlib` backend to `Agg` so static plots work headless

## Install

```bash
# CPU-only PyTorch (smaller, no CUDA runtime)
pip install torch --index-url https://download.pytorch.org/whl/cpu

# masknmf itself
pip install git+https://github.com/apasarkar/masknmf-toolbox.git@main
```

Editable dev install:

```bash
git clone https://github.com/apasarkar/masknmf-toolbox.git
cd masknmf-toolbox
pip install -e ".[dev]"
pytest tests
```

Supported Python: **3.11 – 3.13**.

## Quickstart

```python
import masknmf

pipeline = masknmf.TwoPhotonCalciumPipeline(
    motion_correct_config=masknmf.PiecewiseRigidMotionCorrectionConfig(),
    compress_config=masknmf.CompressConfig(),
    demixing_config=masknmf.MultipassDemixingConfig(),
)

data = masknmf.TiffArray("recording.tif")     # or Hdf5Array("...")
results = pipeline.run(data)

results.a   # sparse (d1*d2, K) spatial footprints
results.c   # dense  (T, K)     temporal traces
results.b   # dense  (d1*d2,)   pixel baselines
```

See the [quickstart](https://apasarkar.github.io/masknmf-toolbox/quickstart.html)
in the docs for the step-by-step (motion correction &rarr; PMD &rarr; demix)
flow.

## Data formats

Built-in loaders:

- multipage TIFF &mdash; `masknmf.TiffArray`
- HDF5 &mdash; `masknmf.Hdf5Array`

To plug in your own format, implement
[`masknmf.LazyFrameLoader`](https://apasarkar.github.io/masknmf-toolbox/api/generated/masknmf.LazyFrameLoader.html).

## Citing

> _maskNMF: A denoise-sparsen-detect approach for extracting neural signals
> from dense imaging data._ (2023). A. Pasarkar\*, I. Kinsella, P. Zhou, M. Wu,
> D. Pan, J.L. Fan, Z. Wang, L. Abdeladim, D.S. Peterka, H. Adesnik, N. Ji,
> L. Paninski.

## License

GPLv3 &mdash; see [LICENSE](./LICENSE).
