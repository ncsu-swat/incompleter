# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/38836795/typeerror-int-argument-must-be-a-string-a-bytes-like-object-or-a-number-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Stats(_a_(415510, _n_(415509, "models", lambda: models), "Model")):
    _l_(415523)

    user = _c_(415512, _a_(415511, models, "OneToOneField"), 'auth.User')
    _l_(415513)
    views = _c_(415515, _a_(415514, models, "IntegerField"))
    _l_(415516)
    visits = _c_(415518, _a_(415517, models, "IntegerField"))
    _l_(415519)
    unique_visits = _c_(415521, _a_(415520, models, "IntegerField"))
    _l_(415522)