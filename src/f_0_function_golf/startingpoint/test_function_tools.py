import sys
import unittest
from function_tools import make_adder, sort_by_magnitude, pipe, compose, add_all


class TestMakeAdder(unittest.TestCase):
    def test_default_adds_0(self):
        add0 = make_adder()
        self.assertEqual(add0(5), 5)
        self.assertEqual(add0(1928), 1928)

    def test_adds_5(self):
        add5 = make_adder(5)
        self.assertEqual(add5(5), 10)
        self.assertEqual(add5(1), 6)


class TestAddAll(unittest.TestCase):
    def test_adds_2_terms(self):
        actual = add_all(5, 1)
        self.assertEqual(actual, 6)

    def test_adds_3_terms(self):
        actual = add_all(5, 1, 2)
        self.assertEqual(actual, 8)

    def test_adds_4_terms(self):
        actual = add_all(5, 1, 2, 3)
        self.assertEqual(actual, 11)

    def test_adds_5_terms(self):
        actual = add_all(5, 1, 2, 3, 4)
        self.assertEqual(actual, 15)


class TestSortByMagnitude(unittest.TestCase):
    def test_sorts_singleton(self):
        expected = [(1, 1)]
        actual = sort_by_magnitude(expected)
        self.assertEqual(actual, expected)

    def test_sorts_in_order(self):
        original = [
            (1, 1),
            (5, 2),
            (0, 0),
            (10, 10),
        ]
        actual = sort_by_magnitude(original)
        expected = [original[3], original[1], original[0], original[2]]
        self.assertEqual(actual, expected)


class TestPipe(unittest.TestCase):
    def test_single_operation(self):
        operations = (lambda x: x * x,)
        actual = pipe(operations, 5)
        self.assertEqual(actual, 25)

    def test_operation_order(self):
        operations = (lambda x: x * x, lambda x: x + x, lambda x: x - 1)
        actual = pipe(operations, 5)
        self.assertEqual(actual, 49)


class TestCompose(unittest.TestCase):
    def test_square_then_double(self):
        square_then_add = compose(lambda x: x * x, lambda x: x + x)
        actual = square_then_add(5)
        self.assertEqual(actual, 50)

    def test_increment_decrement(self):
        increment_decrement = compose(
            lambda x: x + 1,
            lambda x: x - 1,
            lambda x: x + 1,
            lambda x: x - 1,
        )
        expected = 100
        actual = increment_decrement(expected)
        self.assertEqual(actual, expected)

    def test_typing(self):
        def get_abs(n: int) -> int:
            return abs(n)

        def get_square(n: int) -> int:
            return n * n

        def get_neg(n: int) -> int:
            return abs(n) * -1

        def get_shouty(s: str) -> str:
            return s.capitalize() + "!!!!!"

        # If the type hints are good enough, the line below
        # should be red.
        #
        # (You'll also need to enable type
        # checking in settings.json like this:
        # >   "python.analysis.typeCheckingMode": "basic",
        # )
        #
        # Note: this isn't really a unit test.
        composed = compose(get_abs, get_square, get_neg, get_shouty)
        self.assertIsNotNone(composed)


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
