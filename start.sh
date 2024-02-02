#!/bin/bash
# start.sh

cd dependencies
chmod +x install.sh
./install.sh

cd ../scripts
sudo python launcher.py
