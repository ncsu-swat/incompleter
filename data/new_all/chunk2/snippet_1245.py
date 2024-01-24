# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66450526/typeerror-nonetype-object-is-not-callable-when-passing-arguments-to-decorator
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def mytimeit_with_args(stuff_to_print):
    _l_(458234)

    def decorator(f):
        _l_(458233)

        def func(*args, **kwargs):
            _l_(458230)

            start = _c_(458210, _a_(458209, _n_(458208, "time", lambda: time), "time"))
            _l_(458211)
            result = _c_(458215, _n_(458212, "f", lambda: f), *_n_(458213, "args", lambda: args), **_n_(458214, "kwargs", lambda: kwargs))
            _l_(458216)
            _c_(458219, _n_(458217, "print", lambda: print), _n_(458218, "stuff_to_print", lambda: stuff_to_print))
            _l_(458220)
            _c_(458226, _n_(458221, "print", lambda: print), f"Function took {_c_(458224, _a_(458223, _n_(458222, 'time', lambda: time), 'time')) - _n_(458225, 'start', lambda: start)} seconds to run.")
            _l_(458227)
            aux = _n_(458228, "result", lambda: result)
            _l_(458229)
            return aux
        aux = _n_(458231, "func", lambda: func)
        _l_(458232)
        return aux

@_c_(458236, _n_(458235, "mytimeit_with_args", lambda: mytimeit_with_args), "just some stuff")
def harder_loop(n=10, sleep=0.2):
    _l_(458246)

    for i in _c_(458239, _n_(458237, "range", lambda: range), _n_(458238, "n", lambda: n)):
        _l_(458245)

        _c_(458243, _a_(458241, _n_(458240, "time", lambda: time), "sleep"), _n_(458242, "sleep", lambda: sleep))
        _l_(458244)