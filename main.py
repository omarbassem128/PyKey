""" from AppOpener import open,close """
from pynput import keyboard
import psutil
import time

def checkStatus():
    firefoxstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())
    if(firefoxstatus):
        return True
    else:
        return False

def on_key_press(key):
    """ print(f'{key} is pressed') """
    if(checkStatus()):
        print(f'{key} is pressed')
    else:
        return False

while(True):
    if(checkStatus()):
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()
    time.sleep(2)
