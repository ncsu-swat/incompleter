# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75355763/pyhton-typeerror-unsupported-operand-types-for-float-and-nonetype
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def divide(a, b):
    _l_(353707)

    aux = _n_(353704, "a", lambda: a)/_n_(353705, "b", lambda: b)
    _l_(353706)
    return aux
def pow(a, b):
    _l_(353711)

    aux = _n_(353708, "a", lambda: a)**_n_(353709, "b", lambda: b)
    _l_(353710)
    return aux
def addA(a, b):
    _l_(353715)

    aux = _n_(353712, "a", lambda: a)+_n_(353713, "b", lambda: b)
    _l_(353714)
    return aux
def subA(a, b):
    _l_(353719)

    aux = _n_(353716, "a", lambda: a)-_n_(353717, "b", lambda: b)
    _l_(353718)
    return aux
def mul (a, b):
    _l_(353723)

    aux = _n_(353720, "a", lambda: a)*_n_(353721, "b", lambda: b)
    _l_(353722)
    return aux

operators = {
  '+': _n_(353724, "addA", lambda: addA),
  '-': _n_(353725, "subA", lambda: subA),
  '*': _n_(353726, "mul", lambda: mul),
  '/': _n_(353727, "divide", lambda: divide),
  '^': _n_(353728, "pow", lambda: pow),


}
_l_(353729)
def extract_expression(s):
    _l_(353744)

    start = _c_(353732, _a_(353731, _n_(353730, "s", lambda: s), "index"), '[')
    _l_(353733)
    end = _c_(353736, _a_(353735, _n_(353734, "s", lambda: s), "rindex"), ']')
    _l_(353737)
    while ']' in _n_(353738, "s", lambda: s):
        _l_(353743)

        aux = _n_(353739, "s", lambda: s)[_n_(353740, "start", lambda: start) + 1:_n_(353741, "end", lambda: end)]
        _l_(353742)

        return aux

def calculate(s):
    _l_(353793)

    while '[' in _n_(353745, "s", lambda: s):
        _l_(353762)

        sub_expression = _c_(353748, _n_(353746, "extract_expression", lambda: extract_expression), _n_(353747, "s", lambda: s))
        _l_(353749)
        result = _c_(353752, _n_(353750, "calculate", lambda: calculate), _n_(353751, "sub_expression", lambda: sub_expression))
        _l_(353753)
        s = _c_(353760, _a_(353755, _n_(353754, "s", lambda: s), "replace"), '[' + _n_(353756, "sub_expression", lambda: sub_expression) + ']', _c_(353759, _n_(353757, "str", lambda: str), _n_(353758, "result", lambda: result)))
        _l_(353761)

    if _c_(353765, _a_(353764, _n_(353763, "s", lambda: s), "isdigit")):
        _l_(353770)

        aux = _c_(353768, _n_(353766, "float", lambda: float), _n_(353767, "s", lambda: s))
        _l_(353769)
        return aux

    for c in _c_(353773, _a_(353772, _n_(353771, "operators", lambda: operators), "keys")):
        _l_(353792)

        left, operator, right = _c_(353777, _a_(353775, _n_(353774, "s", lambda: s), "partition"), _n_(353776, "c", lambda: c))
        _l_(353778)
        if _n_(353779, "operator", lambda: operator) in _n_(353780, "operators", lambda: operators):
            _l_(353791)

            aux = _c_(353789, _n_(353781, "operators", lambda: operators)[_n_(353782, "operator", lambda: operator)], _c_(353785, _n_(353783, "calculate", lambda: calculate), _n_(353784, "left", lambda: left)), _c_(353788, _n_(353786, "calculate", lambda: calculate), _n_(353787, "right", lambda: right)))
            _l_(353790)
            return aux

calc = _c_(353795, _n_(353794, "input", lambda: input), "Type calculation:\n")
_l_(353796)
_c_(353803, _n_(353797, "print", lambda: print), "Answer: " + _c_(353802, _n_(353798, "str", lambda: str), _c_(353801, _n_(353799, "calculate", lambda: calculate), _n_(353800, "calc", lambda: calc))))
_l_(353804)