# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(72276)

except ImportError:
    pass
try:
    import re as re
    _l_(72278)

except ImportError:
    pass
_c_(72280, _n_(72279, "print", lambda: print), 'Original DataFrame:')
_l_(72281)
_c_(72284, _n_(72282, "print", lambda: print), _n_(72283, "df", lambda: df))
_l_(72285)

def remove_tags(string):
    _l_(72293)

    result = _c_(72289, _a_(72287, _n_(72286, "re", lambda: re), "sub"), '<.*?>', '', _n_(72288, "string", lambda: string))
    _l_(72290)
    aux = _n_(72291, "result", lambda: result)
    _l_(72292)
    return aux
_n_(72294, "df", lambda: df)['with_out_tags'] = _c_(72300, _a_(72296, _n_(72295, "df", lambda: df)['address'], "apply"), lambda cw: _c_(72299, _n_(72297, "remove_tags", lambda: remove_tags), _n_(72298, "cw", lambda: cw)))
_l_(72301)
_c_(72303, _n_(72302, "print", lambda: print), "\nSentences without tags':")
_l_(72304)
_c_(72307, _n_(72305, "print", lambda: print), _n_(72306, "df", lambda: df))
_l_(72308)