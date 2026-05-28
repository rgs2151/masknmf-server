Motion correction
=================

.. currentmodule:: masknmf

Motion-correction strategies and the lazy registration array that applies
them on the fly when frames are requested.

Strategies
----------

.. autosummary::
    :toctree: generated
    :nosignatures:

    MotionCorrectionStrategy
    DummyMotionCorrector
    RigidMotionCorrector
    PiecewiseRigidMotionCorrector
    GradientMotionCorrector

Lazy arrays
-----------

.. autosummary::
    :toctree: generated
    :nosignatures:

    RegistrationArray
    FilteredArray
