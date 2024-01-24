# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61043476/how-do-i-fix-a-typeerror-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from Classes.game import player, bcolors
    _l_(565351)

except ImportError:
    pass

magic = [{"name": "Tackle", "cost": 1, "dmg": 4},
         {"name": "Ember", "cost": 3, "dmg": 6},
         {"name": "Leech", "cost": 4, "hp": +5, "dmg": 4},
         {"name": "Explosion", "cost": 5, "hp": -10, "dmg": 30}]
_l_(565352)

_c_(565355, _n_(565353, "player", lambda: player), 100, 20, 5, 10,_n_(565354, "magic", lambda: magic))
_l_(565356)

_c_(565361, _n_(565357, "print", lambda: print), _c_(565360, _a_(565359, _n_(565358, "player", lambda: player), "generate_damage")))
_l_(565362)