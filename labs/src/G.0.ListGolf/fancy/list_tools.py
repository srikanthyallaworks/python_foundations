"""



"""
import math
from typing import List



def get_unique_elements(xs):
  seen = set()

  def already_seen(x):
    if x not in seen:
      seen.add(x)
      return False
    return True

  return [x for x in xs if not already_seen(x)]


def get_clone(xs):
  return xs[:]


def get_partitions(items,partition_count=1):
  assert partition_count > 0
  assert partition_count < len(items)
  assert (len(items) % partition_count) ==0

  size = int(len(items) / partition_count)  
  return [items[i:i + size] for i in range(0, len(items), size)]



def get_flattened(items):
  flattened = []

  for item in items:
    if isinstance(item,List):
      flattened += get_flattened(item)
    else:
      flattened.append(item)

  return flattened