import unittest
from main import to_text


class TestToText(unittest.TestCase):
    """Tests for to_text
    """

    def test_threes_should_fizz(self):
        expected = "fizz"
        self.assertEqual(to_text(3), expected)
        self.assertEqual(to_text(99), expected)
        self.assertEqual(to_text(33), expected)

    def test_fives_should_buzz(self):
        expected = "buzz"
        self.assertEqual(to_text(5), expected)
        self.assertEqual(to_text(25), expected)

    def test_both_should_fizzbuzz(self):
        expected = "fizzbuzz"
        self.assertEqual(to_text(15), expected)
        self.assertEqual(to_text(90), expected)

    def test_primes_should_do_numbers(self):
        self.assertEqual(to_text(17), str(17))


if __name__ == '__main__':
    unittest.main(verbosity=2)
