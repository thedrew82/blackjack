import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = (
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King',
    'Ace'
)
values = {
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5,
    'Six': 6,
    'Seven': 7,
    'Eight': 8,
    'Nine': 9,
    'Ten': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
    'Ace': 11
}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return ', '.join(str(x) for x in self.deck)

    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        return ', '.join(str(x) for x in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        pass


test_deck = Deck()
test_deck.shuffle()

test_hand = Hand()
test_hand.add_card(test_deck.deal())
test_hand.add_card(test_deck.deal())
test_hand.add_card(test_deck.deal())
test_hand.add_card(test_deck.deal())

print(test_hand)
