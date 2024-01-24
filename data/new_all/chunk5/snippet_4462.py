# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57211695/importing-modules-results-in-attribute-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(671729)

except ImportError:
    pass
try:
    import seaborn
    _l_(671731)

except ImportError:
    pass


x = []
_l_(671732)
y = []
_l_(671733)

with _c_(671735, _n_(671734, "open", lambda: open), 'main.csv','r') as csvfile:
    _l_(671761)

    plots = _c_(671739, _a_(671737, _n_(671736, "csv", lambda: csv), "reader"), _n_(671738, "csvfile", lambda: csvfile), delimiter=',')
    _l_(671740)
    count = 1
    _l_(671741)
    for row in _n_(671742, "plots", lambda: plots):
        _l_(671760)

        if _n_(671743, "count", lambda: count) % 2 == 1:
            _l_(671758)

            _c_(671749, _a_(671745, _n_(671744, "x", lambda: x), "append"), _c_(671748, _n_(671746, "int", lambda: int), _n_(671747, "row", lambda: row)[0]))
            _l_(671750)
            _c_(671756, _a_(671752, _n_(671751, "y", lambda: y), "append"), _c_(671755, _n_(671753, "int", lambda: int), _n_(671754, "row", lambda: row)[1]))
            _l_(671757)
        count += 1
        _l_(671759)

_c_(671766, _a_(671763, _n_(671762, "seaborn", lambda: seaborn), "scatterplot"), _n_(671764, "x", lambda: x), _n_(671765, "y", lambda: y))
_l_(671767)