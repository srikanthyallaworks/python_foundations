
def get_unique_elements(xs):
  uniques = []
  for x in xs:
    if x not in uniques:
      uniques.append(x)
  return uniques


def get_clone(xs):
  cloned=[]
  for x in xs:
    cloned.append(x)
  return cloned



def get_partitions(items,partition_count=1):
  assert partition_count > 0
  assert partition_count < len(items)
  assert (len(items) % partition_count) ==0
  partitions = []
  size = int(len(items) / partition_count)
  
  for i in range(partition_count):
    starting_at = i*size
    part = items[starting_at:starting_at+size]
    partitions.append(part)

  return partitions



def get_flattened(items):
  flattened = []

  for item in items:
    if isinstance(item,list):
      flattened += get_flattened(item)
    else:
      flattened.append(item)

  return flattened