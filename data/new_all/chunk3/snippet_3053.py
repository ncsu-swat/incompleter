# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51315053/nameerror-while-trying-to-extend-a-class
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Charmander import *
    _l_(561442)

except ImportError:
    pass
try:
    from Bulbasaur import *
    _l_(561444)

except ImportError:
    pass
try:
    from Turtwig import *
    _l_(561446)

except ImportError:
    pass
class Pokemon:
    _l_(561556)

    def __init__(self, current_hp, attack, defense):
        _l_(561462)

        _n_(561447, "self", lambda: self).name = "PlaceHolder"
        _l_(561448)
        _n_(561449, "self", lambda: self).pokemon_type = "PlaceHolder"
        _l_(561450)
        _n_(561451, "self", lambda: self).current_hp = _n_(561452, "current_hp", lambda: current_hp)
        _l_(561453)
        _n_(561454, "self", lambda: self).attack = _n_(561455, "attack", lambda: attack)
        _l_(561456)
        _n_(561457, "self", lambda: self).defense = _n_(561458, "defense", lambda: defense)
        _l_(561459)
        _n_(561460, "self", lambda: self).fainted = False
        _l_(561461)

    def getName(self):
        _l_(561466)

        aux = _a_(561464, _n_(561463, "self", lambda: self), "name")
        _l_(561465)
        return aux

    def getType(self):
        _l_(561470)

        aux = _a_(561468, _n_(561467, "self", lambda: self), "pokemon_type")
        _l_(561469)
        return aux

    def getCurrentHP(self):
        _l_(561474)

        aux = _a_(561472, _n_(561471, "self", lambda: self), "current_hp")
        _l_(561473)
        return aux

    def getHealth(self):
        _l_(561478)

        aux = _a_(561476, _n_(561475, "self", lambda: self), "current_hp")
        _l_(561477)
        return aux

    def getAttack(self):
        _l_(561482)

        aux = _a_(561480, _n_(561479, "self", lambda: self), "attack")
        _l_(561481)
        return aux

    def getDefense(self):
        _l_(561486)

        aux = _a_(561484, _n_(561483, "self", lambda: self), "defense")
        _l_(561485)
        return aux

    def getFainted(self):
        _l_(561490)

        aux = _a_(561488, _n_(561487, "self", lambda: self), "fainted")
        _l_(561489)
        return aux

    def printStatus(self):
        _l_(561503)

        _c_(561494, _n_(561491, "print", lambda: print), _a_(561493, _n_(561492, "self", lambda: self), "name"))
        _l_(561495)
        _c_(561501, _n_(561496, "print", lambda: print), _c_(561500, _n_(561497, "str", lambda: str), _a_(561499, _n_(561498, "self", lambda: self), "current_hp")))
        _l_(561502)
    def takedamage(self, amount):
        _l_(561507)

        _n_(561504, "self", lambda: self).current_hp -= _n_(561505, "amount", lambda: amount)
        _l_(561506)
    def tackle(self, opponent):
        _l_(561511)

        _n_(561508, "opponent", lambda: opponent).current_hp -= _n_(561509, "self", lambda: self).attack
        _l_(561510)

    def die(self, opponent):
        _l_(561526)

        _n_(561512, "self", lambda: self).fainted = True
        _l_(561513)
        if _a_(561515, _n_(561514, "self", lambda: self), "current_hp") == 0:
            _l_(561525)

            _c_(561517, _n_(561516, "print", lambda: print), "You Lose!")
            _l_(561518)
        elif(_a_(561520, _n_(561519, "opponent", lambda: opponent), "current_hp") == 0):
            _l_(561524)

            _c_(561522, _n_(561521, "print", lambda: print), "You win!")
            _l_(561523)

    def checkDead(self, opponent):
        _l_(561537)

        if _a_(561528, _n_(561527, "self", lambda: self), "current_hp") == 0 or _a_(561530, _n_(561529, "opponent", lambda: opponent), "current_hp") == 0:
            _l_(561536)

            _c_(561534, _a_(561532, _n_(561531, "self", lambda: self), "die"), _n_(561533, "opponent", lambda: opponent))
            _l_(561535)

    def assignPokemon(self, player):
        _l_(561555)

        if _n_(561538, "player", lambda: player) == "Charmander":
            _l_(561542)

            player = _c_(561540, _n_(561539, "Charmander", lambda: Charmander), 200, 20, 20)
            _l_(561541)
        if _n_(561543, "player", lambda: player) == "Bulbasaur":
            _l_(561547)

            player = _c_(561545, _n_(561544, "Bulbasaur", lambda: Bulbasaur), 200, 20, 20)
            _l_(561546)
        if _n_(561548, "player", lambda: player) == "Turtwig":
            _l_(561552)

            player = _c_(561550, _n_(561549, "Turtwig", lambda: Turtwig), 200, 20, 20)
            _l_(561551)
        aux = _n_(561553, "player", lambda: player)
        _l_(561554)
        return aux