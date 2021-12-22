import unittest
try:
    from .main import toText
except:
    from main import toText


class TestToText(unittest.TestCase):

    def test_4_should_be_4(self):
        result = toText(4)
        self.assertEqual("4", result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
