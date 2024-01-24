# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47064968/attributeerror-nonetype-object-has-no-attribute-foo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import player
    _l_(592848)

except ImportError:
    pass
Dice = _c_(592851, _a_(592850, _n_(592849, "random", lambda: random), "randrange"), 1, 7)
_l_(592852)
set_p_w = _c_(592855, _a_(592854, _n_(592853, "player", lambda: player), "set_player_weapon"))
_l_(592856)
PlayerDamage = _n_(592857, "Dice", lambda: Dice) * _a_(592859, _n_(592858, "set_p_w", lambda: set_p_w), "player_damage")
_l_(592860)