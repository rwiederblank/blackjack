from card import Card
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card: Card):
        self.cards.append(card)

    def get_total(self):
        total = 0
        aces = 0
        for card in self.cards:
            total += card.value
            if card.value == 11:
                aces += 1
        while aces > 0 and total > 21:
            total -= 10
            aces -= 1
        return total

    def show_hand(self):
        result = ""
        for card in self.cards:
            result += str(card) + "\n"
        return result

    def __str__(self):
        return self.show_hand()

