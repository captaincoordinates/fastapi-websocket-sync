#!/bin/bash


if [[ -z "$REQUIREMENTS_FILE" ]]; then
    echo "no requirements file to install"
else
    pip install -r $REQUIREMENTS_FILE
fi

if [[ -z "$PYTHONPATH_APPEND" ]]; then
    echo "no pythonpath_append to add"
else
    export PYTHONPATH=$PYTHONPATH:$PYTHONPATH_APPEND
    echo "PYTHONPATH: $PYTHONPATH"
fi

"$@"
