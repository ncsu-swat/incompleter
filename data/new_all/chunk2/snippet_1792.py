# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55506571/python-nameerror-name-engine-is-not-defined-driver-not-found
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(426294)

except ImportError:
    pass
_c_(426298, _n_(426295, "print", lambda: print), _a_(426297, _n_(426296, "sys", lambda: sys), "path"))
_l_(426299)
try:
    import speech_recognition as sr
    _l_(426301)

except ImportError:
    pass
try:
    import pyttsx3
    _l_(426303)

except ImportError:
    pass

try:
    _l_(426318)

    engine = _c_(426306, _a_(426305, _n_(426304, "pyttsx3", lambda: pyttsx3), "init"))
    _l_(426307)
except _n_(426308, "ImportError", lambda: ImportError):
    _l_(426312)

    _c_(426310, _n_(426309, "print", lambda: print), "Driver not found")
    _l_(426311)
except _n_(426313, "RuntimeError", lambda: RuntimeError):
    _l_(426317)

    _c_(426315, _n_(426314, "print", lambda: print), "Driver fails to init")
    _l_(426316)

voices = _c_(426321, _a_(426320, _n_(426319, "engine", lambda: engine), "getProperty"), "voices")
_l_(426322)

for voice in _n_(426323, "voices", lambda: voices):
    _l_(426329)

    _c_(426327, _n_(426324, "print", lambda: print), _a_(426326, _n_(426325, "voice", lambda: voice), "id"))
    _l_(426328)