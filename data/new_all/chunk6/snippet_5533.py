# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64630972/typeerror-object-of-type-int-has-no-len-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
res = []
_l_(335134)

for x in _c_(335136, _n_(335135, "range", lambda: range), 9):
    _l_(335185)


    if _n_(335137, "x", lambda: x) == 0:
        _l_(335176)

        _c_(335140, _a_(335139, _n_(335138, "res", lambda: res), "append"), [1])
        _l_(335141)
    elif _n_(335142, "x", lambda: x) == 1:
        _l_(335175)

        _c_(335145, _a_(335144, _n_(335143, "res", lambda: res), "append"), [1,1])
        _l_(335146)
        _c_(335149, _n_(335147, "print", lambda: print), _n_(335148, "res", lambda: res))
        _l_(335150)
    else:
        l=[]
        _l_(335151)
        for y in _c_(335157, _n_(335152, "range", lambda: range), _c_(335156, _n_(335153, "len", lambda: len), _n_(335154, "res", lambda: res)[_n_(335155, "x", lambda: x)-1])):
            _l_(335174)

            if _n_(335158, "y", lambda: y) == 0:
                _l_(335173)

                _c_(335161, _a_(335160, _n_(335159, "l", lambda: l), "append"), 1)
                _l_(335162)
            else:
                _c_(335171, _a_(335164, _n_(335163, "l", lambda: l), "append"), _n_(335165, "res", lambda: res)[_n_(335166, "x", lambda: x)-1][_n_(335167, "y", lambda: y)] + _n_(335168, "res", lambda: res)[_n_(335169, "x", lambda: x)-1][_n_(335170, "y", lambda: y)-1])
                _l_(335172)
    _c_(335179, _a_(335178, _n_(335177, "l", lambda: l), "append"), 1)
    _l_(335180)
    _c_(335183, _a_(335182, _n_(335181, "res", lambda: res), "append"), 1)
    _l_(335184)