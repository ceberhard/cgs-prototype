import uuid
import collections

class Card:
    def __init__(self, suit, numval):
        self.suit = suit
        self.numval = numval
        self.__cardnames = ['ace',2,3,4,5,6,7,8,9,10,'jack','queen','king']
        self.name = str(self.__cardnames[numval])

    def __repr__(self):
        return '{0} of {1}'.format(self.name, self.suit)

    def __str__(self):
        return '{0} of {1}'.format(self.name, self.suit)

class Deck:
    def __init__(self):
        self.deck = collections.deque(self.__create_deck())

    def shuffle(self):
        prepdeck = dict([(uuid.uuid4(), card) for card in self.deck])
        shuffledeck = collections.OrderedDict(sorted(prepdeck.items()))
        self.deck = collections.deque([shuffledeck[key] for key in shuffledeck.keys()])

    def draw(self, handsize):
        return [self.deck.popleft() for i in range(handsize)]

    def __create_deck(self):
        suits = ['clubs','diamonds','hearts','spades']
        return [Card(suit, val) for suit in suits for val in range(13)]




