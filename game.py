from pokemon import Pokemon
from trainer import Trainer

k = Trainer("Kenzie",1)

badass = Pokemon("Badass",1,5,1)
badass.displayPokemon()

chuck = Pokemon("Chuck Norris",4,5,1)
chuck.displayPokemon()

badass.defeatPokemon(chuck)
badass.displayStats()