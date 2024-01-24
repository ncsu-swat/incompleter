# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44934948/typeerror-list-indices-must-be-integers-or-slices-not-str-get-from-json
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import urllib.parse
    _l_(473503)

except ImportError:
    pass
try:
    import requests
    _l_(473505)

except ImportError:
    pass

raw_json = 'http://live.ksmobile.net/live/getreplayvideos?userid='
_l_(473506)
_c_(473508, _n_(473507, "print", lambda: print))
_l_(473509)

userid = 735890904669618176
_l_(473510)
#userid = input('UserID: ')

url = _n_(473511, "raw_json", lambda: raw_json) + _c_(473515, _a_(473513, _a_(473512, urllib, "parse"), "urlencode"), {'userid=': _n_(473514, "userid", lambda: userid)}) + '&page_size=1000'
_l_(473516)
_c_(473519, _n_(473517, "print", lambda: print), _n_(473518, "url", lambda: url))
_l_(473520)

json_data = _c_(473526, _a_(473525, _c_(473524, _a_(473522, _n_(473521, "requests", lambda: requests), "get"), _n_(473523, "url", lambda: url)), "json"))
_l_(473527)
_c_(473529, _n_(473528, "print", lambda: print))
_l_(473530)


for coordinates in _n_(473531, "json_data", lambda: json_data)['data']['video_info']:
    _l_(473540)

    _c_(473535, _n_(473532, "print", lambda: print), _n_(473533, "coordinates", lambda: coordinates)['lat'], _n_(473534, "coordinates", lambda: coordinates)['lnt'])
    _l_(473536)
    _c_(473538, _n_(473537, "print", lambda: print))
    _l_(473539)