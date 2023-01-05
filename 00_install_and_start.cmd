@echo off

virtualenv --no-setuptools venv
venv\Scripts\pip install --upgrade pip
venv\Scripts\pip install deephaven-example-app
explorer http://localhost:10000/ide/
venv\Scripts\python -m deephaven_example_app

