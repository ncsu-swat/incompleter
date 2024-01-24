# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44036914/why-do-i-get-attributeerror-super-object-has-no-attribute-del-when-ca
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class MyThread(_a_(455845, _n_(455844, "threading", lambda: threading), "Thread")):
    _l_(455866)

    def __init__(self):
        _l_(455853)

        _c_(455850, _a_(455849, _n_(455846, "super", lambda: super)(_n_(455847, "MyThread", lambda: MyThread), _n_(455848, "self", lambda: self)), "__init__"))
        _l_(455851)
        ...
        _l_(455852)

    def __del__(self):
        _l_(455863)

        ...
        _l_(455854)
        _c_(455861, _a_(455860, _n_(455855, "super", lambda: super)(_c_(455858, _n_(455856, "type", lambda: type), _n_(455857, "self", lambda: self)), _n_(455859, "self", lambda: self)), "__del__"))
        _l_(455862)

    def run(self):
        _l_(455865)

        ...
        _l_(455864)