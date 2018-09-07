def turn_off_all_leds():
  set_leds_in_range((0,LED_COUNT), Color(0,0,0))
  strip.show()

def set_leds_in_range(input_range, color):
  for x in range(input_range[0], input_range[1]):
    strip.setPixelColor(x, color)