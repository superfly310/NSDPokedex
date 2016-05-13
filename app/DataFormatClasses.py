# Chris Davis -- 4/24/16
# DataFormatClasses -- methods that format various information from database so it is more usable

from .models import Pokedex


def formatAbilities(abilityRaw, hidability):
    abilitySplit = abilityRaw.split("/")

    try:
        return {"ability1": abilitySplit[0], "ability2": abilitySplit[1], "ability3": hidability}
    except IndexError:
        return {"ability1": abilityRaw, "ability2": None, "ability3": hidability}

def formatNavButtons(id):
    prevPoke = Pokedex.query.filter_by(id=id-1).first()
    nextPoke = Pokedex.query.filter_by(id=id+1).first()

    if prevPoke == None:
        prevPoke = Pokedex.query.filter_by(id=251).first()
    if nextPoke == None:
        nextPoke = Pokedex.query.filter_by(id=1).first()

    return {"prev": prevPoke.name, "next": nextPoke.name}

def formatEvoButtons(evoLine):
    print(evoLine)
    evoButtons = {}

    if evoLine is None:
        return None, False

    i = 0
    multiEvoCheck = False
    for e in evoLine.split("/"):
        multiEvo = e.split(":")
        if len(multiEvo) > 1:
            multiEvoList = []
            for m in multiEvo:
                multiEvoList.append(m)
            evoButtons.update({"evo"+str(i):multiEvoList})
            multiEvoCheck = i
        else:
            evoButtons.update({"evo"+str(i):e})

        i += 1

    print(evoButtons)
    return evoButtons, multiEvoCheck

def formatMegaEvoButtons(megaEvo):
    if not megaEvo:
        return None

    try:
        return {"evo1": megaEvo[0].name, "evo2": megaEvo[1].name}
    except IndexError:
        return {"evo1": megaEvo[0].name}
    except TypeError:
        return {"evo1": megaEvo.name}

def formatMegaEvoEntry(pokemon, mega):
    return {
        "id": pokemon.id,
        "name": "Mega " + mega.name,
        "species": pokemon.species,
        "poketype": mega.type,
        "ability": mega.ability,
        "evoline": pokemon.evoline,
        "mega": True,
        "image": mega.image,
        "descrip": pokemon.descrip,
        "hp": mega.hp,
        "attack": mega.attack,
        "defense": mega.defense,
        "sattack": mega.sattack,
        "sdefense": mega.sdefense,
        "speed": mega.speed,
        "stone": mega.stone
    }