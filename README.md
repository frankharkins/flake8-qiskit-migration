# flake8-qiskit-migration

Flake8 plugin to detect deprecated imports deprecated in Qiskit 1.0

## Install

```sh
pip install flake8
pip install git+https://github.com/frankharkins/flake8-qiskit-migration
```

## Run

To run only the deprecation detection plugin (`QKT100`), use the `--select` argument.

```sh
flake8 --select QKT100 <path-to-source>
```
