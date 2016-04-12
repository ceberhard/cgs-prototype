
class Deck:
    def __init__(self):
        self.__initialize_deck()

    def __initialize_deck(self):
        suits = ['clubs','diamonds','hearts','spades']
        self.deck = [(suit, val + 1) for suit in suits for val in range(13)]




