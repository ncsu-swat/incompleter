# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65881771/typeerror-cant-concat-str-to-bytes-for-google-indexing-api
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from oauth2client.service_account import ServiceAccountCredentials
    _l_(596994)

except ImportError:
    pass
try:
    import httplib2
    _l_(596996)

except ImportError:
    pass
try:
    import json
    _l_(596998)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(597000)

except ImportError:
    pass

SCOPES = "https://www.googleapis.com/auth/indexing"
_l_(597001)
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
_l_(597002)
JSON_KEY_FILE = "river-formula-BLABLA.json"
_l_(597003)

credentials = _c_(597008, _a_(597005, _n_(597004, "ServiceAccountCredentials", lambda: ServiceAccountCredentials), "from_json_keyfile_name"), _n_(597006, "JSON_KEY_FILE", lambda: JSON_KEY_FILE), scopes=_n_(597007, "SCOPES", lambda: SCOPES))
_l_(597009)
http = _c_(597015, _a_(597011, _n_(597010, "credentials", lambda: credentials), "authorize"), _c_(597014, _a_(597013, _n_(597012, "httplib2", lambda: httplib2), "Http")))
_l_(597016)
content = {"url":"https://www.parmalat.it/chef/ricette/cannelloni-al-ragu","type":"URL_UPDATED"}
_l_(597017)

response, content=_c_(597022, _a_(597019, _n_(597018, "http", lambda: http), "request"), _n_(597020, "ENDPOINT", lambda: ENDPOINT), method="POST", body=_n_(597021, "content", lambda: content))
_l_(597023)

_c_(597026, _n_(597024, "print", lambda: print), _n_(597025, "response", lambda: response))
_l_(597027)
_c_(597030, _n_(597028, "print", lambda: print), _n_(597029, "content", lambda: content))
_l_(597031)