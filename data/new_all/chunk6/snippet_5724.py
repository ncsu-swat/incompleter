# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51236398/typeerror-zip-argument-1-must-support-iteration-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [0, 2, 4, 8, 0, 2, 8, 0, 0, 0, 0, 2, 4, 2, 2, 0]
_l_(344223)
def drawBoard():
    _l_(344240)

    count = 0
    _l_(344224)
    for i in _c_(344226, _n_(344225, "range", lambda: range), 16):
        _l_(344239)

        _c_(344230, _n_(344227, "print", lambda: print), _n_(344228, "data", lambda: data)[_n_(344229, "i", lambda: i)], end = ' ')
        _l_(344231)
        count += 1
        _l_(344232)
        if _n_(344233, "count", lambda: count) == 4:
            _l_(344238)

            _c_(344235, _n_(344234, "print", lambda: print), "")
            _l_(344236)
            count = 0
            _l_(344237)
_c_(344242, _n_(344241, "drawBoard", lambda: drawBoard))
_l_(344243)
data = _c_(344246, _n_(344244, "zip", lambda: zip), *_n_(344245, "data", lambda: data)[::-1])
_l_(344247)
data = _n_(344248, "data", lambda: data)[::-1]
_l_(344249)
for col in _c_(344251, _n_(344250, "range", lambda: range), 4):
    _l_(344275)

    count = 0  
    _l_(344252)  
    for row in _c_(344254, _n_(344253, "range", lambda: range), 4):
        _l_(344266)

        if _n_(344255, "data", lambda: data)[_n_(344256, "row", lambda: row)*4+_n_(344257, "col", lambda: col)] != 0:
            _l_(344265)

            _n_(344258, "data", lambda: data)[_n_(344259, "count", lambda: count)*4+_n_(344260, "col", lambda: col)] = _n_(344261, "data", lambda: data)[_n_(344262, "row", lambda: row)*4+_n_(344263, "col", lambda: col)]
            _l_(344264)
    for row in _c_(344269, _n_(344267, "range", lambda: range), _n_(344268, "count", lambda: count), 4):
        _l_(344274)

        _n_(344270, "data", lambda: data)[_n_(344271, "row", lambda: row)*4+_n_(344272, "col", lambda: col)] = 0
        _l_(344273)
data = _n_(344276, "data", lambda: data)[::-1]
_l_(344277)
data = _c_(344284, _n_(344278, "list", lambda: list), _c_(344283, _n_(344279, "zip", lambda: zip), *_c_(344282, _n_(344280, "reversed", lambda: reversed), _n_(344281, "data", lambda: data))))
_l_(344285)
_c_(344287, _n_(344286, "drawBoard", lambda: drawBoard))
_l_(344288)