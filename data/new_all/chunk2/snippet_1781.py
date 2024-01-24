# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56161667/typeerror-in-number-of-arguments-passed-to-the-target
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import threading
    _l_(474974)

except ImportError:
    pass

class Example:
    _l_(474998)

    def instruct(self, message_type):
        _l_(474986)

        instruction_thread = _c_(474980, _a_(474976, _n_(474975, "threading", lambda: threading), "Thread"), target=_a_(474978, _n_(474977, "self", lambda: self), "speak"), args=_n_(474979, "message_type", lambda: message_type))
        _l_(474981)
        _c_(474984, _a_(474983, _n_(474982, "instruction_thread", lambda: instruction_thread), "start"))
        _l_(474985)

    def speak(self, message_type):
        _l_(474997)

        if _n_(474987, "message_type", lambda: message_type) == 'send':
            _l_(474996)

            _c_(474989, _n_(474988, "print", lambda: print), 'send the message')
            _l_(474990)
        elif _n_(474991, "message_type", lambda: message_type) == 'inbox':
            _l_(474995)

            _c_(474993, _n_(474992, "print", lambda: print), 'read the message')
            _l_(474994)


e = _c_(475000, _n_(474999, "Example", lambda: Example))
_l_(475001)
_c_(475004, _a_(475003, _n_(475002, "e", lambda: e), "instruct"), 'send')
_l_(475005)