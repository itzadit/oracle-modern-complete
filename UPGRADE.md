UPGRADE notes
=============
- Replaced old qiskit execute/Aer usage with qiskit_aer.AerSimulator, transpile, and sim.run(...).result()
- Replaced mock grover with a real Grover circuit builder that accepts target_index and iterations.
- Seed handling: execute() passes seed_simulator and seed_transpiler for reproducible results.
- References: https://qiskit.org/documentation/, AerSimulator docs, Qiskit migration notes.
