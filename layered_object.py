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