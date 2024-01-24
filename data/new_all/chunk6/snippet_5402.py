# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55615018/how-to-fix-typeerror-for-this-line-of-code-printyou-will-be-strintmy-ag
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(339975, _n_(339974, "print", lambda: print), "Hello World!")
_l_(339976)
my_name = _c_(339978, _n_(339977, "input", lambda: input), "what is your name? ")
_l_(339979)
_c_(339982, _n_(339980, "print", lambda: print), 'well it is nice to meet you, ' + _n_(339981, "my_name", lambda: my_name))
_l_(339983)
name_length = _c_(339986, _n_(339984, "len", lambda: len), _n_(339985, "my_name", lambda: my_name))
_l_(339987)
_c_(339992, _n_(339988, "print", lambda: print), 'The length of your name is ' + _c_(339991, _n_(339989, "str", lambda: str), _n_(339990, "name_length", lambda: name_length)))
_l_(339993)
my_age = _c_(339997, _n_(339994, "print", lambda: print), _c_(339996, _n_(339995, "input", lambda: input), "How old are you? "))
_l_(339998)
my_age = _c_(340001, _n_(339999, "int", lambda: int), _n_(340000, "my_age", lambda: my_age))
_l_(340002)
_c_(340007, _n_(340003, "print", lambda: print), 'You will be ' + _c_(340006, _n_(340004, "str", lambda: str), _n_(340005, "my_age", lambda: my_age) + 1) + ' in a year.')
_l_(340008)