# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58086286/i-am-getting-attributeerror-type-object-observable-has-no-attribute-from
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(460180)

except ImportError:
    pass
try:
    from rx import Observable
    _l_(460182)

except ImportError:
    pass

argv = _c_(460187, _a_(460184, _n_(460183, "Observable", lambda: Observable), "from_"), _a_(460186, _n_(460185, "sys", lambda: sys), "argv")[1:])
_l_(460188)
_c_(460203, _a_(460190, _n_(460189, "argv", lambda: argv), "subscribe"), on_next=lambda i: _c_(460195, _n_(460191, "print", lambda: print), _c_(460194, _a_(460192, "on_next: {}", "format"), _n_(460193, "i", lambda: i))),
    on_error=lambda e: _c_(460200, _n_(460196, "print", lambda: print), _c_(460199, _a_(460197, "on_error: {}", "format"), _n_(460198, "e", lambda: e))),
    on_completed=lambda: _c_(460202, _n_(460201, "print", lambda: print), "on_completed")
)
_l_(460204)