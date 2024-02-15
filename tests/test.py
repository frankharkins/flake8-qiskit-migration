import ast
from textwrap import dedent

from flake8_qiskit_migration.plugin import Plugin


def _results(code: str):
    code = dedent(code)
    tree = ast.parse(code)
    plugin = Plugin(tree)
    return {f"{line}:{col} {msg}" for line, col, msg, _ in plugin.run()}


def test_trivial_case():
    assert _results("") == set()


def test_simple_import_path():
    code = """
    from qiskit import QuantumCircuit
    import qiskit.extensions
    import qiskit.extensions.item  # should raise error even though `.item` doesn't exist as whole path is deprecated
    import qiskit.quantum_info.synthesis.OneQubitEulerDecomposer
    import numpy
    """
    assert _results(code) == {
        "3:0 QKT100: qiskit.extensions has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
        "4:0 QKT100: qiskit.extensions.item has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
        "5:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    }


def test_simple_from_import_path():
    code = """
    from qiskit.quantum_info.synthesis import OneQubitEulerDecomposer
    from qiskit.quantum_info.synthesis import XXDecomposer as xxd
    from qiskit.quantum_info.synthesis import NonDeprecatedClass
    from qiskit.quantum_info.synthesis import OtherNonDeprecatedClass as XXDecomposer
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
        "3:0 QKT100: qiskit.quantum_info.synthesis.XXDecomposer has moved to `qiskit.synthesis.two_qubits.XXDecomposer`",
    }


def test_module_attribute_later_in_script():
    code = """
    import qiskit.quantum_info.synthesis
    xxd = qiskit.quantum_info.synthesis.XXDecomposer()
    qiskit.quantum_info.synthesis.OneQubitEulerDecomposer().run()
    allowed = qiskit.quantum_info.synthesis.AllowedPath
    """
    assert _results(code) == {
        "3:6 QKT100: qiskit.quantum_info.synthesis.XXDecomposer has moved to `qiskit.synthesis.two_qubits.XXDecomposer`",
        "4:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    }


def test_module_attribute_later_in_script_with_alias():
    code = """
    import qiskit as qk
    qk.extensions.thing()
    """
    assert _results(code) == {
        "3:0 QKT100: qiskit.extensions.thing has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    }


def test_alias_scope():
    code = """
    import safe_module as qk

    def my_function():
        import qiskit as qk
        return qk.extensions.thing()  # deprecated

    print(qk.extensions.thing())  # safe import
    """
    assert _results(code) == {
        "6:11 QKT100: qiskit.extensions.thing has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    }

    code = """
    import qiskit as qk

    def my_function():
        import safe_module as qk
        return qk.extensions.thing()  # safe

    print(qk.extensions.thing())  # deprecated
    """
    assert _results(code) == {
        "8:6 QKT100: qiskit.extensions.thing has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    }

def test_exceptions():
    code = """
    from qiskit.fake_provider.utils import json_decoder
    """
    assert _results(code) == set()

def test_basicaer():
    code = """
    from qiskit import BasicAer
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.BasicAer has been removed; either install separate `qiskit-aer` package and replace import with `qiskit_aer.Aer`, or follow https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#providers.basicaer"
    }

def test_providers():
    code = """
    from qiskit.providers.fake_provider import FakeCairo
    from qiskit.providers.fake_provider import GenericBackendV2
    from qiskit.providers.fake_provider import FakeBackend
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.providers.fake_provider.FakeCairo has moved; install separate `qiskit-ibm-runtime` package and replace `qiskit.providers.fake_provider` with `qiskit_ibm_runtime.fake_provider`"
    }
