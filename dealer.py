from participant import Participant
from deck import Deck
class Dealer(Participant):
    def __init__(self):
        super().__init__("Dealer")

    def show_first_card(self):
        return str(self.hand.cards[0])

    def take_turn(self, deck: Deck):
        while self.get_total() < 17:
            self.take_card(deck.deal_card())
