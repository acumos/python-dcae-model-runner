# Contributing Guidelines

## Testing
We use a combination of `tox`, `pytest`, and `flake8` to test `acumos`. Code which is not PEP8 compliant (aside from E501) will be considered a failing test. You can use tools like `autopep8` to "clean" your code as follows:

```
$ pip install autopep8
$ cd python-dcae-model-runner
$ autopep8 -r --in-place --ignore E501 acumos_dcae_model_runner/
```

Run tox directly:

```
$ cd python-dcae-model-runner
$ export WORKSPACE=$(pwd)  # env var normally provided by Jenkins
$ tox
```

You can also specify certain tox environments to test:

```
$ tox -e py34  # only test against Python 3.4
$ tox -e flake8  # only lint code
```
