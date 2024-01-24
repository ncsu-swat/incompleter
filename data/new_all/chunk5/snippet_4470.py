# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57095785/how-to-fix-typeerror-while-trying-to-find-a-tag-using-xml-etree
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.etree.ElementTree as ET
    _l_(693478)

except ImportError:
    pass
try:
    import ssl
    _l_(693480)

except ImportError:
    pass
try:
    import urllib.error, urllib.parse, urllib.request
    _l_(693482)

except ImportError:
    pass

ctx = _c_(693485, _a_(693484, _n_(693483, "ssl", lambda: ssl), "create_default_context"))
_l_(693486)
_n_(693487, "ctx", lambda: ctx).check_hostname = False
_l_(693488)
_n_(693489, "ctx", lambda: ctx).verify_mode = _a_(693491, _n_(693490, "ssl", lambda: ssl), "CERT_NONE")
_l_(693492)

service_url = 'http://www.geoplugin.net/xml.gp?'
_l_(693493)
ip_api = 'https://api.ipify.org'
_l_(693494)

ip_addr = _c_(693503, _a_(693502, _c_(693501, _a_(693500, _c_(693499, _a_(693496, _a_(693495, urllib, "request"), "urlopen"), _n_(693497, "ip_api", lambda: ip_api), context=_n_(693498, "ctx", lambda: ctx)), "read")), "decode")) 
_l_(693504) 
parms = _c_(693506, _n_(693505, "dict", lambda: dict))
_l_(693507)
_n_(693508, "parms", lambda: parms)['ip'] = _n_(693509, "ip_addr", lambda: ip_addr)
_l_(693510)
url = _n_(693511, "service_url", lambda: service_url) + _c_(693515, _a_(693513, _a_(693512, urllib, "parse"), "urlencode"), _n_(693514, "parms", lambda: parms))
_l_(693516)
_c_(693519, _n_(693517, "print", lambda: print), 'Retrieving:',_n_(693518, "url", lambda: url))
_l_(693520)

xmldat = _c_(693529, _a_(693528, _c_(693527, _a_(693526, _c_(693525, _a_(693522, _a_(693521, urllib, "request"), "urlopen"), _n_(693523, "url", lambda: url), context=_n_(693524, "ctx", lambda: ctx)), "read")), "decode"))
_l_(693530)
_c_(693535, _n_(693531, "print", lambda: print), 'Retrieved', _c_(693534, _n_(693532, "len", lambda: len), _n_(693533, "xmldat", lambda: xmldat)), 'characters' )
_l_(693536)
_c_(693539, _n_(693537, "print", lambda: print), _n_(693538, "xmldat", lambda: xmldat))
_l_(693540)
tree = _c_(693544, _a_(693542, _n_(693541, "ET", lambda: ET), "fromstring"), _n_(693543, "xmldat", lambda: xmldat))
_l_(693545)

region = _c_(693550, _a_(693549, _c_(693548, _a_(693547, _n_(693546, "tree", lambda: tree), "find"), 'geoplugin_region'), "text"))
_l_(693551)
country = _c_(693556, _a_(693555, _c_(693554, _a_(693553, _n_(693552, "tree", lambda: tree), "find"), 'geoplugin_countryName'), "text"))
_l_(693557)
latitude = _c_(693562, _a_(693561, _c_(693560, _a_(693559, _n_(693558, "tree", lambda: tree), "find"), 'geoplugin_latitude'), "text"))
_l_(693563)
longitude = _c_(693568, _a_(693567, _c_(693566, _a_(693565, _n_(693564, "tree", lambda: tree), "find"), 'geoplugin_longitude'), "text"))
_l_(693569)
currency_exchange = _c_(693574, _a_(693573, _c_(693572, _a_(693571, _n_(693570, "tree", lambda: tree), "find"), 'geoplugin_currencyConverter'), "text"))
_l_(693575)

_c_(693582, _n_(693576, "print", lambda: print), 'Region:', _n_(693577, "region", lambda: region), '\nCountry:', _n_(693578, "country", lambda: country), '\nLatitude', _n_(693579, "latitude", lambda: latitude), '\nLongitude:', _n_(693580, "longitude", lambda: longitude), '\nCurrency Exchange Rate (relative to US Dollar)', _n_(693581, "currency_exchange", lambda: currency_exchange))
_l_(693583)