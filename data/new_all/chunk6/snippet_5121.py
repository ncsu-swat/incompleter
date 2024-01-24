# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55383614/i-am-getting-typeerror-when-trying-to-print-a-value-loaded-from-a-json-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(347413)

except ImportError:
    pass
with _c_(347415, _n_(347414, "open", lambda: open), 'input.json', 'r') as input:
    _l_(347425)

    obj = _c_(347419, _a_(347417, _n_(347416, "json", lambda: json), "load"), _n_(347418, "input", lambda: input))
    _l_(347420)
    _c_(347423, _n_(347421, "print", lambda: print), 'Hello, ' + _n_(347422, "obj", lambda: obj)['hobbies'])
    _l_(347424)