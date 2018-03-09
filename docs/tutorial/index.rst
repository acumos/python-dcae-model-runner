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

========
Tutorial
========

CLI Usage
=========

To execute the model runner, use the provided CLI:

.. code:: bash

    $ acumos_dcae_model_runner --help
    usage: acumos_dcae_model_runner [-h] [--timeout TIMEOUT] [--debug] model_dir

    positional arguments:
      model_dir          Directory that contains either the dumped model.zip or
                         its unzipped contents.

    optional arguments:
      -h, --help         show this help message and exit
      --timeout TIMEOUT  Timeout (ms) used when fetching.
      --debug            Sets the log level to DEBUG

DCAE Onboarding Example
=======================

The ``python-dcae-model-runner`` repository has an ``example/`` directory
that shows how an Acumos model can be onboarded as a DCAE component.

After executing the steps below, the directory should have this
structure:

.. code:: bash

    example/
    ├── Dockerfile
    ├── dcae-artifacts
    │   ├── component.json
    │   ├── number-out.json
    │   └── numbers-in.json
    ├── example-model
    │   ├── metadata.json
    │   ├── model.proto
    │   └── model.zip
    ├── example_model.py
    └── requirements.txt

**Note:** For this example, the ``requirements.txt`` file should reflect the
packages and versions listed in ``example-model/metadata.json``.

Steps
-----

1) Create the Acumos model
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``example_model.py`` script defines a simple Acumos model that can
add two integers together. The following will generate
``example-model/``:

.. code:: bash

    python example_model.py

2) Build the docker image
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    docker build -t acumos-python-model-test:0.1.0 .

3) Onboard the Acumos model to DCAE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The onboarding procedure involves adding the component and data format
artifacts provided in ``example/dcae-artifacts`` to the DCAE catalog.

Refer to the official DCAE onboarding documentation for the full
procedure.
