#!/usr/bin/env python

import glob
import time

# DS18B20.py
# 2016-04-25
# Public Domain

# Typical reading
# 73 01 4b 46 7f ff 0d 10 41 : crc=41 YES
# 73 01 4b 46 7f ff 0d 10 41 t=23187
# Example cmd output:
# 28-0114481055aa 74.9
# 28-020f924587f3 74.4

while True:

   for sensor in glob.glob("/sys/bus/w1/devices/28*/w1_slave"):
      id2 = sensor.split("/")[5]

      try:
         f = open(sensor, "r")
         data = f.read()
         f.close()
         if "YES" in data:
            (discard, sep, reading) = data.partition(' t=')
            t = (float(reading) / 1000.0)*9/5+32
            print("{} {:.1f}".format(id2, t))
         else:
            print("999.9")

      except:
         pass

   time.sleep(3.0)
