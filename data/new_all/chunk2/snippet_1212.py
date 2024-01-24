# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30912607/python3-csv-dictwriter-writing-through-bz2-fails-typeerror-str-buffer-inter
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from csv import DictWriter
    _l_(447820)

except ImportError:
    pass
try:
    import bz2
    _l_(447822)

except ImportError:
    pass

FIELDNAMES = ('a', 'b')
_l_(447823)
OUT_BZ2 = 'out.csv.bz2'
_l_(447824)

DATA = ({'a': 1, 'b': 2}, {'a':3, 'b':4})
_l_(447825)

# this fails
with _c_(447829, _a_(447827, _n_(447826, "bz2", lambda: bz2), "open"), _n_(447828, "OUT_BZ2", lambda: OUT_BZ2), mode='w', compresslevel=9) as file_pointer:
    _l_(447846)

    csv_writer = _c_(447833, _n_(447830, "DictWriter", lambda: DictWriter), _n_(447831, "file_pointer", lambda: file_pointer), fieldnames=_n_(447832, "FIELDNAMES", lambda: FIELDNAMES))
    _l_(447834)
    _c_(447837, _a_(447836, _n_(447835, "csv_writer", lambda: csv_writer), "writeheader")) # fails here; raises "TypeError: 'str' does not support the buffer interface"
    _l_(447838) # fails here; raises "TypeError: 'str' does not support the buffer interface"
    for dataset in _n_(447839, "DATA", lambda: DATA):
        _l_(447845)

        _c_(447843, _a_(447841, _n_(447840, "csv_writer", lambda: csv_writer), "writerow"), _n_(447842, "dataset", lambda: dataset))
        _l_(447844)