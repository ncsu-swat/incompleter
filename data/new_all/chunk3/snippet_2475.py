# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76448088/python-attribute-error-not-recocgnising-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(565670)

except ImportError:
    pass
try:
    import speech_recognition as sr
    _l_(565672)

except ImportError:
    pass

# Beginning of the AI
class ChatBot():
    _l_(565681)

    def __init__(self, name):
        _l_(565680)

        _c_(565675, _n_(565673, "print", lambda: print), "----- starting up", _n_(565674, "name", lambda: name), "-----")
        _l_(565676)
        _n_(565677, "self", lambda: self).name = _n_(565678, "name", lambda: name)
        _l_(565679)
# Execute the AI
if _n_(565682, "__name__", lambda: __name__) == "__main__":
    _l_(565686)

    ai = _c_(565684, _n_(565683, "ChatBot", lambda: ChatBot), name="Dev")
    _l_(565685)
#name of AI is Dev
# Execute the AI

#speech recognition with microphone, it converts it to text
def speech_to_text(self):
    _l_(565719)

    recognizer = _c_(565689, _a_(565688, _n_(565687, "sr", lambda: sr), "Recognizer"))
    _l_(565690)
    with _c_(565693, _a_(565692, _n_(565691, "sr", lambda: sr), "Microphone")) as mic:
        _l_(565702)

        _c_(565695, _n_(565694, "print", lambda: print), "listening...")
        _l_(565696)
        audio = _c_(565700, _a_(565698, _n_(565697, "recognizer", lambda: recognizer), "listen"), _n_(565699, "mic", lambda: mic))
        _l_(565701)
    try:
        _l_(565718)

        _n_(565703, "self", lambda: self).text = _c_(565707, _a_(565705, _n_(565704, "recognizer", lambda: recognizer), "recognize_google"), _n_(565706, "audio", lambda: audio))
        _l_(565708)
        _c_(565712, _n_(565709, "print", lambda: print), "me --> ", _a_(565711, _n_(565710, "self", lambda: self), "text"))
        _l_(565713)
    except:
        _l_(565717)

        _c_(565715, _n_(565714, "print", lambda: print), "me -->  ERROR")
        _l_(565716)

def wake_up(self, text):
    _l_(565726)

    aux = True if _a_(565721, _n_(565720, "self", lambda: self), "name") in _c_(565724, _a_(565723, _n_(565722, "text", lambda: text), "lower")) else False
    _l_(565725)
    return aux

# Execute the AI
if _n_(565727, "__name__", lambda: __name__) == "__main__":
    _l_(565736)

    ai = _c_(565729, _n_(565728, "ChatBot", lambda: ChatBot), name="Dev")
    _l_(565730)
    while True:
        _l_(565735)

        _c_(565733, _a_(565732, _n_(565731, "ai", lambda: ai), "speech_to_text"))
        _l_(565734)

def wake_up(self, text):
    _l_(565743)

    aux = True if _a_(565738, _n_(565737, "self", lambda: self), "name") in _c_(565741, _a_(565740, _n_(565739, "text", lambda: text), "lower")) else False
    _l_(565742)
    return aux
try:
    from gtts import gTTS
    _l_(565745)

except ImportError:
    pass
try:
    import os
    _l_(565747)

except ImportError:
    pass
@_n_(565748, "staticmethod", lambda: staticmethod)
def text_to_speech(text):
    _l_(565769)

    _c_(565751, _n_(565749, "print", lambda: print), "AI --> ", _n_(565750, "text", lambda: text))
    _l_(565752)
    speaker = _c_(565755, _n_(565753, "gTTS", lambda: gTTS), text=_n_(565754, "text", lambda: text), lang="en", slow=False)
    _l_(565756)
    _c_(565759, _a_(565758, _n_(565757, "speaker", lambda: speaker), "save"), "res.mp3")
    _l_(565760)
    _c_(565763, _a_(565762, _n_(565761, "os", lambda: os), "system"), "start res.mp3")  # windows use->start
    _l_(565764)  # windows use->start
    _c_(565767, _a_(565766, _n_(565765, "os", lambda: os), "remove"), "res.mp3")
    _l_(565768)