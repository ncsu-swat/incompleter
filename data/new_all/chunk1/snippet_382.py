# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34733871/attributeerror-recognizer-object-has-no-attribute-recognize
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyaudio
    _l_(381378)

except ImportError:
    pass
try:
    import speech_recognition as sr
    _l_(381380)

except ImportError:
    pass

r = _c_(381383, _a_(381382, _n_(381381, "sr", lambda: sr), "Recognizer"))
_l_(381384)
_n_(381385, "r", lambda: r).energy_threshold=4000
_l_(381386)

with _c_(381389, _a_(381388, _n_(381387, "sr", lambda: sr), "Microphone")) as source:
    _l_(381395)

    audio = _c_(381393, _a_(381391, _n_(381390, "r", lambda: r), "listen"), _n_(381392, "source", lambda: source))
    _l_(381394)

try:
    _l_(381408)

    _c_(381401, _n_(381396, "print", lambda: print), "Speech was:" + _c_(381400, _a_(381398, _n_(381397, "r", lambda: r), "recognize"), _n_(381399, "audio", lambda: audio)))
    _l_(381402)
except _n_(381403, "LookupError", lambda: LookupError):
    _l_(381407)

    _c_(381405, _n_(381404, "print", lambda: print), 'Speech not understood')
    _l_(381406)