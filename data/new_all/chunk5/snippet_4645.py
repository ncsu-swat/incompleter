# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53586382/csv-file-and-typeerror-a-bytes-like-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
seat =[]
_l_(660782)
csvfile = _c_(660784, _n_(660783, "open", lambda: open), 'coba.csv') 
_l_(660785) 
seating = _c_(660789, _a_(660787, _n_(660786, "csv", lambda: csv), "reader"), _n_(660788, "csvfile", lambda: csvfile))
_l_(660790)
for line in _n_(660791, "seating", lambda: seating):
    _l_(660797)

    _c_(660795, _a_(660793, _n_(660792, "seat", lambda: seat), "append"), _n_(660794, "line", lambda: line))
    _l_(660796)

_c_(660799, _n_(660798, "print", lambda: print), "Buy seat ?")
_l_(660800)
answer_1 = _c_(660802, _n_(660801, "input", lambda: input), "Answer : ")
_l_(660803)
if (_n_(660804, "answer_1", lambda: answer_1) == "yes"):
    _l_(660835)

    answer_2 = _c_(660806, _n_(660805, "input", lambda: input), "Enter preferred seat: ")
    _l_(660807)
    if (_n_(660808, "answer_2", lambda: answer_2) == "A1"):
        _l_(660834)

        row = 1
        _l_(660809)
        column = 0
        _l_(660810)
        _n_(660811, "seat", lambda: seat)[_n_(660812, "row", lambda: row)][_n_(660813, "column", lambda: column)] = "X"
        _l_(660814)
        writer = _c_(660819, _a_(660816, _n_(660815, "csv", lambda: csv), "writer"), _c_(660818, _n_(660817, "open", lambda: open), 'coba.csv', 'wb'))
        _l_(660820)
        _c_(660824, _a_(660822, _n_(660821, "writer", lambda: writer), "writerows"), _n_(660823, "seat", lambda: seat))
        _l_(660825)
        for line in _n_(660826, "seat", lambda: seat):
            _l_(660833)

            _c_(660831, _n_(660827, "print", lambda: print), _c_(660830, _a_(660828, ' | ', "join"), _n_(660829, "line", lambda: line)))
            _l_(660832)