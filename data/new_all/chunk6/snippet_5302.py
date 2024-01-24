# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71905524/vonage-voice-api-calling-error-exception-has-occurred-typeerror-expecting-a-p
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(354932)

except ImportError:
    pass
try:
    from os.path import join, dirname
    _l_(354934)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(354936)

except ImportError:
    pass
try:
    from vonage import *
    _l_(354938)

except ImportError:
    pass
try:
    from dotenv import load_dotenv
    _l_(354940)

except ImportError:
    pass

dotenv_path = _c_(354945, _n_(354941, "join", lambda: join), _c_(354944, _n_(354942, "dirname", lambda: dirname), _n_(354943, "file", lambda: file)), "../.env")
_l_(354946)
_c_(354949, _n_(354947, "load_dotenv", lambda: load_dotenv), _n_(354948, "dotenv_path", lambda: dotenv_path))
_l_(354950)

VONAGE_APPLICATION_ID = _c_(354954, _a_(354953, _a_(354952, _n_(354951, "os", lambda: os), "environ"), "get"), "VONAGE_APPLICATION_ID")
_l_(354955)
VONAGE_APPLICATION_PRIVATE_KEY_PATH = _c_(354959, _a_(354958, _a_(354957, _n_(354956, "os", lambda: os), "environ"), "get"), "VONAGE_APPLICATION_PRIVATE_KEY_PATH")
_l_(354960)
VONAGE_NUMBER = _c_(354964, _a_(354963, _a_(354962, _n_(354961, "os", lambda: os), "environ"), "get"), "VONAGE_NUMBER")
_l_(354965)
TO_NUMBER = _c_(354969, _a_(354968, _a_(354967, _n_(354966, "os", lambda: os), "environ"), "get"), "TO_NUMBER")
_l_(354970)

client = _c_(354975, _a_(354972, _n_(354971, "vonage", lambda: vonage), "Client"), application_id=_n_(354973, "VONAGE_APPLICATION_ID", lambda: VONAGE_APPLICATION_ID),
private_key=_n_(354974, "VONAGE_APPLICATION_PRIVATE_KEY_PATH", lambda: VONAGE_APPLICATION_PRIVATE_KEY_PATH),
)
_l_(354976)

voice = _c_(354980, _a_(354978, _n_(354977, "vonage", lambda: vonage), "Voice"), _n_(354979, "client", lambda: client))
_l_(354981)

response = _c_(354986, _a_(354983, _n_(354982, "voice", lambda: voice), "create_call"), {
'to': [{'type': 'phone', 'number': _n_(354984, "TO_NUMBER", lambda: TO_NUMBER)}],
'from': {'type': 'phone', 'number': _n_(354985, "VONAGE_NUMBER", lambda: VONAGE_NUMBER)},
'ncco': [{'action': 'talk', 'text': 'This is a text to speech call from Nexmo'}]
})
_l_(354987)

_c_(354990, _n_(354988, "pprint", lambda: pprint), _n_(354989, "response", lambda: response))
_l_(354991)