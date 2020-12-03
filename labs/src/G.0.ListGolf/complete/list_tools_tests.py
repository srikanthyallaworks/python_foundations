import unittest
from list_tools import clone,unique_elements,partition, flatten
import sys



class TestUniqueElements(unittest.TestCase):

  def test_empty_for_empty_array(self):
    result = unique_elements([])
    self.assertEqual(len(result),0)

  def test_same_for_no_repeats(self):
    expected = [1,2,3,4]
    actual = unique_elements(expected)
    self.assertEqual(len(expected),len(actual))

  def test_single_member_for_repeats(self):
    result = unique_elements([1,1,1,1])
    self.assertEqual(result,[1])   

  def test_handles_multiple_duplicates(self):
    result = unique_elements([1,1,2,2,3,3,4,4,4,4,7])
    self.assertEqual(result,[1,2,3,4,7])


class TestClone(unittest.TestCase):

  def test_has_the_same_things(self):
    original = [2,11,'chicken',0,0,None]
    cloned = clone(original)
    self.assertEqual(cloned,original)

  def test_not_the_same_container(self):
    original = [2,11,'chicken',0,0,None]
    cloned = clone(original)
    self.assertFalse(original is cloned)


class TestPartition(unittest.TestCase):

  def test_wraps_for_single_partition(self):
    original = [2,11,'chicken',0,0,None]
    partitions = partition(original,1)
    self.assertEqual(len(partitions),1)
    self.assertEqual(original,partitions[0])

  def test_splits_evenly(self):
    original = ['a','b','c','d','e','f']
    partitions = partition(original,3)
    self.assertEqual(len(partitions),3)

    self.assertEqual(original[0:2],partitions[0])
    self.assertEqual(original[2:4],partitions[1])
    self.assertEqual(original[4:6],partitions[2])


class TestFlatten(unittest.TestCase):

  def test_single_dimension(self):
    expected = [1,2,3,4]
    actual = flatten(expected)
    self.assertEqual(expected,actual)


  def test_lots_of_dimension(self):
    original = [1,[2,3],[],[[4]]]
    actual = flatten(original)
    self.assertEqual(actual, [1,2,3,4])




def run_tests():
  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(sys.modules[__name__])
  runner = unittest.TextTestRunner(verbosity=3)
  runner.run(suite)


if __name__ == '__main__':
    run_tests()
