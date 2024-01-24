# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67560562/pandas-read-csv-error-i-e-filenotfounderror-errno-2-no-such-file-or-direct
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
file_path = "%s.csv" % _n_(548646, "i", lambda: (i))
_l_(548647)
df = _c_(548651, _a_(548649, _n_(548648, "pd", lambda: pd), "read_csv"), _n_(548650, "file_path", lambda: file_path))
_l_(548652)
sma_padded = _c_(548664, _a_(548654, _n_(548653, "np", lambda: np), "concatenate"), [_c_(548662, _a_(548656, _n_(548655, "np", lambda: np), "zeros"), _c_(548659, _n_(548657, "len", lambda: len), _n_(548658, "df", lambda: df)) - _a_(548661, _n_(548660, "sma", lambda: sma), "shape")[0]), _n_(548663, "sma", lambda: sma)])
_l_(548665)
_n_(548666, "df", lambda: df)['SMA'] = _c_(548672, _a_(548668, _n_(548667, "pd", lambda: pd), "Series"), _n_(548669, "sma_padded", lambda: sma_padded), index=_a_(548671, _n_(548670, "df", lambda: df), "index"))   
_l_(548673)   
_c_(548677, _a_(548675, _n_(548674, "df", lambda: df), "to_csv"), _n_(548676, "file_path", lambda: file_path), index=False)
_l_(548678)