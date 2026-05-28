# Quickstart

## Install

This build runs CPU-only. Any PyTorch wheel works; we recommend the
CPU-only wheels for a smaller footprint.

```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install git+https://github.com/apasarkar/masknmf-toolbox.git@main
```

For an editable dev checkout:

```bash
git clone https://github.com/apasarkar/masknmf-toolbox.git
cd masknmf-toolbox
pip install -e ".[dev]"
```

## Two-photon calcium pipeline

```python
import masknmf

pipeline = masknmf.TwoPhotonCalciumPipeline(
    motion_correct_config=masknmf.PiecewiseRigidMotionCorrectionConfig(),
    compress_config=masknmf.CompressConfig(),
    demixing_config=masknmf.MultipassDemixingConfig(),
    device="auto",   # silently coerced to "cpu" in this build
)

data = masknmf.TiffArray("recording.tif")
results = pipeline.run(data)
```

The pipeline writes intermediate stacks (motion-corrected, compressed) to
HDF5 files alongside the final demixing result so each stage is checkpointed
and individually inspectable.

## Component-by-component

If you'd rather drive the pipeline by hand:

```python
import masknmf

raw = masknmf.TiffArray("recording.tif")

# 1. motion correction
moco = masknmf.PiecewiseRigidMotionCorrector(batch_size=200, device="cpu")
moco.compute_template(raw)
moco_arr = masknmf.RegistrationArray(raw, strategy=moco)

# 2. compression (PMD)
compressor = masknmf.CompressStrategy(
    block_sizes=(32, 32),
    max_components=20,
    frame_batch_size=2000,
    device="cpu",
)
pmd = compressor.compress(moco_arr)

# 3. signal demixing
demixer = masknmf.SignalDemixer(pmd, device="cpu")
demixer.initialize_signals()
demixer.lock_results_and_continue()
demixer.demix()
results = demixer.results
```

## Output

`results` is a {class}`masknmf.DemixingResults` carrying everything you need:

| Attribute | Shape | Description |
|-----------|-------|-------------|
| `results.a` | sparse `(d1*d2, K)` | spatial footprints |
| `results.c` | dense `(T, K)` | temporal traces |
| `results.b` | dense `(d1*d2,)` | static baseline |
| `results.pmd_array` | `(T, d1, d2)` | denoised stack |
| `results.residual_array` | `(T, d1, d2)` | post-fit residual |

Persist with `results.save("out.hdf5")` and load back with the matching
loader on a different machine — no GUI required.

## What got removed?

See [Headless build notes](headless.md) for the full diff between this build
and the upstream interactive build.
