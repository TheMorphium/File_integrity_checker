# File Integrity Checker
Ensures files arent changed, and sends alerts via Twilio if any do.

You will need to have a Twilio account, with an SMS enabled phone number.  Twilio will charge you per your contract for each sms message this tool sends.

To Install:
1) Elevate yourself to root "sudo su"
2) Go to your opt folder "cd /opt"
2) Clone this repo to this location "git clone https://github.com/TheMorphium/File_integrity_checker.git"
3) Make a new .env file with the ENV_EXAMPLE text as a template.
4) Make a service to launch watchdog:
5) Edit a new file "nano /etc/systemd/system py_watchdog.service"
6) Paste below text

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

7) Press Ctrl-X to exit, and press y to save changes
8) Reload the service daemon "systemctl daemon-reload"
9) Enable service "systemctl enable py_watchdog"
10) Start service "systemctl start py_watchdog"