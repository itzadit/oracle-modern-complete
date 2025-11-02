.PHONY: install test run-hello build
install:
	python -m pip install -r requirements.txt
test:
	pytest -q
run-hello:
	python hello.py --seed 42
build:
	python -m build
