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
    print(skills)

    chris = Player(skills)
    print(chris.skills)

if __name__ == '__main__':
    main()
