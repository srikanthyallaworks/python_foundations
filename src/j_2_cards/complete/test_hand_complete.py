import unittest
import sys
from hand import Hands, HandRank


lines = [
    "5H 5C 6S 7S KD 2C 3S 8S 8D TD",
    "5D 8C 9S JS AC 2C 5C 7D 8S QH",
    "2D 9C AS AH AC 3D 6D 7D TD QD",
    "4D 6S 9H QH QC 3D 6D 7H QD QS",
    "2H 2D 4C 4D 4S 3C 3D 3S 9S 9D",
]


def string_to_value(value: str):
    hand = Hands.from_string(value)
    return Hands.get_hand_value(hand)


class Test_Hands_Get_Hand_Value(unittest.TestCase):
    def test_high_card_scenario_1(self):
        a = string_to_value("♣4 ♥6 ♦7 ♠8 ♣9")
        b = string_to_value("♣3 ♥6 ♦7 ♠8 ♣9")

        self.assertTrue(a > b)

    def test_pair_scenario_0(self):
        a = string_to_value("♣5 ♥5 ♦9 ♠4 ♣2")
        b = string_to_value("♣4 ♥4 ♦A ♠2 ♣T")

        self.assertTrue(a > b)

    def test_pair_scenario_1(self):
        a = string_to_value("♣5 ♥5 ♦A ♠2 ♣3")
        b = string_to_value("♦5 ♠5 ♣K ♣Q ♣T")

        self.assertTrue(a > b)

    def test_full_house_scenario_0(self):
        a = string_to_value("♣A ♥A ♦A ♠Q ♣Q")
        b = string_to_value("♦K ♠K ♣K ♣Q ♦Q")

        self.assertTrue(a > b)

    def test_two_pair_scenario_0(self):
        a = string_to_value("♣A ♥A ♦3 ♠2 ♣2")
        b = string_to_value("♦K ♠K ♣J ♣Q ♣Q")

        self.assertTrue(a > b)

    def test_two_pair_scenario_1(self):
        a = string_to_value("♣A ♥A ♦3 ♠Q ♣Q")
        b = string_to_value("♦A ♠A ♣2 ♣Q ♣Q")

        self.assertTrue(a > b)


def string_to_rank(value: str):
    hand = Hands.from_string(value)
    return Hands.get_hand_rank(hand)


class Test_Hands_Get_Hand_Rank(unittest.TestCase):
    def test_four_of_a_kind(self):
        actual = string_to_rank("♣5 ♥5 ♦5 ♠5 ♣9")
        expected = HandRank.FourOfAKind
        self.assertEqual(actual, expected)

    def test_two_pair(self):
        actual = string_to_rank("♣5 ♥5 ♦2 ♠2 ♣9")
        expected = HandRank.TwoPair
        self.assertEqual(actual, expected)

    def test_full_house(self):
        actual = string_to_rank("♣5 ♥5 ♦5 ♠2 ♣2")
        expected = HandRank.FullHouse
        self.assertEqual(actual, expected)

    def test_straight_flush(self):
        actual = string_to_rank("♣5 ♣6 ♣7 ♣8 ♣9")
        expected = HandRank.StraightFlush
        self.assertEqual(actual, expected)

    def test_trips(self):
        actual = string_to_rank("♣5 ♥5 ♦5 ♠8 ♣9")
        expected = HandRank.ThreeOfAKind
        self.assertEqual(actual, expected)

    def test_pair(self):
        actual = string_to_rank("♣5 ♥5 ♦2 ♠A ♣J")
        expected = HandRank.Pair
        self.assertEqual(actual, expected)

    def test_high_card(self):
        actual = string_to_rank("♣5 ♥6 ♦2 ♠A ♣J")
        expected = HandRank.HighCard
        self.assertEqual(actual, expected)


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)


if __name__ == "__main__":
    run_tests()
