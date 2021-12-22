
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
    return items


def get_clone(items):
    """Builds a new list with its
       contents identical to the specified
       value.

    Args:
        items (list): Some list

    Returns:
        list: New list with identical contents
    """
    return items


def get_partitions(items, partition_size=2):
    # pylint: disable=unused-argument
    """Divides the specified list into partitions

    Args:
        items (list): Arbitrary list
        partition_size (int, optional):
          Size of each partition.
          Defaults to 2.

    Returns:
        list: List of partitions (which are lists)
    """
    return [items]


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
    return items
