from random import choice

def choice():
  print("I choo choo choose you!")


result = choice(['Red', 'Desk', 1192, 11.339])

print (result)
exit()

def describe_car(make, model, wheel_count=4,color='oxidized red'):
    """Display information about a car."""
    print(f"\nI have a {make}.")
    print(f"My {make} is a {model}.")

def setup_wheels(car, wheels=[]):
  new_wheels = list(wheels)
  new_wheels += ['wheel1','wheel2']
  print(new_wheels)


def setup_wheels(car, wheels):
  if not wheels:
    wheels = []
  wheels += ['wheel1','wheel2']
  print(wheels)

# def setup_wheels(car, wheels=None):
#   if not wheels:
#     wheels = []
#   wheels += ['wheel1','wheel2']
#   print(wheels)

setup_wheels('truck', wheels = ['wheel0'])
setup_wheels('volvo', [])
setup_wheels('acura',[])
setup_wheels('toyota',[])
setup_wheels('jeep',[])

exit()

class DoVeryLittle:
    # def __len__(self):
    #   return 5
    # def __str__(self):
    #   return f'Very little: 5'
    # def __del__(self):
    #   print('Deleting!!!!')
    def __add__(self, other):
      return 5
    

instance = DoVeryLittle()
total = instance + 8

print(f'Total is {total}')

exit()


from dataclasses import dataclass

@dataclass(frozen=True)
class Color:
  r:int
  g:int
  b:int

  @property
  def hex(self):
      #return f'#{self.r:x}{self.g:x}{self.b:x}'
      return f'{hex(10)}'


interior = Color(250,240,250)

print(interior.hex)

exit()

class Person:
  def __init__(self,age):
    self._age = age

  @property
  def age(self):
    return self._age

  @age.setter
  def age(self, value):
    if value<0:
      raise ValueError('age must be > 0')
    self._age = value




alice = Person(10)
print(f'Alice is {alice.age}')





exit()

class Car:

  def __init__(self,make,model):
    self._make=make
    self._model=model

  @property
  def make(self):
    return self._make


ride = Car('volvo', '240')
print(f'Car is a {ride.make}')



exit()


class Car:
    def __init__(self,make,model):
      self._make=make
      self._model=model    
    
    def drive(self):
        print(f'Just me and my {self._make}')
    
ride = Car('volvo','240')
#ride.drive()

Car.drive(ride)


exit()

class Car:
  def _something_internal(self):
    print("internal")

  def __diagnose(self):
    print("diagnose")

  def drive(self):
    pass

car = Car()
car._Car__diagnose()

# for attr in dir(car):
#   if not attr.endswith('__'):
#     print(attr)









exit()


class Color:
  def __init__(self,red,blue,green):
      self.red=red
      self.blue=blue
      self.green=green    
  def to_hex(self):
      return f'#{self.red:x}{self.green:x}{self.blue:x}'

  @staticmethod
  def from_hex(hex):
      #string parsing here
      return Color(0,0,0)

  @staticmethod
  def from_hsv(h,s,v):
      #string parsing here
      return Color(0,0,0)
  

purple = Color.from_hsv(10,91,1)
brick_red = Color.from_hex('#992938')

purple = Color(128,128,0)
print(purple.to_hex())


exit()

class Car:
  def __init__(self,make,model):
      self.make=make
      self.model=model

  def drive(self):
      print(f'This {self.make} is one sweet ride!')

  @staticmethod
  def from_():
    return ["volvo","chevy"]

print(Car.get_makes())

ride = Car('volvo','240')
ride.get_makes()

#ride.drive()

