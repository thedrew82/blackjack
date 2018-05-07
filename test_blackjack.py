import unittest
import blackjack


class TestBlackJack(unittest.TestCase):

    def test_card_str(self):
        text = 'Two of Hearts'
        result = str(blackjack.Card('Hearts', 'Two'))
        self.assertEqual(result, text)

    def test_card_value(self):
        value = 4
        card = blackjack.Card('Diamonds', 'Four')
        self.assertEqual(card.value, value)

    def test_deck_init(self):
        self.assertEqual(len(blackjack.Deck()), 52)

    def test_deck_shuffle(self):
        test_deck = blackjack.Deck()
        self.assertIsNone(test_deck.shuffle())

    def test_deck_deal(self):
        test_deck = blackjack.Deck()
        result = str(test_deck.deal())
        text = 'Ace of Clubs'
        self.assertEqual(result, text)

    def test_hand_adjust_ace(self):
        test_hand = blackjack.Hand()
        test_hand.value = 31
        test_hand.cards = ['Two of Hearts', 'Ace of Spades']
        self.assertEqual(21, test_hand.adjust_for_ace())


if __name__ == '__main__':
    unittest.main()
