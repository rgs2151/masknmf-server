masknmf
=======

**A CPU / headless-server build of the maskNMF pipeline for functional
neuroimaging data.**

``masknmf`` takes raw imaging data in, runs motion correction → compression /
denoising → signal demixing, and gives you neuron-level traces and footprints
back out. This build has been stripped of all GUI / GPU dependencies
(``fastplotlib``, ``imgui``, ``glfw``, ``pygfx``, ``wgpu``) so it runs on any
CPU-only Linux box - bare-metal server, Docker container, batch worker.

.. grid:: 1 2 2 2
    :gutter: 3

    .. grid-item-card:: Quickstart
        :link: quickstart
        :link-type: doc

        Install, point at a TIFF/HDF5 dataset, and run the two-photon pipeline.

    .. grid-item-card:: Pipelines
        :link: api/pipelines
        :link-type: doc

        High-level end-to-end pipelines: ``TwoPhotonCalciumPipeline``,
        ``WidefieldSinglechannelPipeline``.

    .. grid-item-card:: API Reference
        :link: api/index
        :link-type: doc

        Full reference for every public class & function in ``masknmf``.

    .. grid-item-card:: Headless vs. GUI build
        :link: headless
        :link-type: doc

        What was removed in this build and what to use instead.

.. toctree::
    :hidden:
    :maxdepth: 1
    :caption: Get started

    quickstart
    headless

.. toctree::
    :hidden:
    :maxdepth: 2
    :caption: Reference

    api/index


Why a headless build?
---------------------

The upstream ``masknmf-toolbox`` ships with a heavy interactive visualisation
stack designed for Jupyter notebooks with a GPU. That stack pulls in
``fastplotlib``, ``imgui_bundle``, ``pygfx``, ``glfw``, ``ipywidgets``,
``simplejpeg``, ``jupyterlab`` - none of which install or run on a typical
production server. This build cuts those dependencies out, coerces every
``device="cuda"`` request to ``device="cpu"``, and keeps the same public API
so existing scripts continue to work.

The result: ``params in → results out`` on any machine that has Python and a
few hundred MB of RAM. No display, no GPU, no extra system packages.

Getting help
------------

Open an issue at https://github.com/apasarkar/masknmf-toolbox/issues.

If you use this method, please cite the accompanying `paper
<https://www.biorxiv.org/content/10.1101/2023.09.14.557777v1>`_:

    *maskNMF: A denoise-sparsen-detect approach for extracting neural
    signals from dense imaging data.* (2023). A. Pasarkar, I. Kinsella,
    P. Zhou, M. Wu, D. Pan, J.L. Fan, Z. Wang, L. Abdeladim, D.S. Peterka,
    H. Adesnik, N. Ji, L. Paninski.

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
