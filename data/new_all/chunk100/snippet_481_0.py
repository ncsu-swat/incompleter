# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def second_smallest(numbers):
    _l_(50329)

    if _c_(50295, _n_(50293, "len", lambda: len), _n_(50294, "numbers", lambda: numbers)) < 2:
        _l_(50297)

        aux = ""
        _l_(50296)
        return aux
    if _c_(50300, _n_(50298, "len", lambda: len), _n_(50299, "numbers", lambda: numbers)) == 2 and _n_(50301, "numbers", lambda: numbers)[0] == _n_(50302, "numbers", lambda: numbers)[1]:
        _l_(50304)

        aux = ""
        _l_(50303)
        return aux
    dup_items = _c_(50306, _n_(50305, "set", lambda: set))
    _l_(50307)
    for x in _n_(50308, "numbers", lambda: numbers):
        _l_(50322)

        if _n_(50309, "x", lambda: x) not in _n_(50310, "dup_items", lambda: dup_items):
            _l_(50321)

            _c_(50314, _a_(50312, _n_(50311, "uniq_items", lambda: uniq_items), "append"), _n_(50313, "x", lambda: x))
            _l_(50315)
            _c_(50319, _a_(50317, _n_(50316, "dup_items", lambda: dup_items), "add"), _n_(50318, "x", lambda: x))
            _l_(50320)
    _c_(50325, _a_(50324, _n_(50323, "uniq_items", lambda: uniq_items), "sort"))
    _l_(50326)
    aux = _n_(50327, "uniq_items", lambda: uniq_items)[1]
    _l_(50328)
    return aux
_c_(50333, _n_(50330, "print", lambda: print), _c_(50332, _n_(50331, "second_smallest", lambda: second_smallest), [1, 2, -8, -2, 0, -2]))
_l_(50334)
_c_(50338, _n_(50335, "print", lambda: print), _c_(50337, _n_(50336, "second_smallest", lambda: second_smallest), [1, 1, 0, 0, 2, -2, -2]))
_l_(50339)
_c_(50343, _n_(50340, "print", lambda: print), _c_(50342, _n_(50341, "second_smallest", lambda: second_smallest), [1, 1, 1, 0, 0, 0, 2, -2, -2]))
_l_(50344)
_c_(50348, _n_(50345, "print", lambda: print), _c_(50347, _n_(50346, "second_smallest", lambda: second_smallest), [2, 2]))
_l_(50349)
_c_(50353, _n_(50350, "print", lambda: print), _c_(50352, _n_(50351, "second_smallest", lambda: second_smallest), [2]))
_l_(50354)