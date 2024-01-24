# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67823362/b-0-lenst-typeerror-object-of-type-function-has-no-len
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from turtle import st
    _l_(557271)

except ImportError:
    pass

mxdiff = 0
_l_(557272)
buy = 0
_l_(557273)
sell = 0
_l_(557274)
a = []  # min array from left
_l_(557275)  # min array from left
b = [0] * _c_(557278, _n_(557276, "len", lambda: len), _n_(557277, "st", lambda: st))  # max array from right
_l_(557279)  # max array from right
d = []  # difference array
_l_(557280)  # difference array
minleft = _n_(557281, "st", lambda: st)[0]
_l_(557282)
maxright = _n_(557283, "st", lambda: st)[_c_(557286, _n_(557284, "len", lambda: len), _n_(557285, "st", lambda: st)) - 1]
_l_(557287)

for i in _c_(557292, _n_(557288, "range", lambda: range), 0, _c_(557291, _n_(557289, "len", lambda: len), _n_(557290, "st", lambda: st))):
    _l_(557311)

    if (_n_(557293, "st", lambda: st)[_n_(557294, "i", lambda: i)] < _n_(557295, "minleft", lambda: minleft)):
        _l_(557310)

        minleft = _n_(557296, "st", lambda: st)[_n_(557297, "i", lambda: i)]
        _l_(557298)
        _c_(557303, _a_(557300, _n_(557299, "a", lambda: a), "append"), _n_(557301, "st", lambda: st)[_n_(557302, "i", lambda: i)])
        _l_(557304)
    else:
        _c_(557308, _a_(557306, _n_(557305, "a", lambda: a), "append"), _n_(557307, "minleft", lambda: minleft))
        _l_(557309)

for i in _c_(557316, _n_(557312, "range", lambda: range), _c_(557315, _n_(557313, "len", lambda: len), _n_(557314, "st", lambda: st)) - 1, -1, -1):
    _l_(557333)

    if (_n_(557317, "st", lambda: st)[_n_(557318, "i", lambda: i)] > _n_(557319, "maxright", lambda: maxright)):
        _l_(557332)

        maxright = _n_(557320, "st", lambda: st)[_n_(557321, "i", lambda: i)]
        _l_(557322)
        _n_(557323, "b", lambda: b)[_n_(557324, "i", lambda: i)] = _n_(557325, "st", lambda: st)[_n_(557326, "i", lambda: i)]
        _l_(557327)
    else:
        _n_(557328, "b", lambda: b)[_n_(557329, "i", lambda: i)] = _n_(557330, "maxright", lambda: maxright)
        _l_(557331)

for i in _c_(557338, _n_(557334, "range", lambda: range), 0, _c_(557337, _n_(557335, "len", lambda: len), _n_(557336, "st", lambda: st))):
    _l_(557347)

    _c_(557345, _a_(557340, _n_(557339, "d", lambda: d), "append"), _n_(557341, "b", lambda: b)[_n_(557342, "i", lambda: i)] - _n_(557343, "a", lambda: a)[_n_(557344, "i", lambda: i)])
    _l_(557346)

mxdiff = _c_(557350, _n_(557348, "max", lambda: max), _n_(557349, "d", lambda: d))
_l_(557351)

for i in _c_(557356, _n_(557352, "range", lambda: range), 0, _c_(557355, _n_(557353, "len", lambda: len), _n_(557354, "st", lambda: st))):
    _l_(557367)

    if (_n_(557357, "d", lambda: d)[_n_(557358, "i", lambda: i)] == _n_(557359, "mxdiff", lambda: mxdiff) and _n_(557360, "d", lambda: d)[_n_(557361, "i", lambda: i) + 1] == _n_(557362, "mxdiff", lambda: mxdiff)):
        _l_(557366)

        buy = _n_(557363, "i", lambda: i)
        _l_(557364)
        break
        _l_(557365)

for i in _c_(557372, _n_(557368, "range", lambda: range), _c_(557371, _n_(557369, "len", lambda: len), _n_(557370, "st", lambda: st)) - 1, -1, -1):
    _l_(557383)

    if (_n_(557373, "d", lambda: d)[_n_(557374, "i", lambda: i)] == _n_(557375, "mxdiff", lambda: mxdiff) and _n_(557376, "d", lambda: d)[_n_(557377, "i", lambda: i) - 1] == _n_(557378, "mxdiff", lambda: mxdiff)):
        _l_(557382)

        sell = _n_(557379, "i", lambda: i)
        _l_(557380)
        break
        _l_(557381)

_c_(557385, _n_(557384, "print", lambda: print), "stocks has to be bought on day ")
_l_(557386)
_c_(557389, _n_(557387, "print", lambda: print), _n_(557388, "buy", lambda: buy) + 1)
_l_(557390)

_c_(557392, _n_(557391, "print", lambda: print), "stocks has to be sold on day ")
_l_(557393)
_c_(557396, _n_(557394, "print", lambda: print), _n_(557395, "sell", lambda: sell) + 1)
_l_(557397)