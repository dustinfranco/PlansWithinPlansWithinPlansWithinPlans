#
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse
from random import randint
import numpy as np

# LED strip configuration:
LED_COUNT      = 1185  # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
 
p_layers = [
		[(0,62),(141,160)],	
		[(62,91),(160,176)],
		[(91,119),(176,190)],
		[(119,141),(190,201)],
	        [(0,1)]
             ]
  
l_layers = [
	        [(202,274)],
		[(275,307)],
		[(308,338)],
		[(339,353)],
	        [(0,1)] 
           ]
 
  a_layers = [
		[(354,431),(533,555)],
		[(432,466),(556,575)],
		[(467,500),(576,591)],\
		[(501,532),(592,601)],
	        [(0,1)]
             ]

  n_layers = [
		[(602,669)],\
		[(670,733)],\
		[(734,795)],\
		[(796,864)],
	        [(0,1)]
             ]

  s_layers = [
		[(865,910)],\
		[(911,954)],\
		[(955,995)],\
		[(996,1051)],
	        [(0,1)]
             ]
    
  b_layers = [[(1119,1130)]]
  for x in range (0,55):
    b_layers.append([(1118-x,1119-x), (1130+x,1131+x)])
  b_layers.append([(1052,1063)])
 
letters = {
    "p" : layered_object(p_layers),
      "l" : layered_object(l_layers),
      "a" : layered_object(a_layers),
      "n" : layered_object(n_layers),
      "s" : layered_object(s_layers),
      "b" : layered_object(b_layers)
    }


