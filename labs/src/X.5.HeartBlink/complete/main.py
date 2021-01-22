import os
import time
from enum import IntEnum

class Led(IntEnum):
  Zero = 0
  One = 1

class State(IntEnum):
  Off=0
  On=1

def get_path(led:Led):
  return f'/sys/class/leds/led{led.value}'

def setup(led:Led):
  os.system(f'echo gpio | sudo tee {get_path(led)}/trigger > /dev/null')

def set_state(led:Led, state:State):
  os.system(f'echo {state.value} | sudo tee {get_path(led)}/brightness > /dev/null') 

led = Led.One
setup(led)

for _ in range(10):
  set_state(led,State.On)
  time.sleep(.15)
  set_state(led,State.Off)
  time.sleep(.2)
  set_state(led,State.On)
  time.sleep(.2)
  set_state(led,State.Off)
  time.sleep(.6)