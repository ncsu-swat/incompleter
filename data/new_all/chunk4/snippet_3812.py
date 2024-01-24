# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67348417/attribute-error-python-pncc-using-spafe-module-scipy-has-no-attribute-fftpa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import scipy
    _l_(589688)

except ImportError:
    pass
try:
    from spafe.utils import vis
    _l_(589690)

except ImportError:
    pass
try:
    from spafe.features.pncc import pncc
    _l_(589692)

except ImportError:
    pass
try:
    import scipy.io.wavfile as wav
    _l_(589694)

except ImportError:
    pass

# init input vars
num_ceps = 13
_l_(589695)
low_freq = 0
_l_(589696)
high_freq = 2000
_l_(589697)
nfilts = 24
_l_(589698)
nfft = 512
_l_(589699)
dct_type = 2,
_l_(589700)
use_energy = False,
_l_(589701)
lifter = 5
_l_(589702)
normalize = True
_l_(589703)

# read wav
(fs, sig) = _c_(589706, _a_(589705, _n_(589704, "wav", lambda: wav), "read"), "sample.wav")
_l_(589707)

# compute features
pnccs = _c_(589720, _n_(589708, "pncc", lambda: pncc), sig=_n_(589709, "sig", lambda: sig),
             fs=_n_(589710, "fs", lambda: fs),
             num_ceps=_n_(589711, "num_ceps", lambda: num_ceps),
             nfilts=_n_(589712, "nfilts", lambda: nfilts),
             nfft=_n_(589713, "nfft", lambda: nfft),
             low_freq=_n_(589714, "low_freq", lambda: low_freq),
             high_freq=_n_(589715, "high_freq", lambda: high_freq),
             dct_type=_n_(589716, "dct_type", lambda: dct_type),
             use_energy=_n_(589717, "use_energy", lambda: use_energy),
             lifter=_n_(589718, "lifter", lambda: lifter),
             normalize=_n_(589719, "normalize", lambda: normalize))
_l_(589721)

# visualize spectogram
_c_(589726, _a_(589723, _n_(589722, "vis", lambda: vis), "spectogram"), _n_(589724, "sig", lambda: sig), _n_(589725, "fs", lambda: fs))
_l_(589727)
# visualize features
_c_(589731, _a_(589729, _n_(589728, "vis", lambda: vis), "visualize_features"), _n_(589730, "pnccs", lambda: pnccs), 'PNCC Index', 'Frame Index')
_l_(589732)