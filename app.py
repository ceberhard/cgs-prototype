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

    playcard = chris.play(2)
    print(playcard)

    print(chris.hand)




if __name__ == '__main__':
    main()
