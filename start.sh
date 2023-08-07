echo """
SMALL SCRIPT THAT INDICATES BATTERY LEVEL CHANGE AFTER REACHING THE THRESHOLD

MADE BY MATEUSZ PIETKA matipietka@gmail.com
"""

python -m venv env
./env/bin/pip install gtts
./env/bin/python main.py
