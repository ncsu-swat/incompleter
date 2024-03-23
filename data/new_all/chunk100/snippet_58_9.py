# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62723)

    _c_(62638, _n_(62636, "print", lambda: print), 'Splitting ', _n_(62637, "nlist", lambda: nlist))
    _l_(62639)
    if _c_(62642, _n_(62640, "len", lambda: len), _n_(62641, "nlist", lambda: nlist)) > 1:
        _l_(62718)

        mid = _c_(62645, _n_(62643, "len", lambda: len), _n_(62644, "nlist", lambda: nlist)) // 2
        _l_(62646)
        lefthalf = _n_(62647, "nlist", lambda: nlist)[:_n_(62648, "mid", lambda: mid)]
        _l_(62649)
        righthalf = _n_(62650, "nlist", lambda: nlist)[_n_(62651, "mid", lambda: mid):]
        _l_(62652)
        _c_(62655, _n_(62653, "mergeSort", lambda: mergeSort), _n_(62654, "lefthalf", lambda: lefthalf))
        _l_(62656)
        _c_(62659, _n_(62657, "mergeSort", lambda: mergeSort), _n_(62658, "righthalf", lambda: righthalf))
        _l_(62660)
        i = j = k = 0
        _l_(62661)
        while _n_(62662, "i", lambda: i) < _c_(62665, _n_(62663, "len", lambda: len), _n_(62664, "lefthalf", lambda: lefthalf)) and _n_(62666, "j", lambda: j) < _c_(62669, _n_(62667, "len", lambda: len), _n_(62668, "righthalf", lambda: righthalf)):
            _l_(62691)

            if _n_(62670, "lefthalf", lambda: lefthalf)[_n_(62671, "i", lambda: i)] < _n_(62672, "righthalf", lambda: righthalf)[_n_(62673, "j", lambda: j)]:
                _l_(62688)

                _n_(62674, "nlist", lambda: nlist)[_n_(62675, "k", lambda: k)] = _n_(62676, "lefthalf", lambda: lefthalf)[_n_(62677, "i", lambda: i)]
                _l_(62678)
                i = _n_(62679, "i", lambda: i) + 1
                _l_(62680)
            else:
                _n_(62681, "nlist", lambda: nlist)[_n_(62682, "k", lambda: k)] = _n_(62683, "righthalf", lambda: righthalf)[_n_(62684, "j", lambda: j)]
                _l_(62685)
                j = _n_(62686, "j", lambda: j) + 1
                _l_(62687)
            k = _n_(62689, "k", lambda: k) + 1
            _l_(62690)
        while _n_(62692, "i", lambda: i) < _c_(62695, _n_(62693, "len", lambda: len), _n_(62694, "lefthalf", lambda: lefthalf)):
            _l_(62703)

            _n_(62696, "nlist", lambda: nlist)[_n_(62697, "k", lambda: k)] = _n_(62698, "lefthalf", lambda: lefthalf)[_n_(62699, "i", lambda: i)]
            _l_(62700)
            i = _n_(62701, "i", lambda: i) + 1
            _l_(62702)
        while _n_(62704, "j", lambda: j) < _c_(62707, _n_(62705, "len", lambda: len), _n_(62706, "righthalf", lambda: righthalf)):
            _l_(62717)

            _n_(62708, "nlist", lambda: nlist)[_n_(62709, "k", lambda: k)] = _n_(62710, "righthalf", lambda: righthalf)[_n_(62711, "j", lambda: j)]
            _l_(62712)
            j = _n_(62713, "j", lambda: j) + 1
            _l_(62714)
            k = _n_(62715, "k", lambda: k) + 1
            _l_(62716)
    _c_(62721, _n_(62719, "print", lambda: print), 'Merging ', _n_(62720, "nlist", lambda: nlist))
    _l_(62722)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62724)
_c_(62727, _n_(62725, "mergeSort", lambda: mergeSort), _n_(62726, "nlist", lambda: nlist))
_l_(62728)
_c_(62731, _n_(62729, "print", lambda: print), _n_(62730, "nlist", lambda: nlist))
_l_(62732)