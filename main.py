""" from AppOpener import open,close """
from pynput import keyboard
import psutil
import time

def on_key_press(key):
    print(f'{key} is pressed')

while(True):
    firefoxstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())
    if(firefoxstatus):
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()
