from lib.cards import Deck


def main():
    playercards = Deck()
    print('Player Deck:')
    print(playercards.deck)
    playercards.shuffle()
    print('Shuffled:')
    print(playercards.deck)
    hand = playercards.draw(3)
    print('Hand:')
    print(hand)
    print('New Deck')
    print(playercards.deck)

if __name__ == '__main__':
    main()
