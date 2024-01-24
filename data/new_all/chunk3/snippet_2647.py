# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68013248/why-am-i-getting-typeerror-int-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(568187)

except ImportError:
    pass
try:
    import location
    _l_(568189)

except ImportError:
    pass
if _n_(568190, "__name__", lambda: __name__) == "__main__" :
    _l_(568227)

    locationlist = []
    _l_(568191)
    while True :
        _l_(568216)

        try :
            _l_(568215)

            coordinate = _c_(568193, _n_(568192, "input", lambda: input), "Enter X and Y separated by a space, or enter a non-number to stop: ")
            _l_(568194)
            x,y = _c_(568197, _a_(568196, _n_(568195, "coordinate", lambda: coordinate), "split"))
            _l_(568198)
            x = _c_(568201, _n_(568199, "int", lambda: int), _n_(568200, "x", lambda: x))
            _l_(568202)
            y = _c_(568205, _n_(568203, "int", lambda: int), _n_(568204, "y", lambda: y))
            _l_(568206)
            _c_(568210, _a_(568208, _n_(568207, "locationlist", lambda: locationlist), "append"), _n_(568209, "coordinate", lambda: coordinate))
            _l_(568211)
        except _n_(568212, "ValueError", lambda: ValueError):
            _l_(568214)

            break
            _l_(568213)
    _c_(568219, _n_(568217, "print", lambda: print), "Points: ",_n_(568218, "locationlist", lambda: locationlist))
    _l_(568220)
    _c_(568225, _a_(568222, _n_(568221, "location", lambda: location), "where_is_xy"), _n_(568223, "coordinate", lambda: coordinate),_n_(568224, "locationlist", lambda: locationlist))
    _l_(568226)
if(_c_(568230, _n_(568228, "len", lambda: len), _n_(568229, "locationlist", lambda: locationlist))>=2):
    _l_(568272)

    _c_(568232, _n_(568231, "print", lambda: print), "Distances:")
    _l_(568233)
    for i in _c_(568238, _n_(568234, "range", lambda: range), 0,_c_(568237, _n_(568235, "len", lambda: len), _n_(568236, "locationlist", lambda: locationlist))-1):
        _l_(568271)

        a=_c_(568242, _n_(568239, "list", lambda: list), _n_(568240, "locationlist", lambda: locationlist)[_n_(568241, "i", lambda: i)])
        _l_(568243)
        b=_c_(568247, _n_(568244, "list", lambda: list), _n_(568245, "locationlist", lambda: locationlist)[_n_(568246, "i", lambda: i)+1])
        _l_(568248)
        distance=_c_(568255, _a_(568250, _n_(568249, "math", lambda: math), "sqrt"), (_n_(568251, "a", lambda: a)[0]-_n_(568252, "b", lambda: b)[0])**2 + (_n_(568253, "a", lambda: a)[1]-_n_(568254, "b", lambda: b)[1])**2)
        _l_(568256)
        _c_(568269, _n_(568257, "print", lambda: print), _c_(568260, _n_(568258, "str", lambda: str), _n_(568259, "a", lambda: a))+" "+_c_(568263, _n_(568261, "str", lambda: str), _n_(568262, "b", lambda: b))+" = "+_c_(568268, _n_(568264, "str", lambda: str), "%.2f" % _c_(568267, _n_(568265, "round", lambda: round), _n_(568266, "distance", lambda: distance), 2)))
        _l_(568270)