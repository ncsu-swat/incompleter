# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55383614/i-am-getting-typeerror-when-trying-to-print-a-value-loaded-from-a-json-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(705851)

except ImportError:
    pass
with _c_(705853, _n_(705852, "open", lambda: open), 'input.json', 'r') as input:
    _l_(705863)

    obj = _c_(705857, _a_(705855, _n_(705854, "json", lambda: json), "load"), _n_(705856, "input", lambda: input))
    _l_(705858)
    _c_(705861, _n_(705859, "print", lambda: print), 'Hello, ' + _n_(705860, "obj", lambda: obj)['hobbies'])
    _l_(705862)