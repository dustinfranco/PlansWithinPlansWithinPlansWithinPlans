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

p = 0
l = 0
a = 0
n = 0
s = 0

pl = 200
ll = 375
al = 600
nl = 875
sl = 1075

class layered_object():
  layers = [[(0,1)]]
  
  def __init__(self, layers):
    print("init")
    self.layers = layers
    #print(self.layers)
  def color_layers(self, input_colors):
    for i in range(0,len(self.layers) - 1):
      select_color = input_colors[i]
      for layer_tuple in self.layers[i]:
	#print("applying " + str(select_color) + " to " + str(layer_tuple))
        set_leds_in_range(layer_tuple, select_color)
  
def create_sine_time(time_range, number_samples):
  x = np.arange(number_samples)
  y = (np.sin(2 * np.pi * x / number_samples) + 1) * (time_range[1] - time_range[0]) + time_range[0]
  return y 


def lerp_int(a, b, step):
  a_step = 1.0 - step
  return int((a * a_step + b * step)/2)

def lerp_color(color_a, color_b, step):
  red_a = color_a >> 16
  green_a = (color_a & 65280) >> 8
  blue_a = color_a & 255

  red_b = color_b >> 16
  green_b = (color_b & 65280) >> 8
  blue_b = color_b & 255

  output_color = Color(
		        lerp_int(red_a, red_b, step),
		        lerp_int(green_a, green_b, step),
		        lerp_int(blue_a, blue_b, step)
		      )
  
  return output_color

def blend_colors(input_colors, step):
  output_color = []
  for i in range(0,len(input_colors)-1):
    output_color.append(lerp_color(input_colors[i], input_colors[i + 1], step))
  return output_color
  
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def turn_off_all_leds():
  set_leds_in_range((0,LED_COUNT), Color(0,0,0))
  strip.show()

def set_leds_in_range(input_range, color):
  for x in range(input_range[0], input_range[1]):
    strip.setPixelColor(x, color)

# Define functions which animate LEDs in various ways.
def layers_in_layers_animation(colors = [], wait_ms=50):
  """Wipe color across display a pixel at a time."""
  pl = 201
  ll = 352
  al = 601
  nl = 864
  sl = LED_COUNT
 
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
 
  try:
    sine_time_series = create_sine_time((0,0.05),120)
    print("begin")
    letters = {
      "p" : layered_object(p_layers),
      "l" : layered_object(l_layers),
      "a" : layered_object(a_layers),
      "n" : layered_object(n_layers),
      "s" : layered_object(s_layers),
      "b" : layered_object(b_layers)
    }
    red = Color(160,0,0)
    green = Color(0,160,0)
    blue = Color(0,0,160)
    yellow = Color(160,160,0)
    pink = Color(0,160,160)
    cyan = Color(160,0,160)
    off = Color(0,0,0)
    colors = [red,red,red,red,red,off,off,off,off,off,off,
              blue,blue,blue,blue,blue,off,off,off,off,off,off,
              green,green,green,green,green,off,off,off,off,off,off,
              pink,pink,pink,pink,pink,off,off,off,off,off,off,
              cyan,cyan,cyan,cyan,cyan,off,off,off,off,off,off,
              yellow,yellow,yellow,yellow,yellow,off,off,off,off,off,off
             ]
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
          #print(blended_colors)
          #time.sleep(0.075)
          #input("blended colors printed continue?")
          letters[letter].color_layers(blended_colors) 
      #FLASHING BACK
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
        set_leds_in_range((1052,1185), Color(redR, blueR, greenR))
      else:
        back=True
        set_leds_in_range((1052,1185), Color(0,0,0)) 
      #"""
      
      strip.show()
      sine_time_tracker +=1
      if(sine_time_tracker == len(sine_time_series)):
        sine_time_tracker = 0
      #time.sleep(0.25)
      #print(sine_time_series[sine_time_tracker])
      #time.sleep(sine_time_series[sine_time_tracker])
  except Exception as e:
    print(e)

def main():
    turn_off_all_leds()
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


