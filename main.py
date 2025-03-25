from AppOpener import open,close
import psutil
import time


while(True):
    notepadstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())
    if(notepadstatus):
        close("firefox")
    time.sleep(4)
