# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62407341/attributeerror-nonetype-object-has-no-attribute-lower-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3
    _l_(347157)

except ImportError:
    pass
try:
    import speech_recognition as sr
    _l_(347159)

except ImportError:
    pass
try:
    import datetime
    _l_(347161)

except ImportError:
    pass
try:
    import wikipedia
    _l_(347163)

except ImportError:
    pass
try:
    import webbrowser
    _l_(347165)

except ImportError:
    pass
try:
    import os
    _l_(347167)

except ImportError:
    pass
try:
    import smtplib
    _l_(347169)

except ImportError:
    pass
try:
    import jdatetime
    _l_(347171)

except ImportError:
    pass
try:
    import persian
    _l_(347173)

except ImportError:
    pass

Boss = 'Mohamaad'
_l_(347174)
_c_(347177, _n_(347175, "print", lambda: print), 'Hello sir %s' % _n_(347176, "Boss", lambda: Boss))
_l_(347178)
engine = _c_(347181, _a_(347180, _n_(347179, "pyttsx3", lambda: pyttsx3), "init"), 'sapi5')
_l_(347182)
voices = _c_(347185, _a_(347184, _n_(347183, "engine", lambda: engine), "getProperty"), 'voices')
_l_(347186)
_c_(347191, _a_(347188, _n_(347187, "engine", lambda: engine), "setProperty"), 'voice',_a_(347190, _n_(347189, "voices", lambda: voices)[0], "id"))
_l_(347192)

def speak(text):
    _l_(347202)

    _c_(347196, _a_(347194, _n_(347193, "engine", lambda: engine), "say"), _n_(347195, "text", lambda: text))
    _l_(347197)
    _c_(347200, _a_(347199, _n_(347198, "engine", lambda: engine), "runAndWait"))
    _l_(347201)

_c_(347205, _n_(347203, "speak", lambda: speak), 'Hello sir %s' % _n_(347204, "Boss", lambda: Boss))
_l_(347206)

def takeCommand():
    _l_(347255)

    r = _c_(347209, _a_(347208, _n_(347207, "sr", lambda: sr), "Recognizer"))
    _l_(347210)
    with _c_(347213, _a_(347212, _n_(347211, "sr", lambda: sr), "Microphone")) as source:
        _l_(347230)

        _c_(347217, _a_(347215, _n_(347214, "r", lambda: r), "record"), _n_(347216, "source", lambda: source),duration=2)
        _l_(347218)
        _c_(347220, _n_(347219, "speak", lambda: speak), 'I am Listening sir')
        _l_(347221)
        _c_(347223, _n_(347222, "print", lambda: print), "Listening ....")
        _l_(347224)
        audio = _c_(347228, _a_(347226, _n_(347225, "r", lambda: r), "listen"), _n_(347227, "source", lambda: source))
        _l_(347229)

    try :
        _l_(347252)

        _c_(347232, _n_(347231, "print", lambda: print), "Recognizing...")
        _l_(347233)
        query = _c_(347237, _a_(347235, _n_(347234, "r", lambda: r), "recognize_google"), _n_(347236, "audio", lambda: audio), Language ='en-us')
        _l_(347238)
        _c_(347241, _n_(347239, "print", lambda: print), f"user said: {_n_(347240, 'query', lambda: query)}\n")
        _l_(347242)

    except _n_(347243, "Exception", lambda: Exception) as e:
        _l_(347251)

        _c_(347245, _n_(347244, "print", lambda: print), "Say that again please")
        _l_(347246)
        _c_(347248, _n_(347247, "speak", lambda: speak), 'Say that again please')
        _l_(347249)
        query=None
        _l_(347250)
    aux = _n_(347253, "query", lambda: query)
    _l_(347254)

    return aux

_c_(347257, _n_(347256, "wishMe", lambda: wishMe))
_l_(347258)
query = _c_(347260, _n_(347259, "takeCommand", lambda: takeCommand))
_l_(347261)



#Logic for executing tasks as per the query
if 'wikipedia' in _c_(347264, _a_(347263, _n_(347262, "query", lambda: query), "lower")):
    _l_(347366)

    _c_(347266, _n_(347265, "speak", lambda: speak), 'searching in wikipedia....')
    _l_(347267)
    query = _c_(347270, _a_(347269, _n_(347268, "query", lambda: query), "replace"), "wikipedia", "")
    _l_(347271)
    results = _c_(347275, _a_(347273, _n_(347272, "wikipedia", lambda: wikipedia), "summary"), _n_(347274, "query", lambda: query), sentences =2)
    _l_(347276)
    _c_(347279, _n_(347277, "print", lambda: print), _n_(347278, "results", lambda: results))
    _l_(347280)
    _c_(347283, _n_(347281, "speak", lambda: speak), _n_(347282, "results", lambda: results))
    _l_(347284)

elif 'open youtube' in _c_(347287, _a_(347286, _n_(347285, "query", lambda: query), "lower")):
    _l_(347365)

    url = 'youtube.com'
    _l_(347288)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %s'
    _l_(347289)
    _c_(347296, _a_(347294, _c_(347293, _a_(347291, _n_(347290, "webbrowser", lambda: webbrowser), "get"), _n_(347292, "chrome_path", lambda: chrome_path)), "open"), _n_(347295, "url", lambda: url))
    _l_(347297)
elif 'open Google' in _c_(347300, _a_(347299, _n_(347298, "query", lambda: query), "lower")):
    _l_(347364)

    url = 'Google.com'
    _l_(347301)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %'
    _l_(347302)
    _c_(347309, _a_(347307, _c_(347306, _a_(347304, _n_(347303, "webbrowser", lambda: webbrowser), "get"), _n_(347305, "chrome_path", lambda: chrome_path)), "open"), _n_(347308, "url", lambda: url))
    _l_(347310)
elif 'open github' in _c_(347313, _a_(347312, _n_(347311, "query", lambda: query), "lower")):
    _l_(347363)

    url = 'github.com'
    _l_(347314)
    chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application/chrome.exe %'
    _l_(347315)
    _c_(347322, _a_(347320, _c_(347319, _a_(347317, _n_(347316, "webbrowser", lambda: webbrowser), "get"), _n_(347318, "chrome_path", lambda: chrome_path)), "open"), _n_(347321, "url", lambda: url))
    _l_(347323)
elif 'Play music' in _c_(347326, _a_(347325, _n_(347324, "query", lambda: query), "lower")):
    _l_(347362)

    songs_dir = "C:\\Users\\mohmmad\\Downloads\\Music"
    _l_(347327)
    songs = _c_(347331, _a_(347329, _n_(347328, "os", lambda: os), "listdir"), _n_(347330, "songs_dir", lambda: songs_dir))
    _l_(347332)
    _c_(347335, _n_(347333, "speak", lambda: speak), _n_(347334, "songs", lambda: songs))
    _l_(347336)
    _c_(347345, _a_(347338, _n_(347337, "os", lambda: os), "startfile"), _c_(347344, _a_(347341, _a_(347340, _n_(347339, "os", lambda: os), "path"), "join"), _n_(347342, "songs_dir", lambda: songs_dir),_n_(347343, "songs", lambda: songs)[0]))
    _l_(347346)

elif 'time' in _c_(347348, _n_(347347, "query", lambda: query)):
    _l_(347361)

    strTime = _c_(347354, _a_(347353, _c_(347352, _a_(347351, _a_(347350, _n_(347349, "datetime", lambda: datetime), "datetime"), "now")), "strftime"), "%H:%M:%S")
    _l_(347355)
    _c_(347359, _n_(347356, "speak", lambda: speak), f"{_n_(347357, 'Boss', lambda: Boss)} the time is {_n_(347358, 'strTime', lambda: strTime)}")
    _l_(347360)