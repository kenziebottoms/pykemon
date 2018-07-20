class Pokedex:
    
    # dictionaries
    names = ['','Bulbasaur','Ivysaur','Venusaur','Charmander','Charmeleon','Charizard']
    types = ['Normal','Fire','Fighting','Water','Flying',           # 0-4
                'Grass','Poison','Electric','Ground','Psychic',     # 5-9
                'Rock','Ice','Bug','Dragon','Ghost',                # 10-14
                'Dark','None']                                      # 15-16

    # types
    type1 = [16,5,5,5,1,1,1]
    type2 = [16,6,6,6,16,16,4]
    
    # base stats
    hp = [0,45,60,80,39,58,78]
    attack = [0,49,62,82,52,64,84]
    defense = [0,49,63,83,43,58,78]
    spAtt = [0,65,80,100,60,80,109]
    spDef = [0,65,80,100,50,65,85]
    speed = [0,45,60,80,65,80,100]

    # ev return values
    ev = [0,1,2,3,1,2,3]
    exp = [0,64,142,236,62,142,240]