# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65300596/typeerror-type-object-is-not-subscriptable
#Lua in Python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class string:
    _l_(349707)

    def find(stringVariable, stringValue):
        _l_(349685)

        output = _c_(349681, _a_(349679, _n_(349678, "stringVariable", lambda: stringVariable), "find"), _n_(349680, "stringValue", lambda: stringValue))
        _l_(349682)
        aux = _n_(349683, "output", lambda: output)
        _l_(349684)
        return aux

    def sub(stringVariable, indexValueStart, *indexValueEnd):
        _l_(349698)

        indexValueStart = _n_(349686, "int", lambda: int)[_n_(349687, "indexValueStart", lambda: indexValueStart)]
        _l_(349688)
        indexValueEnd = _n_(349689, "int", lambda: int)[_n_(349690, "indexValueEnd", lambda: indexValueEnd)]
        _l_(349691)
        output = _n_(349692, "stringVariable", lambda: stringVariable)[_n_(349693, "indexValueStart", lambda: indexValueStart):_n_(349694, "indexValueEnd", lambda: indexValueEnd)]
        _l_(349695)
        aux = _n_(349696, "output", lambda: output)
        _l_(349697)
        return aux

    def gsub(stringVariable, stringIndex):
        _l_(349706)

        stringN = _n_(349699, "stringVariable", lambda: stringVariable)[:_n_(349700, "stringIndex", lambda: stringIndex)] + _n_(349701, "stringVariable", lambda: stringVariable)[_n_(349702, "stringIndex", lambda: stringIndex) + 1:]
        _l_(349703)
        aux = _n_(349704, "stringN", lambda: stringN)
        _l_(349705)
        return aux

a = _c_(349709, _n_(349708, "input", lambda: input))
_l_(349710)

b = _c_(349714, _a_(349712, _n_(349711, "string", lambda: string), "find"), _n_(349713, "a", lambda: a), "abc")
_l_(349715)

c = _c_(349720, _a_(349717, _n_(349716, "string", lambda: string), "sub"), _n_(349718, "a", lambda: a), _n_(349719, "b", lambda: b), 5)
_l_(349721)

_c_(349724, _n_(349722, "print", lambda: print), _n_(349723, "c", lambda: c))
_l_(349725)