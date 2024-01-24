# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42117948/pycharm-typeerror-a-bytes-like-object-is-required-not-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
mysock = _c_(704891, _a_(704886, _n_(704885, "socket", lambda: socket), "socket"), _a_(704888, _n_(704887, "socket", lambda: socket), "AF_INET"), _a_(704890, _n_(704889, "socket", lambda: socket), "SOCK_STREAM")) # This is the      line that PyCharm flags as causing the problem.
_l_(704892) # This is the      line that PyCharm flags as causing the problem.