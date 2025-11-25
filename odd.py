"""Odd number finder example (Grover's Algorithm).
Creates a random integer array and uses Grover search to locate odd numbers.
Usage: python odd.py --seed 42
"""

from __future__ import annotations
import argparse
import random
from math import floor, log
from lib.util import execute
from lib.grover import grover
from lib.oracles.logic import oracle

def init(n: int, max_num: int = 20):
    """Generate random integer array of length n."""
    return [random.randint(0, max_num) for _ in range(n)]

def logic(arr, n, find_odd=True):
    """Return oracle predicate for odd numbers."""
    qubits = floor(log(n, 2))
    clauses = []
    for idx, val in enumerate(arr):
        if (val % 2 == 1) == find_odd:
            b = format(idx, f'0{qubits}b')
            clause = ' and '.join(
                (f'x{j+1}' if bit == '1' else f'not x{j+1}') for j, bit in enumerate(b[::-1])
            )
            clauses.append(f'({clause})')
    if not clauses:
        return None
    prog = f"""def oracle_func({', '.join(f'x{i+1}: Int1' for i in range(qubits))})->Int1:\n    return {' or '.join(clauses)}"""
    return prog

def main(seed: int | None = None):
    if seed is not None:
        random.seed(seed)
    qubits = 3  # 8 possibilities
    bits = 2 ** qubits
    arr = init(bits)
    print(f"{qubits} qubits, {bits} possibilities")
    print("Using random numbers:")
    print(arr)

    prog = logic(arr, bits, find_odd=True)
    if prog is None:
        print("\nNo odd numbers found in array.")
        return

    print("\nRunning Grover search for odd numbers...")
    qc = grover(oracle, prog, qubits)
    result = execute(qc, seed=seed)
    counts = result.get_counts()
    key = max(counts, key=counts.get)
    index = int(key, 2)
    print(counts)
    print(f"\nFound odd number: {arr[index]} (at index {index} [{key}])")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()
    main(seed=args.seed)
