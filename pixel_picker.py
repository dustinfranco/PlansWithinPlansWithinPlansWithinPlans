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
 
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
strip.begin()

def turn_off_all_leds():
  set_leds_in_range((0,LED_COUNT), Color(0,0,0))
  strip.show()

def set_leds_in_range(input_range, color):
  for x in range(input_range[0], input_range[1]):
    strip.setPixelColor(x, color)

def pixel_picking(colors = [], wait_ms=50):
  try:
    colors = [Color(160,0,0),Color(0,160,0),Color(0,0,160)]
    while(1):
      for color in colors:
        x = input("which pixel?")
	strip.setPixelColor(x,color)
	strip.show()	  
  except Exception as e:
    print(e)

def main():
    try:
        print("start")        
	pixel_picking()
    finally:
	turn_off_all_leds()


if __name__ == '__main__':
  main()


