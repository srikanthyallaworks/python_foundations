"""



"""
import math
from typing import List



# /**
#  * @brief Takes a list, returns a new
#  *        list in the same order with no repeated values.
#  * 
#  * @param {Array} xs 
#  */
def get_unique_elements(xs):
  seen = set()

  def already_seen(x):
    if x not in seen:
      seen.add(x)
      return False
    return True

  return [x for x in xs if not already_seen(x)]




# /**
#  * @brief Takes an array, returns a new
#  *        array with the same contents.
#  * 
#  * @param {Array} xs 
#  */
def get_clone(xs):
  return xs[:]



def partition(items,partition_count=1):
  assert partition_count > 0
  assert partition_count < len(items)
  assert (len(items) % partition_count) ==0

  size = int(len(items) / partition_count)  
  return [items[i:i + size] for i in range(0, len(items), size)]



def flatten(items):
  flattened = []

  for item in items:
    if isinstance(item,List):
      flattened += flatten(item)
    else:
      flattened.append(item)

  return flattened