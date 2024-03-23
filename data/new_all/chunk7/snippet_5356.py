# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62407341/attributeerror-nonetype-object-has-no-attribute-lower-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3
    _l_(348795)

except ImportError:
    pass
try:
    import speech_recognition as sr
    _l_(348797)

except ImportError:
    pass
try:
    import datetime
    _l_(348799)

except ImportError:
    pass
try:
    import wikipedia
    _l_(348801)

except ImportError:
    pass
try:
    import webbrowser
    _l_(348803)

except ImportError:
    pass
try:
    import os
    _l_(348805)

except ImportError:
    pass
try:
    import smtplib
    _l_(348807)

except ImportError:
    pass
try:
    import jdatetime
    _l_(348809)

except ImportError:
    pass
try:
    import persian
    _l_(348811)

except ImportError:
    pass

Boss = 'Mohamaad'
_l_(348812)
_c_(348815, _n_(348813, "print", lambda: print), 'Hello sir %s' % _n_(348814, "Boss", lambda: Boss))
_l_(348816)
engine = _c_(348819, _a_(348818, _n_(348817, "pyttsx3", lambda: pyttsx3), "init"), 'sapi5')
_l_(348820)
voices = _c_(348823, _a_(348822, _n_(348821, "engine", lambda: engine), "getProperty"), 'voices')
_l_(348824)
_c_(348829, _a_(348826, _n_(348825, "engine", lambda: engine), "setProperty"), 'voice',_a_(348828, _n_(348827, "voices", lambda: voices)[0], "id"))
_l_(348830)

def speak(text):
    _l_(348840)

    _c_(348834, _a_(348832, _n_(348831, "engine", lambda: engine), "say"), _n_(348833, "text", lambda: text))
    _l_(348835)
    _c_(348838, _a_(348837, _n_(348836, "engine", lambda: engine), "runAndWait"))
    _l_(348839)

_c_(348843, _n_(348841, "speak", lambda: speak), 'Hello sir %s' % _n_(348842, "Boss", lambda: Boss))
_l_(348844)

def takeCommand():
    _l_(348893)

    r = _c_(348847, _a_(348846, _n_(348845, "sr", lambda: sr), "Recognizer"))
    _l_(348848)
    with _c_(348851, _a_(348850, _n_(348849, "sr", lambda: sr), "Microphone")) as source:
        _l_(348868)

        _c_(348855, _a_(348853, _n_(348852, "r", lambda: r), "record"), _n_(348854, "source", lambda: source),duration=2)
        _l_(348856)
        _c_(348858, _n_(348857, "speak", lambda: speak), 'I am Listening sir')
        _l_(348859)
        _c_(348861, _n_(348860, "print", lambda: print), "Listening ....")
        _l_(348862)
        audio = _c_(348866, _a_(348864, _n_(348863, "r", lambda: r), "listen"), _n_(348865, "source", lambda: source))
        _l_(348867)

    try :
        _l_(348890)

        _c_(348870, _n_(348869, "print", lambda: print), "Recognizing...")
        _l_(348871)
        query = _c_(348875, _a_(348873, _n_(348872, "r", lambda: r), "recognize_google"), _n_(348874, "audio", lambda: audio), Language ='en-us')
        _l_(348876)
        _c_(348879, _n_(348877, "print", lambda: print), f"user said: {_n_(348878, 'query', lambda: query)}\n")
        _l_(348880)

    except _n_(348881, "Exception", lambda: Exception) as e:
        _l_(348889)

        _c_(348883, _n_(348882, "print", lambda: print), "Say that again please")
        _l_(348884)
        _c_(348886, _n_(348885, "speak", lambda: speak), 'Say that again please')
        _l_(348887)
        query=None
        _l_(348888)
    aux = _n_(348891, "query", lambda: query)
    _l_(348892)

    return aux

_c_(348895, _n_(348894, "wishMe", lambda: wishMe))
_l_(348896)
query = _c_(348898, _n_(348897, "takeCommand", lambda: takeCommand))
_l_(348899)



#Logic for executing tasks as per the query
if 'wikipedia' in _c_(348902, _a_(348901, _n_(348900, "query", lambda: query), "lower")):
    _l_(349004)

    _c_(348904, _n_(348903, "speak", lambda: speak), 'searching in wikipedia....')
    _l_(348905)
    query = _c_(348908, _a_(348907, _n_(348906, "query", lambda: query), "replace"), "wikipedia", "")
    _l_(348909)
    results = _c_(348913, _a_(348911, _n_(348910, "wikipedia", lambda: wikipedia), "summary"), _n_(348912, "query", lambda: query), sentences =2)
    _l_(348914)
    _c_(348917, _n_(348915, "print", lambda: print), _n_(348916, "results", lambda: results))
    _l_(348918)
    _c_(348921, _n_(348919, "speak", lambda: speak), _n_(348920, "results", lambda: results))
    _l_(348922)

elif 'open youtube' in _c_(348925, _a_(348924, _n_(348923, "query", lambda: query), "lower")):
    _l_(349003)

    url = 'youtube.com'
    _l_(348926)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
    _l_(348927)
    _c_(348934, _a_(348932, _c_(348931, _a_(348929, _n_(348928, "webbrowser", lambda: webbrowser), "get"), _n_(348930, "chrome_path", lambda: chrome_path)), "open"), _n_(348933, "url", lambda: url))
    _l_(348935)
elif 'open Google' in _c_(348938, _a_(348937, _n_(348936, "query", lambda: query), "lower")):
    _l_(349002)

    url = 'Google.com'
    _l_(348939)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %'
    _l_(348940)
    _c_(348947, _a_(348945, _c_(348944, _a_(348942, _n_(348941, "webbrowser", lambda: webbrowser), "get"), _n_(348943, "chrome_path", lambda: chrome_path)), "open"), _n_(348946, "url", lambda: url))
    _l_(348948)
elif 'open github' in _c_(348951, _a_(348950, _n_(348949, "query", lambda: query), "lower")):
    _l_(349001)

    url = 'github.com'
    _l_(348952)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %'
    _l_(348953)
    _c_(348960, _a_(348958, _c_(348957, _a_(348955, _n_(348954, "webbrowser", lambda: webbrowser), "get"), _n_(348956, "chrome_path", lambda: chrome_path)), "open"), _n_(348959, "url", lambda: url))
    _l_(348961)
elif 'Play music' in _c_(348964, _a_(348963, _n_(348962, "query", lambda: query), "lower")):
    _l_(349000)

    songs_dir = "C:\\Users\\mohmmad\\Downloads\\Music"
    _l_(348965)
    songs = _c_(348969, _a_(348967, _n_(348966, "os", lambda: os), "listdir"), _n_(348968, "songs_dir", lambda: songs_dir))
    _l_(348970)
    _c_(348973, _n_(348971, "speak", lambda: speak), _n_(348972, "songs", lambda: songs))
    _l_(348974)
    _c_(348983, _a_(348976, _n_(348975, "os", lambda: os), "startfile"), _c_(348982, _a_(348979, _a_(348978, _n_(348977, "os", lambda: os), "path"), "join"), _n_(348980, "songs_dir", lambda: songs_dir),_n_(348981, "songs", lambda: songs)[0]))
    _l_(348984)

elif 'time' in _c_(348986, _n_(348985, "query", lambda: query)):
    _l_(348999)

    strTime = _c_(348992, _a_(348991, _c_(348990, _a_(348989, _a_(348988, _n_(348987, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%H:%M:%S")
    _l_(348993)
    _c_(348997, _n_(348994, "speak", lambda: speak), f"{_n_(348995, 'Boss', lambda: Boss)} the time is {_n_(348996, 'strTime', lambda: strTime)}")
    _l_(348998)