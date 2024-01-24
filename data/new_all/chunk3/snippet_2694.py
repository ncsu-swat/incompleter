# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66467222/typeerror-int-object-is-not-callable-unique-problem-in-python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from fuzzywuzzy import fuzz
    _l_(559189)

except ImportError:
    pass
try:
    import sys
    _l_(559191)

except ImportError:
    pass
try:
    from aiy.voice import tts
    _l_(559193)

except ImportError:
    pass
#import tts
_c_(559196, _a_(559195, _n_(559194, "tts", lambda: tts), "say"), 'Harry activated')
_l_(559197)
try:
    from os import environ, path
    _l_(559199)

except ImportError:
    pass
try:
    import os
    _l_(559201)

except ImportError:
    pass
try:
    from pocketsphinx import LiveSpeech, get_model_path
    _l_(559203)

except ImportError:
    pass
model_path = _c_(559205, _n_(559204, "get_model_path", lambda: get_model_path))
_l_(559206)
_c_(559208, _n_(559207, "print", lambda: print), "active")
_l_(559209)
speech = _c_(559226, _n_(559210, "LiveSpeech", lambda: LiveSpeech), verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=_c_(559215, _a_(559213, _a_(559212, _n_(559211, "os", lambda: os), "path"), "join"), _n_(559214, "model_path", lambda: model_path), 'en-us'),
    lm=_c_(559220, _a_(559218, _a_(559217, _n_(559216, "os", lambda: os), "path"), "join"), _n_(559219, "model_path", lambda: model_path), 'en-us.lm.bin'),
    dic=_c_(559225, _a_(559223, _a_(559222, _n_(559221, "os", lambda: os), "path"), "join"), _n_(559224, "model_path", lambda: model_path), 'cmudict-en-us.dict')
)
_l_(559227)

for phrase in _n_(559228, "speech", lambda: speech):
    _l_(559256)

    p = _c_(559231, _n_(559229, "str", lambda: str), _n_(559230, "phrase", lambda: phrase))
    _l_(559232)
    _c_(559235, _n_(559233, "print", lambda: print), _n_(559234, "p", lambda: p))
    _l_(559236)
    r1 = _c_(559240, _a_(559238, _n_(559237, "fuzz", lambda: fuzz), "ratio"), _n_(559239, "p", lambda: p),"harry")
    _l_(559241)
    _c_(559244, _n_(559242, "print", lambda: print), _n_(559243, "r1", lambda: r1))
    _l_(559245)
    ri = _c_(559248, _n_(559246, "int", lambda: int), _n_(559247, "r1", lambda: r1))
    _l_(559249)
    if _n_(559250, "ri", lambda: ri) > _c_(559251, 60):
        _l_(559255)

        _c_(559253, _n_(559252, "print", lambda: print), "you said my name")
        _l_(559254)