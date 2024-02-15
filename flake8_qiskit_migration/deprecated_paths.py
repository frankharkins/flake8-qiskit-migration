### This file contains all the deprecated paths for the linter to catch.
### Dictionaries are in the form:
###     "qiskit.path": "{} advice to user"
### where `{}` will be replaced with the matched path.
###
### Each path matches all sub-paths, for example `qiskit.thing` will match
### `qiskit.thing.otherthing` in the user's code, unless
### `qiskit.thing.otherthing` appears in EXCEPTIONS.

ALGORITHMS = {
    "qiskit.algorithms": "{} has moved; install the separate `qiskit-algorithms` package and replace `qiskit.algorithms` with `qiskit_algorithms`",
}

CONVERTERS = {
    "qiskit.converters.ast_to_dag": "{} has been removed; load QASM directly to a QuantumCircuit instead  (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
}

OPFLOW = {
    "qiskit.opflow": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-opflow-module",
}

PROVIDERS = {
    "qiskit.Aer": "{} has moved; install separate `qiskit-aer` package and replace `qiskit.Aer` with `qiskit_aer.Aer`",
    "qiskit.BasicAer": "{} has been removed; either install separate `qiskit-aer` package and replace import with `qiskit_aer.Aer`, or follow https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#providers.basicaer",
    "qiskit.providers.aer": "{} has been removed; install separate `qiskit-aer` package and replace `qiskit.aer` with `qiskit_aer`",
    "qiskit.providers.basicaer": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features",
    "qiskit.providers.fake_provider": "{} has moved; install separate `qiskit-ibm-runtime` package and replace `qiskit.providers.fake_provider` with `qiskit_ibm_runtime.fake_provider`",
    "qiskit.providers.fake_provider.FakeQasmBackend": "{} has moved; replace with `qiskit_ibm_runtime.fake_provider.fake_qasm_backend.FakeQasmBackend`",
    "qiskit.providers.fake_provider.FakePulseBackend": "{} has moved; replace with qiskit_ibm_runtime.fake_provider.fake_pulse_backend.FakePulseBackend",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendV2": "{} has moved; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendV2LegacyQubitProps": "{} has moved; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackend5QV2": "{} has moved; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.FakeBackendSimple": "{} has moved; replace with `qiskit.providers.fake_provider.GenericBackendV2`",
    "qiskit.providers.fake_provider.fake_backend_v2.ConfigurableFakeBackend": "{} has moved; migrate to `qiskit.providers.fake_provider.GenericBackendV2`",
}

PULSE = {
    "qiskit.pulse.library.parametric_pulses.ParametricPulse": "{} has been removed; use alternative `qiskit.pulse.SymbolicPulse`",
    "qiskit.pulse.library.parametric_pulses.Constant": "{} has been removed; use alternative `qiskit.pulse.symbolic_pulses.Constant`",
    "qiskit.pulse.library.parametric_pulses.Drag": "{} has been removed; use alternative `qiskit.pulse.symbolic_pulses.Drag`",
    "qiskit.pulse.library.parametric_pulses.Gaussian": "{} has been removed; use alternative `qiskit.pulse.symbolic_pulses.Gaussian`",
    "qiskit.pulse.library.parametric_pulses.GaussianSquare": "{} has been removed; use alternative `qiskit.pulse.symbolic_pulses.GaussianSquare`",
    "qiskit.pulse.builder.call_gate": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features",
    "qiskit.pulse.builder.cx": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.builder.u1": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.builder.u2": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.builder.u3": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.builder.x": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.call_gate": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.cx": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.u1": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.u2": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.u3": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.x": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#injecting-circuit-gate-operations",
    "qiskit.pulse.builder.build.default_transpiler_settings": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#builder.build",
    "qiskit.pulse.builder.build.default_circuit_scheduler_settings": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#builder.build",
    "qiskit.pulse.builder.active_transpiler_settings": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#builder.build",
    "qiskit.pulse.builder.active_circuit_scheduler_settings": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#builder.build",
    "qiskit.pulse.builder.transpiler_settings": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#builder.build",
    "qiskit.pulse.builder.circuit_scheduler_settings": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#builder.build",
    "qiskit.pulse.library.constant": "{} has been removed; use `qiskit.pulse.Constant` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.zero": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library",
    "qiskit.pulse.library.square": "{} has been removed; use `qiskit.pulse.Square` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.sawtooth": "{} has been removed; use `qiskit.pulse.Sawtooth` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.triangle": "{} has been removed; use `qiskit.pulse.Triangle` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.cos": "{} has been removed; use `qiskit.pulse.Cos` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.sin": "{} has been removed; use `qiskit.pulse.Sin` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.gaussian": "{} has been removed; use `qiskit.pulse.Gaussian` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.gaussian_deriv": "{} has been removed; use `qiskit.pulse.GaussianDeriv` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.sech": "{} has been removed; use `qiskit.pulse.Sech` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.sech_deriv": "{} has been removed; use `qiskit.pulse.SechDeriv` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.gaussian_square": "{} has been removed; use `qiskit.pulse.GaussianSquare` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
    "qiskit.pulse.library.drag": "{} has been removed; use `qiskit.pulse.Drag` and its `get_waveform()` method (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#pulse.library)",
}

TRANSPILER = {
    "qiskit.transpiler.synthesis.aqc": "{} has been removed; replace with `qiskit.synthesis.unitary.aqc`",
    "qiskit.synthesis.unitary.aqc.AQCSynthesisPlugin": "{} has been removed; replace with `qiskit.transpiler.passes.synthesis.AQCSynthesisPlugin`",
    "qiskit.transpiler.synthesis.graysynth": "{} has been removed; replace with `qiskit.synthesis.synth_cnot_phase_aam`",
    "qiskit.transpiler.synthesis.cnot_synth": "{} has been removed; replace with`qiskit.synthesis.synth_cnot_count_full_pmh`",
    "qiskit.transpiler.passes.NoiseAdaptiveLayout": "{} has been removed; migrate to `qiskit.transpiler.passes.VF2PostLayout`",
    "qiskit.transpiler.passes.CrosstalkAdaptiveSchedule": "{} as been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#transpiler.passes",
    "qiskit.transpiler.passes.Unroller": "{} has been removed; use alternative `qiskit.transpiler.passes.BasisTranslator`",
    "qiskit.transpiler.preset_passmanagers.common.get_vf2_call_limit": "{} has been removed; migrate to `qiskit.transpiler.preset_passmanagers.common.get_vf2_limits` (note the plural)",
    "qiskit.transpiler.passes.LinearFunctionsSynthesis": "{} has been removed; migrate to `qiskit.transpiler.HighLevelSynthesis`",
}

EXECUTE = {
    "qiskit.execute": "{} has been removed; explicitly transpile and run the circuit instead (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#execute)",
    "qiskit.execute_function": "{} has been removed; explicitly transpile and run the circuit instead (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#execute)",
}

EXTENSIONS = {
    "qiskit.extensions": "{} has been removed; most objects have been moved to `qiskit.circuit.library` (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features)",
    "qiskit.extensions.DiagonalGate": "{} has been removed; replace with `qiskit.circuit.library.DiagonalGate`",
    "qiskit.extensions.HamiltonianGate": "{} has been removed; replace with `qiskit.circuit.library.HamiltonianGate`",
    "qiskit.extensions.Initialize": "{} has been removed; replace with `qiskit.circuit.library.Initialize`",
    "qiskit.extensions.Isometry": "{} has been removed; replace with `qiskit.circuit.library.Isometry`",
    "qiskit.extensions.generalized_gates.mcg_up_diag.MCGupDiag": "{} has been removed; replace with `qiskit.circuit.library.generalized_gates.MCGupDiag`",
    "qiskit.extensions.UCGate": "{} has been removed; replace with `qiskit.circuit.library.UCGate`",
    "qiskit.extensions.UCPauliRotGate": "{} has been removed; replace with `qiskit.circuit.library.UCPauliRotGate`",
    "qiskit.extensions.UCRXGate": "{} has been removed; replace with `qiskit.circuit.library.UCRXGate`",
    "qiskit.extensions.UCRYGate": "{} has been removed; replace with `qiskit.circuit.library.UCRYGate`",
    "qiskit.extensions.UCRZGate": "{} has been removed; replace with `qiskit.circuit.library.UCRZGate`",
    "qiskit.extensions.UnitaryGate": "{} has been removed; replace with `qiskit.circuit.library.UnitaryGate`",
}

QUANTUM_INFO = {
    "qiskit.quantum_info.synthesis.OneQubitEulerDecomposer": "{} has moved to `qiskit.synthesis.one_qubit.OneQubitEulerDecomposer`",
    "qiskit.quantum_info.synthesis.TwoQubitBasisDecomposer": "{} has moved to `qiskit.synthesis.two_qubits.TwoQubitBasisDecomposer`",
    "qiskit.quantum_info.synthesis.XXDecomposer": "{} has moved to `qiskit.synthesis.two_qubits.XXDecomposer`",
    "qiskit.quantum_info.synthesis.two_qubit_cnot_decompose": "{} has moved to `qiskit.synthesis.two_qubits.two_qubit_cnot_decompose`",
    "qiskit.quantum_info.synthesis.Quaternion": "{} has moved to `qiskit.quantum_info.Quaternion`",
    "qiskit.quantum_info.synthesis.cnot_rxx_decompose": "{} has been removed with no replacement",
}

QASM = {
    "qiskit.qasm": "{} has been removed; use qiskit.qasm2 instead (see https://docs.quantum.ibm.com/api/migration-guides/qiskit-1.0-features#qiskit.qasm)",
}

TOOLS = {
    "qiskit.tools": "{} has moved; replace `qiskit.tools` with `qiskit.utils`",
    "qiskit.tools.jupyter": "{} has been removed; see separate `qiskit-ibm-provider` package for similar functionality",
    "qiskit.tools.monitor": "{} has been removed; see separate `qiskit-ibm-provider` package for similar functionality",
    "qiskit.tools.visualization": "{} has moved to `qiskit.visualization`",
    "qiskit.tools.events": "{} has been removed",
    "qiskit.tools.events.progressbar": "{} has been removed; use a dedicated package such as `tqdm`",
}

TEST = {
    "qiskit.test": "{} has been removed; if necessary, consider copying the code into your own test infrastructure",
}

UTILS = {
    "qiskit.utils": "{} has been removed with no replacement",
    "qiskit.utils.QuantumInstance": "{} has been removed; see https://docs.quantum.ibm.com/api/migration-guides/qiskit-quantum-instance",
}

VISUALIZATION = {
    "qiskit.visualization.qcstyle": "{} has moved; replace with `qiskit.visualization.circuit.qcstyle`",
    "qiskit.visualization.state_visualization.num_to_latex_ket": "{} has been removed. For similar functionality, see Sympy's `nsimplify` and `latex` functions.",
    "qiskit.visualization.state_visualization.numbers_to_latex_terms": "{} has been removed. For similar functionality, see Sympy's `nsimplify` and `latex` functions.",

}

OTHER = {
    "qiskit.__qiskit_version__": "{} has been removed; use `qiskit.__version__` instead",
}


# These paths are still good; if we hit them, exit early with no problem
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
