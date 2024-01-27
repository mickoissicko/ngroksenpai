#!/bin/bash
# install.sh

if [ -e lock.pa ]; then
    echo Already satisfied
    echo Exiting in 3s..
    sleep 3
    python ../bin/ngroksenpai.py
    exit 0
fi

sudo pacman -Sy python
sudo pacman -S python-requests

touch lock.pa