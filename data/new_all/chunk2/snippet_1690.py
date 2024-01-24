# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63091432/typeerror-float-argument-must-be-a-string-or-a-number-not-polycollection
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import librosa.display
    _l_(475029)

except ImportError:
    pass
ax1 = _c_(475033, _a_(475031, _n_(475030, "plt", lambda: plt), "subplot"), _n_(475032, "gs", lambda: gs)[1])
_l_(475034)
y, sr = _c_(475037, _a_(475036, _n_(475035, "librosa", lambda: librosa), "load"), "Audiofilepath")
_l_(475038)
_c_(475046, _a_(475040, _n_(475039, "ax1", lambda: ax1), "plot"), _c_(475045, _a_(475042, _a_(475041, librosa, "display"), "waveplot"), _n_(475043, "y", lambda: y), _n_(475044, "sr", lambda: sr)))
_l_(475047)