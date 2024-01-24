# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57472047/trying-to-connect-hdfs-using-python-client-library-pyarrow-but-getting-error-fil
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyarrow
    _l_(380375)

except ImportError:
    pass
try:
    import os
    _l_(380377)

except ImportError:
    pass
try:
    import posixpath
    _l_(380379)

except ImportError:
    pass
try:
    import sys
    _l_(380381)

except ImportError:
    pass
try:
    from pyarrow.util import implements
    _l_(380383)

except ImportError:
    pass
try:
    from pyarrow.filesystem import FileSystem
    _l_(380385)

except ImportError:
    pass
try:
    import pyarrow.lib as lib
    _l_(380387)

except ImportError:
    pass

_c_(380391, _a_(380390, _a_(380389, _n_(380388, "pyarrow", lambda: pyarrow), "hdfs"), "connect"), host='xx.xx.xx.xx', port=22, user='cloudera', kerb_ticket=None, driver='libhdfs', extra_conf=None)
_l_(380392)