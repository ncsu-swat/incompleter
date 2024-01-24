# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62285920/python-error-attributeerror-str-object-has-no-attribute-read
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests as req
    _l_(370620)

except ImportError:
    pass
try:
    import json
    _l_(370622)

except ImportError:
    pass
Bin = _c_(370624, _n_(370623, "int", lambda: int), 300000)
_l_(370625)
BinMax = _c_(370627, _n_(370626, "int", lambda: int), 600000)
_l_(370628)
File = _c_(370630, _n_(370629, "open", lambda: open), "C:/Users/admin/Desktop/PS Now Generaetors/Bins.txt", 'a')
_l_(370631)

while _n_(370632, "bin", lambda: bin) != _n_(370633, "BinMax", lambda: BinMax):
    _l_(370668)

    json1 = _c_(370639, _a_(370635, _n_(370634, "req", lambda: req), "get"), "https://lookup.binlist.net/" + _c_(370638, _n_(370636, "str", lambda: str), _n_(370637, "Bin", lambda: Bin)))
    _l_(370640)
    json2 = _a_(370642, _n_(370641, "json1", lambda: json1), "text")
    _l_(370643)
    jsonout = _c_(370647, _a_(370645, _n_(370644, "json", lambda: json), "load"), _n_(370646, "json2", lambda: json2))
    _l_(370648)
    country = _n_(370649, "jsonout", lambda: jsonout)["country"]
    _l_(370650)
    cc = _n_(370651, "country", lambda: country)["alpha2"]
    _l_(370652)
    if _n_(370653, "cc", lambda: cc) == "US" or "AT" or "BE" or "CA" or "FR" or "De" or "IE" or "JP" or "LU" or "NL" or "CH" or "GB" or "ES" or "IT" or "PT" or "NO" or "DK" or "FI" or "SE" or "PH":
        _l_(370666)

        _c_(370656, _n_(370654, "print", lambda: print), _n_(370655, "bin", lambda: bin), "writed")
        _l_(370657)
        _c_(370664, _a_(370659, _n_(370658, "File", lambda: File), "write"), "\n" + _c_(370662, _n_(370660, "str", lambda: str), _n_(370661, "Bin", lambda: Bin)) + ";" + _n_(370663, "cc", lambda: cc))
        _l_(370665)
    bin =+ 1
    _l_(370667)