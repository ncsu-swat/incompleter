# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52816850/typeerror-nonetype-object-is-not-subscriptable-about-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(407641)

except ImportError:
    pass
try:
    from statistics import mean
    _l_(407643)

except ImportError:
    pass

averages = _c_(407645, _n_(407644, "list", lambda: list))
_l_(407646)
sorted_averages = _c_(407648, _n_(407647, "list", lambda: list))
_l_(407649)
dic = _c_(407651, _n_(407650, "dict", lambda: dict))
_l_(407652)
with _c_(407654, _n_(407653, "open", lambda: open), 'first.csv') as fopen:
    _l_(407736)

    reader = _c_(407658, _a_(407656, _n_(407655, "csv", lambda: csv), "reader"), _n_(407657, "fopen", lambda: fopen))
    _l_(407659)
    for line in _n_(407660, "reader", lambda: reader):
        _l_(407690)

        name = _n_(407661, "line", lambda: line)[0]
        _l_(407662)
        line = _n_(407663, "line", lambda: line)[1:]
        _l_(407664)
        counter = 0
        _l_(407665)
        for i in _n_(407666, "line", lambda: line):
            _l_(407676)

            i = _c_(407669, _n_(407667, "float", lambda: float), _n_(407668, "i", lambda: i))
            _l_(407670)
            _n_(407671, "line", lambda: line)[_n_(407672, "counter", lambda: counter)] = _n_(407673, "i", lambda: i)
            _l_(407674)
            counter += 1
            _l_(407675)
        average = _c_(407679, _n_(407677, "mean", lambda: mean), _n_(407678, "line", lambda: line))
        _l_(407680)
        _c_(407684, _a_(407682, _n_(407681, "averages", lambda: averages), "append"), _n_(407683, "average", lambda: average))
        _l_(407685)
        _n_(407686, "dic", lambda: dic)[_n_(407687, "name", lambda: name)] = _n_(407688, "average", lambda: average)
        _l_(407689)
    for i in _c_(407695, _n_(407691, "range", lambda: range), 0, _c_(407694, _n_(407692, "len", lambda: len), _n_(407693, "averages", lambda: averages))):
        _l_(407724)

        maxi = 0
        _l_(407696)
        maxi1 = 0
        _l_(407697)
        for number in _n_(407698, "averages", lambda: averages):
            _l_(407713)

            if _n_(407699, "number", lambda: number) > _n_(407700, "maxi", lambda: maxi):
                _l_(407712)

                maxi = _n_(407701, "number", lambda: number)
                _l_(407702)
            elif _n_(407703, "number", lambda: number) == _n_(407704, "maxi", lambda: maxi):
                _l_(407711)

                maxi = _n_(407705, "number", lambda: number)
                _l_(407706)
                maxi1 = _n_(407707, "number", lambda: number)
                _l_(407708)
            else:
                maxi = _n_(407709, "maxi", lambda: maxi)
                _l_(407710)
        _c_(407717, _a_(407715, _n_(407714, "sorted_averages", lambda: sorted_averages), "append"), _n_(407716, "maxi", lambda: maxi))
        _l_(407718)
        _c_(407722, _a_(407720, _n_(407719, "averages", lambda: averages), "remove"), _n_(407721, "maxi", lambda: maxi))
        _l_(407723)
    del(averages)
    _l_(407725)
    insorted_averages = _c_(407728, _a_(407727, _n_(407726, "sorted_averages", lambda: sorted_averages), "reverse"))
    _l_(407729)
    for z in _n_(407730, "insorted_averages", lambda: insorted_averages)[:3]:
        _l_(407735)

        _c_(407733, _n_(407731, "print", lambda: print), _n_(407732, "z", lambda: z))
        _l_(407734)