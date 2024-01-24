# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60750349/python-typeerror-descriptor-append-for-list-objects-doesnt-apply-to-a-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Solution:
    _l_(419951)

    def combinationSum2(self, candidates: List[_n_(419875, "int", lambda: int)], target: _n_(419876, "int", lambda: int)) -> List[List[_n_(419877, "int", lambda: int)]]:
        _l_(419899)

        result = []
        _l_(419878)
        c = []
        _l_(419879)
        _c_(419888, _a_(419881, _n_(419880, "self", lambda: self), "combSum2"), 0,_c_(419884, _n_(419882, "sorted", lambda: sorted), _n_(419883, "candidates", lambda: candidates)),_n_(419885, "target", lambda: target),_n_(419886, "result", lambda: result),_n_(419887, "c", lambda: c))
        _l_(419889)
        _c_(419891, _n_(419890, "print", lambda: print), "result:")
        _l_(419892)
        _c_(419895, _n_(419893, "print", lambda: print), _n_(419894, "result", lambda: result))
        _l_(419896)
        aux = _n_(419897, "result", lambda: result)
        _l_(419898)
        return aux

    def combSum2(self, i: _n_(419900, "int", lambda: int), l: List[_n_(419901, "int", lambda: int)], t: _n_(419902, "int", lambda: int), res: [], curr: []):
        _l_(419950)

        if _n_(419903, "t", lambda: t) == 0:
            _l_(419914)

            _c_(419906, _n_(419904, "print", lambda: print), _n_(419905, "curr", lambda: curr))
            _l_(419907)
            _c_(419911, _a_(419909, _n_(419908, "res", lambda: res), "append"), _n_(419910, "curr", lambda: curr))
            _l_(419912)
            aux = ""
            _l_(419913)
            return aux
        if _n_(419915, "t", lambda: t) < 0:
            _l_(419917)

            aux = ""
            _l_(419916)
            return aux
        for idx in _c_(419923, _n_(419918, "range", lambda: range), _n_(419919, "i", lambda: i),_c_(419922, _n_(419920, "len", lambda: len), _n_(419921, "l", lambda: l))):
            _l_(419949)

            if(_n_(419924, "idx", lambda: idx) == _n_(419925, "i", lambda: i) or _n_(419926, "l", lambda: l)[_n_(419927, "idx", lambda: idx)] != _n_(419928, "l", lambda: l)[_n_(419929, "idx", lambda: idx)-1]):
                _l_(419948)

                _c_(419934, _a_(419931, _n_(419930, "curr", lambda: curr), "append"), _n_(419932, "l", lambda: l)[_n_(419933, "idx", lambda: idx)])
                _l_(419935)
                _c_(419945, _a_(419937, _n_(419936, "self", lambda: self), "combSum2"), _n_(419938, "idx", lambda: idx)+1,_n_(419939, "l", lambda: l),_n_(419940, "t", lambda: t)-_n_(419941, "l", lambda: l)[_n_(419942, "idx", lambda: idx)],_n_(419943, "res", lambda: res),_n_(419944, "curr", lambda: curr))
                _l_(419946)
                del curr[-1]
                _l_(419947)