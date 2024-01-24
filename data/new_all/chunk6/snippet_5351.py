# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62960685/why-do-i-receive-error-typeerror-argument-of-type-name-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Person:
    _l_(362298)

    def __init__(self):
        _l_(362285)

        list = _c_(362278, _a_(362277, _n_(362276, "pd", lambda: pd), "read_csv"), "mycsv.csv")
        _l_(362279)
        _n_(362280, "self", lambda: self).name = _c_(362283, _a_(362282, _n_(362281, "self", lambda: self), "Name"))
        _l_(362284)

    class Name:
        _l_(362297)

        def __init__(self):
            _l_(362296)

            _n_(362286, "self", lambda: self).name = _c_(362291, _n_(362287, "list", lambda: list), _c_(362290, _a_(362289, _a_(362288, ['Name'], "str"), "lower")))
            _l_(362292)
            for i in _n_(362293, "list", lambda: list):
                _l_(362295)

                pass
                _l_(362294)
if _n_(362299, "__name__", lambda: __name__) == "__main__":
    _l_(362319)

    
    person = _c_(362301, _n_(362300, "Person", lambda: Person))
    _l_(362302)
    checking_name = _c_(362308, _a_(362307, _c_(362306, _n_(362303, "str", lambda: str), _c_(362305, _n_(362304, "input", lambda: input))), "lower"))
    _l_(362309)
    list = _a_(362311, _n_(362310, "person", lambda: person), "name")
    _l_(362312)

    if(_n_(362313, "checking_name", lambda: checking_name) in _n_(362314, "list", lambda: list)):
        _l_(362318)

        _c_(362316, _n_(362315, "print", lambda: print), "Hit")
        _l_(362317)