import unittest
import blackjack


class TestBlackJackCard(unittest.TestCase):

    def test_str(self):
        text = 'Two of Hearts'
        result = str(blackjack.Card('Hearts', 'Two'))
        self.assertEqual(result, text)

    def test_value(self):
        value = 4
        card = blackjack.Card('Diamonds', 'Four')
        self.assertEqual(card.value, value)


class TestBlackJackDeck(unittest.TestCase):

    def test_init(self):
        self.assertEqual(len(blackjack.Deck()), 52)

    def test_shuffle(self):
        test_deck = blackjack.Deck()
        self.assertIsNone(test_deck.shuffle())

    def test_deal(self):
        test_deck = blackjack.Deck()
        result = str(test_deck.deal())
        text = 'Ace of Clubs'
        self.assertEqual(result, text)


class TestBlackJackHand(unittest.TestCase):

    def test_add_card(self):
        test_hand = blackjack.Hand()
        test_hand.cards = ['Two of Hearts', 'Ace of Spades']
        test_hand.add_card('King of Clubs')
        result = ['Two of Hearts', 'Ace of Spades', 'King of Clubs']
        self.assertEqual(result.sort(), test_hand.cards.sort())

    def test_check_ace(self):
        test_hand = blackjack.Hand()
        test_hand.cards = ['Ace of Hearts', 'Ace of Spades']
        test_hand.check_for_ace()
        self.assertEqual(2, test_hand.aces)

    def test_adjust_ace(self):
        test_hand = blackjack.Hand()
        test_hand.value = 31
        test_hand.adjust_for_ace()
        self.assertEqual(21, test_hand.value)


class TestBlackJackChips(unittest.TestCase):

    def test_win_bet(self):
        test_chips = blackjack.Chips()
        test_chips.total = 100
        test_chips.bet = 20
        test_chips.win_bet()
        self.assertEqual(120, test_chips.total)

    def test_lose_bet(self):
        test_chips = blackjack.Chips()
        test_chips.total = 100
        test_chips.bet = 30
        test_chips.lose_bet()
        self.assertEqual(70, test_chips.total)


if __name__ == '__main__':
    unittest.main()
