#!/bin/bash

cd ../config

if [ -e lock.pa ]; then
    echo Already satisfied
    echo Exiting in 3s..
    sleep 3
    python ../main.py
    exit 0
fi

sudo pacman -Sy python
sudo pacman -S python-requests
sudo pacman -S git

cd ..
git clone https://aur.archlinux.org/ngrok.git
cd ngrok
makepkg -si

cd ../config

touch lock.pa
exit
