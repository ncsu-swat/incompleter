# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75198341/filenotfounderror-errno-2-no-such-file-or-directory-sp500-stocks-csv
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import errno
    _l_(396293)

except ImportError:
    pass
try:
    import os
    _l_(396295)

except ImportError:
    pass

raise _c_(396304, _n_(396296, "FileNotFoundError", lambda: FileNotFoundError), _a_(396298, _n_(396297, "errno", lambda: errno), "ENOENT"), _c_(396303, _a_(396300, _n_(396299, "os", lambda: os), "strerror"), _a_(396302, _n_(396301, "errno", lambda: errno), "ENOENT")), 'sp500_stocks.csv')
_l_(396305)