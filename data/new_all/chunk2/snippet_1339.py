# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/35492825/user-attribute-errors-on-github3-py-login
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from github3 import login
    _l_(432175)

except ImportError:
    pass

gh = _c_(432177, _n_(432176, "login", lambda: login), 'sigmavirus24', password='<password>')
_l_(432178)

sigmavirus24 = _c_(432181, _a_(432180, _n_(432179, "gh", lambda: gh), "me"))
_l_(432182)
# <User [sigmavirus24:Ian Cordasco]>

_c_(432186, _n_(432183, "print", lambda: print), _a_(432185, _n_(432184, "sigmavirus24", lambda: sigmavirus24), "name"))
_l_(432187)
# Ian Cordasco
_c_(432191, _n_(432188, "print", lambda: print), _a_(432190, _n_(432189, "sigmavirus24", lambda: sigmavirus24), "login"))
_l_(432192)
# sigmavirus24
_c_(432196, _n_(432193, "print", lambda: print), _a_(432195, _n_(432194, "sigmavirus24", lambda: sigmavirus24), "followers_count"))
_l_(432197)
# 4`