# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71484368/typeerror-data-type-category-not-understood-while-looping-through-the-column
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
for col in _a_(588235, _n_(588234, "data", lambda: data), "columns"):
    _l_(588250)

    if _a_(588238, _n_(588236, "data", lambda: data)[_n_(588237, "col", lambda: col)], "dtype") == "category":
        _l_(588249)

        _c_(588244, _n_(588239, "print", lambda: print), _c_(588243, _a_(588242, _n_(588240, "data", lambda: data)[_n_(588241, "col", lambda: col)], "value_counts")))
        _l_(588245)
        _c_(588247, _n_(588246, "print", lambda: print), "\n\n")
        _l_(588248)