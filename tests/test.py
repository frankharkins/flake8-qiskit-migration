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
        "3:0 QKT100: qiskit.extensions is deprecated; most objects have been moved to `qiskit.circuit.library` (see <link-to-guide>)",
        "4:0 QKT100: qiskit.extensions is deprecated; most objects have been moved to `qiskit.circuit.library` (see <link-to-guide>)",
        "5:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer is deprecated; replace with `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    }


def test_simple_from_import_path():
    code = """
    from qiskit.quantum_info.synthesis import OneQubitEulerDecomposer
    from qiskit.quantum_info.synthesis import XXDecomposer as xxd
    from qiskit.quantum_info.synthesis import NonDeprecatedClass
    from qiskit.quantum_info.synthesis import OtherNonDeprecatedClass as XXDecomposer
    """
    assert _results(code) == {
        "2:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer is deprecated; replace with `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
        "3:0 QKT100: qiskit.quantum_info.synthesis.XXDecomposer is deprecated; replace with `qiskit.synthesis.two_qubits.XXDecomposer`",
    }


def test_module_attribute_later_in_script():
    code = """
    import qiskit.quantum_info.synthesis
    xxd = qiskit.quantum_info.synthesis.XXDecomposer()
    qiskit.quantum_info.synthesis.OneQubitEulerDecomposer().run()
    allowed = qiskit.quantum_info.synthesis.AllowedPath
    """
    assert _results(code) == {
        "3:6 QKT100: qiskit.quantum_info.synthesis.XXDecomposer is deprecated; replace with `qiskit.synthesis.two_qubits.XXDecomposer`",
        "4:0 QKT100: qiskit.quantum_info.synthesis.OneQubitEulerDecomposer is deprecated; replace with `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    }


def test_module_attribute_later_in_script_with_alias():
    code = """
    import qiskit as qk
    qk.extensions.thing()
    """
    assert _results(code) == {
        "3:0 QKT100: qiskit.extensions is deprecated; most objects have been moved to `qiskit.circuit.library` (see <link-to-guide>)",
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
        "6:11 QKT100: qiskit.extensions is deprecated; most objects have been moved to `qiskit.circuit.library` (see <link-to-guide>)",
    }

def test_exceptions():
    code = """
    from qiskit.fake_provider.utils import json_decoder
    """
    assert _results(code) == set()
