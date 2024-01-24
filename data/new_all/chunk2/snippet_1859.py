# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/49833108/python-attribute-error-after-result-is-outputed
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import re
    _l_(446563)

except ImportError:
    pass

pattern = _c_(446566, _a_(446565, _n_(446564, "re", lambda: re), "compile"), r'(?<=\>)(.*?)(?=\|)')
_l_(446567)

# open input file
input_file = _c_(446569, _n_(446568, "open", lambda: open), 'input.fas', 'r')
_l_(446570)

while True:
    _l_(446593)

    line = _c_(446573, _a_(446572, _n_(446571, "input_file", lambda: input_file), "readline"))
    _l_(446574)
    if _n_(446575, "line", lambda: line) == '' or _n_(446576, "line", lambda: line) is None:
        _l_(446592)

        _c_(446578, _n_(446577, "print", lambda: print), 'EOF')
        _l_(446579)
        break
        _l_(446580)
    else:
        output = _c_(446586, _a_(446585, _c_(446584, _a_(446582, _n_(446581, "pattern", lambda: pattern), "search"), _n_(446583, "line", lambda: line)), "group"))
        _l_(446587)
        _c_(446590, _n_(446588, "print", lambda: print), _n_(446589, "output", lambda: output))
        _l_(446591)