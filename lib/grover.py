"""Grover circuit builder using Qiskit primitives."""
from __future__ import annotations
from qiskit import QuantumCircuit
from qiskit.circuit.library import MCXGate

def _apply_phase_oracle(qc: QuantumCircuit, target_index: int, n_qubits: int):
    bits = format(target_index, f'0{n_qubits}b')[::-1]
    for i, b in enumerate(bits):
        if b == '0':
            qc.x(i)
    qc.h(n_qubits-1)
    if n_qubits-1 == 0:
        qc.z(0)
    else:
        qc.mcx(list(range(n_qubits-1)), n_qubits-1)
    qc.h(n_qubits-1)
    for i, b in enumerate(bits):
        if b == '0':
            qc.x(i)
    return qc

def diffuser(n_qubits: int):
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    qc.x(range(n_qubits))
    if n_qubits > 0:
        qc.h(n_qubits-1)
        if n_qubits-1 == 0:
            qc.z(0)
        else:
            qc.mcx(list(range(n_qubits-1)), n_qubits-1)
        qc.h(n_qubits-1)
    qc.x(range(n_qubits))
    qc.h(range(n_qubits))
    return qc

def grover(target_index: int, n_qubits: int, iterations: int = 1):
    if n_qubits <= 0:
        raise ValueError('n_qubits must be >=1')
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    for _ in range(iterations):
        _apply_phase_oracle(qc, target_index, n_qubits)
        d = diffuser(n_qubits)
        qc.compose(d, range(n_qubits), inplace=True)
    return qc
