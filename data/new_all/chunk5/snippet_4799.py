# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47954452/helping-out-with-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def write_password():
    _l_(649066)

    points = 0 
    _l_(649018) 
    #askpassword = input("enter in a password. only use the chasricters")
    #char = "qwertyuiopasdfghjklzxcvbnmQERTYUIOPASDFGHJKLZXCVBNM"
    askpassword = "asdf"
    _l_(649019)
    char = ["qwertyuiop","asdfghjkl", "zxcvbnm"]
    _l_(649020)
    triples = []
    _l_(649021)
    for chars in _n_(649022, "char", lambda: char):
        _l_(649036)

        for i in _c_(649027, _n_(649023, "range", lambda: range), _c_(649026, _n_(649024, "len", lambda: len), _n_(649025, "chars", lambda: chars))-2):
            _l_(649035)

            _c_(649033, _a_(649029, _n_(649028, "triples", lambda: triples), "append"), _n_(649030, "char", lambda: char)[_n_(649031, "i", lambda: i):_n_(649032, "i", lambda: i)+3])
            _l_(649034)
    askpassword = _c_(649040, _a_(649039, _c_(649038, _a_(649037, "askpassword", "strip")), "lower"))
    _l_(649041)
    for triple in _n_(649042, "triples", lambda: triples):
        _l_(649047)

        if _n_(649043, "triple", lambda: triple) in _n_(649044, "askpassword", lambda: askpassword):
            _l_(649046)

            points += -5
            _l_(649045)
    for char in _n_(649048, "askpassword", lambda: askpassword):
        _l_(649061)

        if _n_(649049, "char", lambda: char) in _n_(649050, "askpassword", lambda: askpassword):
            _l_(649060)

            if _c_(649053, _n_(649051, "len", lambda: len), _n_(649052, "askpassword", lambda: askpassword)) >= 8:
                _l_(649059)

                points = _n_(649054, "points", lambda: points) + 1
                _l_(649055)
            else:
                _c_(649057, _n_(649056, "print", lambda: print), "no points")
                _l_(649058)
    _c_(649064, _n_(649062, "print", lambda: print), "this password is worth",_n_(649063, "points", lambda: points),"points")
    _l_(649065)

_c_(649068, _n_(649067, "write_password", lambda: write_password))
_l_(649069)