from AppOpener import open,close
import psutil
import time



notepadstatus = "notepad.exe" not in (i.name() for i in psutil.process_iter())
if(notepadstatus):
    open("notepad")
else:
    close("notepad")
time.sleep(5)
