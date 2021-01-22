import os
import time

class Led:
  def __init__(self,index, previous_trigger):
    self._index=index
    self._is_on=False
    self._is_set_up=False
    self._previous_trigger = previous_trigger
  
  def get_path(self):
    return f'/sys/class/leds/led{self._index}'

  def ensure_setup(self):
    if not self._is_set_up:
      os.system(f'echo gpio | sudo tee {self.get_path()}/trigger > /dev/null')
      self._is_set_up=True

  def toggle(self):
    self.ensure_setup()
    self._is_on= not self._is_on
    os.system(f'echo {int(not self._is_on)} | sudo tee {self.get_path()}/brightness > /dev/null') 

  def __del__(self):
    if not self._is_set_up:
      return
    os.system(f'echo {self._previous_trigger} | sudo tee {self.get_path()}/trigger > /dev/null')

led = Led(1,'mmc0')

for _ in range(10):
  led.toggle()
  time.sleep(.15)
  led.toggle()
  time.sleep(.2)
  led.toggle()
  time.sleep(.2)
  led.toggle()
  time.sleep(.6)