#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-full

VENV_PATH="$HOME/django_projects/django_venv"

if [ -d "$VENV_PATH" ]; then
    rm -rf "$VENV_PATH"
fi

mkdir -p "$HOME/django_projects"

python3 -m venv "$VENV_PATH"

source "$VENV_PATH/bin/activate"

python3 -m pip install --upgrade pip

pip install -r requirement.txt
