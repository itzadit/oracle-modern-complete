"""Emotion finder example using Grover's Algorithm.
Randomly creates a list of emotions, sometimes missing the target one.
Then uses Grover search to locate the target emotion if it exists.
Usage: python emotion.py --seed 42
"""

from __future__ import annotations
import argparse
import random
from math import floor, log
from lib.util import execute
from lib.grover import grover
from lib.oracles.logic import oracle

# possible emotions
EMOTIONS = ["happy", "sad", "angry", "calm", "excited", "nervous", "tired", "bored"]

def init(target: str, n: int, plant_probability: float = 0.7):
    """
    Create random emotion array of n elements.
    Each target emotion has a 'plant_probability' chance to appear at least once.
    """
    arr = [random.choice(EMOTIONS) for _ in range(n)]
    if random.random() < plant_probability:
        index = random.randint(0, n - 1)
        arr[index] = target
    return arr

def logic(arr, target, n):
    """Return oracle predicate for the target emotion."""
    qubits = floor(log(n, 2))
    clauses = []
    start = 0
    while True:
        try:
            idx = arr.index(target, start)
        except ValueError:
            break
        start = idx + 1
        b = format(idx, f'0{qubits}b')
        clause = ' and '.join(
            (f'x{j+1}' if bit == '1' else f'not x{j+1}') for j, bit in enumerate(b[::-1])
        )
        clauses.append(f'({clause})')

    if not clauses:
        return None
    prog = f"""def oracle_func({', '.join(f'x{i+1}: Int1' for i in range(qubits))})->Int1:\n    return {' or '.join(clauses)}"""
    return prog

def main(target_emotion: str, seed: int | None = None):
    if seed is not None:
        random.seed(seed)
    qubits = 3  # 8 possibilities
    bits = 2 ** qubits
    arr = init(target_emotion, bits)
    print(f"{qubits} qubits, {bits} possibilities")
    print("Available emotions:")
    print(arr)

    prog = logic(arr, target_emotion, bits)
    if prog is None:
        print(f"\nEmotion '{target_emotion}' not found in the array 😢")
        return

    print(f"\nRunning Grover search for '{target_emotion}' emotion...")
    qc = grover(oracle, prog, qubits)
    result = execute(qc, seed=seed)
    counts = result.get_counts()
    key = max(counts, key=counts.get)
    index = int(key, 2)
    print(counts)
    print(f"\nFound emotion: '{arr[index]}' (at index {index} [{key}])")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--emotion", type=str, default="happy", help="Target emotion to search for")
    p.add_argument("--seed", type=int, default=None)
    args = p.parse_args()
    main(args.emotion, seed=args.seed)
