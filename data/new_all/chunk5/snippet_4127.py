# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62621292/filenotfounderror-errno-2-reading-a-file-via-jupyter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(700618)

except ImportError:
    pass
df = _c_(700621, _a_(700620, _n_(700619, "pd", lambda: pd), "read_csv"), 'vgsales.csv')
_l_(700622)
_n_(700623, "df", lambda: df)
_l_(700624)