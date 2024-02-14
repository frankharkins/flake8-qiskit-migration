# Dictionaries of the form
#  "deprecated.path": "How to fix",

ALGORITHMS = {
    "qiskit.algorithms": "; install the separate `qiskit-algorithms` package and replace with `qiskit_algorithms`",
}

CONVERTERS = {
    "qiskit.converters.ast_to_dag": "; see <link-to-guide>",
}

OPFLOW = {
    "qiskit.opflow": "; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-opflow-module",
}

PROVIDERS = {
    "qiskit.Aer": "; install separate `qiskit-aer` package and replace import with `qiskit_aer`",
    "qiskit.providers.aer": "; install separate `qiskit-aer` package and replace import with `qiskit_aer`",
    "qiskit.providers.basicaer": "; see <link-to-guide>",
    "qiskit.BasicAer": "; either install separate `qiskit-aer` package and replace import with `qiskit_aer.Aer`, or follow <link-to-guide>",
    "qiskit.providers.fake_provider": " (with some exceptions); install separate `qiskit-ibm-runtime` and replace with `qiskit_ibm_runtime.fake_provider`",
    "qiskit.providers.fake_provider.backends": "; install separate `qiskit-ibm-runtime` and replace with `qiskit_ibm_runtime.fake_provider`",
    "qiskit.providers.fake_provider.FakeQasmBackend": "; replace with `qiskit_ibm_runtime.fake_provider.fake_qasm_backend.FakeQasmBackend`",
    "qiskit.providers.fake_provider.FakePulseBackend": "; qiskit_ibm_runtime.fake_provider.fake_pulse_backend.FakePulseBackend",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendV2": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendV2LegacyQubitProps": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackend5QV2": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendSimple": "; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.ConfigurableFakeBackend": "; migrate to `qiskit.providers.fake_provider.GenericBackendV2`",
}

PULSE = {
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
    "qiskit.pulse.call_gate": "; see <link-to-guide>",
    "qiskit.pulse.cx": "; see <link-to-guide>",
    "qiskit.pulse.u1": "; see <link-to-guide>",
    "qiskit.pulse.u2": "; see <link-to-guide>",
    "qiskit.pulse.u3": "; see <link-to-guide>",
    "qiskit.pulse.x": "; see <link-to-guide>",
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
}

TRANSPILER = {
    "qiskit.transpiler.synthesis.aqc": "; replace with `qiskit.synthesis.unitary.aqc`",
    "qiskit.synthesis.unitary.aqc.AQCSynthesisPlugin": "; replace with `qiskit.transpiler.passes.synthesis.AQCSynthesisPlugin`",
    "qiskit.transpiler.synthesis.graysynth": "; replace with `qiskit.synthesis.synth_cnot_phase_aam`",
    "qiskit.transpiler.synthesis.cnot_synth": "; replace with`qiskit.synthesis.synth_cnot_count_full_pmh`",
    "qiskit.transpiler.passes.NoiseAdaptiveLayout": "; migrate to `qiskit.transpiler.passes.VF2PostLayout`",
    "qiskit.transpiler.passes.CrosstalkAdaptiveSchedule": "; ",
    "qiskit.transpiler.passes.Unroller": "; migrate to `qiskit.transpiler.passes.BasisTranslator`",
}

EXECUTE = {
    "qiskit.execute": "; explicitly transpile and run the circuit instead (see <link-to-guide>)",
    "qiskit.execute_function.execute": "; explicitly transpile and run the circuit instead (see <link-to-guide>)",
}

EXTENSIONS = {
    "qiskit.extensions": "; most objects have been moved to `qiskit.circuit.library` (see <link-to-guide>)",
}

QUANTUM_INFO = {
    "qiskit.quantum_info.synthesis.OneQubitEulerDecomposer": "; replace with `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    "qiskit.quantum_info.synthesis.TwoQubitBasisDecomposer": "; replace with `qiskit.synthesis.two_qubits.TwoQubitBasisDecomposer`",
    "qiskit.quantum_info.synthesis.XXDecomposer": "; replace with `qiskit.synthesis.two_qubits.XXDecomposer`",
    "qiskit.quantum_info.synthesis.two_qubit_cnot_decompose": "; replace with `qiskit.synthesis.two_qubits.two_qubit_cnot_decompose`",
    "qiskit.quantum_info.synthesis.Quaternion": "; replace with `qiskit.quantum_info.Quaternion`",
    "qiskit.quantum_info.synthesis.cnot_rxx_decompose": " with no replacement",
}

QASM = {
    "qiskit.qasm": "; use qiskit.qasm2 instead (see <link-to-guide>)",
}

TOOLS = {
    "qiskit.tools": "; replace with `qiskit.utils`",
    "qiskit.tools.jupyter": "; see separate `qiskit-ibm-provider` package for similar functionality",
    "qiskit.tools.monitor": "; see separate `qiskit-ibm-provider` package for similar functionality",
    "qiskit.tools.visualization": "; replace with `qiskit.visualization`",
    "qiskit.tools.events": "; use a dedicated package such as `tqdm`",
}

TEST = {
    "qiskit.test": "; if necessary, consider copying the code into your own test infrastructure",
}

UTILS = {
    "qiskit.utils.arithmetic": " with no replacement",
    "qiskit.utils.circuit_utils`": " with no replacement",
    "qiskit.utils.entangler_map`": " with no replacement",
    "qiskit.utils.name_unnamed_args`": " with no replacement",
    "qiskit.utils.QuantumInstance": "; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-quantum-instance",
    "qiskit.utils.backend_utils": " with no replacement",
    "qiskit.utils.mitigation": " with no replacement",
    "qiskit.utils.measurement_error_mitigation": " with no replacement",
}

VISUALIZATION = {
    "qiskit.visualization.qcstyle": "; replace with `qiskit.visualization.circuit.qcstyle`",
}

OTHER = {
    "qiskit.__qiskit_version__": "; migrate to `qiskit.__version__`",
}

EXCEPTIONS = [
    "qiskit.providers.fake_provider.utils",
    "qiskit.providers.fake_provider.GenericBackendV2",
    "qiskit.providers.fake_provider.FakeOpenPulse2Q",
    "qiskit.providers.fake_provider.FakeBackend",
]

DEPRECATED_PATHS = (
    ALGORITHMS
    | CONVERTERS
    | OPFLOW
    | PROVIDERS
    | PULSE
    | TRANSPILER
    | EXECUTE
    | EXTENSIONS
    | QUANTUM_INFO
    | QASM
    | TOOLS
    | TEST
    | UTILS
    | VISUALIZATION
    | OTHER
)
