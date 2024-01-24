# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51110837/dataframe-attributeerror-nonetype-object-has-no-attribute-iloc
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for j in _c_(438222, _n_(438220, "range", lambda: range), _n_(438221, "column", lambda: column)):
    _l_(438237)

    if _c_(438228, _a_(438224, _n_(438223, "np", lambda: np), "all"), _a_(438226, _n_(438225, "traindata", lambda: traindata), "iloc")[:, _n_(438227, "j", lambda: j)] == 0):
        _l_(438236)

        traindata = _c_(438234, _a_(438230, _n_(438229, "traindata", lambda: traindata), "drop"), _a_(438232, _n_(438231, "traindata", lambda: traindata), "columns")[_n_(438233, "j", lambda: j)], axis=1, inplace=True)                
        _l_(438235)                
_c_(438241, _n_(438238, "print", lambda: print), _a_(438240, _n_(438239, "traindata", lambda: traindata), "shape"))
_l_(438242)