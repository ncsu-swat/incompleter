# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51236398/typeerror-zip-argument-1-must-support-iteration-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [0, 2, 4, 8, 0, 2, 8, 0, 0, 0, 0, 2, 4, 2, 2, 0]
_l_(342804)
def drawBoard():
    _l_(342821)

    count = 0
    _l_(342805)
    for i in _c_(342807, _n_(342806, "range", lambda: range), 16):
        _l_(342820)

        _c_(342811, _n_(342808, "print", lambda: print), _n_(342809, "data", lambda: data)[_n_(342810, "i", lambda: i)], end = ' ')
        _l_(342812)
        count += 1
        _l_(342813)
        if _n_(342814, "count", lambda: count) == 4:
            _l_(342819)

            _c_(342816, _n_(342815, "print", lambda: print), "")
            _l_(342817)
            count = 0
            _l_(342818)
_c_(342823, _n_(342822, "drawBoard", lambda: drawBoard))
_l_(342824)
data = _c_(342827, _n_(342825, "zip", lambda: zip), *_n_(342826, "data", lambda: data)[::-1])
_l_(342828)
data = _n_(342829, "data", lambda: data)[::-1]
_l_(342830)
for col in _c_(342832, _n_(342831, "range", lambda: range), 4):
    _l_(342856)

    count = 0  
    _l_(342833)  
    for row in _c_(342835, _n_(342834, "range", lambda: range), 4):
        _l_(342847)

        if _n_(342836, "data", lambda: data)[_n_(342837, "row", lambda: row)*4+_n_(342838, "col", lambda: col)] != 0:
            _l_(342846)

            _n_(342839, "data", lambda: data)[_n_(342840, "count", lambda: count)*4+_n_(342841, "col", lambda: col)] = _n_(342842, "data", lambda: data)[_n_(342843, "row", lambda: row)*4+_n_(342844, "col", lambda: col)]
            _l_(342845)
    for row in _c_(342850, _n_(342848, "range", lambda: range), _n_(342849, "count", lambda: count), 4):
        _l_(342855)

        _n_(342851, "data", lambda: data)[_n_(342852, "row", lambda: row)*4+_n_(342853, "col", lambda: col)] = 0
        _l_(342854)
data = _n_(342857, "data", lambda: data)[::-1]
_l_(342858)
data = _c_(342865, _n_(342859, "list", lambda: list), _c_(342864, _n_(342860, "zip", lambda: zip), *_c_(342863, _n_(342861, "reversed", lambda: reversed), _n_(342862, "data", lambda: data))))
_l_(342866)
_c_(342868, _n_(342867, "drawBoard", lambda: drawBoard))
_l_(342869)