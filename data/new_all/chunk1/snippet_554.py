# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32889157/typeerror-endswith-first-arg-must-be-str-or-a-tuple-of-str-not-bool
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
s = 'like go goes likes liked liked liking likes like'
_l_(385290)
lst = _c_(385293, _a_(385292, _n_(385291, "s", lambda: s), "split"))
_l_(385294)
suffixes = ['s', 'es', 'ies', 'ed', 'ing']
_l_(385295)

counter = 0
_l_(385296)
prompt = 'like'
_l_(385297)
for x in _n_(385298, "lst", lambda: lst):
    _l_(385312)

    if _c_(385302, _a_(385300, _n_(385299, "x", lambda: x), "startswith"), _n_(385301, "prompt", lambda: prompt)) and _c_(385309, _a_(385304, _n_(385303, "x", lambda: x), "endswith"), _c_(385308, _n_(385305, "any", lambda: any), (_n_(385306, "suffix", lambda: suffix) for suffix in _n_(385307, "suffixes", lambda: suffixes)))):
        _l_(385311)

        counter += 1
        _l_(385310)