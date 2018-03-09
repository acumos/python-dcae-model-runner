.. ===============LICENSE_START=======================================================
.. Acumos CC-BY-4.0
.. ===================================================================================
.. Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
.. ===================================================================================
.. This Acumos documentation file is distributed by AT&T and Tech Mahindra
.. under the Creative Commons Attribution 4.0 International License (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..      http://creativecommons.org/licenses/by/4.0
..
.. This file is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. ===============LICENSE_END=========================================================

========================
Acumos DCAE Model Runner
========================

The Acumos DCAE model runner enables Acumos models to be run as if they were
DCAE components.

Each Acumos model method is mapped to a subscriber and publisher stream,
with ``_subscriber`` and ``_publisher`` suffixes respectively. For example,
a model with a ``transform`` method would have ``transform_subscriber`` and
``transform_publisher`` streams.

The model runner implements DCAE APIs such as health checks and configuration
updates.

The ``acumos_dcae_model_runner`` Python package provides a command line utility
that can be used to instantiate the model runner. See the tutorial for more information.

The ``acumos_dcae_model_runner`` package should be installed in the docker image
that is ultimately on-boarded into DCAE. The model runner CLI utility should be
the entry point of that Docker image, as shown in the Dockerfile provided
in ``example/`` directory in the root of the repository.

Installation
============

The ``acumos_dcae_model_runner`` package can be installed with pip like so:

.. code:: bash

    pip install acumos_dcae_model_runner --process-dependency-links

**Note:** The ``--process-dependency-links`` flag is **required**
because the required ``dcaeapplib`` dependency is not yet hosted on
PyPI.

If you'd prefer, you can maintain a local directory of Python packages containing
``dcaeapplib``, and use the ``--find-links`` option:

.. code:: bash

    pip install acumos_dcae_model_runner --find-links path/to/pkgs/
