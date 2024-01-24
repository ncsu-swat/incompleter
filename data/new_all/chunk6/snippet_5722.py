# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51236398/typeerror-zip-argument-1-must-support-iteration-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = [0, 2, 4, 8, 0, 2, 8, 0, 0, 0, 0, 2, 4, 2, 2, 0]
_l_(373902)
def drawBoard():
    _l_(373919)

    count = 0
    _l_(373903)
    for i in _c_(373905, _n_(373904, "range", lambda: range), 16):
        _l_(373918)

        _c_(373909, _n_(373906, "print", lambda: print), _n_(373907, "data", lambda: data)[_n_(373908, "i", lambda: i)], end = ' ')
        _l_(373910)
        count += 1
        _l_(373911)
        if _n_(373912, "count", lambda: count) == 4:
            _l_(373917)

            _c_(373914, _n_(373913, "print", lambda: print), "")
            _l_(373915)
            count = 0
            _l_(373916)
_c_(373921, _n_(373920, "drawBoard", lambda: drawBoard))
_l_(373922)
data = _c_(373925, _n_(373923, "zip", lambda: zip), *_n_(373924, "data", lambda: data)[::-1])
_l_(373926)
data = _n_(373927, "data", lambda: data)[::-1]
_l_(373928)
for col in _c_(373930, _n_(373929, "range", lambda: range), 4):
    _l_(373954)

    count = 0  
    _l_(373931)  
    for row in _c_(373933, _n_(373932, "range", lambda: range), 4):
        _l_(373945)

        if _n_(373934, "data", lambda: data)[_n_(373935, "row", lambda: row)*4+_n_(373936, "col", lambda: col)] != 0:
            _l_(373944)

            _n_(373937, "data", lambda: data)[_n_(373938, "count", lambda: count)*4+_n_(373939, "col", lambda: col)] = _n_(373940, "data", lambda: data)[_n_(373941, "row", lambda: row)*4+_n_(373942, "col", lambda: col)]
            _l_(373943)
    for row in _c_(373948, _n_(373946, "range", lambda: range), _n_(373947, "count", lambda: count), 4):
        _l_(373953)

        _n_(373949, "data", lambda: data)[_n_(373950, "row", lambda: row)*4+_n_(373951, "col", lambda: col)] = 0
        _l_(373952)
data = _n_(373955, "data", lambda: data)[::-1]
_l_(373956)
data = _c_(373963, _n_(373957, "list", lambda: list), _c_(373962, _n_(373958, "zip", lambda: zip), *_c_(373961, _n_(373959, "reversed", lambda: reversed), _n_(373960, "data", lambda: data))))
_l_(373964)
_c_(373966, _n_(373965, "drawBoard", lambda: drawBoard))
_l_(373967)