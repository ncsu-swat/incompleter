# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyException(_n_(65233, "Exception", lambda: Exception)):
    _l_(65235)

    pass
    _l_(65234)

raise _c_(65237, _n_(65236, "MyException", lambda: MyException), "My hovercraft is full of eels")
_l_(65238)

raise _c_(65240, _n_(65239, "MyException", lambda: MyException), {"message":"My hovercraft is full of animals", "animal":"eels"})
_l_(65241)

try:
    _l_(65254)

    raise _c_(65243, _n_(65242, "MyException", lambda: MyException), {"message":"My hovercraft is full of animals", "animal":"eels"})
    _l_(65244)
except _n_(65245, "MyException", lambda: MyException) as e:
    _l_(65253)

    details = _a_(65247, _n_(65246, "e", lambda: e), "args")[0]
    _l_(65248)
    _c_(65251, _n_(65249, "print", lambda: print), _n_(65250, "details", lambda: details)["animal"])
    _l_(65252)

class MyError(_n_(65255, "Exception", lambda: Exception)):
    _l_(65267)

    def __init__(self, message, animal):
        _l_(65262)

        _n_(65256, "self", lambda: self).message = _n_(65257, "message", lambda: message)
        _l_(65258)
        _n_(65259, "self", lambda: self).animal = _n_(65260, "animal", lambda: animal)
        _l_(65261)
    def __str__(self):
        _l_(65266)

        aux = _a_(65264, _n_(65263, "self", lambda: self), "message")
        _l_(65265)
        return aux

