# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
new_list = _c_(1547670, _a_(1547669, _n_(1547668, "old_list", lambda: old_list), "copy"))
_l_(1547671)

new_list = _n_(1547672, "old_list", lambda: old_list)[:]
_l_(1547673)

new_list = _c_(1547676, _n_(1547674, "list", lambda: list), _n_(1547675, "old_list", lambda: old_list))
_l_(1547677)
try:
    import copy
    _l_(1547679)

except ImportError:
    pass
new_list = _c_(1547683, _a_(1547681, _n_(1547680, "copy", lambda: copy), "copy"), _n_(1547682, "old_list", lambda: old_list))
_l_(1547684)
try:
    import copy
    _l_(1547686)

except ImportError:
    pass
new_list = _c_(1547690, _a_(1547688, _n_(1547687, "copy", lambda: copy), "deepcopy"), _n_(1547689, "old_list", lambda: old_list))
_l_(1547691)
try:
    import copy
    _l_(1547693)

except ImportError:
    pass

class Foo(_n_(1547694, "object", lambda: object)):
    _l_(1547703)

    def __init__(self, val):
        _l_(1547698)

        _n_(1547695, "self", lambda: self).val = _n_(1547696, "val", lambda: val)
        _l_(1547697)

    def __repr__(self):
        _l_(1547702)

        aux = f'Foo({_a_(1547700, _n_(1547699, "self", lambda: self), "val")!r})'
        _l_(1547701)
        return aux

foo = _c_(1547705, _n_(1547704, 'Foo', lambda: Foo), 1)
_l_(1547706)

a = ['foo', _n_(1547707, 'foo', lambda: foo)]
_l_(1547708)
b = _c_(1547711, _a_(1547710, _n_(1547709, 'a', lambda: a), 'copy'))
_l_(1547712)
c = _n_(1547713, 'a', lambda: a)[:]
_l_(1547714)
d = _c_(1547717, _n_(1547715, 'list', lambda: list), _n_(1547716, 'a', lambda: a))
_l_(1547718)
e = _c_(1547722, _a_(1547720, _n_(1547719, 'copy', lambda: copy), 'copy'), _n_(1547721, 'a', lambda: a))
_l_(1547723)
f = _c_(1547727, _a_(1547725, _n_(1547724, 'copy', lambda: copy), 'deepcopy'), _n_(1547726, 'a', lambda: a))
_l_(1547728)

# edit orignal list and instance 
_c_(1547731, _a_(1547730, _n_(1547729, 'a', lambda: a), 'append'), 'baz')
_l_(1547732)
_n_(1547733, 'foo', lambda: foo).val = 5
_l_(1547734)

_c_(1547742, _n_(1547735, 'print', lambda: print), f'original: {_n_(1547736, "a", lambda: a)}\nlist.copy(): {_n_(1547737, "b", lambda: b)}\nslice: {_n_(1547738, "c", lambda: c)}\nlist(): {_n_(1547739, "d", lambda: d)}\ncopy: {_n_(1547740, "e", lambda: e)}\ndeepcopy: {_n_(1547741, "f", lambda: f)}')
_l_(1547743)

original: ['foo', _c_(1547745, _n_(1547744, 'Foo', lambda: Foo), 5), 'baz']
_l_(1547746)
_c_(1547749, _a_(1547748, _n_(1547747, 'list', lambda: list), 'copy')): ['foo', _c_(1547751, _n_(1547750, 'Foo', lambda: Foo), 5)]
_l_(1547752)
slice: ['foo', _c_(1547754, _n_(1547753, 'Foo', lambda: Foo), 5)]
_l_(1547755)
_c_(1547756, list): ['foo', _c_(1547758, _n_(1547757, 'Foo', lambda: Foo), 5)]
_l_(1547759)
copy: ['foo', _c_(1547761, _n_(1547760, 'Foo', lambda: Foo), 5)]
_l_(1547762)
deepcopy: ['foo', _c_(1547764, _n_(1547763, 'Foo', lambda: Foo), 1)]
_l_(1547765)

