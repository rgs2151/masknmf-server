Arrays & data loaders
=====================

.. currentmodule:: masknmf

Lazy / memory-mapped array interfaces.  All pipeline stages accept either a
plain :class:`numpy.ndarray` (frames, height, width) or any object that
implements the :class:`LazyFrameLoader` protocol below.

Data loaders
------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    TiffArray
    Hdf5Array

Protocols & base types
----------------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    LazyFrameLoader
    FactorizedVideo
    ArrayLike
