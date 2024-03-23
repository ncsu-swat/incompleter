# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(98264)

except ImportError:
    pass
_c_(98267, _a_(98266, _n_(98265, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(98268)
_c_(98270, _n_(98269, "print", lambda: print), 'Original Orders DataFrame:')
_l_(98271)
_c_(98274, _n_(98272, "print", lambda: print), _n_(98273, "df", lambda: df))
_l_(98275)
_c_(98277, _n_(98276, "print", lambda: print), '\nNew column with count from groupby:')
_l_(98278)
result = _c_(98285, _a_(98284, _c_(98283, _a_(98282, _c_(98281, _a_(98280, _n_(98279, "df", lambda: df), "groupby"), ['book_name', 'book_type'])['book_type'], "count")), "reset_index"), name='count')
_l_(98286)
_c_(98289, _n_(98287, "print", lambda: print), _n_(98288, "result", lambda: result))
_l_(98290)