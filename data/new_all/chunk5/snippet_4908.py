# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41153215/sum-columns-in-2-d-array-typeerror-list-indices-must-be-integers-or-slices-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
array = [[3, 5, 7, 9]
        [2, 7, 3, 5],
        [1, 2, 6, 3],
        [6, 9, 5, 3]]
_l_(653284)

column_sum = []
_l_(653285)
total = 0
_l_(653286)
i = 0
_l_(653287)
for row in _n_(653288, "aList", lambda: aList):
    _l_(653301)

    total = _n_(653289, "total", lambda: total) + _n_(653290, "row", lambda: row)[_n_(653291, "i", lambda: i)]
    _l_(653292)
    _c_(653296, _a_(653294, _n_(653293, "column_sum", lambda: column_sum), "append"), _n_(653295, "total", lambda: total))
    _l_(653297)
    total = 0
    _l_(653298)
    i = _n_(653299, "i", lambda: i) + 1
    _l_(653300)
_c_(653304, _n_(653302, "print", lambda: print), _n_(653303, "column_sum", lambda: column_sum))
_l_(653305)