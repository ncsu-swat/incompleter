# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mergeSort(nlist):
    _l_(62626)

    _c_(62540, _n_(62538, "print", lambda: print), 'Splitting ', _n_(62539, "nlist", lambda: nlist))
    _l_(62541)
    if _c_(62544, _n_(62542, "len", lambda: len), _n_(62543, "nlist", lambda: nlist)) > 1:
        _l_(62621)

        mid = _c_(62547, _n_(62545, "len", lambda: len), _n_(62546, "nlist", lambda: nlist)) // 2
        _l_(62548)
        lefthalf = _n_(62549, "nlist", lambda: nlist)[:_n_(62550, "mid", lambda: mid)]
        _l_(62551)
        righthalf = _n_(62552, "nlist", lambda: nlist)[_n_(62553, "mid", lambda: mid):]
        _l_(62554)
        _c_(62557, _n_(62555, "mergeSort", lambda: mergeSort), _n_(62556, "lefthalf", lambda: lefthalf))
        _l_(62558)
        _c_(62561, _n_(62559, "mergeSort", lambda: mergeSort), _n_(62560, "righthalf", lambda: righthalf))
        _l_(62562)
        while _n_(62563, "i", lambda: i) < _c_(62566, _n_(62564, "len", lambda: len), _n_(62565, "lefthalf", lambda: lefthalf)) and _n_(62567, "j", lambda: j) < _c_(62570, _n_(62568, "len", lambda: len), _n_(62569, "righthalf", lambda: righthalf)):
            _l_(62592)

            if _n_(62571, "lefthalf", lambda: lefthalf)[_n_(62572, "i", lambda: i)] < _n_(62573, "righthalf", lambda: righthalf)[_n_(62574, "j", lambda: j)]:
                _l_(62589)

                _n_(62575, "nlist", lambda: nlist)[_n_(62576, "k", lambda: k)] = _n_(62577, "lefthalf", lambda: lefthalf)[_n_(62578, "i", lambda: i)]
                _l_(62579)
                i = _n_(62580, "i", lambda: i) + 1
                _l_(62581)
            else:
                _n_(62582, "nlist", lambda: nlist)[_n_(62583, "k", lambda: k)] = _n_(62584, "righthalf", lambda: righthalf)[_n_(62585, "j", lambda: j)]
                _l_(62586)
                j = _n_(62587, "j", lambda: j) + 1
                _l_(62588)
            k = _n_(62590, "k", lambda: k) + 1
            _l_(62591)
        while _n_(62593, "i", lambda: i) < _c_(62596, _n_(62594, "len", lambda: len), _n_(62595, "lefthalf", lambda: lefthalf)):
            _l_(62606)

            _n_(62597, "nlist", lambda: nlist)[_n_(62598, "k", lambda: k)] = _n_(62599, "lefthalf", lambda: lefthalf)[_n_(62600, "i", lambda: i)]
            _l_(62601)
            i = _n_(62602, "i", lambda: i) + 1
            _l_(62603)
            k = _n_(62604, "k", lambda: k) + 1
            _l_(62605)
        while _n_(62607, "j", lambda: j) < _c_(62610, _n_(62608, "len", lambda: len), _n_(62609, "righthalf", lambda: righthalf)):
            _l_(62620)

            _n_(62611, "nlist", lambda: nlist)[_n_(62612, "k", lambda: k)] = _n_(62613, "righthalf", lambda: righthalf)[_n_(62614, "j", lambda: j)]
            _l_(62615)
            j = _n_(62616, "j", lambda: j) + 1
            _l_(62617)
            k = _n_(62618, "k", lambda: k) + 1
            _l_(62619)
    _c_(62624, _n_(62622, "print", lambda: print), 'Merging ', _n_(62623, "nlist", lambda: nlist))
    _l_(62625)
nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
_l_(62627)
_c_(62630, _n_(62628, "mergeSort", lambda: mergeSort), _n_(62629, "nlist", lambda: nlist))
_l_(62631)
_c_(62634, _n_(62632, "print", lambda: print), _n_(62633, "nlist", lambda: nlist))
_l_(62635)