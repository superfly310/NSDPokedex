from app import db

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    species = db.Column(db.Text)
    poketype = db.Column(db.Text)
    ability = db.Column(db.Text)
    hidability = db.Column(db.Text)
    evoline = db.Column(db.Text)
    mega = db.Column(db.Text)
    image = db.Column(db.Text)
    descrip = db.Column(db.Text)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sattack = db.Column(db.Integer)
    sdefense = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __repr__(self):
        return "<Pokemon %r>" % (self.name)


class Abilities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ability = db.Column(db.Text)
    descrip = db.Column(db.Text)

    def __repr__(self):
        return '<Ability %r>' % (self.ability)


class Megaevos(db.Model):
    id = db.Column(db.Integer)
    name = db.Column(db.Text, primary_key=True)
    type = db.Column(db.Text)
    ability = db.Column(db.Text)
    stone = db.Column(db.Text)
    image = db.Column(db.Text)
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    sattack = db.Column(db.Integer)
    sdefense = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    total = db.Column(db.Integer)

    def __repr__(self):
        return '<MegaEvos %r>' % (self.name)
