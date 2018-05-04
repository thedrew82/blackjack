import unittest
import blackjack


class TestBlackJack(unittest.TestCase):

    def test_str_card(self):
        text = 'Two of Hearts'
        result = str(blackjack.Card('Hearts', 'Two'))
        self.assertEqual(result, text)

    def test_value_card(self):
        value = 4
        card = blackjack.Card('Diamonds', 'Four')
        self.assertEqual(card.value, value)

    def test_init_deck(self):
        self.assertEqual(len(blackjack.Deck()), 52)

    def test_shuffle_deck(self):
        test_deck = blackjack.Deck()
        self.assertIsNone(test_deck.shuffle())

    def test_deal_deck(self):
        test_deck = blackjack.Deck()
        result = str(test_deck.deal())
        text = 'Ace of Clubs'
        self.assertEqual(result, text)


if __name__ == '__main__':
    unittest.main()
