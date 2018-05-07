import random
import yaml


def load_config(file):
    with open(file) as f:
        return yaml.safe_load(f)


house = load_config('house.yaml')
suits = tuple(house['suits'])
ranks = tuple(house['ranks'])
values = house['values']


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

    def add_card(self, card):
        self.cards.append(card)

    def adjust_for_ace(self):
        aces = ('Ace of Clubs', 'Ace of Hearts', 'Ace of Diamonds', 'Ace of Spades')
        for card in self.cards:
            if card in aces:
                result = self.value - 10
                return result
