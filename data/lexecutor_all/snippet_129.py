# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sqr(val):
    _l_(1548530)

    try:
        import time
        _l_(1548522)

    except ImportError:
        pass
    _c_(1548525, _a_(1548524, _n_(1548523, "time", lambda: time), "sleep"), 0.1)
    _l_(1548526)
    aux = _n_(1548527, "val", lambda: val) * _n_(1548528, "val", lambda: val)
    _l_(1548529)
    return aux

def process_result(result):
    _l_(1548535)

    _c_(1548533, _n_(1548531, "print", lambda: print), _n_(1548532, "result", lambda: result))
    _l_(1548534)

def process_these_asap(tasks):
    _l_(1548565)

    try:
        import concurrent.futures
        _l_(1548537)

    except ImportError:
        pass

    with _c_(1548540, _a_(1548539, _a_(1548538, concurrent, "futures"), "ProcessPoolExecutor")) as executor:
        _l_(1548564)

        futures = []
        _l_(1548541)
        for task in _n_(1548542, "tasks", lambda: tasks):
            _l_(1548552)

            _c_(1548550, _a_(1548544, _n_(1548543, "futures", lambda: futures), "append"), _c_(1548549, _a_(1548546, _n_(1548545, "executor", lambda: executor), "submit"), _n_(1548547, "sqr", lambda: sqr), _n_(1548548, "task", lambda: task)))
            _l_(1548551)

        for future in _c_(1548556, _a_(1548554, _a_(1548553, concurrent, "futures"), "as_completed"), _n_(1548555, "futures", lambda: futures)):
            _l_(1548563)

            _c_(1548561, _n_(1548557, "process_result", lambda: process_result), _c_(1548560, _a_(1548559, _n_(1548558, "future", lambda: future), "result")))
            _l_(1548562)

def main():
    _l_(1548587)

    tasks = _c_(1548569, _n_(1548566, "list", lambda: list), _c_(1548568, _n_(1548567, "range", lambda: range), 10))
    _l_(1548570)
    _c_(1548577, _n_(1548571, "print", lambda: print), _c_(1548576, _a_(1548572, 'Processing {} tasks', "format"), _c_(1548575, _n_(1548573, "len", lambda: len), _n_(1548574, "tasks", lambda: tasks))))
    _l_(1548578)
    _c_(1548581, _n_(1548579, "process_these_asap", lambda: process_these_asap), _n_(1548580, "tasks", lambda: tasks))
    _l_(1548582)
    _c_(1548584, _n_(1548583, "print", lambda: print), 'Done')
    _l_(1548585)
    aux = 0
    _l_(1548586)
    return aux

if _n_(1548588, "__name__", lambda: __name__) == '__main__':
    _l_(1548597)

    try:
        import sys
        _l_(1548590)

    except ImportError:
        pass
    _c_(1548595, _a_(1548592, _n_(1548591, "sys", lambda: sys), "exit"), _c_(1548594, _n_(1548593, "main", lambda: main)))
    _l_(1548596)

