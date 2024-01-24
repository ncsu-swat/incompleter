# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67278695/typeerror-name-argument-1-must-be-a-unicode-character-not-str-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(594886)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(594888)

except ImportError:
    pass
try:
    import numpy as np
    _l_(594890)

except ImportError:
    pass
try:
    import re
    _l_(594892)

except ImportError:
    pass

crd = _c_(594895, _a_(594894, _n_(594893, "os", lambda: os), "getcwd"))
_l_(594896)
df_hash = _c_(594900, _a_(594898, _n_(594897, "pd", lambda: pd), "read_csv"), _n_(594899, "crd", lambda: crd) +"\\hashtag4.csv", encoding="utf-8")
_l_(594901)
try:
    from genderComputer import GenderComputer
    _l_(594903)

except ImportError:
    pass
gc = _c_(594905, _n_(594904, "GenderComputer", lambda: GenderComputer))
_l_(594906)

_n_(594907, "df_hash", lambda: df_hash)['gender'] = _c_(594911, _a_(594909, _n_(594908, "gc", lambda: gc), "resolveGender"), _n_(594910, "df_hash", lambda: df_hash)['full_name'], None)
_l_(594912)