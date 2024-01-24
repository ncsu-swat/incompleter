# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56159725/im-trying-to-use-the-classes-that-i-madevehicle-and-customer-but-i-get-typee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(690571)

except ImportError:
    pass
try:
    import csv
    _l_(690573)

except ImportError:
    pass

vehicle = 0
_l_(690574)
customers = []
_l_(690575)

class Vehicle:
    _l_(690583)

    def _init_(self, number, capacity):
        _l_(690582)

        _n_(690576, "self", lambda: self).number = _n_(690577, "number", lambda: number)
        _l_(690578)
        _n_(690579, "self", lambda: self).capacity = _n_(690580, "capacity", lambda: capacity)
        _l_(690581)


class customer:
    _l_(690606)

    def _init_(self, custNo, xCord, yCord, demand, readyT, dueDate, serviceTime):
        _l_(690605)

        _n_(690584, "self", lambda: self).custNo = _n_(690585, "custNo", lambda: custNo)
        _l_(690586)
        _n_(690587, "self", lambda: self).xCord = _n_(690588, "xCord", lambda: xCord)
        _l_(690589)
        _n_(690590, "self", lambda: self).yCord = _n_(690591, "yCord", lambda: yCord)
        _l_(690592)
        _n_(690593, "self", lambda: self).demand = _n_(690594, "demand", lambda: demand)
        _l_(690595)
        _n_(690596, "self", lambda: self).readyT = _n_(690597, "readyT", lambda: readyT)
        _l_(690598)
        _n_(690599, "self", lambda: self).dueDate = _n_(690600, "dueDate", lambda: dueDate)
        _l_(690601)
        _n_(690602, "self", lambda: self).serviceT = _n_(690603, "serviceTime", lambda: serviceTime)
        _l_(690604)


def read():
    _l_(690651)

    global vehicle
    _l_(690607)
    with _c_(690609, _n_(690608, "open", lambda: open), 'C101 BUENO.csv') as cvs_file:
        _l_(690650)

        cvs_reader = _c_(690613, _a_(690611, _n_(690610, "csv", lambda: csv), "reader"), _n_(690612, "cvs_file", lambda: cvs_file), delimiter=';')
        _l_(690614)
        line = 0
        _l_(690615)
        for row in _n_(690616, "cvs_reader", lambda: cvs_reader):
            _l_(690649)

            _c_(690619, _n_(690617, "print", lambda: print), _n_(690618, "line", lambda: line))
            _l_(690620)
            if _n_(690621, "line", lambda: line) == 0 or _n_(690622, "line", lambda: line) == 2:
                _l_(690648)

                line += 1
                _l_(690623)
            elif _n_(690624, "line", lambda: line) == 1:
                _l_(690647)

                vehicle = _c_(690628, _n_(690625, "Vehicle", lambda: Vehicle), _n_(690626, "row", lambda: row)[0], _n_(690627, "row", lambda: row)[1])
                _l_(690629)
                line += 1
                _l_(690630)
            else:
                c = _c_(690639, _n_(690631, "customer", lambda: customer), _n_(690632, "row", lambda: row)[0],_n_(690633, "row", lambda: row)[1],_n_(690634, "row", lambda: row)[2],_n_(690635, "row", lambda: row)[3],_n_(690636, "row", lambda: row)[4],_n_(690637, "row", lambda: row)[5],_n_(690638, "row", lambda: row)[6])
                _l_(690640)
                _c_(690644, _a_(690642, _n_(690641, "customers", lambda: customers), "append"), _n_(690643, "c", lambda: c))
                _l_(690645)
                line += 1
                _l_(690646)

_c_(690653, _n_(690652, "read", lambda: read))
_l_(690654)