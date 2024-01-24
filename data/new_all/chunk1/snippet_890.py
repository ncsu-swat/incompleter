# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52312736/getting-attributeerror-while-loading-and-accessing-the-data-using-csv-reader
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(398123)

except ImportError:
    pass
try:
    import numpy
    _l_(398125)

except ImportError:
    pass
def loadCsv(filename):
    _l_(398153)

    lines = _c_(398131, _a_(398127, _n_(398126, "csv", lambda: csv), "reader"), _c_(398130, _n_(398128, "open", lambda: open), _n_(398129, "filename", lambda: filename),"r"))
    _l_(398132)
    dataset = _c_(398135, _n_(398133, "list", lambda: list), _n_(398134, "lines", lambda: lines))
    _l_(398136)
    for i in _c_(398141, _n_(398137, "range", lambda: range), _c_(398140, _n_(398138, "len", lambda: len), _n_(398139, "dataset", lambda: dataset))):
        _l_(398150)

        _n_(398142, "dataset", lambda: dataset)[_n_(398143, "i", lambda: i)] = [_c_(398146, _n_(398144, "float", lambda: float), _n_(398145, "x", lambda: x)) for x in _n_(398147, "dataset", lambda: dataset)[_n_(398148, "i", lambda: i)]]
        _l_(398149)
    aux = _n_(398151, "dataset", lambda: dataset)
    _l_(398152)
    return aux
filename = 'data1.csv'
_l_(398154)
dataset = _c_(398157, _n_(398155, "loadCsv", lambda: loadCsv), _n_(398156, "filename", lambda: filename))
_l_(398158)
_c_(398166, _a_(398161, _c_(398160, _n_(398159, "print", lambda: print), 'Loaded data file {0} with {1} rows'), "format"), _n_(398162, "filename", lambda: filename), _c_(398165, _n_(398163, "len", lambda: len), _n_(398164, "dataset", lambda: dataset)))
_l_(398167)