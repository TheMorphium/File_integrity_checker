#!/usr/bin/python3

import ast
import atexit
import os
import signal
import site
import sys

python_version = sys.version_info
python_lib_folder = f'/env/lib/python{sys.version_info[0]}.{sys.version_info[1]}/site-packages/'

site.addsitedir(os.curdir + python_lib_folder)

from datetime import datetime
from sms_messaging import send_message
from time import sleep
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from dotenv import load_dotenv

load_dotenv()

last_start_time_file = './.laststartup'
alert_number = os.getenv('alert_number')
locations = ast.literal_eval(os.getenv('locations'))
locations.append('./')

startup_time = int(datetime.timestamp(datetime.now()))

def check_set_startup():
    error_count = 0
    if os.path.isfile(last_start_time_file):
        previous_start = os.getenv('start_time', last_start_time_file)
        error_count = int(os.getenv('error_count', last_start_time_file))
        time_difference = startup_time - previous_start
        if time_difference >= 600:
            error_count = 0
            system_starting()
        else:
            error_count += 1
    if error_count > 10:
        send_fail()
    updated_file_text = f"start_time = '{startup_time}'"
    updated_file_text += f"\nerror_count = '{error_count}'"
    with open(last_start_time_file, "w") as f:
        f.write(updated_file_text)


def send_fail():
    pass


def on_created(event):
    print(f"hey, {event.src_path} has been created!")
    send_message(alert_number, f"hey, {event.src_path} has been created!")

def on_deleted(event):
    print(f"what the f**k! Someone deleted {event.src_path}!")
    send_message(alert_number, f"what the f**k! Someone deleted {event.src_path}!")

def on_modified(event):
    print(f"hey buddy, {event.src_path} has been modified")
    send_message(alert_number, f"hey buddy, {event.src_path} has been modified")

def on_moved(event):
    print(f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")
    send_message(alert_number, f"ok ok ok, someone moved {event.src_path} to {event.dest_path}")

def system_starting():
    print('Integrity Watchdog is Shutting Down!')
    send_message(alert_number, 'Integrity Watchdog is Shutting Down!')

def exit_handler():
    print('Integrity Watchdog is Shutting Down!')
    send_message(alert_number, 'Integrity Watchdog is Shutting Down!')


atexit.register(exit_handler)
signal.signal(signal.SIGTERM, exit_handler)
signal.signal(signal.SIGINT, exit_handler)

def build_observer():
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved
    my_observer = Observer()
    for location in locations:
        my_observer.schedule(my_event_handler, location, recursive=True)
    my_observer.start()
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()





if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    build_observer()