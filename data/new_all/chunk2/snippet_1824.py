# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51661377/appending-json-file-typeerror-list-indices-must-be-integers-or-slices-not-st
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
filepath = _c_(472212, _a_(472211, _a_(472210, _n_(472209, "os", lambda: os), "path"), "join"), 'filename.json')   
_l_(472213)   
with _c_(472216, _n_(472214, "open", lambda: open), _n_(472215, "filepath", lambda: filepath)) as jsonfile:
    _l_(472235)

    json_data = _c_(472220, _a_(472218, _n_(472217, "json", lambda: json), "load"), _n_(472219, "jsonfile", lambda: jsonfile))
    _l_(472221)

    for i in _c_(472226, _n_(472222, "range", lambda: range), _c_(472225, _n_(472223, "len", lambda: len), _n_(472224, "json_data", lambda: json_data))):
        _l_(472234)

        itemId = _n_(472227, "json_data", lambda: json_data)[_n_(472228, "i", lambda: i)]['itemId']
        _l_(472229)
        _c_(472232, _n_(472230, "print", lambda: print), _n_(472231, "itemId", lambda: itemId))
        _l_(472233)