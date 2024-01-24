# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/48528894/nameerror-name-functionname-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from UserInfo import UserInfo
    _l_(443148)

except ImportError:
    pass

user = _c_(443150, _n_(443149, "UserInfo", lambda: UserInfo))
_l_(443151)
_c_(443155, _n_(443152, "print", lambda: print), _a_(443154, _n_(443153, "user", lambda: user), "username"))
_l_(443156)