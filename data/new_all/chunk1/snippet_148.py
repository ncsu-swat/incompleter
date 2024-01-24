# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60107982/attributeerror-function-object-has-no-attribute-func-name-and-python-3
from __future__ import print_function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_l_(387365)
try:
    from time import sleep
    _l_(387367)

except ImportError:
    pass

def callback_a(i, result):
    _l_(387375)

    _c_(387373, _n_(387368, "print", lambda: print), _c_(387372, _a_(387369, "Items processed: {}. Running result: {}.", "format"), _n_(387370, "i", lambda: i), _n_(387371, "result", lambda: result)))
    _l_(387374)

def square(i):
    _l_(387379)

    aux = _n_(387376, "i", lambda: i) * _n_(387377, "i", lambda: i)
    _l_(387378)
    return aux

def processor(process, times, report_interval, callback):
    _l_(387412)

    _c_(387387, _n_(387380, "print", lambda: print), _c_(387386, _a_(387381, "Entered processor(): times = {}, report_interval = {}, callback = {}", "format"), _n_(387382, "times", lambda: times), _n_(387383, "report_interval", lambda: report_interval), _a_(387385, _n_(387384, "callback", lambda: callback), "func_name")))
    _l_(387388)
    # Can also use callback.__name__ instead of callback.func_name in line above.
    result = 0
    _l_(387389)
    _c_(387391, _n_(387390, "print", lambda: print), "Processing data ...")
    _l_(387392)
    for i in _c_(387395, _n_(387393, "range", lambda: range), 1, _n_(387394, "times", lambda: times) + 1):
        _l_(387411)

        result += _c_(387398, _n_(387396, "process", lambda: process), _n_(387397, "i", lambda: i))
        _l_(387399)
        _c_(387401, _n_(387400, "sleep", lambda: sleep), 1)
        _l_(387402)
        if _n_(387403, "i", lambda: i) % _n_(387404, "report_interval", lambda: report_interval) == 0:
            _l_(387410)

            # This is the call to the callback function 
            # that was passed to this function.
            _c_(387408, _n_(387405, "callback", lambda: callback), _n_(387406, "i", lambda: i), _n_(387407, "result", lambda: result))
            _l_(387409)

_c_(387416, _n_(387413, "processor", lambda: processor), _n_(387414, "square", lambda: square), 20, 5, _n_(387415, "callback_a", lambda: callback_a))
_l_(387417)