# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63373834/typeerror-can-only-concatenate-str-not-nonetype-to-str-on-recursive-functio
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def NumberToSymbol(r):
    _l_(339804)

    nuc={0:"A", 1:"C", 2:"G",3:"T"}
    _l_(339798)
    aux = _c_(339802, _a_(339800, _n_(339799, "nuc", lambda: nuc), "get"), _n_(339801, "r", lambda: r))
    _l_(339803)
    return aux
def NumberToPattern(index, k):
    _l_(339827)

    if _n_(339805, "k", lambda: k) == 1:
        _l_(339810)

        aux = _c_(339808, _n_(339806, "NumberToSymbol", lambda: NumberToSymbol), _n_(339807, "index", lambda: index))
        _l_(339809)
        return aux
    prefixIndex=_n_(339811, "index", lambda: index)/ 4
    _l_(339812)
    r = _n_(339813, "index", lambda: index) % 4
    _l_(339814)
    symbol=_c_(339817, _n_(339815, "NumberToSymbol", lambda: NumberToSymbol), _n_(339816, "r", lambda: r))
    _l_(339818)
    PrefixPattern =_c_(339822, _n_(339819, "NumberToPattern", lambda: NumberToPattern), _n_(339820, "prefixIndex", lambda: prefixIndex), _n_(339821, "k", lambda: k)-1)
    _l_(339823)
    aux = _n_(339824, "PrefixPattern", lambda: PrefixPattern)+ _n_(339825, "symbol", lambda: symbol)
    _l_(339826)
    return aux

_c_(339831, _n_(339828, "print", lambda: print), _c_(339830, _n_(339829, "NumberToPattern", lambda: NumberToPattern), 45,4))
_l_(339832)