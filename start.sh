#!/bin/bash

echo """
#!# BATTERY MONITOR #!#

--> https://github.com/matipatapon <--
"""

python3 --version > /dev/null
if [ $? != 0 ]
then
	echo "python3 not installed !!!"
	exit 1
fi

python3 -m venv env
./env/bin/pip install pyttsx3 --disable-pip-version-check -q
./env/bin/pip install pyaudio --disable-pip-version-check -q
./env/bin/pip install pydub --disable-pip-version-check -q
./env/bin/pip install pytest --disable-pip-version-check -q

if [ $# == 0 ] ; then
	./env/bin/python3 src/main.py
elif [ $1 == "ut" ] ; then
	./env/bin/pytest -rAs -k test_ut
elif [ $1 == "it" ] ; then
	./env/bin/pytest -rAs -k test_it
elif [ $1 == "all" ] ; then
	./env/bin/pytest -rAs
else
	echo "Unknown arg !!!"
	exit 1
fi
