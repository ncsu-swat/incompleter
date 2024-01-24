# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75461472/attributeerror-audio-object-has-no-attribute-to-intensity
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
data = _c_(613770, _n_(613768, "Audio", lambda: Audio), _n_(613769, "file_path", lambda: file_path))
_l_(613771)
def _vad(sdata):
    _l_(613797)

    intensity = _c_(613774, _a_(613773, _n_(613772, "data", lambda: data), "to_intensity"))
    _l_(613775)
    intensity = _c_(613779, _a_(613778, _a_(613777, _n_(613776, "intensity", lambda: intensity), "values"), "squeeze"))
    _l_(613780)
    _n_(613781, "intensity", lambda: intensity)[_n_(613782, "intensity", lambda: intensity) <= 0] = 0
    _l_(613783)
    intensity = _c_(613786, _n_(613784, "_length", lambda: _length), _n_(613785, "intensity", lambda: intensity))
    _l_(613787)
    length= _c_(613790, _n_(613788, "_length", lambda: _length), _n_(613789, "intensity", lambda: intensity))
    _l_(613791)
    intensity_mean = _c_(613794, _n_(613792, "len", lambda: len), _n_(613793, "intensity", lambda: intensity))
    _l_(613795)
    temp = []
    _l_(613796)