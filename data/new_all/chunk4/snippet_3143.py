# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40559769/typeerror-cant-convert-module-object-to-str-implicitly
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(618028)

except ImportError:
    pass
try:
    import csv
    _l_(618030)

except ImportError:
    pass
try:
    import os
    _l_(618032)

except ImportError:
    pass

#readfile
loandata=_c_(618038, _a_(618034, _n_(618033, "pd", lambda: pd), "DataFrame"), _c_(618037, _a_(618036, _n_(618035, "pd", lambda: pd), "read_table"), '/Users/lixuefei/Desktop/Sample Dataset/test.txt',header = None,index_col=2))
_l_(618039)

#classify
volume_type=_c_(618044, _n_(618040, "list", lambda: list), _c_(618043, _n_(618041, "set", lambda: set), _n_(618042, "loandata", lambda: loandata)[3]))
_l_(618045)
system_type=_c_(618050, _n_(618046, "list", lambda: list), _c_(618049, _n_(618047, "set", lambda: set), _n_(618048, "loandata", lambda: loandata)[4]))
_l_(618051)
area_name=_c_(618056, _n_(618052, "list", lambda: list), _c_(618055, _n_(618053, "set", lambda: set), _n_(618054, "loandata", lambda: loandata)[5]))
_l_(618057)

df=_c_(618067, _a_(618059, _n_(618058, "pd", lambda: pd), "DataFrame"), _n_(618060, "loandata", lambda: loandata)[(_n_(618061, "loandata", lambda: loandata)[3]==_n_(618062, "volume_type", lambda: volume_type)[0])& (_n_(618063, "loandata", lambda: loandata)[4]==_n_(618064, "system_type", lambda: system_type)[0])&(_n_(618065, "loandata", lambda: loandata)[5]==_n_(618066, "area_name", lambda: area_name)[0])])
_l_(618068)
#set the file path
path='/Users/lixuefei/Desktop/Sample Dataset'
_l_(618069)
filename=_n_(618070, "volume_type", lambda: volume_type)[0]+_n_(618071, "system_type", lambda: system_type)[0]+_n_(618072, "area_name", lambda: area_name)[0]
_l_(618073)
filetype=_n_(618074, "csv", lambda: csv)
_l_(618075)

if not _a_(618077, _n_(618076, "df", lambda: df), "empty"):
    _l_(618092)

    _c_(618087, _a_(618079, _n_(618078, "df", lambda: df), "to_csv"), _c_(618086, _a_(618082, _a_(618081, _n_(618080, "os", lambda: os), "path"), "join"), _n_(618083, "path", lambda: path),_n_(618084, "filename", lambda: filename)+_n_(618085, "filetype", lambda: filetype)),header=None)
    _l_(618088)
else:
    _c_(618090, _n_(618089, "print", lambda: print), "Empty")
    _l_(618091)