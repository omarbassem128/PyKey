import psutil, time
""" from pynput import keyboard """

firefoxstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())

if(firefoxstatus):
    print(True)
else:
    print(False)