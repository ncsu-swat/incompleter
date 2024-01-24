# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55984129/attributeerror-could-not-find-pyaudio-check-installation-cant-use-speech-re
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def hear():
    _l_(415197)

    try:
        import speech_recognition as sr
        _l_(415166)

    except ImportError:
        pass
    ear = _c_(415169, _a_(415168, _n_(415167, "sr", lambda: sr), "Recognizer"))
    _l_(415170)
    with _c_(415173, _a_(415172, _n_(415171, "sr", lambda: sr), "Microphone")) as sourse:
        _l_(415196)

        _c_(415175, _n_(415174, "print", lambda: print), "listening...")
        _l_(415176)
        audio = _c_(415180, _a_(415178, _n_(415177, "ear", lambda: ear), "listen"), _n_(415179, "sourse", lambda: sourse))
        _l_(415181)
        try:
            _l_(415195)

            text = _c_(415185, _a_(415183, _n_(415182, "ear", lambda: ear), "recognize_google"), _n_(415184, "audio", lambda: audio))
            _l_(415186)
            _c_(415189, _n_(415187, "print", lambda: print), _n_(415188, "text", lambda: text))
            _l_(415190)
        except:
            _l_(415194)

            _c_(415192, _n_(415191, "print", lambda: print), "i didn't get that...")
            _l_(415193)

_c_(415199, _n_(415198, "hear", lambda: hear))
_l_(415200)