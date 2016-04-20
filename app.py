from lib.cards import Deck
from lib.player import SkillRatings
from lib.player import Skills
from lib.player import Player

def main():
    skills = Skills()
    skills.combative = SkillRatings.superior
    skills.social = SkillRatings.average
    skills.kinetic = SkillRatings.above_average
    skills.technical = SkillRatings.average
    chris = Player(skills)
    print(chris.skills)

    playerdeck = Deck()
    playerdeck.shuffle()

    chris.hand = playerdeck.draw(3)
    print(chris.hand)

    card_index = int(input('Please Select Card to Play:\n[0] {0}\n[1] {1}\n[2] {2}\n'.format(chris.hand[0], chris.hand[1], chris.hand[2])))

    play_card = chris.play(card_index)
    print(play_card)
    print(chris.hand)

if __name__ == '__main__':
    main()
