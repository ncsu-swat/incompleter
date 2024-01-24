# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75473452/why-is-python-throwing-a-nameerror-when-doing-nested-exceptions-with-same-variab
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    _l_(425818)

    1 / 0
    _l_(425806)
except _n_(425807, "ZeroDivisionError", lambda: ZeroDivisionError) as error:
    _l_(425817)

    try:
        _l_(425812)

        [1, 2, 3][3]
        _l_(425808)
    except _n_(425809, "IndexError", lambda: IndexError) as error:
        _l_(425811)

        pass
        _l_(425810)
    _c_(425815, _n_(425813, "print", lambda: print), "The last error was:", _n_(425814, "error", lambda: error))
    _l_(425816)