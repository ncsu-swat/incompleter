# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43197848/python-regex-issue-involving-typeerror-expected-string-or-bytes-like-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(547557)

except ImportError:
    pass
original_file = _c_(547559, _n_(547558, "open", lambda: open), 'jokes.txt', 'r+')
_l_(547560)
_c_(547563, _a_(547562, _n_(547561, "original_file", lambda: original_file), "read"))
_l_(547564)
original_file = _c_(547568, _a_(547566, _n_(547565, "re", lambda: re), "sub"), "\d+\. ", "", _n_(547567, "original_file", lambda: original_file))
_l_(547569)