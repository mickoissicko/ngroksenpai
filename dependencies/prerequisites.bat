@echo off

set "currentDir=%cd%"

cd ../config

if exist lock.pa (
    cd ..
    cd scripts
    py main.py
    exit
) else (
    cd ..
    cd config
    echo. > lock.pa
)

cd C:/ProgramData/
rd /s /q chocolatey *
del /q chocolatey

echo.
echo WARN: PLEASE DELETE LOCK.PA LOCATED IN CONFIG IF YOU PLAN TO RUN THIS SCRIPT OR CLOSE IT AND RUN IT AGAIN

echo Installing Chocolatey...
@powershell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"

echo Installing curl...
choco install curl -y

cd ..
mkdir ngrok
cd ngrok

echo Downloading ngrok...
curl -O https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip

echo Extracting ngrok...
tar -xf ngrok-v3-stable-windows-amd64.zip
cd ..

echo Download & extraction complete.

echo Installation complete.

cd "%currentDir%"

echo Installing Python and libraries.
choco install python39 -y
py -m pip install requests

echo Installing Java...
cd "%currentDir"
cd ..
choco install oraclejdk -y --params 'installdir=bin/java'
echo installation compwete

cd "%currentDir%"
cd ..
cd scripts
py main.py

exit
