#
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
from color_presets import *
from layered_config import *
from layered_object import *
from simple_led_functions import *
from hardware_configuration import *

print(LED_COUNT)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()



# Define functions which animate LEDs in various ways.
def layers_in_layers_animation(colors = [], wait_ms=50):
  try:
    flashing_back = True
    sine_time_series = create_sine_time((0,0.05),120)
    print("begin")
    letters = {
      "p" : layered_object(p_layers, strip),
      "l" : layered_object(l_layers, strip),
      "a" : layered_object(a_layers, strip),
      "n" : layered_object(n_layers, strip),
      "s" : layered_object(s_layers, strip),
      "b" : layered_object(b_layers, strip)
    }
    colors = multi_color_echo()
    x = 0.0
    back = True;
    sine_time_tracker = 0
    blueR = 0
    redR = 0
    greenR = 0
    oldR = 0
    oldB = 0
    oldG = 0
    back_colors = []
    for z in range (0,11):
      back_colors.append(off)
    for z in range (0,11):
      back_colors.append(green)
    for z in range (0,11):
	     back_colors.append(off)
    for z in range (0,11):
	     back_colors.append(red)
    for z in range (0,11):
	     back_colors.append(off)
    for z in range (0,11):
	     back_colors.append(blue)
    while(1):
      if(x < 0.9):
        x = x + 0.2
      else:
        x = 0.0
     	#colors.append(Color(randint(0,96), randint(0,96), randint(0,96)))      
    	back_colors.append(back_colors[0])
    	del back_colors[0]
        colors.append(colors[0])
    	del colors[0]
        for letter in letters:
          if letter == "b":
            #b_color = blend_colors(back_colors, x)
            #letters[letter].color_layers(b_color)
            pass
    	  else:
    	    blended_colors = blend_colors(colors, x)
            letters[letter].color_layers(blended_colors) 

        #FLASHING BACK
        if(flashing_back):
          if(back):
            back = False
    	    oldR = redR
            oldB = blueR
            oldG = greenR
            redR = randint(0,1) * 255
            blueR = randint(0,1) * 255
            greenR = randint(0,1) * 255
            while(not (redR or blueR or greenR) or (redR == oldR and blueR == oldB and greenR == oldG)):
                redR = randint(0,1) * 255
                blueR = randint(0,1) * 255
                greenR = randint(0,1) * 255
            set_leds_in_range(strip, (1052,1185), Color(redR, blueR, greenR))
          else:
            back=True
            set_leds_in_range(strip, (1052,1185), Color(0,0,0)) 
        
        strip.show()
        sine_time_tracker +=1
        if(sine_time_tracker == len(sine_time_series)):
          sine_time_tracker = 0
        if(sine_time_series):
          time.sleep(static_time)
        else:
          time.sleep(sine_time_series[sine_time_tracker])
  except Exception as e:
    print(e)

def main():
    turn_off_all_leds(strip)
    # Main program logic follows:
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    # Intialize the library (must be called once before other functions).

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        print("start")
        
	layers_in_layers_animation()
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)



if __name__ == '__main__':
  main()


