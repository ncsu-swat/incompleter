# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4675728/redirect-stdout-to-a-file-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class out_to_lt():
    _l_(1545570)

    def __init__(self, lt):
        _l_(1545541)

        if _c_(1545532, _n_(1545530, "type", lambda: type), _n_(1545531, "lt", lambda: lt)) == _n_(1545533, "list", lambda: list):
            _l_(1545540)

            _n_(1545534, "self", lambda: self).lt = _n_(1545535, "lt", lambda: lt)
            _l_(1545536)
        else:
            raise _c_(1545538, _n_(1545537, "Exception", lambda: Exception), "Need to pass a list")            
            _l_(1545539)            
    def __enter__(self):
        _l_(1545556)

        try:
            import sys
            _l_(1545543)

        except ImportError:
            pass
        _n_(1545544, "self", lambda: self)._sys = _n_(1545545, "sys", lambda: sys)
        _l_(1545546)
        _n_(1545547, "self", lambda: self)._stdout = _a_(1545549, _n_(1545548, "sys", lambda: sys), "stdout")
        _l_(1545550)
        _n_(1545551, "sys", lambda: sys).stdout = _n_(1545552, "self", lambda: self)
        _l_(1545553)
        aux = _n_(1545554, "self", lambda: self)
        _l_(1545555)
        return aux
    def write(self,txt):
        _l_(1545563)

        _c_(1545561, _a_(1545559, _a_(1545558, _n_(1545557, "self", lambda: self), "lt"), "append"), _n_(1545560, "txt", lambda: txt))    
        _l_(1545562)    
    def __exit__(self, type, value, traceback):
        _l_(1545569)

        _a_(1545565, _n_(1545564, "self", lambda: self), "_sys").stdout = _a_(1545567, _n_(1545566, "self", lambda: self), "_stdout")
        _l_(1545568)

lt = []
_l_(1545571)
with _c_(1545574, _n_(1545572, "out_to_lt", lambda: out_to_lt), _n_(1545573, "lt", lambda: lt)) as o:
    _l_(1545584)

    _c_(1545576, _n_(1545575, "print", lambda: print), "Test 123\n\n")
    _l_(1545577)
    _c_(1545582, _n_(1545578, "print", lambda: print), _c_(1545581, _n_(1545579, "help", lambda: help), _n_(1545580, "str", lambda: str)))
    _l_(1545583)

class out_to_lt():
    _l_(1545590)

    ...
    _l_(1545585)
    def isatty(self):
        _l_(1545587)

        aux = True #True: You're running in a real terminal, False:You're being piped, redirected, cron
        _l_(1545586) #True: You're running in a real terminal, False:You're being piped, redirected, cron
        return aux #True: You're running in a real terminal, False:You're being piped, redirected, cron
    def flush(self):
        _l_(1545589)

        pass
        _l_(1545588)

