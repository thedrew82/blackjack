import random
import yaml


def load_cards(file):
    with open(file) as f:
        data = yaml.safe_load(f)
        s = tuple(data['suits'])
        r = tuple(data['ranks'])
        v = data['values']
        return s, r, v


(suits, ranks, values) = load_cards('house.yaml')


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
        self.aces = 0
        self.value = 0

    def __str__(self):
        return ', '.join(str(x) for x in self.cards)

    def add_card(self, card):
        self.cards.append(card)

    def check_for_ace(self):
        ace = ('Ace of Clubs', 'Ace of Spades', 'Ace of Hearts', 'Ace of Diamonds')
        for card in self.cards:
            if card in ace:
                self.aces += 1

    def adjust_for_ace(self):
        self.value = self.value - 10


class Chips:

    def __init__(self):
        self.total = 0
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total = self.total - self.bet


def take_bet(total):
    while True:
        try:
            b = int(input(f'Enter your bet: [max {total}] '))
            if b <= total:
                return b
            else:
                raise ValueError()
        except ValueError:
            print('Invalid bet, please bet again.\n')
            continue


def hit(deck, hand):
    hand.add_card(deck.deal())


def get_hand_value(hand):
    hand.value = 0
    for card in hand.cards:
        hand.value += card.value


def hit_or_stand(deck, hand):
    global playing

    try:
        action = input(f'Hit or Stand? [H/s]\n').lower()
        if action == 'hit' or action == 'h':
            hit(deck, hand)
            playing = True
        elif action == 'stand' or action == 's':
            playing = False
        elif not action:
            hit(deck, hand)
        else:
            raise ValueError()
    except ValueError:
        print('Invalid action, please try again.\n')


if __name__ == '__main__':
    my_deck = Deck()
    my_deck.shuffle()
    my_chips = Chips()
    my_chips.total = 100
    my_hand = Hand()
    my_hand.add_card(my_deck.deal())
    my_hand.add_card(my_deck.deal())
    while True:
        take_bet(my_chips.total)
        get_hand_value(my_hand)
        print(my_hand)
        print(my_hand.value)
        hit_or_stand(my_deck, my_hand)

        while playing:
            hit_or_stand(my_deck, my_hand)
            get_hand_value(my_hand)
            print(my_hand)
            print(my_hand.value)

        if my_hand.value == 21:
            print('WIN!')
        elif my_hand.value > 21:
            print('BUST!')
        else:
            print(my_hand.value)

        break
