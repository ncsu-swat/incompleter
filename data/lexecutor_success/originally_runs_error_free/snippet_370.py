# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def ordinal(year, month, day):
    _l_(1546344)

    aux = ((_n_(1546331, "year", lambda: year)-1)*365 + (_n_(1546332, "year", lambda: year)-1)//4 - (_n_(1546333, "year", lambda: year)-1)//100 + (_n_(1546334, "year", lambda: year)-1)//400
         + [ 0,31,59,90,120,151,181,212,243,273,304,334][_n_(1546335, "month", lambda: month) - 1]
         + _n_(1546336, "day", lambda: day)
         + _c_(1546342, _n_(1546337, "int", lambda: int), ((_n_(1546338, "year", lambda: year)%4==0 and _n_(1546339, "year", lambda: year)%100!=0) or _n_(1546340, "year", lambda: year)%400==0) and _n_(1546341, "month", lambda: month) > 2))
    _l_(1546343)
    return aux

_c_(1546350, _n_(1546345, "print", lambda: print), _c_(1546347, _n_(1546346, "ordinal", lambda: ordinal), 2021, 5, 10) - _c_(1546349, _n_(1546348, "ordinal", lambda: ordinal), 2001, 9, 11))
_l_(1546351)

