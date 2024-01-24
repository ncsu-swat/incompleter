# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55507226/attributeerror-module-pyaudio-has-no-attribute-version
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
     import speech_recognition as sr
     _l_(548245)

except ImportError:
     pass

r = _c_(548248, _a_(548247, _n_(548246, "sr", lambda: sr), "Recognizer"))
_l_(548249)
with _c_(548252, _a_(548251, _n_(548250, "sr", lambda: sr), "Microphone")) as source:
     _l_(548277)

     _c_(548254, _n_(548253, "print", lambda: print), 'speak say anything')
     _l_(548255)
     audio = _c_(548259, _a_(548257, _n_(548256, "r", lambda: r), "listen"), _n_(548258, "source", lambda: source))
     _l_(548260)
     try:
          _l_(548276)

          text = _c_(548264, _a_(548262, _n_(548261, "r", lambda: r), "recognize_google"), _n_(548263, "audio", lambda: audio))
          _l_(548265)
          _c_(548270, _n_(548266, "print", lambda: print), _c_(548269, _a_(548267, "you said:{}", "format"), _n_(548268, "text", lambda: text)))
          _l_(548271)
     except:
          _l_(548275)

          _c_(548273, _n_(548272, "print", lambda: print), "cant recognize")
          _l_(548274)