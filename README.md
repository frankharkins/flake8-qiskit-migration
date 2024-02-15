# flake8-qiskit-migration

Flake8 plugin to detect imports deprecated in Qiskit 1.0

> [!WARNING]
> This tool only detects deprecated import paths, it does not detect use of
> deprecated methods (such as `QuantumCircuit.qasm`), deprecated arguments, or
> assignments such as `qk = qiskit` (although it can handle _aliases_ such as
> `import qiskit as qk`).

This tool is to help you quickly identify deprecated imports and work out how
to fix them. This tool is not perfect and will make some mistakes, so make sure
to test your project thoroughly after migrating.

## Through pipx

We recommend using this plugin through [`pipx`](https://github.com/pypa/pipx).
If you have `pipx` installed, simply run:

```sh
pipx run flake8-qiskit-migration <path-to-source>
```

This will install this plugin in a temporary environment and run it. If you're
at the root of your Python project, then `<path-to-source>` is `./`.

## With Python venv

If you don't want to use `pipx`, you can manually create a new environment for
the linter. This approach also lets you use
[`nbqa`](https://github.com/nbQA-dev/nbQA) to check Jupyter notebooks. Delete
the environment when you're finished.

```sh
# Make new environment and install
python -m venv .flake8-qiskit-migration-venv
source .flake8-qiskit-migration-venv/bin/activate
pip install flake8-qiskit-migration

# Run plugin on Python code
flake8 --select QKT100 <path-to-source>  # e.g. `src/`

# Run plugin on notebooks
pip install nbqa
nbqa flake8 ./**/*.ipynb --select QKT100

# Deactivate and delete environment
deactivate
rm -r .flake8-qiskit-migration-venv
```

## With existing flake8

If you already have `flake8` installed and want run this plugin that way, 
To run only the deprecation detection plugin (`QKT100`), use the `--select`
argument. You'll probably want to uninstall it when you're done.

```sh
# Install plugin
pip install flake8-qiskit-migration

# Run all flake8 checks (including this plugin)
flake8 <path-to-source>

# Run only this plugin
flake8 --select QKT100 <path-to-source>

# Uninstall plugin
pip uninstall flake8-qiskit-migration
```
