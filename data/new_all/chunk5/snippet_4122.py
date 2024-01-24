# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62621292/filenotfounderror-errno-2-reading-a-file-via-jupyter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(705539)

except ImportError:
    pass
df = _c_(705542, _a_(705541, _n_(705540, "pd", lambda: pd), "read_csv"), 'vgsales.csv')
_l_(705543)
_n_(705544, "df", lambda: df)
_l_(705545)