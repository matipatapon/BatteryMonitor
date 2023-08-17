#!/bin/bash

echo """
SMALL SCRIPT THAT INDICATES BATTERY LEVEL CHANGE AFTER REACHING THE THRESHOLD

MADE BY MATEUSZ PIETKA matipietka@gmail.com
"""

mpg123 --version

if [ $? != 0 ]
then
	echo "mpg123 not installed !!!"
	exit 1	
fi

python -m venv env
./env/bin/pip install gtts
./env/bin/python main.py
