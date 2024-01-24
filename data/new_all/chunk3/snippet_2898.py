# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59078817/keep-on-getting-an-attributeerror-and-not-sure-why
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def gcd(n, d):
        _l_(578232)

        if _n_(578214, "n", lambda: n)==0 or _n_(578215, "d", lambda: d)==0:
                _l_(578217)

                aux = 1
                _l_(578216)
                return aux
        while(_n_(578218, "n", lambda: n) != _n_(578219, "d", lambda: d)):
                _l_(578229)

                if(_n_(578220, "n", lambda: n) > _n_(578221, "d", lambda: d)):
                        _l_(578228)

                        n = _n_(578222, "n", lambda: n) - _n_(578223, "d", lambda: d)
                        _l_(578224)
                else:
                    d = _n_(578225, "d", lambda: d) - _n_(578226, "n", lambda: n)
                    _l_(578227)
        aux = _n_(578230, "n", lambda: n)
        _l_(578231)
        return aux

class Fraction:
        _l_(578365)

        def __init__(self, n, d):
                _l_(578277)

                _n_(578233, "self", lambda: self).num = _c_(578244, _n_(578234, "int", lambda: int), _n_(578235, "n", lambda: n) / _c_(578243, _n_(578236, "gcd", lambda: gcd), _c_(578239, _n_(578237, "abs", lambda: abs), _n_(578238, "n", lambda: n)), _c_(578242, _n_(578240, "abs", lambda: abs), _n_(578241, "d", lambda: d))))
                _l_(578245)
                _n_(578246, "self", lambda: self).denom = _c_(578257, _n_(578247, "int", lambda: int), _n_(578248, "d", lambda: d) / _c_(578256, _n_(578249, "gcd", lambda: gcd), _c_(578252, _n_(578250, "abs", lambda: abs), _n_(578251, "n", lambda: n)), _c_(578255, _n_(578253, "abs", lambda: abs), _n_(578254, "d", lambda: d))))
                _l_(578258)
                if _a_(578260, _n_(578259, "self", lambda: self), "denom") < 0:
                        _l_(578276)

                        _n_(578261, "self", lambda: self).denom = _c_(578265, _n_(578262, "abs", lambda: abs), _a_(578264, _n_(578263, "self", lambda: self), "denom"))
                        _l_(578266)
                        _n_(578267, "self", lambda: self).num = -1 * _a_(578269, _n_(578268, "self", lambda: self), "num")
                        _l_(578270)
                elif _a_(578272, _n_(578271, "self", lambda: self), "denom") == 0:
                        _l_(578275)

                        raise _n_(578273, "ZeroDivisionError", lambda: ZeroDivisionError)
                        _l_(578274)
        def __str__(self):
                _l_(578304)

                if _c_(578280, _n_(578278, "type", lambda: type), _n_(578279, "self", lambda: self)) is _n_(578281, "tuple", lambda: tuple):
                        _l_(578303)

                        if _n_(578282, "self", lambda: self)[1] < 0:
                                _l_(578289)

                                aux = '%s/%s' %(_n_(578283, "self", lambda: self)[0], -1*_n_(578284, "self", lambda: self)[1])
                                _l_(578285)
                                return aux
                        else:
                            aux = '%s/%s' %(_n_(578286, "self", lambda: self)[0], _n_(578287, "self", lambda: self)[1])
                            _l_(578288)
                            return aux
                elif _a_(578291, _n_(578290, "self", lambda: self), "denom") == 1:
                        _l_(578302)

                        aux = _c_(578295, _n_(578292, "str", lambda: str), _a_(578294, _n_(578293, "self", lambda: self), "num"))
                        _l_(578296)
                        return aux
                else:
                    aux = '%s/%s' %(_a_(578298, _n_(578297, "self", lambda: self), "num"), _a_(578300, _n_(578299, "self", lambda: self), "denom"))
                    _l_(578301)
                    return aux

        def __add__(self, other):
                _l_(578318)

                aux = _a_(578306, _n_(578305, "self", lambda: self), "num")*_a_(578308, _n_(578307, "other", lambda: other), "denom") + _a_(578310, _n_(578309, "self", lambda: self), "denom")*_a_(578312, _n_(578311, "other", lambda: other), "num"), _a_(578314, _n_(578313, "self", lambda: self), "denom")*_a_(578316, _n_(578315, "other", lambda: other), "denom")
                _l_(578317)
                return aux

        def __sub__(self, other):
                _l_(578332)

                aux = _a_(578320, _n_(578319, "self", lambda: self), "num")*_a_(578322, _n_(578321, "other", lambda: other), "denom") - _a_(578324, _n_(578323, "self", lambda: self), "denom")*_a_(578326, _n_(578325, "other", lambda: other), "num"), _a_(578328, _n_(578327, "self", lambda: self), "denom")*_a_(578330, _n_(578329, "other", lambda: other), "denom")
                _l_(578331)
                return aux

        def __mul__(self, other):
                _l_(578342)

                aux = _a_(578334, _n_(578333, "self", lambda: self), "num")*_a_(578336, _n_(578335, "other", lambda: other), "num"), _a_(578338, _n_(578337, "self", lambda: self), "denom")*_a_(578340, _n_(578339, "other", lambda: other), "denom")
                _l_(578341)
                return aux

        def __div__(self, other):
                _l_(578352)

                aux = _a_(578344, _n_(578343, "self", lambda: self), "num")*_a_(578346, _n_(578345, "other", lambda: other), "denom"), _a_(578348, _n_(578347, "self", lambda: self), "denom")*_a_(578350, _n_(578349, "other", lambda: other), "num")
                _l_(578351)
                return aux

        def __eq__(self, other):
                _l_(578364)

                if _a_(578354, _n_(578353, "self", lambda: self), "num") == _a_(578356, _n_(578355, "other", lambda: other), "num") and _a_(578358, _n_(578357, "self", lambda: self), "denom") == _a_(578360, _n_(578359, "other", lambda: other), "denom"):
                        _l_(578363)

                        aux = "Equal"
                        _l_(578361)
                        return aux
                else:
                    aux = "Not Equal"
                    _l_(578362)
                    return aux


f1 = _c_(578367, _n_(578366, "Fraction", lambda: Fraction), 2, 4)
_l_(578368)
f2 = _c_(578370, _n_(578369, "Fraction", lambda: Fraction), 4, 20)
_l_(578371)
add = _c_(578376, _a_(578373, _n_(578372, "Fraction", lambda: Fraction), "__add__"), _n_(578374, "f1", lambda: f1), _n_(578375, "f2", lambda: f2))
_l_(578377)
sub = _c_(578382, _a_(578379, _n_(578378, "Fraction", lambda: Fraction), "__sub__"), _n_(578380, "f1", lambda: f1), _n_(578381, "f2", lambda: f2))
_l_(578383)
eq = _c_(578388, _a_(578385, _n_(578384, "Fraction", lambda: Fraction), "__eq__"), _n_(578386, "f1", lambda: f1), _n_(578387, "f2", lambda: f2))
_l_(578389)
mul = _c_(578394, _a_(578391, _n_(578390, "Fraction", lambda: Fraction), "__mul__"), _n_(578392, "f1", lambda: f1), _n_(578393, "f2", lambda: f2))
_l_(578395)
div = _c_(578400, _a_(578397, _n_(578396, "Fraction", lambda: Fraction), "__div__"), _n_(578398, "f1", lambda: f1), _n_(578399, "f2", lambda: f2))
_l_(578401)
_c_(578443, _n_(578402, "print", lambda: print), "Fraction one: "+_c_(578408, _n_(578403, "str", lambda: str), _c_(578407, _a_(578405, _n_(578404, "Fraction", lambda: Fraction), "__str__"), _n_(578406, "f1", lambda: f1)))+"\n"+"Second Fraction: "+_c_(578414, _n_(578409, "str", lambda: str), _c_(578413, _a_(578411, _n_(578410, "Fraction", lambda: Fraction), "__str__"), _n_(578412, "f2", lambda: f2)))+"\n"+"Add: "+_c_(578420, _n_(578415, "str", lambda: str), _c_(578419, _a_(578417, _n_(578416, "Fraction", lambda: Fraction), "__str__"), _n_(578418, "add", lambda: add)))+"\n"+"Subtract: "+_c_(578426, _n_(578421, "str", lambda: str), _c_(578425, _a_(578423, _n_(578422, "Fraction", lambda: Fraction), "__str__"), _n_(578424, "sub", lambda: sub)))+"\n"+"Multiply: "+_c_(578432, _n_(578427, "str", lambda: str), _c_(578431, _a_(578429, _n_(578428, "Fraction", lambda: Fraction), "__str__"), _n_(578430, "mul", lambda: mul)))+"\n"+"Divide: "+_c_(578438, _n_(578433, "str", lambda: str), _c_(578437, _a_(578435, _n_(578434, "Fraction", lambda: Fraction), "__str__"), _n_(578436, "div", lambda: div)))+_c_(578442, _a_(578440, _n_(578439, "Fraction", lambda: Fraction), "__str__"), _n_(578441, "eq", lambda: eq)))
_l_(578444)