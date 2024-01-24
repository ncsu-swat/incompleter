# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72098676/python-google-my-business-v1-error-attributeerror-resource-object-has-no-at
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
CLIENT_SECRETS_FILE = "client_secret.json"
_l_(531614)
SCOPES = ["https://www.googleapis.com/auth/business.manage"]
_l_(531615)

API_SERVICE_NAME = "mybusiness"
_l_(531616)
API_VERSION = "v1"
_l_(531617)

service = _c_(531624, _a_(531620, _a_(531619, _n_(531618, "googleapiclient", lambda: googleapiclient), "discovery"), "build"), _n_(531621, "API_SERVICE_NAME", lambda: API_SERVICE_NAME),
        _n_(531622, "API_VERSION", lambda: API_VERSION),
        credentials=_n_(531623, "credentials", lambda: credentials),
        discoveryServiceUrl="https://mybusinessaccountmanagement.googleapis.com/$discovery/rest?version=v1",
    )
_l_(531625)

response = _c_(531634, _a_(531633, _c_(531632, _a_(531631, _c_(531630, _a_(531629, _c_(531628, _a_(531627, _n_(531626, "service", lambda: service), "accounts")), "locations")), "lists"), parent="accounts/113097808549740046769"), "execute"))
_l_(531635)