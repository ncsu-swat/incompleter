# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59314321/interactive-dictionary-typeerror-dict-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(342478)

except ImportError:
    pass

data = _c_(342483, _a_(342480, _n_(342479, "json", lambda: json), "load"), _c_(342482, _n_(342481, "open", lambda: open), "files1\data.json"))
_l_(342484)

def definitioner(w):
    _l_(342489)

    aux = _c_(342487, _n_(342485, "data", lambda: data), _n_(342486, "w", lambda: w))
    _l_(342488)
    return aux

word = _c_(342491, _n_(342490, "input", lambda: input), "Enter the word you are looking for: ")
_l_(342492)
_c_(342497, _n_(342493, "print", lambda: print), _c_(342496, _n_(342494, "definitioner", lambda: definitioner), _n_(342495, "word", lambda: word)))
_l_(342498)