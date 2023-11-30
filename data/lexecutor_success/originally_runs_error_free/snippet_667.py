# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/11941817/how-to-avoid-runtimeerror-dictionary-changed-size-during-iteration-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
dicti = {
"k0_l0":{
    "k0_l1": {
        "k0_l2": {
                "k0_0":None,
                "k1_1":1,
                "k2_2":2.2
                }
        },
        "k1_l1":None,
        "k2_l1":"not none",
        "k3_l1":[]
    },
    "k1_l0":"l0"
}
_l_(1541835)

def pop_nested_nulls(dicti):
    _l_(1541863)

    for k in _c_(1541838, _n_(1541836, "list", lambda: list), _n_(1541837, "dicti", lambda: dicti)):
        _l_(1541860)

        if _c_(1541843, _n_(1541839, "isinstance", lambda: isinstance), _n_(1541840, "dicti", lambda: dicti)[_n_(1541841, "k", lambda: k)], _n_(1541842, "dict", lambda: dict)):
            _l_(1541859)

            _n_(1541844, "dicti", lambda: dicti)[_n_(1541845, "k", lambda: k)] = _c_(1541849, _n_(1541846, "pop_nested_nulls", lambda: pop_nested_nulls), _n_(1541847, "dicti", lambda: dicti)[_n_(1541848, "k", lambda: k)])
            _l_(1541850)
        elif not _n_(1541851, "dicti", lambda: dicti)[_n_(1541852, "k", lambda: k)]:
            _l_(1541858)

            _c_(1541856, _a_(1541854, _n_(1541853, "dicti", lambda: dicti), "pop"), _n_(1541855, "k", lambda: k))
            _l_(1541857)
    aux = _n_(1541861, "dicti", lambda: dicti)
    _l_(1541862)
    return aux

{'k0_l0': {'k0_l1': {'k0_l2': {'k1_1': 1,
                               'k2_2': 2.2}},
           'k2_l1': 'not '
                    'none'},
 'k1_l0': 'l0'}
_l_(1541864)

