Compression & denoising
=======================

.. currentmodule:: masknmf

Penalised Matrix Decomposition (PMD) compression of the motion-corrected
stack, plus optional temporal denoising.

Strategies
----------

.. autosummary::
    :toctree: generated
    :nosignatures:

    CompressStrategy
    CompressDenoiseStrategy

Free functions
--------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    pmd_decomposition
    train_total_variance_denoiser

PMD result arrays
-----------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    PMDArray
    PMDResidualArray

Denoisers
---------

.. autosummary::
    :toctree: generated
    :nosignatures:

    PMDTemporalDenoiser
