# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54965624/typeerror-unsupported-operand-types-for-int-and-tuple-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a=[1,2,3,4,5]
_l_(437150)
for i in _c_(437155, _n_(437151, "range", lambda: range), _c_(437154, _n_(437152, "len", lambda: len), _n_(437153, "a", lambda: a))):
    _l_(437170)

    sum=2
    _l_(437156)
    for j in _c_(437159, _n_(437157, "range", lambda: range), _n_(437158, "i", lambda: i)):
        _l_(437163)

        sum+=_n_(437160, "a", lambda: a)[_n_(437161, "j", lambda: j)]
        _l_(437162)
    _n_(437164, "a", lambda: a)[_n_(437165, "i", lambda: i)]=(_n_(437166, "a", lambda: a)[_n_(437167, "i", lambda: i)],_n_(437168, "sum", lambda: sum))
    _l_(437169)
_c_(437173, _n_(437171, "print", lambda: print), _n_(437172, "a", lambda: a))
_l_(437174)