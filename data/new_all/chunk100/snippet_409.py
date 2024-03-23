# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
#!python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _c_(61485, _n_(61484, "open", lambda: open), '/pythonwork/thefile_subset11.csv', 'w', newline='') as outfile:
    _l_(61491)

    writer = _c_(61489, _a_(61487, _n_(61486, "csv", lambda: csv), "writer"), _n_(61488, "outfile", lambda: outfile))
    _l_(61490)

#!python2
with _c_(61493, _n_(61492, "open", lambda: open), '/pythonwork/thefile_subset11.csv', 'wb') as outfile:
    _l_(61499)

    writer = _c_(61497, _a_(61495, _n_(61494, "csv", lambda: csv), "writer"), _n_(61496, "outfile", lambda: outfile))
    _l_(61498)

