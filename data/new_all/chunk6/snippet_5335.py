# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65300596/typeerror-type-object-is-not-subscriptable
#Lua in Python

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class string:
    _l_(359580)

    def find(stringVariable, stringValue):
        _l_(359558)

        output = _c_(359554, _a_(359552, _n_(359551, "stringVariable", lambda: stringVariable), "find"), _n_(359553, "stringValue", lambda: stringValue))
        _l_(359555)
        aux = _n_(359556, "output", lambda: output)
        _l_(359557)
        return aux

    def sub(stringVariable, indexValueStart, *indexValueEnd):
        _l_(359571)

        indexValueStart = _n_(359559, "int", lambda: int)[_n_(359560, "indexValueStart", lambda: indexValueStart)]
        _l_(359561)
        indexValueEnd = _n_(359562, "int", lambda: int)[_n_(359563, "indexValueEnd", lambda: indexValueEnd)]
        _l_(359564)
        output = _n_(359565, "stringVariable", lambda: stringVariable)[_n_(359566, "indexValueStart", lambda: indexValueStart):_n_(359567, "indexValueEnd", lambda: indexValueEnd)]
        _l_(359568)
        aux = _n_(359569, "output", lambda: output)
        _l_(359570)
        return aux

    def gsub(stringVariable, stringIndex):
        _l_(359579)

        stringN = _n_(359572, "stringVariable", lambda: stringVariable)[:_n_(359573, "stringIndex", lambda: stringIndex)] + _n_(359574, "stringVariable", lambda: stringVariable)[_n_(359575, "stringIndex", lambda: stringIndex) + 1:]
        _l_(359576)
        aux = _n_(359577, "stringN", lambda: stringN)
        _l_(359578)
        return aux

a = _c_(359582, _n_(359581, "input", lambda: input))
_l_(359583)

b = _c_(359587, _a_(359585, _n_(359584, "string", lambda: string), "find"), _n_(359586, "a", lambda: a), "abc")
_l_(359588)

c = _c_(359593, _a_(359590, _n_(359589, "string", lambda: string), "sub"), _n_(359591, "a", lambda: a), _n_(359592, "b", lambda: b), 5)
_l_(359594)

_c_(359597, _n_(359595, "print", lambda: print), _n_(359596, "c", lambda: c))
_l_(359598)