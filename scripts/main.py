import platform
import os

def launch_ngs():
    if platform.system() == 'Linux' or platform.system() == 'Darwin' or platform.system() == 'MacOS':
        os.system('sudo python bin/ngroksenpai.py')
    elif platform.system() == 'Windows':
        os.system('python bin/ngroksenpai.py')

def modconf():
    config_file_path = "../config/ngs.conf"
    webhook_file_path = "../config/webhook.txt"

    try:
        with open(config_file_path, 'r') as file:
            config_lines = file.readlines()

        for i in range(len(config_lines)):
            if config_lines[i].startswith("# autongrok="):
                current_setting = config_lines[i].strip().split('=')[1].lower()
                auto_start_ngrok = input(f"Automatically start NGROK? [Y/N] (current setting: {current_setting}): ").upper()

                if auto_start_ngrok == 'Y':
                    config_lines[i] = "autongrok=True\n"
                elif auto_start_ngrok == 'N':
                    config_lines[i] = "# autongrok=True\n"
                else:
                    print("Invalid input. Keeping the current setting.")

        with open(config_file_path, 'w') as file:
            file.writelines(config_lines)

        print("Configuration updated successfully.")

        webhook_url = input("Enter the webhook URL: (Enter to skip) ")
        if webhook_url:
            with open(webhook_file_path, 'w') as webhook_file:
                webhook_file.write(webhook_url)
            print("Webhook URL saved successfully.")
        else:
            print("Webhook URL not provided. Skipping.")

    except FileNotFoundError:
        print("Configuration file not found. Please make sure the file exists.")


def main():
    while True:
        print("\n[1] Launch NGS")
        print("[2] Modify configuration")
        print("[X] Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            launch_ngs()
        elif choice == '2':
            modconf()
        elif choice.upper() == 'X':
            print("Quitting...")
            break
        else:
            print("ERR: Not found. Please enter a valid option.")

if __name__ == "__main__":
    main()