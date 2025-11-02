"""Utility functions for running circuits on AerSimulator with reproducible seeding."""
from __future__ import annotations
import random
from math import ceil, log2
from qiskit import transpile
from qiskit_aer import AerSimulator
from qiskit import QuantumCircuit

def num_qubits(n: int) -> int:
    if n <= 1:
        return 0
    return int(ceil(log2(n)))

def random_letters(n: int) -> list[str]:
    import string
    letters = list(string.ascii_lowercase + string.ascii_uppercase + ' ')
    rng = random
    return [rng.choice(letters) for _ in range(n)]

class SimpleResult:
    def __init__(self, counts):
        self._counts = counts
    def get_counts(self):
        return self._counts

def execute(qc: QuantumCircuit, seed: int|None=None, shots: int=1024):
    sim = AerSimulator()
    circ = qc.copy()
    # add measurements if not present
    has_measure = any(instr.operation.name == 'measure' for instr in circ.data)
    if not has_measure:
        circ.measure_all()
    transpiled = transpile(circ, sim, seed_transpiler=seed)
    run_result = sim.run(transpiled, shots=shots, seed_simulator=seed, seed_transpiler=seed).result()
    counts = run_result.get_counts()
    return SimpleResult(counts)
