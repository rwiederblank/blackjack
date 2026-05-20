from participant import Participant
from deck import Deck
class Player(Participant):
    def __init__(self, name: str):
        super().__init__(name)

    def take_turn(self, deck: Deck):
        busted = False
        while not busted:
            print(f"Your total: {self.get_total()}")
            users_choice = ""
            while True:
                choice = input("Hit or Stand? ")
                if choice.lower().strip() != "hit" and choice.lower().strip() != "stand":
                    continue
                users_choice = choice.lower().strip()
                break
            if users_choice == "hit":
                self.take_card(deck.deal_card())
                if self.is_busted():
                    break
            else:
                break
