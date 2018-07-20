class Trainer:

    def __init__(self, name, idNo):
        self.name = name
        self.idNo = idNo
        self.party = []
        self.pc = []

    def addPokemon(self, pokemon):
        if len(self.party) < 6:
            self.party.append(pokemon)
        else:
            print "Party's too big. Into the PC it goes."
            self.pc.append(pokemon)