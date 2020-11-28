import unittest
from main import get_euler02_solution


class TestGetEuler02Solution(unittest.TestCase):

    def test_solution_shoud_be_4613732(self):
        expected = 4613732
        actual = get_euler02_solution()
        assert actual==expected

if __name__ == '__main__':
    unittest.main(verbosity=2)
