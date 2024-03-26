# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(118982)

except ImportError:
    pass
try:
    import re as re
    _l_(118984)

except ImportError:
    pass
_c_(118986, _n_(118985, "print", lambda: print), 'Original DataFrame:')
_l_(118987)
_c_(118990, _n_(118988, "print", lambda: print), _n_(118989, "df", lambda: df))
_l_(118991)

def search_words(text):
    _l_(119001)

    result = _c_(118995, _a_(118993, _n_(118992, "re", lambda: re), "findall"), '\\b[^\\d\\W]+\\b', _n_(118994, "text", lambda: text))
    _l_(118996)
    aux = _c_(118999, _a_(118997, ' ', "join"), _n_(118998, "result", lambda: result))
    _l_(119000)
    return aux
_n_(119002, "df", lambda: df)['only_words'] = _c_(119008, _a_(119004, _n_(119003, "df", lambda: df)['address'], "apply"), lambda x: _c_(119007, _n_(119005, "search_words", lambda: search_words), _n_(119006, "x", lambda: x)))
_l_(119009)
_c_(119011, _n_(119010, "print", lambda: print), '\nOnly words:')
_l_(119012)
_c_(119015, _n_(119013, "print", lambda: print), _n_(119014, "df", lambda: df))
_l_(119016)