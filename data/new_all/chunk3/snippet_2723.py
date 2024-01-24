# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65547733/attributeerror-engine-object-has-no-attribute-runandwait
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3 as tts
    _l_(565963)

except ImportError:
    pass

def speak(text):
    _l_(565977)

    engine = _c_(565966, _a_(565965, _n_(565964, "tts", lambda: tts), "init"), "sapi5")
    _l_(565967)
    _c_(565971, _a_(565969, _n_(565968, "engine", lambda: engine), "say"), _n_(565970, "text", lambda: text))
    _l_(565972)
    _c_(565975, _a_(565974, _n_(565973, "engine", lambda: engine), "runandwait"))
    _l_(565976)

_c_(565979, _n_(565978, "speak", lambda: speak), 'Hello user this is a test message.')
_l_(565980)