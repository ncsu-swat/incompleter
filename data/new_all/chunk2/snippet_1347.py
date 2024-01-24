# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20126320/attribute-error-int-object-has-no-attribute-choice
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
while _n_(441499, "health_1", lambda: health_1) > 0 and _n_(441500, "health", lambda: health) > 0 and _n_(441501, "stamina", lambda: stamina) > 0:
    _l_(441534)

    random = _c_(441505, _a_(441503, _n_(441502, "random", lambda: random), "choice"), _n_(441504, "accuracy", lambda: accuracy))
    _l_(441506)
    if _n_(441507, "random", lambda: random) != "0":
        _l_(441533)

        _c_(441510, _n_(441508, "print", lambda: print), "\n\n", _n_(441509, "random", lambda: random))
        _l_(441511)
        _c_(441514, _n_(441512, "print", lambda: print), "\nYou manage to hit the creature for", _n_(441513, "dmg", lambda: dmg), "damage!")
        _l_(441515)
        health_1 -= _n_(441516, "dmg", lambda: dmg)
        _l_(441517)
        stamina -= _n_(441518, "stam_loss", lambda: stam_loss)
        _l_(441519)
        _c_(441522, _n_(441520, "print", lambda: print), "The creature now has", _n_(441521, "health_1", lambda: health_1), "health")
        _l_(441523)
        _c_(441525, _n_(441524, "print", lambda: print), "\nThe creature hits you for 1 damage!")
        _l_(441526)
        health -= 1
        _l_(441527)
        _c_(441531, _n_(441528, "print", lambda: print), "Health:", _n_(441529, "health", lambda: health), "Stamina:", _n_(441530, "stamina", lambda: stamina),) 
        _l_(441532) 