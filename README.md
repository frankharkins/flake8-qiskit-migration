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

## With Python venv

Create a new environment for the linter, run it, and delete the environment
when you're finished.

```sh
# Make new environment and install
python -m venv .flake8-qiskit-migration-venv
source .flake8-qiskit-migration-venv/bin/activate
pip install flake8-qiskit-migration

# Run plugin on Python code
flake8 --select QKT100 <path-to-source>  # e.g. `src/`

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
