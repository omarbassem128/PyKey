import psutil
import event
firefoxstatus = "firefox.exe" in (i.name() for i in psutil.process_iter())

print(firefoxstatus)