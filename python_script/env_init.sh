#!/bin/bash

# Get the main path of the project
cd "$(dirname "$0")"
PROJECTPATH="$(pwd)"
cd -

export PYTHONPATH="$PROJECTPATH/src"
python -c 'import sys;print(sys.path)' | grep $PROJECTPATH
