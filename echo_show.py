import time
from neopixel import *
from random import randint
# LED strip configuration:
LED_COUNT      = 1052  # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


class layered_object():
  layers = [[(0,1)]]
  
  def __init__(self, layers):
    print("init")
    self.layers = layers
  
  def color_layers(self, input_colors):
    for i in range(0,len(self.layers)):
      select_color = input_colors[i]
      for layer_tuple in self.layers[i]:
	set_leds_in_range(layer_tuple, select_color)

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

def layers_in_layers_animation(colors = [], wait_ms=50):
  #p length = 201
  #l length = 352
  #a length = 601
  #n length = 864
  #s length = LED_COUNT
 
  p_layers = [\
		[(0,62),(141,160)],	
		[(62,91),(160,176)],
		[(91,119),(176,190)],
		[(119,141),(190,201)]
	     ]
  
  l_layers = [\
		[(202,274)],
		[(275,307)],
		[(308,338)],
		[(339,353)]
	      ]
 
  a_layers = [\
		[(354,431),(533,555)],
		[(432,466),(556,575)],
		[(467,500),(576,591)],\
		[(501,532),(592,601)]
	     ]

  n_layers = [\
		[(602,669)],\
		[(670,733)],\
		[(734,795)],\
		[(796,864)]
	     ]

  s_layers = [\
		[(865,910)],\
		[(911,954)],\
		[(955,995)],\
		[(996,1051)]\
	     ]

  try:
    print("begin")
    letters = {
      "p" : layered_object(p_layers),
      "l" : layered_object(l_layers),
      "a" : layered_object(a_layers),
      "n" : layered_object(n_layers),
      "s" : layered_object(s_layers)
    }
    red = Color(160,0,0)
    green = Color(0,160,0)
    blue = Color(0,0,160)
    yellow = Color(160,160,0)
    pink = Color(160,0,160)
    cyan = Color(160,0,160)
    off = Color(0,0,0)
    colors = [red,cyan,green,pink,blue,yellow]
    x = 0.0
    while(1):
      if(x < 0.999):
	x = x - 0.00001
        x = x + 0.1
      else:
        x = 0.0
	#colors.append(Color(randint(0,96), randint(0,96), randint(0,96)))        
        colors.append(colors[0])
	del colors[0]
      for letter in letters:
	blended_colors = blend_colors(colors, x)
        letters[letter].color_layers(blended_colors) 
      strip.show()
      time.sleep(0.05)
  except Exception as e:
    print(e)

def main():
    try:
        print("start")        
	layers_in_layers_animation()
    except KeyboardInterrupt:
	turn_off_all_leds()


if __name__ == '__main__':
  main()


