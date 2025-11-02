Local (venv)
---------------
python -m venv .venv
.venv\Scripts\Activate.ps1   # PowerShell
pip install -r requirements.txt
python hello.py --seed 42

Docker
---------------
docker build -t oracle-modern-complete .
docker run --rm oracle-modern-complete python hello.py --seed 42

GitHub Actions
---------------
CI defined in .github/workflows/ci.yml (Python 3.11)
