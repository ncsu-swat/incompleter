# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76737790/filenotfounderror-using-gcsfs-and-pandas-but-only-on-my-machine
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import gcsfs
    _l_(561104)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(561106)

except ImportError:
    pass
x = _c_(561109, _a_(561108, _n_(561107, "pd", lambda: pd), "read_table"), "gs://MYBUCKET/clinvar/gene_specific_summary.txt")
_l_(561110)