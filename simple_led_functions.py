from hardware_configuration import *
from neopixel import *


def turn_off_all_leds(strip):
  set_leds_in_range(strip, (0,LED_COUNT), Color(0,0,0))
  strip.show()

def set_leds_in_range(strip, input_range, color):
  for x in range(input_range[0], input_range[1]):
    strip.setPixelColor(x, color)
