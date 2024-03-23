# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(98240)

except ImportError:
    pass
_c_(98243, _a_(98242, _n_(98241, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(98244)
df = _c_(98247, _a_(98246, _n_(98245, "pd", lambda: pd), "DataFrame"), {'book_name': ['Book1', 'Book2', 'Book3', 'Book4', 'Book1', 'Book2', 'Book3', 'Book5'], 'book_type': ['Math', 'Physics', 'Computer', 'Science', 'Math', 'Physics', 'Computer', 'English'], 'book_id': [1, 2, 3, 4, 1, 2, 3, 5]})
_l_(98248)
_c_(98250, _n_(98249, "print", lambda: print), 'Original Orders DataFrame:')
_l_(98251)
_c_(98254, _n_(98252, "print", lambda: print), _n_(98253, "df", lambda: df))
_l_(98255)
_c_(98257, _n_(98256, "print", lambda: print), '\nNew column with count from groupby:')
_l_(98258)
_c_(98261, _n_(98259, "print", lambda: print), _n_(98260, "result", lambda: result))
_l_(98262)