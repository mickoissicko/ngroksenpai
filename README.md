# Ngrok Senpai
* Does your ISP use CGNAT, or just hates everyone and blocks port-forwarding? And you are too much of a wuss to call them to fix it? This is for you!
* Is copy-pasting the multiple Ngrok proxies for each of your friends too hard? NGS' 'gotchu covered!

## Supported Python versions
* Python 3.12.1
* Python 3.11.7
* Python 3.9.10

## Features
* Not a stupid Docker container
* Works with Archlinux
* Better than Hardware Haven's solution, can work on multiple Ngrok sessions.

# Installation for Archlinux
Step 1 **Installing ngrok**

Step 1a **Install snap**

`$ cd ~/`

`$ git clone https://aur.archlinux.org/snapd.git`

`$ cd snapd`

`$ makepkg -si`

Step 1b **Install ngrok**

`$ sudo snap install ngrok`

Step 2 **Making an account and logging in**

Make an account on the [ngrok](https://dashboard.ngrok.com/signup) website.

After you have made the account, navigate to the [setup](https://dashboard.ngrok.com/get-started/setup/linux) page

`$ ngrok config add-authtoken THE-AUTHTOKEN-GIVEN`

Change 'the-authtoken-given' to the one given on the website.

Step 3 **Starting Ngrok**
You can start 3 ngrok tunnels in locations: in, ap, eu, au, and us.

`$ ngrok tcp --region eu 25565`

`$ ngrok tcp --region ap 25565`

`$ ngrok tcp --region in 25565`

`$ ngrok tcp --region au 25565`

`$ ngrok tcp --region us 25565`

Let's say you have 3 friends **(impossible)**. One is from Amsterdam, one is from Sydney, and the other one is from Hong Kong. This is perfect as you can only operate 3 Ngrok tunnels per account (max).

You start the tunnels.

Step 4 **Running the tool**
Copy the webhook URL

![](https://i.ibb.co/0Qb8d4q/Untitled.png)

Navigate to Line 26, and edit this:

`discord_webhook_url = "ur_webhook_noob"`

with the actual webhook URI.

![](https://i.ibb.co/wyTZ0nH/2.png)

After you have added the URL, run the following command in the directory where `ngroksenpai.py` is located.

`$ sudo python ngroksenpai.py`

Enter your password and it should send the links in Discord!

# Installation for Windows
Step 1. **Installing Ngrok**

Install [ngrok](ngrok.com). You can choose the [64-bit version](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip) or the [32-bit version](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-386.zip). 

Step 2 **Making an account and logging in**

Make an account on the [ngrok](https://dashboard.ngrok.com/signup) website.

After you have made the account, navigate to the [setup](https://dashboard.ngrok.com/get-started/setup/linux) page

Open a command prompt window in the folder where you downloaded ngrok, and type

`$ ngrok.exe config add-authtoken THE-AUTHTOKEN-GIVEN`

Step 3 **Starting the service**

Open a command prompt window in the folder where you downloaded ngrok.

You can start 3 ngrok tunnels in locations: in, ap, eu, au, and us.

`$ ngrok tcp --region eu 25565`

`$ ngrok tcp --region ap 25565`

`$ ngrok tcp --region in 25565`

`$ ngrok tcp --region au 25565`

`$ ngrok tcp --region us 25565`

Select the region closest to your friends.

IN is India, AP is Asia Pacific, EU is Europe, AU is Australia, and US is the United States.

Let's say you have 3 friends **(impossible)**. One is from Amsterdam, one is from Sydney, and the other one is from Hong Kong. This is perfect as you can only operate 3 Ngrok tunnels per account (max).

You start the tunnels.
