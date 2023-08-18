#!/bin/bash

echo """
SMALL SCRIPT THAT INDICATES BATTERY LEVEL CHANGE AFTER REACHING THE THRESHOLD

MADE BY MATEUSZ PIETKA matipietka@gmail.com
"""

mpg123 --version > /dev/null
if [ $? != 0 ]
then
	echo "mpg123 not installed !!!"
	exit 1	
fi

python3 --version > /dev/null
if [ $? != 0 ]
then
	echo "python3 not installed !!!"
	exit 1	
fi

python3 -m venv env
./env/bin/pip install gtts --disable-pip-version-check -q

echo "Starting tests ..."
./env/bin/python3 src/tests.py

echo "Started ..."
./env/bin/python3 src/main.py
