# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66557452/google-indexing-api-batch-request-attributeerror-resource-object-has-no-attri
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from oauth2client.service_account import ServiceAccountCredentials
    _l_(543803)

except ImportError:
    pass
try:
    from googleapiclient.http import BatchHttpRequest
    _l_(543805)

except ImportError:
    pass
try:
    import httplib2
    _l_(543807)

except ImportError:
    pass
try:
    from googleapiclient.discovery import build
    _l_(543809)

except ImportError:
    pass
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
_l_(543810)
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
_l_(543811)

# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = "service_account_file.json"
_l_(543812)

credentials = _c_(543817, _a_(543814, _n_(543813, "ServiceAccountCredentials", lambda: ServiceAccountCredentials), "from_json_keyfile_name"), _n_(543815, "JSON_KEY_FILE", lambda: JSON_KEY_FILE), scopes=_n_(543816, "SCOPES", lambda: SCOPES))
_l_(543818)

service = _c_(543821, _n_(543819, "build", lambda: build), 'indexing', 'v3', credentials=_n_(543820, "credentials", lambda: credentials))
_l_(543822)

def insert_event(request_id, response, exception):
    _l_(543833)

    if _n_(543823, "exception", lambda: exception) is not None:
        _l_(543832)

        _c_(543826, _n_(543824, "print", lambda: print), _n_(543825, "exception", lambda: exception))
        _l_(543827)
    else:
      _c_(543830, _n_(543828, "print", lambda: print), _n_(543829, "response", lambda: response))
      _l_(543831)

batch = _c_(543836, _n_(543834, "BatchHttpRequest", lambda: BatchHttpRequest), callback=_n_(543835, "insert_event", lambda: insert_event))
_l_(543837)
_c_(543845, _a_(543839, _n_(543838, "batch", lambda: batch), "add"), _c_(543844, _a_(543843, _c_(543842, _a_(543841, _n_(543840, "service", lambda: service), "events")), "quickAdd"), url="URL HERE", type="URL_UPDATED"))
_l_(543846)
_c_(543854, _a_(543848, _n_(543847, "batch", lambda: batch), "add"), _c_(543853, _a_(543852, _c_(543851, _a_(543850, _n_(543849, "service", lambda: service), "events")), "quickAdd"), url="URL HERE", type="URL_UPDATED"))
_l_(543855)
_c_(543859, _a_(543857, _n_(543856, "batch", lambda: batch), "execute"), http=_n_(543858, "http", lambda: http))
_l_(543860)