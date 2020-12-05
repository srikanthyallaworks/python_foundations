import unittest
from cards import Suites,Suite,Color,Cards,Hands,HandRank
import sys


lines = ['5H 5C 6S 7S KD 2C 3S 8S 8D TD',
'5D 8C 9S JS AC 2C 5C 7D 8S QH',
'2D 9C AS AH AC 3D 6D 7D TD QD',
'4D 6S 9H QH QC 3D 6D 7H QD QS',
'2H 2D 4C 4D 4S 3C 3D 3S 9S 9D']




class Test_Hands_IsFlush(unittest.TestCase):

  def test_works_for_real_flush(self):
    hand = Hands.from_string('♣5 ♣6 ♣8 ♣9 ♣T')
    result = Hands.is_flush(hand)
    self.assertTrue(result)

  def test_works_for_Non_flush(self):
    hand = Hands.from_string('♣5 ♣6 ♣8 ♣9 ♦T')
    result = Hands.is_flush(hand)
    self.assertFalse(result)


class Test_Hands_Is_Straight(unittest.TestCase):

  def test_works_for_real_straight(self):
    hand = Hands.from_string('♣5 ♣6 ♦7 ♣8 ♣9')
    result = Hands.is_straight(hand)
    self.assertTrue(result)

  def test_works_for_missed_straight(self):
    hand = Hands.from_string('♣5 ♣6 ♣8 ♣9 ♦T')
    result = Hands.is_straight(hand)
    self.assertFalse(result)




class Test_Hands_Get_Hand_Value(unittest.TestCase):

  def test_high_card_scenario_1(self):
    hand_a = Hands.from_string('♣4 ♥6 ♦7 ♠8 ♣9')
    hand_b = Hands.from_string('♣3 ♥6 ♦7 ♠8 ♣9')

    value_a = Hands.get_hand_value(hand_a)
    value_b = Hands.get_hand_value(hand_b)

    self.assertTrue(value_a>value_b)

  def test_pair_scenario_0(self):
    hand_a = Hands.from_string('♣5 ♥5 ♦9 ♠4 ♣2')
    hand_b = Hands.from_string('♣4 ♥4 ♦A ♠2 ♣T')

    value_a = Hands.get_hand_value(hand_a)
    value_b = Hands.get_hand_value(hand_b)

    self.assertTrue(value_a>value_b)


  def test_pair_scenario_1(self):
    hand_a = Hands.from_string('♣5 ♥5 ♦A ♠2 ♣3')
    hand_b = Hands.from_string('♦5 ♠5 ♣K ♣Q ♣T')

    value_a = Hands.get_hand_value(hand_a)
    value_b = Hands.get_hand_value(hand_b)

    self.assertTrue(value_a>value_b)


  def test_full_house_scenario_0(self):
    hand_a = Hands.from_string('♣A ♥A ♦A ♠Q ♣Q')
    hand_b = Hands.from_string('♦K ♠K ♣K ♣Q ♦Q')
    print(Hands.get_hand_rank(hand_b))

    value_a = Hands.get_hand_value(hand_a)
    value_b = Hands.get_hand_value(hand_b)

    self.assertTrue(value_a>value_b) 

  def test_two_pair_scenario_0(self):
    hand_a = Hands.from_string('♣A ♥A ♦3 ♠2 ♣2')
    hand_b = Hands.from_string('♦K ♠K ♣J ♣Q ♣Q')

    value_a = Hands.get_hand_value(hand_a)
    value_b = Hands.get_hand_value(hand_b)

    self.assertTrue(value_a>value_b)        

  def test_two_pair_scenario_1(self):
    hand_a = Hands.from_string('♣A ♥A ♦3 ♠Q ♣Q')
    hand_b = Hands.from_string('♦A ♠A ♣2 ♣Q ♣Q')

    value_a = Hands.get_hand_value(hand_a)
    value_b = Hands.get_hand_value(hand_b)

    self.assertTrue(value_a>value_b)           


class Test_Hands_Get_Hand_Rank(unittest.TestCase):

  def test_four_of_a_kind(self):
    hand = Hands.from_string('♣5 ♥5 ♦5 ♠5 ♣9')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.FourOfAKind
    self.assertEqual(actual,expected)

  def test_two_pair(self):
    hand = Hands.from_string('♣5 ♥5 ♦2 ♠2 ♣9')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.TwoPair
    self.assertEqual(actual,expected)

  def test_full_house(self):
    hand = Hands.from_string('♣5 ♥5 ♦5 ♠2 ♣2')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.FullHouse
    self.assertEqual(actual,expected)

  def test_straight_flush(self):
    hand = Hands.from_string('♣5 ♣6 ♣7 ♣8 ♣9')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.StraightFlush
    self.assertEqual(actual,expected)    

  def test_trips(self):
    hand = Hands.from_string('♣5 ♥5 ♦5 ♠8 ♣9')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.ThreeOfAKind
    self.assertEqual(actual,expected)     

  def test_pair(self):
    hand = Hands.from_string('♣5 ♥5 ♦2 ♠A ♣J')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.Pair
    self.assertEqual(actual,expected)     

  def test_high_card(self):
    hand = Hands.from_string('♣5 ♥6 ♦2 ♠A ♣J')
    actual = Hands.get_hand_rank(hand)
    expected = HandRank.HighCard
    self.assertEqual(actual,expected)    


def run_tests():
  loader = unittest.TestLoader()
  suite = loader.loadTestsFromModule(sys.modules[__name__])
  runner = unittest.TextTestRunner(verbosity=3)
  runner.run(suite)


if __name__ == '__main__':
    run_tests()
