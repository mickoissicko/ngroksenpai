#!/bin/bash
# ngstart.sh

sleep 1 &
ngrok tcp --region ap 25565 &
sleep 1 &
ngrok tcp --region us 25565 &
sleep 1 &
ngrok tcp --region au 25565 &
sleep 1 &
ngrok tcp --region eu 25565 &
sleep 1 &
ngrok tcp --region in 25565