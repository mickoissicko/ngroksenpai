import platform
import os

def cls():
    if platform.system() in ['Linux', 'Darwin']:
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

def launch_ngs():
    cls()
    if platform.system() == 'Linux' or platform.system() == 'Darwin' or platform.system() == 'MacOS':
        os.system('sudo python ../bin/ngroksenpai.py')
    elif platform.system() == 'Windows':
        os.system('python ../bin/ngroksenpai.py')

def modconf():
    cls()
    config_file_path = "../config/ngs.conf"
    webhook_file_path = "../config/webhook.txt"

    start_ngrok = input("Automatically start Ngrok upon launch? [Y/N] (Enter to skip): ").upper()

    with open(config_file_path, 'r') as config_file:
        config_lines = config_file.readlines()
    autongrok_line = next((line for line in config_lines if 'autongrok' in line), None)

    if start_ngrok == 'Y':
        if autongrok_line is not None:
            config_lines = [line.replace('# autongrok=True', 'autongrok=True') for line in config_lines]
        else:
            config_lines.append('\n# Ngrok config\n# do not modify\n#\n# autongrok=True\n# user.choice.1=True\n# user.choice.2=True\n')
            config_lines.append('autongrok=True\n')

    elif start_ngrok == 'N':
        if autongrok_line is not None:
            config_lines = [line.replace('autongrok=True', '# autongrok=True') for line in config_lines]

    with open(config_file_path, 'w') as config_file:
        config_file.writelines(config_lines)
    webhook_url = input("Enter your Discord webhook URL: (Enter to skip): ")

    if webhook_url:
        with open(webhook_file_path, 'w') as webhook_file:
            webhook_file.write(webhook_url)


def main():
    cls()
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