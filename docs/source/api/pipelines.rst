Pipelines
=========

.. currentmodule:: masknmf

End-to-end pipelines wrap motion correction → compression → demixing into a
single ``run(data)`` call.  All pipelines accept the same ``device=`` string
as the underlying strategies; ``"cuda"`` is coerced to ``"cpu"`` in this
build.

High-level pipelines
--------------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    TwoPhotonCalciumPipeline
    WidefieldSinglechannelPipeline

Configuration objects
---------------------

Per-stage configs are plain dataclasses; pass them to the pipeline
constructor to override defaults.

.. autosummary::
    :toctree: generated
    :nosignatures:

    RigidMotionCorrectionConfig
    PiecewiseRigidMotionCorrectionConfig
    CompressConfig
    CompressDenoiseConfig
    SuperpixelInitConfig
    CustomInitConfig
    NMFConfig
    SinglepassDemixingConfig
    MultipassDemixingConfig
    SpatialHighpassConfig
