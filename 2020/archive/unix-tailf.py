import os, time

logfile = open('/var/log/wifi.log')

def follow(file):
    file.seek(0, os.SEEK_END)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


for line in follow(logfile):
    print(line)