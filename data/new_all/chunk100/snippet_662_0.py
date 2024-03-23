# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def move_Spaces_front(str1):
    _l_(68352)

    spaces_char = _c_(68338, _n_(68336, "len", lambda: len), _n_(68337, "str1", lambda: str1)) - _c_(68341, _n_(68339, "len", lambda: len), _n_(68340, "noSpaces_char", lambda: noSpaces_char))
    _l_(68342)
    result = ' ' * _n_(68343, "spaces_char", lambda: spaces_char)
    _l_(68344)
    result = '"' + _n_(68345, "result", lambda: result) + _c_(68348, _a_(68346, '', "join"), _n_(68347, "noSpaces_char", lambda: noSpaces_char)) + '"'
    _l_(68349)
    aux = _n_(68350, "result", lambda: result)
    _l_(68351)
    return aux
_c_(68356, _n_(68353, "print", lambda: print), _c_(68355, _n_(68354, "move_Spaces_front", lambda: move_Spaces_front), 'w3resource .  com  '))
_l_(68357)
_c_(68361, _n_(68358, "print", lambda: print), _c_(68360, _n_(68359, "move_Spaces_front", lambda: move_Spaces_front), '   w3resource.com  '))
_l_(68362)