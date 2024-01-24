# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63428694/how-to-fix-visual-studio-attributeerror-engine-object-has-no-attribute-getp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyttsx3
    _l_(395071)

except ImportError:
    pass

engine = _c_(395074, _a_(395073, _n_(395072, "pyttsx3", lambda: pyttsx3), "init"), 'sapi5')
_l_(395075)
voices = _c_(395078, _a_(395077, _n_(395076, "engine", lambda: engine), "getProperty"), 'voices')
_l_(395079)
_c_(395083, _n_(395080, "print", lambda: print), _a_(395082, _n_(395081, "voices", lambda: voices)[0], "id"))
_l_(395084)
_c_(395089, _a_(395086, _n_(395085, "engine", lambda: engine), "setProperty"), 'voice',_a_(395088, _n_(395087, "voices", lambda: voices)[0], "id"))
_l_(395090)




def speak(audio):
    _l_(395100)

    _c_(395094, _a_(395092, _n_(395091, "engine", lambda: engine), "say"), _n_(395093, "audio", lambda: audio))
    _l_(395095)
    _c_(395098, _a_(395097, _n_(395096, "engine", lambda: engine), "runAndWait"))
    _l_(395099)

if _n_(395101, "__name__", lambda: __name__)=="__main__":
    _l_(395105)

    _c_(395103, _n_(395102, "speak", lambda: speak), "hello world")
    _l_(395104)