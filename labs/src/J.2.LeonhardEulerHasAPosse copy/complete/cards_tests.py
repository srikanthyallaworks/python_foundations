import unittest
from cards import Suites,Suite,Color,Cards,Hands
import sys


class Test_Hands_IsFlush(unittest.TestCase):


  def test_works_for_real_flush(self):
    hand = {Cards.from_string(s) for s in ['♣5','♣6','♣8','♣9','♣10']}
    result = Hands.is_flush(hand)
    self.assertTrue(result)

  def test_works_for_Non_flush(self):
    hand = {Cards.from_string(s) for s in ['♣5','♣6','♣8','♣9','♦10']}
    result = Hands.is_flush(hand)
    self.assertFalse(result)








def run_tests():
  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(sys.modules[__name__])
  runner = unittest.TextTestRunner(verbosity=3)
  runner.run(suite)


if __name__ == '__main__':
    run_tests()
