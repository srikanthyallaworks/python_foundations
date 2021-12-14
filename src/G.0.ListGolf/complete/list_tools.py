
def get_unique_elements(items):
  """Builds a new list using only
     unique members of the original

  Args:
      items (list): List, possibly containing 
        duplicate values

  Returns:
      list: Subset, in the same order, with 
        no duplicates.
  """
  unique_items = []
  for item in items:
    if item not in unique_items:
      unique_items.append(item)
  return unique_items


def get_clone(items):
  """Builds a new list with its 
     contents identical to the specified 
     value.

  Args:
      items (list): Some list

  Returns:
      list: New list with identical contents
  """
  cloned=[]
  for item in items:
    cloned.append(item)
  return cloned



def get_partitions(items,partition_size=2):
  """Divides the specified list into partitions

  Args:
      items (list): Arbitrary list
      partition_size (int, optional): 
        Size of each partition. 
        Defaults to 2.

  Returns:
      list: List of partitions (which are lists)
  """
  partitions = []

  for start in range(0,len(items),partition_size):
    part = items[start:start+partition_size]
    partitions.append(part)

  return partitions



def get_flattened(items):
  """Creates a new, single-dimensional
     containing all the non-list members
     of the specified list.

  Args:
      items (list): List, possibly either
        multi-dimensional or containing
        nested lists.

  Returns:
      [list]: 1 list, same contents, same order,
        no nesting
  """
  flattened = []

  for item in items:
    if isinstance(item,list):
      flattened += get_flattened(item)
    else:
      flattened.append(item)

  return flattened