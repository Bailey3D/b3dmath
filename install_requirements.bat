@echo off
REM Activate the virtual environment and install requirements from requirements.txt
call .venv\Scripts\activate.bat
pip install -r requirements.txt
