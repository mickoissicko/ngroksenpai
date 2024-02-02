#!/bin/bash
# start.sh

cd dependencies
chmod +x install.sh
./install.sh

cd ../scripts
sudo python main.py

exit
