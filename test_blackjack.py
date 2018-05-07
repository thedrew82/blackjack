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

    def test_hand_add_card(self):
        test_hand = blackjack.Hand()
        test_hand.cards = ['Two of Hearts', 'Ace of Spades']
        test_hand.add_card('King of Clubs')
        result = ['Two of Hearts', 'Ace of Spades', 'King of Clubs']
        self.assertEqual(result.sort(), test_hand.cards.sort())

    def test_hand_adjust_ace(self):
        test_hand = blackjack.Hand()
        test_hand.value = 31
        test_hand.adjust_for_ace()
        self.assertEqual(21, test_hand.value)

    def test_chips_win_bet(self):
        test_chips = blackjack.Chips()
        test_chips.total = 100
        test_chips.bet = 20
        test_chips.win_bet()
        self.assertEqual(120, test_chips.total)

    def test_chips_lose_bet(self):
        test_chips = blackjack.Chips()
        test_chips.total = 100
        test_chips.bet = 30
        test_chips.lose_bet()
        self.assertEqual(70, test_chips.total)


if __name__ == '__main__':
    unittest.main()
