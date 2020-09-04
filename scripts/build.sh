#!/bin/bash

cd src
echo "Removing previous .venv"
deactivate
rm -rf .venv/
echo "Creating .venv"
virtualenv -p python3 .venv
source .venv/bin/activate
echo "Installing dependencies"
pip install -r requirements.txt
cd ..
