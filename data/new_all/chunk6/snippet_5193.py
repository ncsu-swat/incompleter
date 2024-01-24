# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62287823/attributeerror-response-object-has-no-attribute-read-uses-requsts-and-json
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests as req
    _l_(348183)

except ImportError:
    pass
try:
    import json
    _l_(348185)

except ImportError:
    pass
Bin = _c_(348187, _n_(348186, "int", lambda: int), 300000)
_l_(348188)
BinMax = _c_(348190, _n_(348189, "int", lambda: int), 600000)
_l_(348191)
File = _c_(348193, _n_(348192, "open", lambda: open), "C:/Users/admin/Desktop/PS Now Generaetors/Bins.txt", 'a')
_l_(348194)

while _n_(348195, "Bin", lambda: Bin) != _n_(348196, "BinMax", lambda: BinMax):
    _l_(348231)

    json1 = _c_(348202, _a_(348198, _n_(348197, "req", lambda: req), "get"), "https://lookup.binlist.net/" + _c_(348201, _n_(348199, "str", lambda: str), _n_(348200, "Bin", lambda: Bin)))
    _l_(348203)
    json2 = _a_(348205, _n_(348204, "json1", lambda: json1), "text")
    _l_(348206)
    jsonout = _c_(348210, _a_(348208, _n_(348207, "json", lambda: json), "loads"), _n_(348209, "json2", lambda: json2))
    _l_(348211)
    country = _n_(348212, "jsonout", lambda: jsonout)["country"]
    _l_(348213)
    cc = _n_(348214, "country", lambda: country)["alpha2"]
    _l_(348215)
    if "US" or "AT" or "BE" or "CA" or "FR" or "De" or "IE" or "JP" or "LU" or "NL" or "CH" or "GB" or "ES" or "IT" or "PT" or "NO" or "DK" or "FI" or "SE" or "PH" == _n_(348216, "cc", lambda: cc):
        _l_(348229)

        _c_(348219, _n_(348217, "print", lambda: print), _n_(348218, "bin", lambda: bin), "writed")
        _l_(348220)
        _c_(348227, _a_(348222, _n_(348221, "File", lambda: File), "write"), "\n" + _c_(348225, _n_(348223, "str", lambda: str), _n_(348224, "Bin", lambda: Bin)) + ";" + _n_(348226, "cc", lambda: cc))
        _l_(348228)
    Bin =+ 1
    _l_(348230)