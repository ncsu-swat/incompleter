# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/29689863/why-do-i-get-typeerror-when-trying-to-do-dot-product
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sig = {'a': 1.0, 'b': 2.0, 'c': 3.0}
_l_(612940)
exp = {'a': (1.0,2.0,3.0), 'b': (1.0,2.0,3.0), 'c': (1.0,2.0,3.0)}
_l_(612941)
man_dot = {'a': 1*1+1*2+1*3, 'b': 2*1+2*2+2*3, 'c': 3*1+3*2+3*3}
_l_(612942)

weighted_dict = {}
_l_(612943)
for s in _n_(612944, "sig", lambda: sig):
    _l_(612968)

    _c_(612949, _n_(612945, "print", lambda: print), _c_(612948, _a_(612946, "this is s:\n{}", "format"), _n_(612947, "s", lambda: s)))
    _l_(612950)
    for e in _n_(612951, "exp", lambda: exp):
        _l_(612967)

        _c_(612956, _n_(612952, "print", lambda: print), _c_(612955, _a_(612953, "this is e:\n{}", "format"), _n_(612954, "e", lambda: e)))
        _l_(612957)
        _n_(612958, "weighted_dict", lambda: weighted_dict)[_n_(612959, "s", lambda: s)] = _c_(612965, _n_(612960, "sum", lambda: sum), _n_(612961, "sig", lambda: sig)[_n_(612962, "s", lambda: s)] * _n_(612963, "exp", lambda: exp)[_n_(612964, "e", lambda: e)])
        _l_(612966)
# weighted_dict should be equivalent to man_dot
# weighted_dict should be {'a': 6, 'c': 18, 'b': 12}