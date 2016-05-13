# Chris Davis -- 4/22/16
# Views for the Flask app

from flask import url_for, redirect, render_template, request
from app import app
from .models import Pokedex, Abilities, Megaevos
from .DataFormatClasses import formatAbilities, formatNavButtons, formatEvoButtons, formatMegaEvoButtons, \
    formatMegaEvoEntry

# When the base page is loaded it redirects to "/index"
@app.route('/')
def base():
    return redirect(url_for('index'))


# Renders "index.html"
@app.route('/index')
def index():
    # checks search field
    query = request.args.get("search")
    if query:
        return redirect(url_for("dexEntry", name=query.capitalize()))  # redirects to "/pokemon/<name>" sends
                                                                       # capitalized "query" as "name" parameter
    #####################

    return render_template('index.html')


# renders "pokedex.html"
@app.route('/pokedex')
def pokedex():
    #####################
    query = request.args.get("search")
    if query:
        return redirect(url_for("dexEntry", name=query.capitalize()))
    #####################

    dex = Pokedex.query.all()  # pulls all entries from "Pokedex"

    return render_template('pokedex.html', dex=dex)


# Unfinished route -- Will display pokemon native to Kanto region only
# @app.route('/pokedex/kanto')
# def kantodex():
#     return render_template('kantodex.html')


# Unfinished route -- Will display pokemon native to Johto region only
# @app.route('/pokedex/johto')
# def johtodex():
#     return render_template('johtodex.html')


# renders "dexEntry.html" takes pokemon "name" as parameter
@app.route('/pokemon/<name>')
def dexEntry(name):
    #####################
    query = request.args.get("search")
    if query:
        return redirect(url_for("dexEntry", name=query.capitalize()))
    #####################

    pokemon = Pokedex.query.filter_by(name=name).first()  # returns "pokemon" from "Pokedex", searches by "name"

    if pokemon == None:  # if no entry is returned, redirect to "/index"
        return redirect(url_for("index"))

    abilities = formatAbilities(pokemon.ability, pokemon.hidability)  # returns dict "abilities" formated for easier
                                                                      # access inside template
    navButtons = formatNavButtons(pokemon.id)  # returns dict "navButtons", contains names of prev and next pokemon
                                               # for top of page
    evoButtons, multiEvoCheck = formatEvoButtons(pokemon.evoline)  # returns dict "evoButtons" containing the text
                                                                   # for the evolution buttons. Also returns bool
                                                                   # "multiEvoCheck" to identify where dropdown menu is
                                                                   # needed
    try:  # checks for multiple evolutions, CATCHES TypeError when pokemon doesn't evolve
        if len(evoButtons) > 2:
            threeEvos = True
        else:
            threeEvos = False
    except TypeError:
        threeEvos = False

    megaEvo = Megaevos.query.filter_by(id=pokemon.id).all()  # pulls "megaEvo" from "Megaevos", searches by "id"
    megaEvoButtons = formatMegaEvoButtons(megaEvo)  # returns dict "megaEvoButtons"

    return render_template("dexEntry.html", pokemon=pokemon, abilities=abilities, navButtons=navButtons,
                           evoButtons=evoButtons, multiEvoCheck=multiEvoCheck, threeEvos=threeEvos,
                           megaEvoButtons=megaEvoButtons)


# renders "megaDexEntry.html", takes name a parameter
@app.route('/pokemon/mega/<name>')
def megaDexEntry(name):
    #####################
    query = request.args.get("search")
    if query:
        return redirect(url_for("dexEntry", name=query.capitalize()))
    #####################

    megaEvo = Megaevos.query.filter_by(name=name).first()  # loads matching entry from "Megaevos"
    pokemon = Pokedex.query.filter_by(id=megaEvo.id).first()  # loads matching entry from "Pokedex"
    megaPokemon = formatMegaEvoEntry(pokemon, megaEvo)  # joins both entries into one

    ### SEE "dexEntry" FOR RELEVANT COMMENTS###
    abilities = formatAbilities(megaPokemon["ability"], None)
    navButtons = formatNavButtons(pokemon.id)
    evoButtons, multiEvoCheck = formatEvoButtons(pokemon.evoline)
    try:
        if len(evoButtons) > 2:
            threeEvos = True
        else:
            threeEvos = False
    except TypeError:
        threeEvos = False
    megaEvoButtons = formatMegaEvoButtons(megaEvo)
    ##########################################

    return render_template("megaDexEntry.html", pokemon=megaPokemon, abilities=abilities, navButtons=navButtons,
                           evoButtons=evoButtons, multiEvoCheck=multiEvoCheck, megaEvoButtons=megaEvoButtons,
                           threeEvos=threeEvos)


# Renders "abilitiesInfo.html"
@app.route('/abilities')
def abilities():
    abilities = Abilities.query.all()  # loads all entries from "Abilities"

    return render_template("abilitiesInfo.html", abilities=abilities)
