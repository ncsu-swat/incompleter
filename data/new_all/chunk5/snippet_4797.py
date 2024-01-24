# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47968210/python-typeerror-str-object-cannot-be-interpreted-as-an-integer
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _n_(666186, "current_ins", lambda: current_ins)[0] == "REPEAT":
    _l_(666212)

    for i in _c_(666189, _n_(666187, "range", lambda: range), _n_(666188, "current_ins", lambda: current_ins)[1]):
        _l_(666211)

        if _n_(666190, "last_ins", lambda: last_ins) != "":
            _l_(666210)

            _c_(666194, _a_(666192, _n_(666191, "instructions", lambda: instructions), "append"), _n_(666193, "last_ins", lambda: last_ins))
            _l_(666195)
            if _n_(666196, "delay", lambda: delay) != -1:
                _l_(666202)

                _c_(666200, _a_(666198, _n_(666197, "instructions", lambda: instructions), "append"), ["DELAY", _n_(666199, "delay", lambda: delay)])
                _l_(666201)
        else:
            _c_(666204, _n_(666203, "print", lambda: print), "ERROR: REPEAT can't be the first instruction")
            _l_(666205)
            _c_(666208, _a_(666207, _n_(666206, "sys", lambda: sys), "exit"), -1)
            _l_(666209)