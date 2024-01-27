#!/bin/bash
# launcher.sh

cd pa
chmod +x install.sh
./install.sh

cd ../bin
sudo python ngroksenpai.py
