import os
import time

led_path='/sys/class/leds/led1'

os.system(f'echo gpio | sudo tee {led_path}/trigger')

for _ in range(10):
  os.system(f'echo 1 | sudo tee {led_path}/brightness') 
  time.sleep(1)
  os.system(f'echo 0 | sudo tee {led_path}/brightness') 
  time.sleep(1)