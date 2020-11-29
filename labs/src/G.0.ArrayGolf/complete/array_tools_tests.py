import unittest
from array_tools import areEquivalentArrays,unique_elements


class TestAreEquivalentArrays(unittest.TestCase):

  def test_true_for_empty_arrays(self):
    areEquivalent = areEquivalentArrays([],[])
    self.assertTrue(areEquivalent)

  def test_false_for_different_length_arrays(self):
    areEquivalent = areEquivalentArrays([1,2,3],[1,2,3,4])
    self.assertFalse(areEquivalent)

  def test_false_for_different_contents(self):
    areEquivalent = areEquivalentArrays([1,2,3],[1,2,4])
    self.assertFalse(areEquivalent)

  def test_true_for_same_contents(self):
    areEquivalent = areEquivalentArrays([1,2,3],[1,2,3])
    self.assertTrue(areEquivalent)


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
    self.assertEqual(len(result),0)    

  def test_handles_multiple_duplicates(self):
    result = unique_elements([1,1,2,2,3,3,4,4,4,4,7])
    self.assertEqual(result,[1,2,3,4,7])



def run_tests():
    print('x')
    unittest.main(verbosity=2)
    print('y')


if __name__ == '__main__':
    run_tests()
