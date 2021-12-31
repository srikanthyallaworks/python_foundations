import unittest
from main import to_text


class TestToText(unittest.TestCase):
    """Tests for to_text"""

    @staticmethod
    def test_threes_should_fizz():
        expected = "fizz"
        assert to_text(3) == expected
        assert to_text(99) == expected
        assert to_text(33) == expected

    @staticmethod
    def test_fives_should_buzz():
        expected = "buzz"
        assert to_text(5) == expected
        assert to_text(25) == expected

    @staticmethod
    def test_both_should_fizzbuzz():
        expected = "fizzbuzz"
        assert to_text(15) == expected
        assert to_text(90) == expected

    @staticmethod
    def test_primes_should_do_numbers():
        assert to_text(17) == str(17)


if __name__ == "__main__":
    unittest.main(verbosity=2)
