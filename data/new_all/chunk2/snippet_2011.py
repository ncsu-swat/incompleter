# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70372223/trying-to-figure-this-error-attributeerror-int-object-has-no-attribute-keys
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data_keys = _c_(427920, _n_(427917, "list", lambda: list), _c_(427919, _n_(427918, "range", lambda: range), -5, -11, -1))
_l_(427921)
result = {}
_l_(427922)

for element in _n_(427923, "data_keys", lambda: data_keys):
    _l_(427929)

    _n_(427924, "result", lambda: result)[_n_(427925, "element", lambda: element)] = _c_(427927, _n_(427926, "random", lambda: random))
    _l_(427928)

sorted_values = _c_(427938, _a_(427931, _n_(427930, "collections", lambda: collections), "OrderedDict"), _c_(427937, _n_(427932, "sorted", lambda: sorted), _c_(427935, _a_(427934, _n_(427933, "result", lambda: result), "items")), key=lambda t: _n_(427936, "t", lambda: t)[1]))
_l_(427939)

_c_(427942, _n_(427940, "pprint", lambda: pprint), _n_(427941, "sorted_values", lambda: sorted_values))
_l_(427943)

d = _c_(427946, _n_(427944, "dict", lambda: dict), _n_(427945, "sorted_values", lambda: sorted_values))
_l_(427947)
_c_(427950, _n_(427948, "pprint", lambda: pprint), _n_(427949, "d", lambda: d))
_l_(427951)

with _c_(427953, _n_(427952, "open", lambda: open), 'ordered-values.csv', 'w', newline='') as file:
    _l_(427972)

    fieldnames = ['keys', 'values']
    _l_(427954)
    writer = _c_(427959, _a_(427956, _n_(427955, "csv", lambda: csv), "DictWriter"), _n_(427957, "file", lambda: file), fieldnames=_n_(427958, "fieldnames", lambda: fieldnames))
    _l_(427960)

    _c_(427963, _a_(427962, _n_(427961, "writer", lambda: writer), "writeheader"))
    _l_(427964)
    for data in _n_(427965, "d", lambda: d):
        _l_(427971)

        _c_(427969, _a_(427967, _n_(427966, "writer", lambda: writer), "writerow"), _n_(427968, "data", lambda: data))
        _l_(427970)