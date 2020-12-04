import unittest
from cards import Suites,Suite,Color,Cards
import sys


class TestIsFlush(unittest.TestCase):

  def test_works_for_thing(self):
    for s in Cards.build_deck():
      print(s)

    self.assertEqual(0,0)










def run_tests():
  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(sys.modules[__name__])
  runner = unittest.TextTestRunner(verbosity=3)
  runner.run(suite)


if __name__ == '__main__':
    run_tests()
