from AppOpener import open,close
import psutil

firefoxstatus = "firefox.exe" not in (i.name() for i in  psutil.process_iter())

if(firefoxstatus):
    #compare search results here
    open('firefox')
    