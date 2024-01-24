# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54402080/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-when-s
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(674590)

except ImportError:
    pass
try:
    from pybloqs import Block, html
    _l_(674592)

except ImportError:
    pass
try:
    import pybloqs.block.table_formatters as tf
    _l_(674594)

except ImportError:
    pass

d = {'one': [1., 2., 3., 4.],
 'two': [4., 3., 2., 1.]}
_l_(674595)

df  =  _c_(674599, _a_(674597, _n_(674596, "pd", lambda: pd), "DataFrame"), _n_(674598, "d", lambda: d))
_l_(674600)

block_df =  _c_(674603, _n_(674601, "Block", lambda: Block), _n_(674602, "df", lambda: df), formatters=None, use_default_formatters=True)
_l_(674604)
_c_(674607, _a_(674606, _n_(674605, "block_df", lambda: block_df), "save"), 'test.pdf')
_l_(674608)