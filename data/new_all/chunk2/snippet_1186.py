# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55770064/python-typeerror-listen-missing-1-required-positional-argument-self
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import speech_recognition as sr
    _l_(442539)

except ImportError:
    pass
try:
    import os
    _l_(442541)

except ImportError:
    pass
try:
    from playsound import playsound
    _l_(442543)

except ImportError:
    pass
try:
    import webbrowser
    _l_(442545)

except ImportError:
    pass
try:
    import random
    _l_(442547)

except ImportError:
    pass

speech = _a_(442549, _n_(442548, "sr", lambda: sr), "Recognizer")
_l_(442550)
_n_(442551, "speech", lambda: speech).energy_threshold = 4000
_l_(442552)

greeting_dictionary = {'sup' : 'whats good','ay' : 'wassup'}
_l_(442553)

def play_sound(mp3_list):
    _l_(442563)

    mp3 = _c_(442557, _a_(442555, _n_(442554, "random", lambda: random), "choice"), _n_(442556, "mp3_list", lambda: mp3_list))
    _l_(442558)
    _c_(442561, _n_(442559, "play_sound", lambda: play_sound), _n_(442560, "mp3", lambda: mp3))
    _l_(442562)

def read_input():
    _l_(442599)

    voice_text = ''
    _l_(442564)
    _c_(442566, _n_(442565, "print", lambda: print), 'Listening...')
    _l_(442567)
    with _c_(442570, _a_(442569, _n_(442568, "sr", lambda: sr), "Microphone")) as source:
        _l_(442576)

        audio = _c_(442574, _a_(442572, _n_(442571, "speech", lambda: speech), "listen"), source=_n_(442573, "source", lambda: source), timeout=10, phrase_time_limit=5) #The error is here
        _l_(442575) #The error is here
    try:
        _l_(442596)

        voice_text = _c_(442580, _a_(442578, _n_(442577, "speech", lambda: speech), "recognize_google"), _n_(442579, "audio", lambda: audio))
        _l_(442581)
    except _a_(442583, _n_(442582, "sr", lambda: sr), "UnknownValueError"):
        _l_(442585)

        pass
        _l_(442584)
    except _a_(442587, _n_(442586, "sr", lambda: sr), "RequestError") as e:
        _l_(442591)

        _c_(442589, _n_(442588, "print", lambda: print), 'Network error')
        _l_(442590)
    except _a_(442593, _n_(442592, "sr", lambda: sr), "WaitTimeoutError"):
        _l_(442595)

        pass
        _l_(442594)
    aux = _n_(442597, "voice_text", lambda: voice_text)
    _l_(442598)
    return aux

if _n_(442600, "__name__", lambda: __name__) == '__main__':
    _l_(442633)


    _c_(442602, _n_(442601, "playsound", lambda: playsound), 'mp3/dawg/greet.mp3')
    _l_(442603)

    while True:
        _l_(442632)


        input = _c_(442605, _n_(442604, "read_input", lambda: read_input))
        _l_(442606)

        _c_(442611, _n_(442607, "print", lambda: print), _c_(442610, _a_(442608, 'You: ', "format"), _n_(442609, "input", lambda: input)))
        _l_(442612)

        if 'hello' in _n_(442613, "input", lambda: input):
            _l_(442631)

            continue
            _l_(442614)
        elif 'open' in _n_(442615, "input", lambda: input):
            _l_(442630)

            _c_(442623, _a_(442617, _n_(442616, "os", lambda: os), "system"), _c_(442622, _a_(442618, 'explorer ~/Desktop {}', "format"), _c_(442621, _a_(442620, _n_(442619, "input", lambda: input), "replace"), 'Open ', '')))
            _l_(442624)
        elif 'bye' in _n_(442625, "input", lambda: input):
            _l_(442629)

            aux = ""
            _l_(442628)
            exit(aux)