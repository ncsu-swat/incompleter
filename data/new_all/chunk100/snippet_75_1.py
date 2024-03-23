# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from itertools import groupby
    _l_(77218)

except ImportError:
    pass

def encode_list(s_list):
    _l_(77229)

    aux = [[_c_(77223, _n_(77219, "len", lambda: len), _c_(77222, _n_(77220, "list", lambda: list), _n_(77221, "group", lambda: group))), _n_(77224, "key", lambda: key)] for (key, group) in _c_(77227, _n_(77225, "groupby", lambda: groupby), _n_(77226, "s_list", lambda: s_list))]
    _l_(77228)
    return aux
_c_(77231, _n_(77230, "print", lambda: print), 'Original list:')
_l_(77232)
_c_(77235, _n_(77233, "print", lambda: print), _n_(77234, "n_list", lambda: n_list))
_l_(77236)
_c_(77238, _n_(77237, "print", lambda: print), '\nList reflecting the run-length encoding from the said list:')
_l_(77239)
_c_(77244, _n_(77240, "print", lambda: print), _c_(77243, _n_(77241, "encode_list", lambda: encode_list), _n_(77242, "n_list", lambda: n_list)))
_l_(77245)
n_list = 'automatically'
_l_(77246)
_c_(77248, _n_(77247, "print", lambda: print), '\nOriginal String:')
_l_(77249)
_c_(77252, _n_(77250, "print", lambda: print), _n_(77251, "n_list", lambda: n_list))
_l_(77253)
_c_(77255, _n_(77254, "print", lambda: print), '\nList reflecting the run-length encoding from the said string:')
_l_(77256)
_c_(77261, _n_(77257, "print", lambda: print), _c_(77260, _n_(77258, "encode_list", lambda: encode_list), _n_(77259, "n_list", lambda: n_list)))
_l_(77262)