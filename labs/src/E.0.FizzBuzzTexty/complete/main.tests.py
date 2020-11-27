import unittest 
from main import toText

class TestToText(unittest.TestCase):
    def test_threes_should_fizz(self):
        expected = "fizz"
        assert toText(3) == expected
        assert toText(99) == expected
        assert toText(33) == expected

    def test_fives_should_buzz(self):
        expected = "buzz"
        assert toText(5) == expected
        assert toText(25) == expected

    def test_both_should_fizzbuzz(self):
        expected = "fizzbuzz"
        assert toText(15) == expected
        assert toText(90) == expected

    def test_primes_should_do_numbers(self):
        assert toText(17) == str(17)

if __name__ == '__main__':
    unittest.main(verbosity=2)
