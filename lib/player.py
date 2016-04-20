from . import cards

class Player:
    def __init__(self, skills):
        self.skills = skills

    @property
    def skills(self):
        return self.__skills
    @skills.setter
    def skills(self, skills):
        if isinstance(skills, Skills):
            self.__skills = skills
        else:
            raise TypeError('skills property should be of lib.player.Skills type')

    @property
    def hand(self):
        return self.__hand
    @hand.setter
    def hand(self, hand):
        self.__hand = hand

    def play(self, cardindex):
        if (len(self.__hand) > cardindex):
            print('Hand is empty, need to draw more')
        else:
            return self.__hand.pop(cardindex)

class SkillRatings:
    superior = 9
    above_average = 7
    average = 4
    unskilled = 2

    def ParseVal(enum_val):
        if enum_val == 9:
            return 'superior'
        elif enum_val == 7:
            return 'above_average'
        elif enum_val == 4:
            return 'average'
        elif enum_val == 2:
            return 'unskilled'

class Skill:
    def __init__(self, name, rating):
        self.__name = name
        self.rating = rating

    def __str__(self):
        return '{0}: {1} ({2})'.format(self.__name, SkillRatings.ParseVal(self.rating), self.rating)

    def __repr__(self):
        return '{0}: {1} ({2})'.format(self.__name, SkillRatings.ParseVal(self.rating), self.rating)


class Skills:
    def __init__(self):
        self.combative = SkillRatings.unskilled
        self.social = SkillRatings.unskilled
        self.investigative = SkillRatings.unskilled
        self.technical = SkillRatings.unskilled
        self.stealthy = SkillRatings.unskilled
        self.kinetic = SkillRatings.unskilled
        self.vehicular = SkillRatings.unskilled

    @property
    def combative(self):
        return self.__combative.rating
    @combative.setter
    def combative(self, combative):
        self.__validate_skill(combative)
        self.__combative = Skill('combative', combative)

    @property
    def social(self):
        return self.__social.rating
    @social.setter
    def social(self, social):
        self.__validate_skill(social)
        self.__social = Skill('social', social)

    @property
    def investigative(self):
        return self.__investigative.rating
    @investigative.setter
    def investigative(self, investigative):
        self.__validate_skill(investigative)
        self.__investigative = Skill('investigative', investigative)

    @property
    def technical(self):
        return self.__technical.rating
    @technical.setter
    def technical(self, technical):
        self.__validate_skill(technical)
        self.__technical = Skill('technical', technical)

    @property
    def stealthy(self):
        return self.__stealthy.rating
    @stealthy.setter
    def stealthy(self, stealthy):
        self.__validate_skill(stealthy)
        self.__stealthy = Skill('stealthy', stealthy)

    @property
    def kinetic(self):
        return self.__kinetic.rating
    @kinetic.setter
    def kinetic(self, kinetic):
        self.__validate_skill(kinetic)
        self.__kinetic = Skill('kinetic', kinetic)

    @property
    def vehicular(self):
        return self.__vehicular.rating
    @vehicular.setter
    def vehicular(self, vehicular):
        self.__validate_skill(vehicular)
        self.__vehicular = Skill('vehicular', vehicular)

    def __str__(self):
        return str([self.__combative, \
                    self.__social, \
                    self.__investigative, \
                    self.__technical, \
                    self.__stealthy, \
                    self.__kinetic, \
                    self.__vehicular])

    def __repr__(self):
        return str([self.__combative, \
                    self.__social, \
                    self.__investigative, \
                    self.__technical, \
                    self.__stealthy, \
                    self.__kinetic, \
                    self.__vehicular])

    def __validate_skill(self, attributevalue):
        if isinstance(attributevalue, int):
            if attributevalue not in [SkillRatings.superior, SkillRatings.above_average, SkillRatings.average, SkillRatings.unskilled]:
                raise AttributeError('Skill Values Must Correspond to SkillRatings enum')
        else:
            raise TypeError('Skill Values Should be int')

