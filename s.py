#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import serial
import time
import random
from numpy.random import *

ser = serial.Serial('/dev/ttyACM0',9600) # シリアル通信開始
time.sleep(2) 
while 1:      # 0と1をループ内でランダムに生成する
   t = randint(2)
   tt = str(t)
   ser.write(tt)
   print tt
   time.sleep(1)
   if t is None:
      ser.write('0')
      ser.close()
      sys.exit()



