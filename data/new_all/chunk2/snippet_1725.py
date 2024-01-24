# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60586521/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified-while
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pysndfx import AudioEffectsChain
    _l_(435924)

except ImportError:
    pass
try:
    import os
    _l_(435926)

except ImportError:
    pass

in_file = _c_(435929, _a_(435928, _n_(435927, "os", lambda: os), "getcwd")) + "\\" + "a.mp3"
_l_(435930)
in_file = _c_(435933, _a_(435932, _n_(435931, "in_file", lambda: in_file), "replace"), "\\", "//")#tried many things here, tried to it without any replacing
_l_(435934)#tried many things here, tried to it without any replacing

if _c_(435939, _a_(435937, _a_(435936, _n_(435935, "os", lambda: os), "path"), "isfile"), _n_(435938, "in_file", lambda: in_file)):
    _l_(435946)

    _c_(435941, _n_(435940, "print", lambda: print), "fileyes") #This returns true
    _l_(435942) #This returns true
else:
    _c_(435944, _n_(435943, "print", lambda: print), "not a file")
    _l_(435945)
_c_(435949, _n_(435947, "print", lambda: print), _n_(435948, "in_file", lambda: in_file))
_l_(435950)


fs = 44100
_l_(435951)
fx = _c_(435959, _a_(435958, _c_(435957, _a_(435956, _c_(435955, _a_(435954, _c_(435953, _n_(435952, "AudioEffectsChain", lambda: AudioEffectsChain)), "reverb")), "delay")), "phaser"))
_l_(435960)

_c_(435963, _n_(435961, "fx", lambda: fx), _n_(435962, "in_file", lambda: in_file),"apro.mp3")
_l_(435964)