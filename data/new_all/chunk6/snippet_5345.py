# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62960685/why-do-i-receive-error-typeerror-argument-of-type-name-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Person:
    _l_(366003)

    def __init__(self):
        _l_(365990)

        list = _c_(365983, _a_(365982, _n_(365981, "pd", lambda: pd), "read_csv"), "mycsv.csv")
        _l_(365984)
        _n_(365985, "self", lambda: self).name = _c_(365988, _a_(365987, _n_(365986, "self", lambda: self), "Name"))
        _l_(365989)

    class Name:
        _l_(366002)

        def __init__(self):
            _l_(366001)

            _n_(365991, "self", lambda: self).name = _c_(365996, _n_(365992, "list", lambda: list), _c_(365995, _a_(365994, _a_(365993, ['Name'], "str"), "lower")))
            _l_(365997)
            for i in _n_(365998, "list", lambda: list):
                _l_(366000)

                pass
                _l_(365999)
if _n_(366004, "__name__", lambda: __name__) == "__main__":
    _l_(366024)

    
    person = _c_(366006, _n_(366005, "Person", lambda: Person))
    _l_(366007)
    checking_name = _c_(366013, _a_(366012, _c_(366011, _n_(366008, "str", lambda: str), _c_(366010, _n_(366009, "input", lambda: input))), "lower"))
    _l_(366014)
    list = _a_(366016, _n_(366015, "person", lambda: person), "name")
    _l_(366017)

    if(_n_(366018, "checking_name", lambda: checking_name) in _n_(366019, "list", lambda: list)):
        _l_(366023)

        _c_(366021, _n_(366020, "print", lambda: print), "Hit")
        _l_(366022)