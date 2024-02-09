# flake8-qiskit-migration

Flake8 plugin to detect deprecated imports deprecated in Qiskit 1.0

> [!WARNING]  
> This tool only detects deprecated import paths, it does not detect use of
> deprecated methods (such as `QuantumCircuit.qasm`) or deprecated arguments.

This tool is not perfect, it will produce some false positives (that is,
claiming you're using a deprecated import path when you're not).

## Install

You might want to do this using [`pipx`](https://github.com/pypa/pipx) or in a
separate virtual environment.

```sh
pip install flake8
pip install git+https://github.com/frankharkins/flake8-qiskit-migration
```

## Run

To run only the deprecation detection plugin (`QKT100`), use the `--select`
argument.

```sh
flake8 --select QKT100 <path-to-source>
```
