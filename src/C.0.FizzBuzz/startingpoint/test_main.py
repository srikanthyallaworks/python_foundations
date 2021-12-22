import unittest
from main import to_text


class TestToText(unittest.TestCase):
    """Tests for to_text
    """

    def test_4_should_be_4(self):
        result = to_text(4)
        self.assertEqual("4", result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
