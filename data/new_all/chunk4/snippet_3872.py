# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65731002/attributeerror-module-apache-beam-has-no-attribute-dofn
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import apache_beam as beam
    _l_(581006)

except ImportError:
    pass

class Func1(_a_(581008, _n_(581007, "beam", lambda: beam), "DoFn")):
    _l_(581020)


    def process(self, x, *args, **kwargs):
        _l_(581019)

        for _ in _c_(581011, _n_(581009, "range", lambda: range), _n_(581010, "x", lambda: x)[1]):
            _l_(581018)

            yield _c_(581016, _n_(581012, "dict", lambda: dict), _c_(581015, _n_(581013, "zip", lambda: zip), ['name','value'],_n_(581014, "x", lambda: x)))
            _l_(581017)

with _c_(581023, _a_(581022, _n_(581021, "beam", lambda: beam), "Pipeline")) as pipe:
    _l_(581038)

    row = (
        _n_(581024, "pipe", lambda: pipe)
        | _c_(581027, _a_(581026, _n_(581025, "beam", lambda: beam), "Create"), [
            ('apple', 1),
            ('banana', 2),
            ('orange', 3),

        ])
        | _c_(581032, _a_(581029, _n_(581028, "beam", lambda: beam), "ParDo"), _c_(581031, _n_(581030, "Func1", lambda: Func1)))
        | _c_(581036, _a_(581034, _n_(581033, "beam", lambda: beam), "Map"), _n_(581035, "print", lambda: print))
    )
    _l_(581037)