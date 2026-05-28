Signal demixing
===============

.. currentmodule:: masknmf

Signal initialisation, NMF-style demixing, and the resulting per-neuron
spatial / temporal factor arrays.

Demixer & state machine
-----------------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    SignalDemixer
    InitializingState
    DemixingState

Results
-------

.. autosummary::
    :toctree: generated
    :nosignatures:

    DemixingResults
    InitializationResults

Lazy arrays carrying demixed signals
------------------------------------

.. autosummary::
    :toctree: generated
    :nosignatures:

    ACArray
    ColorfulACArray
    StandardCorrelationImages
    ResidualCorrelationImages
    ResidCorrMode
    FluctuatingBackgroundArray
    ResidualArray
