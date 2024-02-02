import subprocess
import platform
import requests
import json
import os
import sys
import time

def check_tunnel(curl_command, target_string):
    result = subprocess.run(curl_command, capture_output=True, text=True)
    output = result.stdout
    if target_string in output:
        return output
    return None

def send_discord_webhook(webhook_url, region, url):
    message = f"* {region} === `{url}`"
    payload = {"content": message}
    requests.post(webhook_url, json=payload)

def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if '=' in line:
                key, value = line.strip().split('=')
                config[key.strip()] = value.strip()
    return config

def main():
        config = read_config('../config/ngs.conf')

        if config.get('autongrok') == 'True':
            if platform.system() == "Windows":
                starter_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scripts/ngstart.bat')
                subprocess.Popen([starter_script_path], shell=True)
            else:
                starter_script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../scripts/ngstart.sh')
                subprocess.Popen(['bash', starter_script_path])

        time.sleep(15)
        print("WORKING")

        curl_commands = [
            "curl 127.0.0.1:4040/api/tunnels",
            "curl 127.0.0.1:4041/api/tunnels",
            "curl 127.0.0.1:4042/api/tunnels",
            "curl 127.0.0.1:4043/api/tunnels",
            "curl 127.0.0.1:4044/api/tunnels",
        ]

        target_string = "tcp://"

        webhook_file_path = '../config/webhook.txt'  # Updated webhook file path
        if os.path.exists(webhook_file_path):
            with open(webhook_file_path, 'r') as webhook_file:

                discord_webhook_url = webhook_file.read().strip() # webhook func
        else:
            print("Error: webhook.txt not found. Please create the file with your Discord webhook URL and rerun the application.")
            sys.exit(1)

        region_mapping = {
            ".au": "Sydney",
            ".ap": "Singapore",
            ".in": "Mumbai",
            ".eu": "Europe",
            "": "Ohio",
        }

        for curl_command in curl_commands:
            result = check_tunnel(curl_command.split(), target_string)
            if result:
                data = json.loads(result)
                tunnel_info = data["tunnels"][0]
                public_url = tunnel_info["public_url"]

                for region_code, region_name in region_mapping.items():
                    if region_code in public_url:
                        public_url = public_url.replace("tcp://", "")
                        send_discord_webhook(discord_webhook_url, f"{region_name}", public_url)
                        break
                
if __name__ == "__main__":
    main()
