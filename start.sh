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
./env/bin/pip install pydub --disable-pip-version-check -q

if [ $# == 0 ] ; then
	echo "Running unit tests, integration tests and statring app ..."
	./env/bin/python3 src/tests.py ut it
	if [ $? != 0 ] ; then
		echo "TESTS FAILED !!!"
		exit 1
	fi

	./env/bin/python3 src/main.py

elif [ $1 == "ut" ] ; then
	./env/bin/python3 src/tests.py ut
else
	echo "Unknown arg !!!"
	exit 1
fi
