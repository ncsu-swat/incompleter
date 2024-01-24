# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55673906/typeerror-str-object-is-not-callable-when-extracting-from-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
game = [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0]]
_l_(369391)

for instructions in _n_(369392, "game", lambda: game):
    _l_(369402)

    for placement in _n_(369393, "instructions", lambda: instructions):
        _l_(369401)

        if 'Stack 6' in _c_(369395, _n_(369394, "placement", lambda: placement)):
            _l_(369400)

            _c_(369398, _n_(369396, "print", lambda: print), _n_(369397, "placement", lambda: placement))
            _l_(369399)