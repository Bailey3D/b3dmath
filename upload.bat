@echo off
REM Build and upload the b3dmath package to PyPI
python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*
