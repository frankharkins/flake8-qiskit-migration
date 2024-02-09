import ast
from dataclasses import dataclass
import importlib.metadata


DEPRECATED = {
    #  Dict of the form
    #   "deprecated.path": "How to fix",
    # algorithms
    "qiskit.algorithms": "; install the separate `qiskit-algorithms` package and replace with `qiskit_algorithms`",
    # converters
    "qiskit.converters.ast_to_dag": "; see <link-to-guide>",
    # opflow
    "qiskit.opflow": "; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-opflow-module",
    # providers
    "qiskit.Aer": "; install separate `qiskit-aer` package and replace import with `qiskit_aer`",
    "qiskit.providers.aer": "; install separate `qiskit-aer` package and replace import with `qiskit_aer`",
    "qiskit.providers.basicaer": "; see <link-to-guide>",
    "qiskit.providers.fake_provider": "; install separate `qiskit-ibm-runtime` and replace with `qiskit_ibm_runtime.fake_provider`",
    "qiskit.providers.fake_provider.FakeQasmBackend": "; replace with `qiskit_ibm_runtime.fake_provider.fake_qasm_backend.FakeQasmBackend`",
    "qiskit.providers.fake_provider.FakePulseBackend": "; qiskit_ibm_runtime.fake_provider.fake_pulse_backend.FakePulseBackend",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendV2": "; replace with `qiskit.providers.fake_providerGenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendV2LegacyQubitProps": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackend5QV2": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendSimple": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.ConfigurableFakeBackend": "; migrate to `qiskit.providers.fake_provider.GenericBackendV2`",
    # pulse
    "qiskit.pulse.library.parametric_pulses.ParametricPulse": "; migrate to `qiskit.pulse.SymbolicPulse`",
    "qiskit.pulse.library.parametric_pulses.Constant": "; migrate to `qiskit.pulse.SymbolicPulse`",
    "qiskit.pulse.library.parametric_pulses.Drag": "; migrate to `qiskit.pulse.SymbolicPulse`",
    "qiskit.pulse.library.parametric_pulses.Gaussian": "; migrate to `qiskit.pulse.SymbolicPulse`",
    "qiskit.pulse.library.parametric_pulses.GaussianSquare": "; migrate to `qiskit.pulse.SymbolicPulse`",
    "qiskit.pulse.builder.call_gate": "; see <link-to-guide>",
    "qiskit.pulse.builder.cx": "; see <link-to-guide>",
    "qiskit.pulse.builder.u1": "; see <link-to-guide>",
    "qiskit.pulse.builder.u2": "; see <link-to-guide>",
    "qiskit.pulse.builder.u3": "; see <link-to-guide>",
    "qiskit.pulse.builder.x": "; see <link-to-guide>",
    "qiskit.pulse.builder.build.default_transpiler_settings": " with no replacement",
    "qiskit.pulse.builder.build.default_circuit_scheduler_settings": " with no replacement",
    "qiskit.pulse.builder.active_transpiler_settings": " with no replacement",
    "qiskit.pulse.builder.active_circuit_scheduler_settings": " with no replacement",
    "qiskit.pulse.builder.transpiler_settings": " with no replacement",
    "qiskit.pulse.builder.circuit_scheduler_settings": " with no replacement",
    "qiskit.pulse.library.constant": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.zero": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.square": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.sawtooth": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.triangle": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.cos": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.sin": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.gaussian": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.gaussian_deriv": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.sech": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.sech_deriv": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.gaussian_square": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    "qiskit.pulse.library.drag": "; use the corresponding `qiskit.pulse.SymbolicPulse` and its `get_waveform()` method",
    # transpiler
    "qiskit.transpiler.synthesis.aqc": "; replace with `qiskit.synthesis.unitary.aqc`",
    "qiskit.synthesis.unitary.aqc.AQCSynthesisPlugin": "; replace with `qiskit.transpiler.passes.synthesis.AQCSynthesisPlugin`",
    "qiskit.transpiler.synthesis.graysynth": "; replace with `qiskit.synthesis.synth_cnot_phase_aam`",
    "qiskit.transpiler.synthesis.cnot_synth": "; replace with`qiskit.synthesis.synth_cnot_count_full_pmh`",
    "qiskit.transpiler.passes.NoiseAdaptiveLayout": "; migrate to `qiskit.transpiler.passes.VF2PostLayout`",
    "qiskit.transpiler.passes.CrosstalkAdaptiveSchedule": "; ",
    "qiskit.transpiler.passes.Unroller": "; migrate to `qiskit.transpiler.passes.BasisTranslator`",
    # execute
    "qiskit.execute": "; explicitly transpile and run the circuit instead (see <link-to-guide>)",
    "qiskit.execute_function.execute": "; explicitly transpile and run the circuit instead (see <link-to-guide>)",
    # extensions
    "qiskit.extensions": "; most objects have been moved to `qiskit.circuit.library` (see <link-to-guide>)",
    # quantum_info.synthesis
    "qiskit.quantum_info.synthesis.OneQubitEulerDecomposer": "; replace with `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    "qiskit.quantum_info.synthesis.TwoQubitBasisDecomposer": "; replace with `qiskit.synthesis.two_qubits.TwoQubitBasisDecomposer`",
    "qiskit.quantum_info.synthesis.XXDecomposer": "; replace with `qiskit.synthesis.two_qubits.XXDecomposer`",
    "qiskit.quantum_info.synthesis.two_qubit_cnot_decompose": "; replace with `qiskit.synthesis.two_qubits.two_qubit_cnot_decompose`",
    "qiskit.quantum_info.synthesis.Quaternion": "; replace with `qiskit.quantum_info.Quaternion`",
    "qiskit.quantum_info.synthesis.cnot_rxx_decompose": " with no replacement",
    # qasm
    "qiskit.qasm": "; use qiskit.qasm2 instead (see <link-to-guide>)",
    # tools
    "qiskit.tools": "; replace with `qiskit.utils`",
    "qiskit.tools.jupyter": "; see separate `qiskit-ibm-provider` package for similar functionality",
    "qiskit.tools.monitor": "; see separate `qiskit-ibm-provider` package for similar functionality",
    "qiskit.tools.visualization": "; replace with `qiskit.visualization`",
    "qiskit.tools.events": "; use a dedicated package such as `tqdm`",
    # test
    "qiskit.test": "; if necessary, consider copying the code into your own test infrastructure",
    # utils
    "qiskit.utils.arithmetic": " with no replacement",
    "qiskit.utils.circuit_utils`": " with no replacement",
    "qiskit.utils.entangler_map`": " with no replacement",
    "qiskit.utils.name_unnamed_args`": " with no replacement",
    "qiskit.utils.QuantumInstance": "; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-quantum-instance",
    "qiskit.utils.backend_utils": " with no replacement",
    "qiskit.utils.mitigation": " with no replacement",
    "qiskit.utils.measurement_error_mitigation": " with no replacement",
    # visualization
    "qiskit.visualization.qcstyle": "; replace with `qiskit.visualization.circuit.qcstyle`",
    # other
    "qiskit.__qiskit_version__": "; migrate to `qiskit.__version__`",
}

EXCEPTIONS = [
    "qiskit.providers.fake_provider.utils",
    "qiskit.providers.fake_provider.fake_backend.FakeBackend",
]


def deprecation_message(path: str) -> str | None:
    """
    Build deprecation message from `DEPRECATED` dict.

    Args:
        path (str): Python import path of the form `qiskit.extensions.thing`

    Returns:
        str: Deprecation message if path is deprecated
        None: If no deprecations detected
    """
    if "." not in path:
        return None
    if path in EXCEPTIONS:
        return None
    if path not in DEPRECATED:
        parent = ".".join(path.split(".")[:-1])
        return deprecation_message(parent)
    return f"QKT100: {path} is deprecated" + DEPRECATED[path]


class Visitor(ast.NodeVisitor):
    """
    Simple visitor to detect deprecated imports. Includes some support for
    aliases and scopes, but not assignments.
    """

    def __init__(self):
        self.problems: list[Problem] = []
        self.mappings: list[dict[str, str]] = [{}]  # track aliases for each scope

    def enter_scope(self) -> None:
        """Add new mapping for scoped aliases"""
        self.mappings.append({})

    def exit_scope(self) -> None:
        """Delete scoped aliases"""
        self.mappings.pop()

    def add_alias(self, alias: ast.alias) -> None:
        if alias.asname is None or alias.asname == alias.name:
            return
        self.mappings[-1][alias.asname] = alias.name

    def resolve_aliases(self, name: str) -> str:
        for mapping in reversed(self.mappings):
            name = mapping.get(name, name)
        return name

    def report_if_deprecated(self, path: str, node) -> None:
        """
        Adds path to problems if deprecated, ignores otherwise
        """
        msg = deprecation_message(path)
        if msg is not None:
            self.problems.append(Problem(node, msg))

    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.add_alias(alias)
            self.report_if_deprecated(alias.name, node)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        for alias in node.names:
            self.add_alias(alias)
            path = f"{node.module}.{alias.name}"
            self.report_if_deprecated(path, node)
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute) -> None:
        def _get_parents(node):
            if isinstance(node, ast.Name):
                return node.id
            if isinstance(node, ast.Attribute):
                parents = _get_parents(node.value)
                parents = self.resolve_aliases(parents)
                return f"{parents}.{node.attr}"

        path = _get_parents(node)
        self.report_if_deprecated(path, node)
        self.generic_visit(node)

    # Push / pop scopes for aliases
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.enter_scope()
        self.generic_visit(node)
        self.exit_scope()

    def visit_AsyncFunctionDef(self, node: ast.FunctionDef):
        self.enter_scope()
        self.generic_visit(node)
        self.exit_scope()

    def visit_ClassDef(self, node: ast.FunctionDef):
        self.enter_scope()
        self.generic_visit(node)
        self.exit_scope()


class Plugin:
    name = __name__
    version = importlib.metadata.version(__name__)

    def __init__(self, tree: ast.AST):
        self._tree = tree

    def run(self):
        """
        Yields:
            int: Line number of problem
            int: Character number of problem
            str: Message for user
           Type: (unused)
        """
        v = Visitor()
        v.visit(self._tree)
        for problem in v.problems:
            yield problem.format()


@dataclass
class Problem:
    def __init__(self, node, msg):
        self.node = node
        self.msg = msg

    def format(self):
        return (self.node.lineno, self.node.col_offset, self.msg, None)
