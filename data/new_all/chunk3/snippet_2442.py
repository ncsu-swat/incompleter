# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34619898/python3-typeerror-the-json-object-must-be-str-not-bytes
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
response = _c_(540063, _a_(540062, _a_(540061, _n_(540060, "urllib", lambda: urllib), "request"), "urlopen"), 'http://api.icndb.com/jokes/random')
_l_(540064)
str_response = _c_(540069, _a_(540068, _c_(540067, _a_(540066, _n_(540065, "joke_json", lambda: joke_json), "readall")), "decode"), 'utf-8')
_l_(540070)
obj = _c_(540074, _a_(540072, _n_(540071, "json", lambda: json), "loads"), _n_(540073, "str_response", lambda: str_response))
_l_(540075)