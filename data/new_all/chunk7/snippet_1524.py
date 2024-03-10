# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45099933/filenotfounderror-file-does-not-exist
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(460327)

except ImportError:
    pass

df = _c_(460330, _a_(460329, _n_(460328, "pd", lambda: pd), "read_csv"), "E:\YangJian\jupyter notebook\movie_metadata.csv")
_l_(460331)
train = _c_(460334, _a_(460333, _n_(460332, "pd", lambda: pd), "read_csv"), "E:\YangJian\jupyter notebook\train_modified.csv")
_l_(460335)