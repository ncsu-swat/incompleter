# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def move_Spaces_front(str1):
    _l_(68381)

    noSpaces_char = [_n_(68363, "ch", lambda: ch) for ch in _n_(68364, "str1", lambda: str1) if _n_(68365, "ch", lambda: ch) != ' ']
    _l_(68366)
    spaces_char = _c_(68369, _n_(68367, "len", lambda: len), _n_(68368, "str1", lambda: str1)) - _c_(68372, _n_(68370, "len", lambda: len), _n_(68371, "noSpaces_char", lambda: noSpaces_char))
    _l_(68373)
    result = '"' + _n_(68374, "result", lambda: result) + _c_(68377, _a_(68375, '', "join"), _n_(68376, "noSpaces_char", lambda: noSpaces_char)) + '"'
    _l_(68378)
    aux = _n_(68379, "result", lambda: result)
    _l_(68380)
    return aux
_c_(68385, _n_(68382, "print", lambda: print), _c_(68384, _n_(68383, "move_Spaces_front", lambda: move_Spaces_front), 'w3resource .  com  '))
_l_(68386)
_c_(68390, _n_(68387, "print", lambda: print), _c_(68389, _n_(68388, "move_Spaces_front", lambda: move_Spaces_front), '   w3resource.com  '))
_l_(68391)