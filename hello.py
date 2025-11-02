"""Hello world example (realistic version).
Builds a random letter array, sometimes missing target letters to simulate "not found" cases.
Uses Grover search circuits to find indices for each letter.
Usage: python hello.py --seed 42
"""

from __future__ import annotations
import argparse, random
from math import floor, log
from lib.util import execute, num_qubits, random_letters
from lib.grover import grover
from lib.oracles.logic import oracle


def init(target: str, n: int, plant_probability: float = 0.7):
    """Create random array of n letters with some target letters possibly missing."""
    arr = random_letters(n)
    indices = set()
    for ch in set(target):
        if random.random() < plant_probability:
            index = random.randint(0, n - 1)
            arr[index] = ch
            indices.add(index)
    return arr


def logic(arr, target, n):
    """Return oracle predicate source and matching indices for target letter."""
    qubits = floor(log(n, 2))
    clauses = []
    indices = []
    start = 0
    while True:
        try:
            idx = arr.index(target, start)
        except ValueError:
            break
        start = idx + 1
        indices.append(idx)
        b = format(idx, f'0{qubits}b')
        clause = ' and '.join(
            (f'x{j+1}' if bit == '1' else f'not x{j+1}') for j, bit in enumerate(b[::-1])
        )
        clauses.append(f'({clause})')

    if not clauses:
        return None, []  # not found
    prog = f"""def oracle_func({', '.join(f'x{i+1}: Int1' for i in range(qubits))})->Int1:\n    return {' or '.join(clauses)}"""
    return prog, indices


def main(phrase: str, seed: int | None = None):
    if seed is not None:
        random.seed(seed)

    qubits = num_qubits(len(phrase))
    bits = 2 ** qubits
    arr = init(phrase, bits)
    print(f"{qubits} qubits, {bits} possibilities")
    print("Using random letters:")
    print(arr)

    indices = []
    for letter in phrase:
        print(f"\nFinding letter '{letter}'")
        prog, idx_list = logic(arr, letter, bits)

        if not idx_list:
            print(f"Letter '{letter}' not found in array.")
            indices.append({'binary': None, 'index': None, 'letter': letter})
            continue

        # Pick one valid index randomly if multiple found
        target_index = random.choice(idx_list)

        # ✅ Call Grover correctly: pass numeric index, not string
        qc = grover(target_index, qubits)
        result = execute(qc, seed=seed)
        counts = result.get_counts()
        key = max(counts, key=counts.get)
        index = int(key, 2)
        print(counts)
        print(f"Found letter: {arr[index]} (at index {index} [{key}])")
        indices.append({'binary': key, 'index': index, 'letter': letter})

    print("\nRandom letters:")
    print(arr)
    print("\nFinal result from the quantum circuit:\n")
    for entry in indices:
        if entry['index'] is None:
            print(f"{entry['letter']} — ❌ Not found")
        else:
            print(f"{arr[entry['index']]} (at index {entry['index']} [{entry['binary']}])")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()
    main("sgsfd", seed=args.seed)
