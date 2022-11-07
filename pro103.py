import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/kpram/OneDrive/Desktop/Python/c-103/Downloadss"
to_dir = "C:/Users/kpram/OneDrive/Desktop/Python/c-103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class file_movment_handler(FileSystemEventHandler):
    def on_created(self , event):
        print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self , event):
        print(f"Oops! Someone deleted {event.src_path}!")

       

# creating object
event_handler = file_movment_handler()

# initialize the observer
observer = Observer()

# scheduling the observer
observer.schedule(event_handler , from_dir , recursive = True )
# starting the observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
