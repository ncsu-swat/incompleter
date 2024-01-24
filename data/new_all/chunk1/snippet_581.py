# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56018370/typeerror-type-object-does-not-support-item-assignment
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
userlist = _n_(400529, "dict", lambda: dict)
_l_(400530)


def main():
    _l_(400538)

    _c_(400532, _n_(400531, "add_user", lambda: add_user))
    _l_(400533)
    _c_(400536, _n_(400534, "print", lambda: print), _n_(400535, "userlist", lambda: userlist))
    _l_(400537)


def add_user():
    _l_(400582)

    global new_user
    _l_(400539)
    global new_password
    _l_(400540)
    _c_(400542, _n_(400541, "print", lambda: print), 'Please indicate your desired username')
    _l_(400543)
    new_user = _a_(400548, _c_(400547, _n_(400544, "str", lambda: str), _c_(400546, _n_(400545, "input", lambda: input), 'User: ')), "lower")
    _l_(400549)
    _c_(400551, _n_(400550, "print", lambda: print), 'Please indicate your desired password')
    _l_(400552)
    new_password = _c_(400556, _n_(400553, "str", lambda: str), _c_(400555, _n_(400554, "input", lambda: input), 'Password: '))
    _l_(400557)
    _c_(400559, _n_(400558, "print", lambda: print), 'Please re-enter your password')
    _l_(400560)
    password_addcheck = _c_(400564, _n_(400561, "str", lambda: str), _c_(400563, _n_(400562, "input", lambda: input), 'Password:'))
    _l_(400565)
    if _n_(400566, "password_addcheck", lambda: password_addcheck) == _n_(400567, "new_password", lambda: new_password):
        _l_(400581)

        _c_(400569, _n_(400568, "print", lambda: print), 'Thank you, you are now successfully registered')
        _l_(400570)
        _n_(400571, "userlist", lambda: userlist)[_n_(400572, "new_user", lambda: new_user)] = _n_(400573, "new_password", lambda: new_password)
        _l_(400574)
    else:
        _c_(400576, _n_(400575, "print", lambda: print), 'Password does not match, please repeat process')
        _l_(400577)
        _c_(400579, _n_(400578, "add_user", lambda: add_user))
        _l_(400580)


_c_(400584, _n_(400583, "main", lambda: main))
_l_(400585)