```markdown
# SSH Brute Force Tool

This Python script is a simple yet powerful SSH brute force tool designed to assist in testing the security of SSH authentication on remote hosts. It attempts to authenticate to the SSH server using a provided list of usernames and passwords.

## Features

- Multi-threaded brute force attack for faster password cracking.
- Graceful interruption using keyboard input (press 'q' to stop).
- Real-time feedback on successful connections and progress.
- Customizable number of threads and password list.
- Simple command-line interface for easy usage.

## Prerequisites

- Python 3.x
- Paramiko library (install via `pip install paramiko`)
- Pwntools library (install via `pip install pwntools`)
- Keyboard library (install via `pip install keyboard`)

## Usage

1. Clone the repository:

```
git clone https://github.com/your_username/ssh-brute-force-tool.git
cd ssh-brute-force-tool
```

2. Run the script:

```
python ssh_brute_force.py
```

3. Follow the on-screen instructions to input the target host IP, username, password list path, and number of threads.

4. Press 'q' at any time to gracefully interrupt the brute force attack.

## Example

```
$ python ssh_brute_force.py

**************************************
*         SSH Brute Force Tool        *
**************************************

Initializing brute force attack...

Enter the target Host IP: 192.168.1.100
Enter the target Username: admin
Enter the path to the password list file: passwords.txt
Enter the number of threads: 8

[+] Connected with password mysecretpassword

Brute force attack completed.
```

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
