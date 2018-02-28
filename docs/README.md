# python-dcae-model-runner

The `acumos_dcae_model_runner` package should be installed in the Docker image that is ultimately on-boarded into DCAE. The CLI utility should be the entry point of that Docker image.

# Installation

The `acumos_dcae_model_runner` package must be installed via source until there is appropriate package hosting infrastructure in place:

```bash
pip install python-dcae-model-runner/ --process-dependency-links
```

**Note:** The `--process-dependency-links` flag is **required** because the required `dcaeapplib` dependency is not yet hosted on PyPI.