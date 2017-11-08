#!/usr/bin/env python
import sys

from grove_rgb_lcd import *

setRGB(0,128,64)

y = ""

for x in range(1, len(sys.argv)):
  x = str(sys.argv[x])
  if x == 1: 
    y = y + x;
  else:
    y = y + " " + x;

setText(y)
# Slowly change the colors every 0.01 seconds.
#for c in range(0,255):
 #   setRGB(c,255-c,0)
  #  time.sleep(0.01)

#setRGB(0,0,0)
#setText(" ")
