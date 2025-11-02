import sys, os, subprocess

# ✅ Add project root to sys.path so imports like "from lib..." work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.util import num_qubits, execute
from lib.grover import grover


def test_num_qubits():
    # Check that the num_qubits function returns an integer >= 0
    result = num_qubits(1)
    assert isinstance(result, int)
    assert result >= 0


def test_grover_basic():
    qc = grover(2, 3, iterations=1)
    assert qc.num_qubits == 3
    res = execute(qc, seed=42, shots=128)
    counts = res.get_counts()
    assert isinstance(counts, dict)
    assert len(counts) > 0


def test_hello_integration(tmp_path):
    # ✅ Use absolute path and ensure hello.py runs end-to-end
    script_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')), 'hello.py')
    p = subprocess.run(
        [sys.executable, script_path, '--seed', '42'],
        capture_output=True, text=True, check=True
    )
    out = p.stdout
    assert 'Final result from the quantum circuit' in out
