#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import bme280

ROOTDIR = "/home/pi/ROOTDIR"
if os.path.isdir(ROOTDIR + '/data/'): 
    pass
else:
    os.mkdir(ROOTDIR + '/data/')

nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
time.sleep(60 - int(time.strftime("%S")))

while 1:

    if nowtime == time.strftime("%Y-%m-%d %H:%M:%S") :
        time.sleep(0.1)
        continue

    nowtime = time.strftime("%Y-%m-%d %H:%M:%S")

    ## get temp and humidity
    nowtemp, nowpress, nowhumid =  bme280.readData()


    ## get localtime and check date
    logfile = ROOTDIR + '/data/' \
        + time.strftime("%Y-%m-%d") + '-logger.txt'
    
    with open(logfile, 'a') as logwrite:

        logwrite.write('{0} {1:-6.1f} {2:6.1f} {3:6.1f}\n'.\
        format(nowtime, nowtemp, nowhumid, nowpress))

    logwrite.closed

