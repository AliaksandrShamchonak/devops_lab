import psutil
import datetime
import time
import ConfigFile
import json

sprintres = str
count = 0


def printres():
    MB = 1024 ** 2
    cpu = str(psutil.cpu_percent(interval=1))
    memu = str(psutil.virtual_memory().available / MB)
    memv = str(psutil.virtual_memory().used / MB)
    ioc = str(psutil.disk_io_counters())
    netw = str(psutil.net_io_counters())
    timenow = str(datetime.datetime.now())
    global count
    count += 1

    if ConfigFile.ConfigFile().confout == "json":
        global sprintres
        sprintres = json.dumps({
            "SNAPSHOT": count,
            "Time": timenow,
            "CPU load %:": cpu,
            "Memory usage MB:": memu,
            "Virtual memory usage MB:": memv,
            "IO information": ioc,
            "Network information": netw
        }, indent=4)
    else:
        sprintres = "SNAPSHOT " + str(count) + ": " + timenow + ":" + \
        " CPU load %: " + cpu + " Memory usage MB: " + memu + " Virtual memory usage MB: " + memv + " IO information " + ioc + " Network information " + netw + "\n"
    print(sprintres)
    return sprintres


while True:
    time.sleep(ConfigFile.ConfigFile().interval)
    printres()
    if ConfigFile.ConfigFile().confout == "json":
        f = open('output.json', 'a')
    else:
        f = open('output.txt', 'a')
    f.write(str(sprintres))
    f.close()
