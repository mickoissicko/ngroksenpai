:: ngstart.bat

@echo off

cd ../ngrok

timeout /t 1 /nobreak
start /b ngrok.exe tcp --region ap 25565
timeout /t 1 /nobreak
start /b ngrok.exe tcp --region us 25565
timeout /t 1 /nobreak
start /b ngrok.exe tcp --region au 25565
timeout /t 1 /nobreak
start /b ngrok.exe tcp --region eu 25565
timeout /t 1 /nobreak
start /b ngrok.exe tcp --region in 25565

timeout /t 15 /nobreak
cd ../scripts