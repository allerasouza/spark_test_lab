venv-create:
	python3 -m venv .venv

venv-activate:
	. .venv/bin/activate

setup: venv-create venv-activate
	pip install --upgrade -r requirements.txt

test-unit: venv-activate
	PYARROW_IGNORE_TIMEZONE=1 pytest -svv tests/


