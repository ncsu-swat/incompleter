# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66145096/typeerror-listen-missing-1-required-positional-argument-source
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3
    _l_(551113)

except ImportError:
    pass
try:
    import speech_recognition as sr
    _l_(551115)

except ImportError:
    pass
try:
    import datetime
    _l_(551117)

except ImportError:
    pass
try:
    import wikipedia
    _l_(551119)

except ImportError:
    pass
try:
    import webbrowser
    _l_(551121)

except ImportError:
    pass
try:
    import random
    _l_(551123)

except ImportError:
    pass
try:
    import os
    _l_(551125)

except ImportError:
    pass

#Speakfunction BACKEND
_c_(551127, _n_(551126, "print", lambda: print), "Initializing FRIDAY")
_l_(551128)

engine = _c_(551131, _a_(551130, _n_(551129, "pyttsx3", lambda: pyttsx3), "init"), 'sapi5')
_l_(551132)
voices = _c_(551135, _a_(551134, _n_(551133, "engine", lambda: engine), "getProperty"), 'voices')
_l_(551136)
_c_(551139, _n_(551137, "print", lambda: print), _n_(551138, "voices", lambda: voices))
_l_(551140)

_c_(551145, _a_(551142, _n_(551141, "engine", lambda: engine), "setProperty"), 'voices', _a_(551144, _n_(551143, "voices", lambda: voices)[0], "id"))
_l_(551146)

def speak(audio):
    _l_(551156)

    _c_(551150, _a_(551148, _n_(551147, "engine", lambda: engine), "say"), _n_(551149, "audio", lambda: audio))
    _l_(551151)
    _c_(551154, _a_(551153, _n_(551152, "engine", lambda: engine), "runAndWait"))
    _l_(551155)

def wish():
    _l_(551180)

    hour = _c_(551163, _n_(551157, "int", lambda: int), _a_(551162, _c_(551161, _a_(551160, _a_(551159, _n_(551158, "datetime", lambda: datetime), "datetime"), "now")), "hour"))
    _l_(551164)
    if _n_(551165, "hour", lambda: hour)  >= 0 and _n_(551166, "hour", lambda: hour)<12:
        _l_(551179)

        _c_(551168, _n_(551167, "speak", lambda: speak), "Good Morning Sam I am up and running")
        _l_(551169)

    elif _n_(551170, "hour", lambda: hour)>=12 and _n_(551171, "hour", lambda: hour)<18:
        _l_(551178)

        _c_(551173, _n_(551172, "speak", lambda: speak), "Good afternoon Sam I am up and running")
        _l_(551174)

    else:
        _c_(551176, _n_(551175, "speak", lambda: speak), "Good Night Sam I am up and running")    
        _l_(551177)    

def takecom():
    _l_(551220)

    r = _a_(551182, _n_(551181, "sr", lambda: sr), "Recognizer")
    _l_(551183)
    with _c_(551186, _a_(551185, _n_(551184, "sr", lambda: sr), "Microphone")) as source:
        _l_(551195)

        _c_(551188, _n_(551187, "print", lambda: print), "Listening ...")
        _l_(551189)
        audio = _c_(551193, _a_(551191, _n_(551190, "r", lambda: r), "listen"), _n_(551192, "source", lambda: source))
        _l_(551194)
    try:
        _l_(551217)

        _c_(551197, _n_(551196, "print", lambda: print), "Recognizing")
        _l_(551198)
        text = _c_(551202, _a_(551200, _n_(551199, "r", lambda: r), "recognize_google"), _n_(551201, "audio", lambda: audio),language='en-in') 
        _l_(551203) 
        _c_(551206, _n_(551204, "print", lambda: print), _n_(551205, "text", lambda: text))
        _l_(551207)
    except _n_(551208, "Exception", lambda: Exception):
        _l_(551216)

        _c_(551210, _n_(551209, "speak", lambda: speak), "error ... ")
        _l_(551211)
        _c_(551213, _n_(551212, "print", lambda: print), "Network error")
        _l_(551214)
        aux = "none"
        _l_(551215)
        return aux
    aux = _n_(551218, "text", lambda: text)
    _l_(551219)
    return aux

if _n_(551221, "__name__", lambda: __name__) == "__main__":
    _l_(551281)

    _c_(551223, _n_(551222, "wish", lambda: wish))
    _l_(551224)

    while True:
        _l_(551280)

        query = _c_(551228, _a_(551227, _c_(551226, _n_(551225, "takecom", lambda: takecom)), "lower"))
        _l_(551229)

        if _n_(551230, "wikipedia", lambda: wikipedia) in _n_(551231, "query", lambda: query):
            _l_(551279)

            _c_(551233, _n_(551232, "speak", lambda: speak), "Searching details...Wait")
            _l_(551234)
            _c_(551237, _a_(551236, _n_(551235, "query", lambda: query), "replace"), "wikipedia", "")
            _l_(551238)
            results = _c_(551242, _a_(551240, _n_(551239, "wikipedia", lambda: wikipedia), "summary"), _n_(551241, "query", lambda: query),sentences=2)
            _l_(551243)
            _c_(551246, _n_(551244, "print", lambda: print), _n_(551245, "results", lambda: results))
            _l_(551247)
            _c_(551250, _n_(551248, "speak", lambda: speak), _n_(551249, "results", lambda: results))
            _l_(551251)
        elif 'open youtube' in _n_(551252, "query", lambda: query) or "open video online" in _n_(551253, "query", lambda: query):
            _l_(551278)

            _c_(551256, _a_(551255, _n_(551254, "webbrowser", lambda: webbrowser), "open"), "www.youtube.com")
            _l_(551257)
            _c_(551259, _n_(551258, "speak", lambda: speak), "Opening Youtube")
            _l_(551260)
        elif 'open google' in _n_(551261, "query", lambda: query):
            _l_(551277)

            _c_(551264, _a_(551263, _n_(551262, "webbrowser", lambda: webbrowser), "open"), "www.google.com")
            _l_(551265)
            _c_(551267, _n_(551266, "speak", lambda: speak), "Opening Google")
            _l_(551268)
        elif 'good bye' in _n_(551269, "query", lambda: query):
            _l_(551276)

            _c_(551271, _n_(551270, "speak", lambda: speak), "Good bye sam")
            _l_(551272)
            aux = ""
            _l_(551275)
            exit(aux)