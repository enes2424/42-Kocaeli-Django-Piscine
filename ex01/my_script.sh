#!/bin/bash

pip --version

mkdir -p local_lib

pip install --break-system-packages --upgrade --target=local_lib git+https://github.com/jaraco/path.git > path_install.log 2>&1

if [ -d "local_lib/path" ] || [ -f "local_lib/path.py" ] || ls local_lib/*path* >/dev/null 2>&1; then
    PYTHONPATH=./local_lib python3 my_program.py
else
    echo "Error: path.py installation failed. See path_install.log for details." >&2
fi
