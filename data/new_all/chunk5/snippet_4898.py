# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42117948/pycharm-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
mysock = _c_(702256, _a_(702251, _n_(702250, "socket", lambda: socket), "socket"), _a_(702253, _n_(702252, "socket", lambda: socket), "AF_INET"), _a_(702255, _n_(702254, "socket", lambda: socket), "SOCK_STREAM")) # This is the      line that PyCharm flags as causing the problem.
_l_(702257) # This is the      line that PyCharm flags as causing the problem.