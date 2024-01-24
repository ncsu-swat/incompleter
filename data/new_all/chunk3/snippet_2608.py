# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67611446/attributeerror-float-object-has-no-attribute-co-names
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import marshal
    _l_(574295)

except ImportError:
    pass
try:
    import types
    _l_(574297)

except ImportError:
    pass

def to_long(s):
    _l_(574303)

    aux = _n_(574298, "s", lambda: s)[0] + (_n_(574299, "s", lambda: s)[1] << 8) + (_n_(574300, "s", lambda: s)[2] << 16) + (_n_(574301, "s", lambda: s)[3] << 24)
    _l_(574302)
    return aux

def inspect_code(code, indent='    '):
    _l_(574328)

    _c_(574312, _n_(574304, "print", lambda: print), _c_(574311, _a_(574305, '{}{}(line:{})', "format"), _n_(574306, "indent", lambda: indent), _a_(574308, _n_(574307, "code", lambda: code), "co_names"), _a_(574310, _n_(574309, "code", lambda: code), "co_firstlineno")))
    _l_(574313)
    for c in _a_(574315, _n_(574314, "code", lambda: code), "co_consts"):
        _l_(574327)

        if _c_(574320, _n_(574316, "isinstance", lambda: isinstance), _n_(574317, "c", lambda: c), _a_(574319, _n_(574318, "types", lambda: types), "CodeType")):
            _l_(574326)

            _c_(574324, _n_(574321, "inspect_code", lambda: inspect_code), _n_(574322, "c", lambda: c), _n_(574323, "indent", lambda: indent) + '    ')
            _l_(574325)

f = _c_(574330, _n_(574329, "open", lambda: open), '__pycache__/add.cpython-39.pyc', 'rb')
_l_(574331)

magic = _c_(574334, _a_(574333, _n_(574332, "f", lambda: f), "read"), 4)
_l_(574335)
_c_(574342, _n_(574336, "print", lambda: print), _c_(574341, _a_(574337, 'magic: {}', "format"), _c_(574340, _a_(574339, _n_(574338, "magic", lambda: magic), "hex"))))
_l_(574343)
mod_time = _c_(574348, _n_(574344, "to_long", lambda: to_long), _c_(574347, _a_(574346, _n_(574345, "f", lambda: f), "read"), 4))
_l_(574349)
_c_(574354, _n_(574350, "print", lambda: print), _c_(574353, _a_(574351, 'mod_time: {}', "format"), _n_(574352, "mod_time", lambda: mod_time)))
_l_(574355)
source_size = _c_(574360, _n_(574356, "to_long", lambda: to_long), _c_(574359, _a_(574358, _n_(574357, "f", lambda: f), "read"), 4))
_l_(574361)
_c_(574366, _n_(574362, "print", lambda: print), _c_(574365, _a_(574363, 'source_size: {}', "format"), _n_(574364, "source_size", lambda: source_size)))
_l_(574367)

_c_(574369, _n_(574368, "print", lambda: print), '\ncode:')
_l_(574370)
code = _c_(574374, _a_(574372, _n_(574371, "marshal", lambda: marshal), "load"), _n_(574373, "f", lambda: f))
_l_(574375)
_c_(574378, _n_(574376, "inspect_code", lambda: inspect_code), _n_(574377, "code", lambda: code))
_l_(574379)

_c_(574382, _a_(574381, _n_(574380, "f", lambda: f), "close"))
_l_(574383)
try:
    import dis
    _l_(574385)

except ImportError:
    pass
_c_(574389, _a_(574387, _n_(574386, "dis", lambda: dis), "disassemble"), _n_(574388, "code", lambda: code))
_l_(574390)