# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def move_Spaces_front(str1):
    _l_(68431)

    noSpaces_char = [_n_(68416, "ch", lambda: ch) for ch in _n_(68417, "str1", lambda: str1) if _n_(68418, "ch", lambda: ch) != ' ']
    _l_(68419)
    spaces_char = _c_(68422, _n_(68420, "len", lambda: len), _n_(68421, "str1", lambda: str1)) - _c_(68425, _n_(68423, "len", lambda: len), _n_(68424, "noSpaces_char", lambda: noSpaces_char))
    _l_(68426)
    result = ' ' * _n_(68427, "spaces_char", lambda: spaces_char)
    _l_(68428)
    aux = _n_(68429, "result", lambda: result)
    _l_(68430)
    return aux
_c_(68435, _n_(68432, "print", lambda: print), _c_(68434, _n_(68433, "move_Spaces_front", lambda: move_Spaces_front), 'w3resource .  com  '))
_l_(68436)
_c_(68440, _n_(68437, "print", lambda: print), _c_(68439, _n_(68438, "move_Spaces_front", lambda: move_Spaces_front), '   w3resource.com  '))
_l_(68441)