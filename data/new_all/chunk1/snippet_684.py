# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57823653/typeerror-headers-is-an-invalid-keyword-argument-for-print
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from tabulate import tabulate
    _l_(386652)

except ImportError:
    pass
i: _n_(386653, "int", lambda: int)
_l_(386654)
with _c_(386656, _n_(386655, "open", lambda: open), "incre.txt", "w") as file:
    _l_(386686)


    for i in _c_(386658, _n_(386657, "range", lambda: range), 1, 100,5):
        _l_(386674)

        mol = _c_(386662, _n_(386659, "int", lambda: int), (_n_(386660, "i", lambda: i)*50)/(_n_(386661, "i", lambda: i)+50))
        _l_(386663)
        _c_(386672, _a_(386665, _n_(386664, "file", lambda: file), "write"), _c_(386668, _n_(386666, "str", lambda: str), _n_(386667, "i", lambda: i))+ " " +_c_(386671, _n_(386669, "str", lambda: str), _n_(386670, "mol", lambda: mol)) + "\n")
        _l_(386673)
    _c_(386680, _n_(386675, "print", lambda: print), _c_(386679, _n_(386676, "tabulate", lambda: tabulate), [[_n_(386677, "i", lambda: i)], [_n_(386678, "mol", lambda: mol)]]), headers=['i' , 'mol'], tablefmt='orgtbl')
    _l_(386681)
    _c_(386684, _a_(386683, _n_(386682, "file", lambda: file), "close"))
    _l_(386685)