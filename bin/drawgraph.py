#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import os
import subprocess
import bme280

ROOTDIR = "/home/pi/ROOTDIR"

PLTFILE = ROOTDIR + "/bin/climate.plt"
PLTBASE = ROOTDIR + "/bin/climate.plt.base"
GNUPLOT = "/usr/bin/gnuplot"
climatepng = "climate.png"
climatepngfull = ROOTDIR + "/html/" +  climatepng
climatepngfulltmp = ROOTDIR + "/html/tmp." +  climatepng
pressurepng = "pressure.png"
pressurepngfull = ROOTDIR + "/html/" +  pressurepng
pressurepngfulltmp = ROOTDIR + "/html/tmp." +  pressurepng
logfile = ROOTDIR + '/data/' \
+ time.strftime("%Y-%m-%d") + '-logger.txt'

GRAPHHTML = ROOTDIR + "/html/graph.html"
GRAPHBASE = ROOTDIR + "/html/graph.html.base"

## get temp and humidity
nowtemp, nowpress, nowhumid =  bme280.readData()

## Heat Index
ftemp = nowtemp * 9 /5 +32
heatindex = -42.379 + 2.04901523 * ftemp + 10.14333127 * nowhumid\
 - 0.22475541 * ftemp * nowhumid - 6.83783e-3 * ftemp ** 2\
 -5.481717e-2 * nowhumid ** 2 + 1.22874e-3 * ftemp ** 2 * nowhumid\
 +8.5282e-4 * ftemp * nowhumid ** 2 - 1.99e-6 * ftemp ** 2 * nowhumid ** 2
cheati = (heatindex - 32) * 5 / 9
if heatindex < 80:
   hi_warn =  '{0:6.1f}'.format(cheati)
elif heatindex < 90:
   hi_warn = '<span style=\"background-color:yellow;\">{0:6.1f}</span>'.format(cheati)
elif heatindex < 103:
   hi_warn = '<span style=\"background-color:orange;">{0:6.1f}</span>'.format(cheati)
elif heatindex < 125:
   hi_warn = '<span style=\"background-color:red;\">{0:6.1f}</span>'.format(cheati)
else:
   hi_warn = '<span style=\"background-color:black;color:red;\">{0:6.1f}</span>'.format(cheati)

## Discomfort Index
discomi = 0.81 * nowtemp + 0.01 * nowhumid * (0.99 * nowtemp - 14.3) + 46.3
if discomi < 70:
   di_warn = '{0:6.1f}'.format(discomi)
elif discomi < 75:
   di_warn = '<span style=\"background-color:yellow;\">{0:6.1f}</span>'.format(discomi)
elif discomi < 80:
   di_warn = '<span style=\"background-color:orange;\">{0:6.1f}</span>'.format(discomi)
elif discomi < 85:
   di_warn = '<span style=\"background-color:red;\">{0:6.1f}</span>'.format(discomi)
else:
   di_warn = '<span style=\"background-color:black;color:red;\">{0:6.1f}</span>'.format(discomi)

## input data to climate.html
with open(GRAPHHTML, 'w') as grphtml, \
 open(GRAPHBASE, 'r') as grpbase:
    for htline in grpbase:
        htline1 = htline.replace('$$date$$', time.strftime("%Y-%m-%d"))\
         .replace('$$time$$', time.strftime("%H:%M"))\
         .replace('$$temp$$', '{0:-6.1f}'.format(nowtemp))\
         .replace('$$humid$$', '{0:6.1f}'.format(nowhumid))\
         .replace('$$press$$', '{0:6.1f}'.format(nowpress))\
         .replace('$$heatindex$$', hi_warn)\
         .replace('$$discomfort$$', di_warn)

        grphtml.write(htline1)
 
grphtml.closed
grpbase.closed

## gnuplot graph

with open(PLTFILE, 'w') as plttd, \
 open(PLTBASE, 'r') as pltbs:
    for pltline in pltbs:
        plt1 = pltline.replace('$$datalog$$', logfile)
        plttd.write(plt1)

plttd.closed
pltbs.closed

subprocess.call([GNUPLOT, PLTFILE])
os.rename(climatepngfulltmp, climatepngfull)
os.rename(pressurepngfulltmp, pressurepngfull)         

