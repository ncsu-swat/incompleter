# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53612583/attempt-to-encrypt-a-text-file-causes-a-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
my_text= F = _c_(431144, _n_(431143, "open", lambda: open), "mytext.txt")
_l_(431145)
KEY=4
_l_(431146)
encoded= ""
_l_(431147)

for c in _n_(431148, "my_text", lambda: my_text):
    _l_(431158)

    rem = (_c_(431151, _n_(431149, "ord", lambda: ord), _n_(431150, "c", lambda: c)) - 97 + _n_(431152, "KEY", lambda: KEY)) % 26
    _l_(431153)
    encoded += _c_(431156, _n_(431154, "chr", lambda: chr), _n_(431155, "rem", lambda: rem) + 97)
    _l_(431157)

_c_(431161, _n_(431159, "print", lambda: print), _n_(431160, "encoded", lambda: encoded))
_l_(431162)