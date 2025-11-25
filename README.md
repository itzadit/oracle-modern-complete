# Oracle Modern Complete 🔍⚛️

A modern Python implementation of **Grover's Algorithm** for quantum search. This project demonstrates how quantum computers can search through unsorted data faster than classical computers, using Qiskit to simulate quantum circuits.

## 🎯 What This Project Does

This project simulates a quantum search algorithm that:
- Creates a random array of letters
- Uses Grover's algorithm to find specific target letters
- Sometimes shows "not found" results (realistic quantum behavior)
- Demonstrates quantum superposition and interference

## 🧠 How It Works

### Grover's Algorithm Basics
1. **Superposition**: Put all qubits in equal probability states
2. **Oracle**: Mark the target items we're searching for
3. **Diffuser**: Amplify the probability of marked items
4. **Measurement**: Collapse to the most probable state

### Project Structure
```
oracle-modern-complete/
├── hello.py              # Main program - searches for "hello" letters
├── lib/
│   ├── grover.py         # Grover's algorithm implementation
│   ├── util.py           # Utility functions for quantum simulation
│   └── oracles/
│       └── logic.py      # Oracle logic for marking target states
├── tests/
│   └── test_hello.py     # Unit tests
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.11 or higher
- Git installed on your computer
- Basic understanding of command line

### Step 1: Clone the Repository
```bash
# Clone the project to your computer
git clone https://github.com/itzadit/oracle-modern-complete.git

# Navigate to the project directory
cd oracle-modern-complete
```

### Step 2: Set Up Python Environment (Recommended)
```bash
# Create a virtual environment
python -m venv quantum_env

# Activate the virtual environment
# On Windows:
quantum_env\Scripts\activate
# On macOS/Linux:
source quantum_env/bin/activate
```

### Step 3: Install Dependencies
```bash
# Install required packages
pip install -r requirements.txt
```

### Step 4: Run the Program
```bash
# Run with default settings
python hello.py

# Run with a specific seed for reproducible results
python hello.py --seed 42
```

## 📊 Example Output

```
3 qubits, 8 possibilities
Using random letters:
['R', 'e', 'M', 'l', 'o', 'K', 'h', 'Q']

Finding letter 'h'
{'000': 45, '110': 979}
Found letter: h (at index 6 [110])

Finding letter 'e'
{'001': 1024}
Found letter: e (at index 1 [001])

Finding letter 'l'
{'011': 1024}
Found letter: l (at index 3 [011])

Finding letter 'l'
{'011': 1024}
Found letter: l (at index 3 [011])

Finding letter 'o'
{'100': 1024}
Found letter: o (at index 4 [100])

Random letters:
['R', 'e', 'M', 'l', 'o', 'K', 'h', 'Q']

Final result from the quantum circuit:
h (at index 6 [110])
e (at index 1 [001])
l (at index 3 [011])
l (at index 3 [011])
o (at index 4 [100])
```

## 🔧 Advanced Usage

### Running Tests
```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v
```

### Code Linting
```bash
# Install ruff (if not already installed)
pip install ruff

# Check code style
python -m ruff check .

# Fix code style issues automatically
python -m ruff check . --fix
```

### Using Docker
```bash
# Build the Docker image
docker build -t oracle-quantum .

# Run the container
docker run oracle-quantum
```

## 📚 Understanding the Code

### Key Files Explained

**`hello.py`** - Main program that:
- Creates a random array of letters
- Searches for each letter in "hello"
- Uses quantum circuits to find the letters

**`lib/grover.py`** - Contains:
- `grover()`: Main Grover's algorithm implementation
- `diffuser()`: Amplitude amplification component
- `_apply_phase_oracle()`: Marks target states

**`lib/util.py`** - Utility functions:
- `execute()`: Runs quantum circuits on simulator
- `num_qubits()`: Calculates required qubits
- `random_letters()`: Generates random letter arrays

## 🎓 Educational Value

This project teaches:
- **Quantum Superposition**: How qubits can be in multiple states
- **Quantum Interference**: How to amplify correct answers
- **Quantum Measurement**: How observation collapses quantum states
- **Practical Quantum Programming**: Using Qiskit for real quantum algorithms

## 🛠️ Troubleshooting

### Common Issues

**Import Errors**:
```bash
# Make sure you're in the project directory
cd oracle-modern-complete
# And have activated your virtual environment
```

**Qiskit Installation Issues**:
```bash
# Try upgrading pip first
pip install --upgrade pip
# Then reinstall requirements
pip install -r requirements.txt
```

**Permission Errors on Windows**:
- Run Command Prompt as Administrator
- Or use PowerShell with execution policy: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests: `pytest`
5. Submit a pull request

## 📄 License

This project is open source. See the LICENSE file for details.

## 🔗 Learn More

- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Grover's Algorithm Explained](https://qiskit.org/textbook/ch-algorithms/grover.html)
- [Quantum Computing Basics](https://qiskit.org/textbook/ch-states/introduction.html)

---

**Happy Quantum Computing!** 🚀⚛️