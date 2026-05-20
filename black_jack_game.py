from dealer import Dealer
from deck import Deck
from player import Player

class BlackJackGame:
    def __init__(self, player_name):
        self.player_name = player_name
        self.deck = Deck()
        self.player = Player(player_name)
        self.dealer = Dealer()

    def initial_deal(self):
        self.player.take_card(self.deck.deal_card())
        self.player.take_card(self.deck.deal_card())
        self.dealer.take_card(self.deck.deal_card())
        self.dealer.take_card(self.deck.deal_card())

    def show_game_state(self):
        print(f"Your hand: ")
        print(self.player.show_hand())
        print("Dealer's first card: ")
        print(self.dealer.show_first_card())
        print()

    def determine_winner(self):
        if self.player.is_busted():
            return "Dealer Wins!"
        if self.dealer.is_busted():
            return f"{self.player_name} Wins!"
        if self.player.get_total() > self.dealer.get_total():
            return f"{self.player_name} Wins!"
        if self.dealer.get_total() > self.player.get_total():
            return "Dealer Wins!"
        return "Tie Game!"

    def play(self):
        self.initial_deal()
        self.show_game_state()
        self.player.take_turn(self.deck)
        self.dealer.take_turn(self.deck)
        self.show_game_state()
        print(self.determine_winner())

play_game = BlackJackGame("Ruchama")
play_game.play()
