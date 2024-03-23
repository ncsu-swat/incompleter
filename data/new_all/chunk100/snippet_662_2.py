# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def move_Spaces_front(str1):
    _l_(68405)

    noSpaces_char = [_n_(68392, "ch", lambda: ch) for ch in _n_(68393, "str1", lambda: str1) if _n_(68394, "ch", lambda: ch) != ' ']
    _l_(68395)
    result = ' ' * _n_(68396, "spaces_char", lambda: spaces_char)
    _l_(68397)
    result = '"' + _n_(68398, "result", lambda: result) + _c_(68401, _a_(68399, '', "join"), _n_(68400, "noSpaces_char", lambda: noSpaces_char)) + '"'
    _l_(68402)
    aux = _n_(68403, "result", lambda: result)
    _l_(68404)
    return aux
_c_(68409, _n_(68406, "print", lambda: print), _c_(68408, _n_(68407, "move_Spaces_front", lambda: move_Spaces_front), 'w3resource .  com  '))
_l_(68410)
_c_(68414, _n_(68411, "print", lambda: print), _c_(68413, _n_(68412, "move_Spaces_front", lambda: move_Spaces_front), '   w3resource.com  '))
_l_(68415)