# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55615018/how-to-fix-typeerror-for-this-line-of-code-printyou-will-be-strintmy-ag
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(372648, _n_(372647, "print", lambda: print), "Hello World!")
_l_(372649)
my_name = _c_(372651, _n_(372650, "input", lambda: input), "what is your name? ")
_l_(372652)
_c_(372655, _n_(372653, "print", lambda: print), 'well it is nice to meet you, ' + _n_(372654, "my_name", lambda: my_name))
_l_(372656)
name_length = _c_(372659, _n_(372657, "len", lambda: len), _n_(372658, "my_name", lambda: my_name))
_l_(372660)
_c_(372665, _n_(372661, "print", lambda: print), 'The length of your name is ' + _c_(372664, _n_(372662, "str", lambda: str), _n_(372663, "name_length", lambda: name_length)))
_l_(372666)
my_age = _c_(372670, _n_(372667, "print", lambda: print), _c_(372669, _n_(372668, "input", lambda: input), "How old are you? "))
_l_(372671)
my_age = _c_(372674, _n_(372672, "int", lambda: int), _n_(372673, "my_age", lambda: my_age))
_l_(372675)
_c_(372680, _n_(372676, "print", lambda: print), 'You will be ' + _c_(372679, _n_(372677, "str", lambda: str), _n_(372678, "my_age", lambda: my_age) + 1) + ' in a year.')
_l_(372681)