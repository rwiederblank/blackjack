from hand import Hand
from card import Card
from deck import Deck
class Participant:
    def __init__(self, name: str):
        self.name = name
        self.hand = Hand()

    def take_card(self, card: Card):
        self.hand.add_card(card)

    def show_hand(self):
        return self.hand.show_hand()

    def get_total(self):
        return self.hand.get_total()

    def is_busted(self):
        total = self.get_total()
        if total > 21:
            return True
        else:
            return False
    def take_turn(self, deck: Deck):
        pass
