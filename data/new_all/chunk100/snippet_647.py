# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/20199126/reading-json-from-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(61624)

except ImportError:
    pass
df = _c_(61627, _a_(61626, _n_(61625, "pd", lambda: pd), "read_json"), 'strings.json', lines=True)
_l_(61628)
_c_(61631, _n_(61629, "print", lambda: print), _n_(61630, "df", lambda: df))
_l_(61632)

