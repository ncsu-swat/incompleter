# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(62884)

except ImportError:
    pass
with _c_(62886, _n_(62885, "open", lambda: open), 'some.csv', 'w', newline='') as f:
    _l_(62897)

    writer = _c_(62890, _a_(62888, _n_(62887, "csv", lambda: csv), "writer"), _n_(62889, "f", lambda: f))
    _l_(62891)
    _c_(62895, _a_(62893, _n_(62892, "writer", lambda: writer), "writerow"), _n_(62894, "l", lambda: l))  # this will output l as a single row.  
    _l_(62896)  # this will output l as a single row.  

