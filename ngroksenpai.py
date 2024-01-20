import subprocess
import requests
import json

def check_tunnel(curl_command, target_string):
    result = subprocess.run(curl_command, capture_output=True, text=True)
    output = result.stdout
    if target_string in output:
        return output
    return None

def send_discord_webhook(webhook_url, message):
    payload = {"content": f"`{message}`"}
    requests.post(webhook_url, json=payload)

def main():
    curl_commands = [
        "curl 127.0.0.1:4040/api/tunnels",
        "curl 127.0.0.1:4041/api/tunnels",
        "curl 127.0.0.1:4042/api/tunnels",
    ]

    target_string = "tcp://"

    discord_webhook_url = "ur_webhook_noob"

    for curl_command in curl_commands:
        result = check_tunnel(curl_command.split(), target_string)
        if result:
            data = json.loads(result)
            tunnel_info = data["tunnels"][0]
            public_url = tunnel_info["public_url"]

            public_url = public_url.replace("tcp://", "")

            send_discord_webhook(discord_webhook_url, public_url)

if __name__ == "__main__":
    main()