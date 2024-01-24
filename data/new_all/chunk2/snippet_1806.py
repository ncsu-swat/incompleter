# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54375286/typeerror-cannot-unpack-non-iterable-axessubplot-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pywt
    _l_(428606)

except ImportError:
    pass
try:
    import scipy.io.wavfile as wavfile
    _l_(428608)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(428610)

except ImportError:
    pass

rate,signal = _c_(428613, _a_(428612, _n_(428611, "wavfile", lambda: wavfile), "read"), 'a0025.wav')
_l_(428614)
time = [_n_(428615, "x", lambda: x) /_n_(428616, "rate", lambda: rate) for x in _c_(428621, _n_(428617, "range", lambda: range), 0,_c_(428620, _n_(428618, "len", lambda: len), _n_(428619, "signal", lambda: signal)))]
_l_(428622)
tree = _c_(428626, _a_(428624, _n_(428623, "pywt", lambda: pywt), "wavedec"), data=_n_(428625, "signal", lambda: signal)[:1000], wavelet='db2', level=4, mode='symmetric')
_l_(428627)
_c_(428632, _n_(428628, "print", lambda: print), _c_(428631, _n_(428629, "len", lambda: len), _n_(428630, "tree", lambda: tree)))
_l_(428633)
newTree = [_n_(428634, "tree", lambda: tree)[0]*0, _n_(428635, "tree", lambda: tree)[1]*0, _n_(428636, "tree", lambda: tree)[2]*0, _n_(428637, "tree", lambda: tree)[3]*0, _n_(428638, "tree", lambda: tree)[4]]
_l_(428639)
recSignal = _c_(428643, _a_(428641, _n_(428640, "pywt", lambda: pywt), "waverec"), _n_(428642, "newTree", lambda: newTree),'db2')
_l_(428644)
fig, ax = _c_(428647, _a_(428646, _n_(428645, "plt", lambda: plt), "subplot"), 2, 1)
_l_(428648)
_c_(428653, _a_(428650, _n_(428649, "ax", lambda: ax)[0], "plot"), _n_(428651, "time", lambda: time)[:1000], _n_(428652, "signal", lambda: signal)[:1000])
_l_(428654)
_c_(428657, _a_(428656, _n_(428655, "ax", lambda: ax)[0], "set_xlabel"), 'Czas [s]')
_l_(428658)
_c_(428661, _a_(428660, _n_(428659, "ax", lambda: ax)[0], "set_ylabel"), 'Amplituda')
_l_(428662)
_c_(428667, _a_(428664, _n_(428663, "ax", lambda: ax)[1], "plot"), _n_(428665, "time", lambda: time)[:1000], _n_(428666, "recSignal", lambda: recSignal)[:1000])
_l_(428668)
_c_(428671, _a_(428670, _n_(428669, "ax", lambda: ax)[1], "set_xlabel"), 'Czas [s]')
_l_(428672)
_c_(428675, _a_(428674, _n_(428673, "ax", lambda: ax)[1], "set_ylabel"), 'Amplituda')
_l_(428676)
_c_(428679, _a_(428678, _n_(428677, "plt", lambda: plt), "show"))
_l_(428680)