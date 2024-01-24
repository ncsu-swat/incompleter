# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61047969/how-do-i-fix-this-typeerror-listen-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import speech_recognition
    _l_(413859)

except ImportError:
    pass

recognizer = _a_(413861, _n_(413860, "speech_recognition", lambda: speech_recognition), "Recognizer")
_l_(413862)
with _c_(413865, _a_(413864, _n_(413863, "speech_recognition", lambda: speech_recognition), "Microphone")) as source:
    _l_(413874)

    _c_(413867, _n_(413866, "print", lambda: print), "Say something")
    _l_(413868)
    audio = _c_(413872, _a_(413870, _n_(413869, "recognizer", lambda: recognizer), "listen"), _n_(413871, "source", lambda: source))
    _l_(413873)

_c_(413876, _n_(413875, "print", lambda: print), "Google thinks you said: ")
_l_(413877)
_c_(413883, _n_(413878, "print", lambda: print), _c_(413882, _a_(413880, _n_(413879, "recognizer", lambda: recognizer), "recognize_google"), _n_(413881, "audio", lambda: audio)))
_l_(413884)