# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60939090/why-do-i-keep-getting-a-attributeerror-nonetype-object-has-no-attribute-lowe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3
    _l_(348610)

except ImportError:
    pass
try:
    import speech_recognition as sr
    _l_(348612)

except ImportError:
    pass
try:
    import datetime
    _l_(348614)

except ImportError:
    pass
try:
    import wikipedia
    _l_(348616)

except ImportError:
    pass
try:
    import webbrowser
    _l_(348618)

except ImportError:
    pass
try:
    import os
    _l_(348620)

except ImportError:
    pass
try:
    import smtplib
    _l_(348622)

except ImportError:
    pass
try:
    import pythoncom
    _l_(348624)

except ImportError:
    pass

_c_(348626, _n_(348625, "print", lambda: print), "Initializing Karren")
_l_(348627)

MASTER = "Bob"
_l_(348628)

engine = _c_(348631, _a_(348630, _n_(348629, "pyttsx3", lambda: pyttsx3), "init"), 'sapi5')
_l_(348632)
voices = _c_(348635, _a_(348634, _n_(348633, "engine", lambda: engine), "getProperty"), 'voices')
_l_(348636)
_c_(348641, _a_(348638, _n_(348637, "engine", lambda: engine), "setProperty"), 'voice', _a_(348640, _n_(348639, "voices", lambda: voices)[1], "id"))
_l_(348642)

def speak(text):
    _l_(348652)

    _c_(348646, _a_(348644, _n_(348643, "engine", lambda: engine), "say"), _n_(348645, "text", lambda: text))
    _l_(348647)
    _c_(348650, _a_(348649, _n_(348648, "engine", lambda: engine), "runAndWait"))
    _l_(348651)


def wishMe():
    _l_(348679)

    hour = _c_(348659, _n_(348653, "int", lambda: int), _a_(348658, _c_(348657, _a_(348656, _a_(348655, _n_(348654, "datetime", lambda: datetime), "datetime"), "now")), "hour"))
    _l_(348660)

    if _n_(348661, "hour", lambda: hour)>=0 and _n_(348662, "hour", lambda: hour) <12:
        _l_(348678)

        _c_(348665, _n_(348663, "speak", lambda: speak), "Good Morning" + _n_(348664, "MASTER", lambda: MASTER))
        _l_(348666)

    elif _n_(348667, "hour", lambda: hour)>=12 and _n_(348668, "hour", lambda: hour)<18:
        _l_(348677)

        _c_(348671, _n_(348669, "speak", lambda: speak), "Good Afternoon" + _n_(348670, "MASTER", lambda: MASTER))
        _l_(348672)
    else:
        _c_(348675, _n_(348673, "speak", lambda: speak), "Good Evening" + _n_(348674, "MASTER", lambda: MASTER))
        _l_(348676)


   # speak("I am Karren. How may I assist you?") # deliberately on not included for now

def takeCommand():
    _l_(348717)

    r = _c_(348682, _a_(348681, _n_(348680, "sr", lambda: sr), "Recognizer"))
    _l_(348683)
    with _c_(348686, _a_(348685, _n_(348684, "sr", lambda: sr), "Microphone")) as source:
        _l_(348695)

        _c_(348688, _n_(348687, "print", lambda: print), "Listening...")
        _l_(348689)
        audio = _c_(348693, _a_(348691, _n_(348690, "r", lambda: r), "listen"), _n_(348692, "source", lambda: source))
        _l_(348694)

    try :
        _l_(348714)

        _c_(348697, _n_(348696, "print", lambda: print), "Recognizing...")
        _l_(348698)
        query = _c_(348702, _a_(348700, _n_(348699, "r", lambda: r), "recognize_google"), _n_(348701, "audio", lambda: audio), Language = 'en-uk')
        _l_(348703)
        _c_(348706, _n_(348704, "print", lambda: print), f"User said: {_n_(348705, 'query', lambda: query)}\n")
        _l_(348707)

    except _n_(348708, "Exception", lambda: Exception) as e:
        _l_(348713)

        _c_(348710, _n_(348709, "print", lambda: print), "Sorry i didn't catch that...")
        _l_(348711)
        query = None
        _l_(348712)
    aux = _n_(348715, "query", lambda: query) 
    _l_(348716) 
    return aux 

_c_(348719, _n_(348718, "speak", lambda: speak), "Initializing Karren...")
_l_(348720)
_c_(348722, _n_(348721, "wishMe", lambda: wishMe))
_l_(348723)
query = _c_(348725, _n_(348724, "takeCommand", lambda: takeCommand))
_l_(348726)


if 'wikipedia' in _c_(348729, _a_(348728, _n_(348727, "query", lambda: query), "lower")):
    _l_(348746)

    _c_(348731, _n_(348730, "speak", lambda: speak), "Searching wikipedia")
    _l_(348732)
    query = _c_(348735, _a_(348734, _n_(348733, "query", lambda: query), "replace"), "wikipedia", "")
    _l_(348736)
    results = _c_(348740, _a_(348738, _n_(348737, "wikipedia", lambda: wikipedia), "summary"), _n_(348739, "query", lambda: query), sentences=2)
    _l_(348741)
    _c_(348744, _n_(348742, "speak", lambda: speak), _n_(348743, "results", lambda: results))
    _l_(348745)