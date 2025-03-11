""" loggingfile = open(file='log.txt', mode='w')
loggingfile.write("Allah The Greatest")
loggingfile.close()
loggingfile = open(file='log.txt', mode='r')
#print(loggingfile.read(-1))
read_from_log = open(file='read_from_log.txt', mode='w')
read_from_log.write(loggingfile.read())
loggingfile.close()
read_from_log.close() """

with open(file='log.txt', mode='w') as logfile:
    logfile.write('olololololololol')
