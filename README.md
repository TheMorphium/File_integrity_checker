# File Integrity Checker
Ensures files arent changed, and sends alerts via Twilio if any do.

You will need to have a Twilio account, with an SMS enabled phone number.  Twilio will charge you per your contract for each sms message this tool sends.

To Install:
1) Elevate yourself to root "sudo su"
2) Ensure you have the python venv tools "apt install python3.10-venv" Use your python version.
2) Go to your opt folder "cd /opt"
2) Clone this repo to this location "git clone https://github.com/TheMorphium/File_integrity_checker.git"
3) Move to new folder "cd File_integrity_checker"
4) Create virtual enviornment "python -m venv env"
5) Install libraries "pip install -r requirements.txt"
3) Make a new .env file with the ENV_EXAMPLE text as a template. "nano .env"
4) Paste contents of ENV_EXAMPLE, and modify for your needs
5) Make a service to launch watchdog:
6) Edit a new file "nano /etc/systemd/system py_watchdog.service"
7) Paste below text

[Unit]
Description=Python Watchdog
After=multi-user.target

[Service]
Type=simple
Restart=always
ExecStart=/opt/File_integrity_checker/integrity_check_tool.py
WorkingDirectory=/opt/File_integrity_checker/
User = root

[Install]
WantedBy=multi-user.target

8) Press Ctrl-X to exit, and press y to save changes
9) Reload the service daemon "systemctl daemon-reload"
10) Enable service "systemctl enable py_watchdog"
11) Start service "systemctl start py_watchdog"

TES