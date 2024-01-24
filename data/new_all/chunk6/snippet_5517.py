# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62285920/python-error-attributeerror-str-object-has-no-attribute-read
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests as req
    _l_(337954)

except ImportError:
    pass
try:
    import json
    _l_(337956)

except ImportError:
    pass
Bin = _c_(337958, _n_(337957, "int", lambda: int), 300000)
_l_(337959)
BinMax = _c_(337961, _n_(337960, "int", lambda: int), 600000)
_l_(337962)
File = _c_(337964, _n_(337963, "open", lambda: open), "C:/Users/admin/Desktop/PS Now Generaetors/Bins.txt", 'a')
_l_(337965)

while _n_(337966, "bin", lambda: bin) != _n_(337967, "BinMax", lambda: BinMax):
    _l_(338002)

    json1 = _c_(337973, _a_(337969, _n_(337968, "req", lambda: req), "get"), "https://lookup.binlist.net/" + _c_(337972, _n_(337970, "str", lambda: str), _n_(337971, "Bin", lambda: Bin)))
    _l_(337974)
    json2 = _a_(337976, _n_(337975, "json1", lambda: json1), "text")
    _l_(337977)
    jsonout = _c_(337981, _a_(337979, _n_(337978, "json", lambda: json), "load"), _n_(337980, "json2", lambda: json2))
    _l_(337982)
    country = _n_(337983, "jsonout", lambda: jsonout)["country"]
    _l_(337984)
    cc = _n_(337985, "country", lambda: country)["alpha2"]
    _l_(337986)
    if _n_(337987, "cc", lambda: cc) == "US" or "AT" or "BE" or "CA" or "FR" or "De" or "IE" or "JP" or "LU" or "NL" or "CH" or "GB" or "ES" or "IT" or "PT" or "NO" or "DK" or "FI" or "SE" or "PH":
        _l_(338000)

        _c_(337990, _n_(337988, "print", lambda: print), _n_(337989, "bin", lambda: bin), "writed")
        _l_(337991)
        _c_(337998, _a_(337993, _n_(337992, "File", lambda: File), "write"), "\n" + _c_(337996, _n_(337994, "str", lambda: str), _n_(337995, "Bin", lambda: Bin)) + ";" + _n_(337997, "cc", lambda: cc))
        _l_(337999)
    bin =+ 1
    _l_(338001)