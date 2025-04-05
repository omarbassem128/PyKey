from AppOpener import open,close
import psutil
import time


while(True):
    firefoxstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())
    if(firefoxstatus):
        close("firefox")
    time.sleep(4)
