# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55476347/how-to-eliminate-type-error-while-using-pandas-apply-function-with-a-lambda-expr
#import modules
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(555361)

except ImportError:
    pass

#define functions
def read_datafile():
    _l_(555368)

    d = _c_(555364, _a_(555363, _n_(555362, "pd", lambda: pd), "read_csv"), 'cmc.data.txt', sep=',')
    _l_(555365)
    aux = _n_(555366, "d", lambda: d)
    _l_(555367)
    return aux

def create_bin_label(data):
    _l_(555379)

    _n_(555369, "data", lambda: data)['numchildren'] = _c_(555373, _a_(555371, _n_(555370, "data", lambda: data), "apply"), lambda row: 1 if (_n_(555372, "row", lambda: row)['number of children']) <= 0 else 0, axis=1)
    _l_(555374)
    data = _c_(555377, _a_(555376, _n_(555375, "data", lambda: data), "drop"), ['number of children'], axis=1)
    _l_(555378)

#read in datafile
data = _c_(555381, _n_(555380, "read_datafile", lambda: read_datafile))
_l_(555382)
_c_(555387, _n_(555383, "print", lambda: print), _c_(555386, _n_(555384, "len", lambda: len), _n_(555385, "data", lambda: data)))
_l_(555388)

#create a binary label column and delete the old column
bl = _c_(555391, _n_(555389, "create_bin_label", lambda: create_bin_label), _n_(555390, "data", lambda: data))
_l_(555392)
_c_(555397, _n_(555393, "print", lambda: print), _c_(555396, _a_(555395, _n_(555394, "data", lambda: data), "head")))
_l_(555398)