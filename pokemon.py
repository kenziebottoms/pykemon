from pokedex import Pokedex
from trainer import Trainer
import random

class Pokemon:

    def __init__(self, nickname, species, level, idNo):
        self.nickname = nickname
        self.species = species
        self.idNo = idNo

        self.level = level
        self.ev = 0
        self.iv = random.randint(0,31)
        self.exp = 0
        self.generateStats()

    def generateStats(self):
        iv = float(self.iv)
        ev = float(self.ev)
        level = float(self.level)
        self.hp = int((iv + 2*float(Pokedex.hp[self.species]) + ev/4) * (level/100) + 10 + level)
        self.attack = int((iv + float(2*Pokedex.attack[self.species]) + ev/4) * (level/100) + 5)
        self.defense = int((iv + 2*float(Pokedex.defense[self.species]) + ev/4) * (level/100) + 5)
        self.spAtt = int((iv + 2*float(Pokedex.spAtt[self.species]) + ev/4) * (level/100) + 5)
        self.spDef = int((iv + 2*float(Pokedex.spDef[self.species]) + ev/4) * (level/100) + 5)
        self.speed = int((iv + 2*float(Pokedex.speed[self.species]) + ev/4) * (level/100) + 5)

    def expUp(self, amt):
        self.exp += amt
        while self.exp >= pow(self.level,3):
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.generateStats()

    def defeatPokemon(self, opponent):
        self.ev += Pokedex.ev[self.species]
        if self.idNo == 0:
            wild = 1
        else:
            wild = 1.5
        exp = int(float(wild * Pokedex.exp[opponent.species] * opponent.level)/7.0)
        self.expUp(exp)

    def displayPokemon(self):
        print self.nickname, "the", Pokedex.names[self.species], "(lv.", str(self.level)+")"
        print

    def displayStats(self):
        self.displayPokemon()
        print "\tType 1:",Pokedex.types[Pokedex.type1[self.species]],
        print "\tType 2:",Pokedex.types[Pokedex.type2[self.species]]
        print "\tLevel:\t\t",self.level
        print "\tIV:\t\t",self.iv
        print "\tEV:\t\t",self.ev
        print "\tHP:\t\t",self.hp
        print "\tAttack:\t\t",self.attack
        print "\tDefense:\t",self.defense
        print "\tSp. Attack:\t",self.spAtt
        print "\tSp. Defense:\t",self.spDef
        print "\tSpeed:\t\t",self.speed
        print "\tExp.:\t\t",self.exp,"out of",str(pow(self.level,3))
        print