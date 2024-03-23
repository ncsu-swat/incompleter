# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(61755)

    _c_(61670, _n_(61668, "print", lambda: print), 'Splitting ', _n_(61669, "nlist", lambda: nlist))
    _l_(61671)
    if _c_(61674, _n_(61672, "len", lambda: len), _n_(61673, "nlist", lambda: nlist)) > 1:
        _l_(61750)

        mid = _c_(61677, _n_(61675, "len", lambda: len), _n_(61676, "nlist", lambda: nlist)) // 2
        _l_(61678)
        lefthalf = _n_(61679, "nlist", lambda: nlist)[:_n_(61680, "mid", lambda: mid)]
        _l_(61681)
        righthalf = _n_(61682, "nlist", lambda: nlist)[_n_(61683, "mid", lambda: mid):]
        _l_(61684)
        _c_(61687, _n_(61685, "mergeSort", lambda: mergeSort), _n_(61686, "lefthalf", lambda: lefthalf))
        _l_(61688)
        _c_(61691, _n_(61689, "mergeSort", lambda: mergeSort), _n_(61690, "righthalf", lambda: righthalf))
        _l_(61692)
        i = j = k = 0
        _l_(61693)
        while _n_(61694, "i", lambda: i) < _c_(61697, _n_(61695, "len", lambda: len), _n_(61696, "lefthalf", lambda: lefthalf)) and _n_(61698, "j", lambda: j) < _c_(61701, _n_(61699, "len", lambda: len), _n_(61700, "righthalf", lambda: righthalf)):
            _l_(61723)

            if _n_(61702, "lefthalf", lambda: lefthalf)[_n_(61703, "i", lambda: i)] < _n_(61704, "righthalf", lambda: righthalf)[_n_(61705, "j", lambda: j)]:
                _l_(61720)

                _n_(61706, "nlist", lambda: nlist)[_n_(61707, "k", lambda: k)] = _n_(61708, "lefthalf", lambda: lefthalf)[_n_(61709, "i", lambda: i)]
                _l_(61710)
                i = _n_(61711, "i", lambda: i) + 1
                _l_(61712)
            else:
                _n_(61713, "nlist", lambda: nlist)[_n_(61714, "k", lambda: k)] = _n_(61715, "righthalf", lambda: righthalf)[_n_(61716, "j", lambda: j)]
                _l_(61717)
                j = _n_(61718, "j", lambda: j) + 1
                _l_(61719)
            k = _n_(61721, "k", lambda: k) + 1
            _l_(61722)
        while _n_(61724, "i", lambda: i) < _c_(61727, _n_(61725, "len", lambda: len), _n_(61726, "lefthalf", lambda: lefthalf)):
            _l_(61735)

            _n_(61728, "nlist", lambda: nlist)[_n_(61729, "k", lambda: k)] = _n_(61730, "lefthalf", lambda: lefthalf)[_n_(61731, "i", lambda: i)]
            _l_(61732)
            k = _n_(61733, "k", lambda: k) + 1
            _l_(61734)
        while _n_(61736, "j", lambda: j) < _c_(61739, _n_(61737, "len", lambda: len), _n_(61738, "righthalf", lambda: righthalf)):
            _l_(61749)

            _n_(61740, "nlist", lambda: nlist)[_n_(61741, "k", lambda: k)] = _n_(61742, "righthalf", lambda: righthalf)[_n_(61743, "j", lambda: j)]
            _l_(61744)
            j = _n_(61745, "j", lambda: j) + 1
            _l_(61746)
            k = _n_(61747, "k", lambda: k) + 1
            _l_(61748)
    _c_(61753, _n_(61751, "print", lambda: print), 'Merging ', _n_(61752, "nlist", lambda: nlist))
    _l_(61754)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(61756)
_c_(61759, _n_(61757, "mergeSort", lambda: mergeSort), _n_(61758, "nlist", lambda: nlist))
_l_(61760)
_c_(61763, _n_(61761, "print", lambda: print), _n_(61762, "nlist", lambda: nlist))
_l_(61764)