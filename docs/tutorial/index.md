# Tutorial

## CLI Usage

To execute the model runner, use the provided CLI:

```bash
$ acumos_dcae_model_runner --help
usage: acumos_dcae_model_runner [-h] [--timeout TIMEOUT] model_dir

positional arguments:
  model_dir          Directory that contains either the dumped model.zip or
                     its unzipped contents.

optional arguments:
  -h, --help         show this help message and exit
  --timeout TIMEOUT  Timeout (ms) used when fetching
```

## DCAE Onboarding Example

The `python-dcae-model-runner/example` directory contains an example of how an Acumos model can be onboarded as a DCAE component.

After executing the steps below, the directory should have this structure:

```bash
python-dcae-model-runner/example
├── Dockerfile
├── dcae-artifacts
│   ├── component.json
│   ├── number-out.json
│   └── numbers-in.json
├── dcae-helpers
│   ├── dcae-cli-commands.txt
│   └── dmaap-file.json
├── example-model
│   ├── metadata.json
│   ├── model.proto
│   └── model.zip
├── example_model.py
├── message_router_test.py
├── packages
│   ├── acumos-0.5.0.tar.gz
│   └── acumos_dcae_model_runner-0.1.0.tar.gz
└── requirements.txt
```

**Note:** The `packages/` directory contains source distributions of the `acumos` and `acumos_dcae_model_runner` packages. These are required to create the Docker image, as they are not resolvable on PyPI. They are not included in this repository.

## Steps

###1) Create the Acumos model

The `example_model.py` script defines a simple Acumos model that can add two integers together. The following will generate `example-model/`:

```bash
python example_model.py
```

###2) Build the docker image 

```bash
docker build -t acumos-python-model-test:0.1.0 .
```

###3) Onboard the Acumos model to DCAE

The onboarding procedure involves adding the component and data format artifacts provided in `example/dcae-artifacts` to the DCAE catalog.

Refer to the [DCAE onboarding documentation](http://dcae-platform.research.att.com/) for the full procedure.

