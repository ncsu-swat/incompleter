# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159725/im-trying-to-use-the-classes-that-i-madevehicle-and-customer-but-i-get-typee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(693585)

except ImportError:
    pass
try:
    import csv
    _l_(693587)

except ImportError:
    pass

vehicle = 0
_l_(693588)
customers = []
_l_(693589)

class Vehicle:
    _l_(693597)

    def _init_(self, number, capacity):
        _l_(693596)

        _n_(693590, "self", lambda: self).number = _n_(693591, "number", lambda: number)
        _l_(693592)
        _n_(693593, "self", lambda: self).capacity = _n_(693594, "capacity", lambda: capacity)
        _l_(693595)


class customer:
    _l_(693620)

    def _init_(self, custNo, xCord, yCord, demand, readyT, dueDate, serviceTime):
        _l_(693619)

        _n_(693598, "self", lambda: self).custNo = _n_(693599, "custNo", lambda: custNo)
        _l_(693600)
        _n_(693601, "self", lambda: self).xCord = _n_(693602, "xCord", lambda: xCord)
        _l_(693603)
        _n_(693604, "self", lambda: self).yCord = _n_(693605, "yCord", lambda: yCord)
        _l_(693606)
        _n_(693607, "self", lambda: self).demand = _n_(693608, "demand", lambda: demand)
        _l_(693609)
        _n_(693610, "self", lambda: self).readyT = _n_(693611, "readyT", lambda: readyT)
        _l_(693612)
        _n_(693613, "self", lambda: self).dueDate = _n_(693614, "dueDate", lambda: dueDate)
        _l_(693615)
        _n_(693616, "self", lambda: self).serviceT = _n_(693617, "serviceTime", lambda: serviceTime)
        _l_(693618)


def read():
    _l_(693665)

    global vehicle
    _l_(693621)
    with _c_(693623, _n_(693622, "open", lambda: open), 'C101 BUENO.csv') as cvs_file:
        _l_(693664)

        cvs_reader = _c_(693627, _a_(693625, _n_(693624, "csv", lambda: csv), "reader"), _n_(693626, "cvs_file", lambda: cvs_file), delimiter=';')
        _l_(693628)
        line = 0
        _l_(693629)
        for row in _n_(693630, "cvs_reader", lambda: cvs_reader):
            _l_(693663)

            _c_(693633, _n_(693631, "print", lambda: print), _n_(693632, "line", lambda: line))
            _l_(693634)
            if _n_(693635, "line", lambda: line) == 0 or _n_(693636, "line", lambda: line) == 2:
                _l_(693662)

                line += 1
                _l_(693637)
            elif _n_(693638, "line", lambda: line) == 1:
                _l_(693661)

                vehicle = _c_(693642, _n_(693639, "Vehicle", lambda: Vehicle), _n_(693640, "row", lambda: row)[0], _n_(693641, "row", lambda: row)[1])
                _l_(693643)
                line += 1
                _l_(693644)
            else:
                c = _c_(693653, _n_(693645, "customer", lambda: customer), _n_(693646, "row", lambda: row)[0],_n_(693647, "row", lambda: row)[1],_n_(693648, "row", lambda: row)[2],_n_(693649, "row", lambda: row)[3],_n_(693650, "row", lambda: row)[4],_n_(693651, "row", lambda: row)[5],_n_(693652, "row", lambda: row)[6])
                _l_(693654)
                _c_(693658, _a_(693656, _n_(693655, "customers", lambda: customers), "append"), _n_(693657, "c", lambda: c))
                _l_(693659)
                line += 1
                _l_(693660)

_c_(693667, _n_(693666, "read", lambda: read))
_l_(693668)