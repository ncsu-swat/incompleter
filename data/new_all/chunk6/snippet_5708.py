# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55673906/typeerror-str-object-is-not-callable-when-extracting-from-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
game = [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0]]
_l_(363697)

for instructions in _n_(363698, "game", lambda: game):
    _l_(363708)

    for placement in _n_(363699, "instructions", lambda: instructions):
        _l_(363707)

        if 'Stack 6' in _c_(363701, _n_(363700, "placement", lambda: placement)):
            _l_(363706)

            _c_(363704, _n_(363702, "print", lambda: print), _n_(363703, "placement", lambda: placement))
            _l_(363705)