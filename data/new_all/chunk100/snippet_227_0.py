# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def test(dictt):
    _l_(17984)

    result = {}
    _l_(17971)
    for val in _c_(17974, _a_(17973, _n_(17972, "dictt", lambda: dictt), "values")):
        _l_(17981)

        _n_(17975, "result", lambda: result)[_n_(17976, "val", lambda: val)] = _c_(17979, _n_(17977, "len", lambda: len), _n_(17978, "val", lambda: val))
        _l_(17980)
    aux = _n_(17982, "result", lambda: result)
    _l_(17983)
    return aux
color_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
_l_(17985)
_c_(17987, _n_(17986, "print", lambda: print), '\nOriginal Dictionary:')
_l_(17988)
_c_(17991, _n_(17989, "print", lambda: print), _n_(17990, "color_dict", lambda: color_dict))
_l_(17992)
_c_(17994, _n_(17993, "print", lambda: print), 'Length of dictionary values:')
_l_(17995)
_c_(18000, _n_(17996, "print", lambda: print), _c_(17999, _n_(17997, "test", lambda: test), _n_(17998, "color_dict", lambda: color_dict)))
_l_(18001)
_c_(18003, _n_(18002, "print", lambda: print), '\nOriginal Dictionary:')
_l_(18004)
_c_(18007, _n_(18005, "print", lambda: print), _n_(18006, "color_dict", lambda: color_dict))
_l_(18008)
_c_(18010, _n_(18009, "print", lambda: print), 'Length of dictionary values:')
_l_(18011)
_c_(18016, _n_(18012, "print", lambda: print), _c_(18015, _n_(18013, "test", lambda: test), _n_(18014, "color_dict", lambda: color_dict)))
_l_(18017)