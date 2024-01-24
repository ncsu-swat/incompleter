# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71011031/attributeerror-dataframe-object-has-no-attribute-operation
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def statSummary(dataset,operation):
    _l_(546271)

    operation = []
    _l_(546258)
    _c_(546265, _a_(546260, _n_(546259, "operation", lambda: operation), "append"), _c_(546264, _a_(546263, _n_(546261, "df", lambda: df)[_n_(546262, "dataset", lambda: dataset)], "operation")))
    _l_(546266)
    aux = _c_(546269, _n_(546267, "print", lambda: print), _n_(546268, "operation", lambda: operation))
    _l_(546270)

    return aux

#load dataset 
df = _c_(546274, _a_(546273, _n_(546272, "pd", lambda: pd), "read_csv"), 'dataset.csv')
_l_(546275)

columnNames = _c_(546279, _n_(546276, "list", lambda: list), _a_(546278, _n_(546277, "df", lambda: df), "columns"))
_l_(546280)

ops = ["mean","median","std","max","min"]
_l_(546281)

for i in _n_(546282, "ops", lambda: ops):
    _l_(546288)

    _c_(546286, _n_(546283, "statSummary", lambda: statSummary), _n_(546284, "columnNames", lambda: columnNames),_n_(546285, "i", lambda: i))
    _l_(546287)