#!/usr/bin/python3

from tkinter import *
import glob
import time
import datetime

time1 =''

sysDir = '/sys/bus/w1/devices/'
w1Device = glob.glob(sysDir + '28*')[0]

w1Slave = w1Device + '/w1_slave'

def readTempDev():
  f = open(w1Slave, 'r') # Opens the temperature device file
  lines = f.readlines() # Returns the text
  f.close()
  return lines

def readTemp():
  lines = readTempDev() # Read the temperature 'device file'

  while lines[0].strip()[-3:] != 'YES':
    time.sleep(0.2)
    lines = readTempDev()

  tEquals = lines[1].find('t=')

  if tEquals != -1:
    tempValue = lines[1][tEquals+2:]
    tempCelsius = float(tempValue) / 1000.0
    tempF = tempCelsius*9/5+32
    return tempF

def tick():
  global time1
  time2=datetime.datetime.now().strftime('%H:%M:%S')
  if time2 != time1:
    time1 = time2
    curTime.config(text=time2)
    curTemp.config(text='%.1f'%readTemp()+'\u00b0'+" F")
  curTime.after(200,tick)

rootWindow = Tk()
rootWindow.title('DS18B20')
rootWindow.geometry("500x500")
curTime = Label(rootWindow, font = ('fixed', 20),)
curTime.grid(sticky = N, row = 1, column = 1, padx = 5, pady = (20,20))
curTemp = Label(rootWindow, font = ('fixed', 40),)
curTemp.grid(sticky = N, row = 2, column = 1, padx = 5, pady = (20,20))

tick()
rootWindow.mainloop()
