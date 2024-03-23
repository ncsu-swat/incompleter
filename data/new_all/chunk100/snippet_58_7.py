# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62528)

    _c_(62444, _n_(62442, "print", lambda: print), 'Splitting ', _n_(62443, "nlist", lambda: nlist))
    _l_(62445)
    if _c_(62448, _n_(62446, "len", lambda: len), _n_(62447, "nlist", lambda: nlist)) > 1:
        _l_(62523)

        mid = _c_(62451, _n_(62449, "len", lambda: len), _n_(62450, "nlist", lambda: nlist)) // 2
        _l_(62452)
        righthalf = _n_(62453, "nlist", lambda: nlist)[_n_(62454, "mid", lambda: mid):]
        _l_(62455)
        _c_(62458, _n_(62456, "mergeSort", lambda: mergeSort), _n_(62457, "lefthalf", lambda: lefthalf))
        _l_(62459)
        _c_(62462, _n_(62460, "mergeSort", lambda: mergeSort), _n_(62461, "righthalf", lambda: righthalf))
        _l_(62463)
        i = j = k = 0
        _l_(62464)
        while _n_(62465, "i", lambda: i) < _c_(62468, _n_(62466, "len", lambda: len), _n_(62467, "lefthalf", lambda: lefthalf)) and _n_(62469, "j", lambda: j) < _c_(62472, _n_(62470, "len", lambda: len), _n_(62471, "righthalf", lambda: righthalf)):
            _l_(62494)

            if _n_(62473, "lefthalf", lambda: lefthalf)[_n_(62474, "i", lambda: i)] < _n_(62475, "righthalf", lambda: righthalf)[_n_(62476, "j", lambda: j)]:
                _l_(62491)

                _n_(62477, "nlist", lambda: nlist)[_n_(62478, "k", lambda: k)] = _n_(62479, "lefthalf", lambda: lefthalf)[_n_(62480, "i", lambda: i)]
                _l_(62481)
                i = _n_(62482, "i", lambda: i) + 1
                _l_(62483)
            else:
                _n_(62484, "nlist", lambda: nlist)[_n_(62485, "k", lambda: k)] = _n_(62486, "righthalf", lambda: righthalf)[_n_(62487, "j", lambda: j)]
                _l_(62488)
                j = _n_(62489, "j", lambda: j) + 1
                _l_(62490)
            k = _n_(62492, "k", lambda: k) + 1
            _l_(62493)
        while _n_(62495, "i", lambda: i) < _c_(62498, _n_(62496, "len", lambda: len), _n_(62497, "lefthalf", lambda: lefthalf)):
            _l_(62508)

            _n_(62499, "nlist", lambda: nlist)[_n_(62500, "k", lambda: k)] = _n_(62501, "lefthalf", lambda: lefthalf)[_n_(62502, "i", lambda: i)]
            _l_(62503)
            i = _n_(62504, "i", lambda: i) + 1
            _l_(62505)
            k = _n_(62506, "k", lambda: k) + 1
            _l_(62507)
        while _n_(62509, "j", lambda: j) < _c_(62512, _n_(62510, "len", lambda: len), _n_(62511, "righthalf", lambda: righthalf)):
            _l_(62522)

            _n_(62513, "nlist", lambda: nlist)[_n_(62514, "k", lambda: k)] = _n_(62515, "righthalf", lambda: righthalf)[_n_(62516, "j", lambda: j)]
            _l_(62517)
            j = _n_(62518, "j", lambda: j) + 1
            _l_(62519)
            k = _n_(62520, "k", lambda: k) + 1
            _l_(62521)
    _c_(62526, _n_(62524, "print", lambda: print), 'Merging ', _n_(62525, "nlist", lambda: nlist))
    _l_(62527)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62529)
_c_(62532, _n_(62530, "mergeSort", lambda: mergeSort), _n_(62531, "nlist", lambda: nlist))
_l_(62533)
_c_(62536, _n_(62534, "print", lambda: print), _n_(62535, "nlist", lambda: nlist))
_l_(62537)