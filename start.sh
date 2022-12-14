#!/bin/bash

export PYTHONPATH="$PWD/src";
apps=('bee');

if [ $1 == "help" ] || [ $1 == "--help" ] 
then
	echo "P-median examples runner"
	echo "Using: ./start.sh <app>"
	echo "Possible apps: $apps"

elif [[ $1 == 'bee' ]] then
	python3 src/beeSolution/main.py
elif [[ $1 == 'gene' ]] then
	python3 src/genetic/main.py
else
	echo "Unkown app! Possible apps: $apps"
fi
