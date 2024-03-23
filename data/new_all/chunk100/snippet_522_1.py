# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import OrderedDict
    _l_(53282)

except ImportError:
    pass
dict = {'Afghanistan': 93, 'Albania': 355, 'Algeria': 213, 'Andorra': 376, 'Angola': 244}
_l_(53283)
for key in _n_(53284, "new_dict", lambda: new_dict):
    _l_(53291)

    _c_(53289, _n_(53285, "print", lambda: print), _n_(53286, "key", lambda: key), _n_(53287, "new_dict", lambda: new_dict)[_n_(53288, "key", lambda: key)])
    _l_(53290)
_c_(53293, _n_(53292, "print", lambda: print), '\nIn reverse order:')
_l_(53294)
for key in _c_(53297, _n_(53295, "reversed", lambda: reversed), _n_(53296, "new_dict", lambda: new_dict)):
    _l_(53304)

    _c_(53302, _n_(53298, "print", lambda: print), _n_(53299, "key", lambda: key), _n_(53300, "new_dict", lambda: new_dict)[_n_(53301, "key", lambda: key)])
    _l_(53303)