from neopixel import *

red = Color(255,0,0)
green = Color(0,255,0)
blue = Color(0,0,255)
yellow = Color(255,255,0)
pink = Color(0,255,255)
cyan = Color(255,0,255)
white = Color(255,255,255)
off = Color(0,0,0)

all_colors = [red, green, blue, yellow, pink, cyan, white]

def multi_color_echo(layers = 5, off_layers = 6):
  simple_color_preset = []
  for c in all_colors:
    for m in range(0, layers):
      simple_color_preset.append(c)
    for m in range(0, off_layers):
      simple_color_preset.append(off)
  return simple_color_preset

def single_color_echo(input_color = red, layers = 5, off_layers = 6):
  simple_color_preset = []
  for m in range(0, layers):
    simple_color_preset.append(input_color)
  for m in range(0, off_layers):
    simple_color_preset.append(off)
  return simple_color_preset

