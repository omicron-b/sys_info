#!/usr/bin/env bash

cd "$(dirname "$0")"
echo "Checking directory"
if [[ "$PWD" = */sys_info ]]; then
chmod +x sysinfo.py
echo "Creating virtual enviroment in $PWD"
python3 -m venv env
echo "Activating venv"
source env/bin/activate
echo "Installing modules to venv"
pip install wheel
pip install psutil
echo "Deactivating venv"
deactivate
chmod +x s_info
echo "You can now run: $PWD/s_info"
else
echo "You are not in sys_info, but we honestly tried to cd you to it. Not doing anything then."
fi
