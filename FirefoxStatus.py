import psutil
""" from pynput import keyboard """

firefoxstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())
if(firefoxstatus):
    #listen for keylogs here
