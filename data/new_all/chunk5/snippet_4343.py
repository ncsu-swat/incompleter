# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59417946/typeerror-int-object-is-not-callable-at-last-lne
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
l=[_c_(654873, _n_(654871, "int", lambda: int), _n_(654872, "x", lambda: x)) for x in _c_(654875, _a_(654874, "10,22,9,33,21,50,41,60,80", "split"), sep = ",")]
_l_(654876)
_c_(654879, _n_(654877, "print", lambda: print), _n_(654878, "l", lambda: l))
_l_(654880)
length1 = [1 for i in _c_(654885, _n_(654881, "range", lambda: range), _c_(654884, _n_(654882, "len", lambda: len), _n_(654883, "l", lambda: l)))]
_l_(654886)
for i in _c_(654891, _n_(654887, "range", lambda: range), _c_(654890, _n_(654888, "len", lambda: len), _n_(654889, "l", lambda: l))):
    _l_(654914)

    max = _n_(654892, "l", lambda: l)[_n_(654893, "i", lambda: i)]
    _l_(654894)
    for j in _c_(654900, _n_(654895, "range", lambda: range), _n_(654896, "i", lambda: i)+1,_c_(654899, _n_(654897, "len", lambda: len), _n_(654898, "l", lambda: l))):
        _l_(654913)

        if _n_(654901, "l", lambda: l)[_n_(654902, "j", lambda: j)]>_n_(654903, "max", lambda: max):
            _l_(654912)

            max=_n_(654904, "l", lambda: l)[_n_(654905, "j", lambda: j)]
            _l_(654906)
            _n_(654907, "length1", lambda: length1)[_n_(654908, "i", lambda: i)]=_n_(654909, "length1", lambda: length1)[_n_(654910, "i", lambda: i)]+1
            _l_(654911)
_c_(654919, _n_(654915, "print", lambda: print), _c_(654918, _n_(654916, "max", lambda: max), _n_(654917, "length1", lambda: length1)))
_l_(654920)