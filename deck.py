from card import Card
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        suits = ["spades", "clubs", "hearts", "diamonds"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        for i in range(4):
            for j in range(13):
                suit = suits[i]
                rank = ranks[j]
                if rank == "Ace":
                    value = 11
                elif rank in ["Jack", "Queen", "King"]:
                    value = 10
                else:
                    value = int(rank)
                self.cards.append(Card(suit, rank, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = random.choice(self.cards)
        self.cards.pop()
        return card

    def cards_remaining(self):
        return len(self.cards)