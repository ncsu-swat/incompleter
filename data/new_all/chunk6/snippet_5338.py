# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63750420/traceback-attributeerror-module-pyaudio-has-no-attribute-version
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import speech_recognition as sr
    _l_(342532)

except ImportError:
    pass

# obtain audio from the microphone
r = _c_(342535, _a_(342534, _n_(342533, "sr", lambda: sr), "Recognizer"))
_l_(342536)
with _c_(342539, _a_(342538, _n_(342537, "sr", lambda: sr), "Microphone")) as source:
    _l_(342548)

    _c_(342541, _n_(342540, "print", lambda: print), "Say something!")
    _l_(342542)
    audio = _c_(342546, _a_(342544, _n_(342543, "r", lambda: r), "listen"), _n_(342545, "source", lambda: source))
    _l_(342547)
try:
    _l_(342571)

    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    _c_(342554, _n_(342549, "print", lambda: print), "Google Speech Recognition thinks you said " + _c_(342553, _a_(342551, _n_(342550, "r", lambda: r), "recognize_google"), _n_(342552, "audio", lambda: audio)))
    _l_(342555)
except _a_(342557, _n_(342556, "sr", lambda: sr), "UnknownValueError"):
    _l_(342561)

    _c_(342559, _n_(342558, "print", lambda: print), "Google Speech Recognition could not understand audio")
    _l_(342560)
except _a_(342563, _n_(342562, "sr", lambda: sr), "RequestError") as e:
    _l_(342570)

    _c_(342568, _n_(342564, "print", lambda: print), _c_(342567, _a_(342565, "Could not request results from Google Speech Recognition service; {0}", "format"), _n_(342566, "e", lambda: e)))
    _l_(342569)