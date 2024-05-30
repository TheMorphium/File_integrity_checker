#!/usr/bin/python3

import ast
import os
import site
import sys

python_version = sys.version_info
python_lib_folder = f'/env/lib/python{sys.version_info[0]}.{sys.version_info[1]}/site-packages/'

site.addsitedir(os.curdir + python_lib_folder)

from sms_messaging import send_message
from time import sleep
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

from dotenv import load_dotenv

load_dotenv()

alert_number = os.getenv('alert_number')
locations = ast.literal_eval(os.getenv('locations'))
locations.append('./')

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