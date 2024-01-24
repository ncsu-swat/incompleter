# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74933471/type-error-and-got-an-unexpected-keyword-argument-when-passing-dict-to-python-z
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from zeep.wsse.signature import BinarySignature
    _l_(623282)

except ImportError:
    pass
try:
    from zeep.wsse import utils
    _l_(623284)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(623286)

except ImportError:
    pass
try:
    import contextlib
    _l_(623288)

except ImportError:
    pass
try:
    import os
    _l_(623290)

except ImportError:
    pass
try:
    import requests
    _l_(623292)

except ImportError:
    pass
try:
    from requests_pkcs12 import Pkcs12Adapter
    _l_(623294)

except ImportError:
    pass
try:
    from zeep.transports import Transport
    _l_(623296)

except ImportError:
    pass
try:
    from zeep import Client, Settings
    _l_(623298)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(623300)

except ImportError:
    pass
try:
    from tempfile import NamedTemporaryFile
    _l_(623302)

except ImportError:
    pass
try:
    from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
    _l_(623304)

except ImportError:
    pass
try:
    from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
    _l_(623306)

except ImportError:
    pass
try:
    import random
    _l_(623308)

except ImportError:
    pass
try:
    import logging.config
    _l_(623310)

except ImportError:
    pass


# USE THE MOST VERBOSE LOGGING LEVEL
_c_(623313, _a_(623312, _a_(623311, logging, "config"), "dictConfig"), {
 'version': 1,
 'formatters': {
 'verbose': {
 'format': '%(name)s: %(message)s'
 }
 },
 'handlers': {
 'console': {
 'level': 'DEBUG',
 'class': 'logging.StreamHandler',
 'formatter': 'verbose',
 },
 },
 'loggers': {
 'zeep.transports': {
 'level': 'DEBUG',
 'propagate': True,
 'handlers': ['console'],
 },
 }
})
_l_(623314)

class BinarySignatureTimestamp(_n_(623315, "BinarySignature", lambda: BinarySignature)):
    _l_(623375)

    def apply(self, envelope, headers):
        _l_(623371)

        security = _c_(623319, _a_(623317, _n_(623316, "utils", lambda: utils), "get_security_header"), _n_(623318, "envelope", lambda: envelope))
        _l_(623320)

        created = _c_(623323, _a_(623322, _n_(623321, "datetime", lambda: datetime), "utcnow"))
        _l_(623324)
        expired = _n_(623325, "created", lambda: created) + _c_(623327, _n_(623326, "timedelta", lambda: timedelta), seconds=1 * 60)
        _l_(623328)

        timestamp = _c_(623331, _a_(623330, _n_(623329, "utils", lambda: utils), "WSU"), 'Timestamp')
        _l_(623332)
        _c_(623343, _a_(623334, _n_(623333, "timestamp", lambda: timestamp), "append"), _c_(623342, _a_(623336, _n_(623335, "utils", lambda: utils), "WSU"), 'Created', _c_(623341, _a_(623340, _c_(623339, _a_(623338, _n_(623337, "created", lambda: created), "replace"), microsecond=0), "isoformat"))+'Z'))
        _l_(623344)
        _c_(623355, _a_(623346, _n_(623345, "timestamp", lambda: timestamp), "append"), _c_(623354, _a_(623348, _n_(623347, "utils", lambda: utils), "WSU"), 'Expires', _c_(623353, _a_(623352, _c_(623351, _a_(623350, _n_(623349, "expired", lambda: expired), "replace"), microsecond=0), "isoformat"))+'Z'))
        _l_(623356)

        _c_(623360, _a_(623358, _n_(623357, "security", lambda: security), "append"), _n_(623359, "timestamp", lambda: timestamp))
        _l_(623361)

        _c_(623366, _a_(623363, _n_(623362, "super", lambda: super)(), "apply"), _n_(623364, "envelope", lambda: envelope), _n_(623365, "headers", lambda: headers))
        _l_(623367)
        aux = _n_(623368, "envelope", lambda: envelope), _n_(623369, "headers", lambda: headers)
        _l_(623370)
        return aux

    def verify(self, envelope):
        _l_(623374)

        aux = _n_(623372, "envelope", lambda: envelope)
        _l_(623373)
        return aux

@_a_(623377, _n_(623376, "contextlib", lambda: contextlib), "contextmanager")
def pfx_to_pem(pfx_path, pfx_password):
    _l_(623436)

    ''' Decrypts the .pfx file to be used with requests. '''
    _l_(623378)
    pfx = _c_(623383, _a_(623382, _c_(623381, _n_(623379, "Path", lambda: Path), _n_(623380, "pfx_path", lambda: pfx_path)), "read_bytes"))
    _l_(623384)
    private_key, main_cert, add_certs = _c_(623390, _n_(623385, "load_key_and_certificates", lambda: load_key_and_certificates), _n_(623386, "pfx", lambda: pfx), _c_(623389, _a_(623388, _n_(623387, "pfx_password", lambda: pfx_password), "encode"), 'utf-8'), None)
    _l_(623391)

    with _c_(623393, _n_(623392, "NamedTemporaryFile", lambda: NamedTemporaryFile), suffix='.pem', delete=False) as t_pem:
        _l_(623435)

        with _c_(623397, _n_(623394, "open", lambda: open), _a_(623396, _n_(623395, "t_pem", lambda: t_pem), "name"), 'wb') as pem_file:
            _l_(623431)

            _c_(623409, _a_(623399, _n_(623398, "pem_file", lambda: pem_file), "write"), _c_(623408, _a_(623401, _n_(623400, "private_key", lambda: private_key), "private_bytes"), _a_(623403, _n_(623402, "Encoding", lambda: Encoding), "PEM"), _a_(623405, _n_(623404, "PrivateFormat", lambda: PrivateFormat), "PKCS8"), _c_(623407, _n_(623406, "NoEncryption", lambda: NoEncryption))))
            _l_(623410)
            _c_(623418, _a_(623412, _n_(623411, "pem_file", lambda: pem_file), "write"), _c_(623417, _a_(623414, _n_(623413, "main_cert", lambda: main_cert), "public_bytes"), _a_(623416, _n_(623415, "Encoding", lambda: Encoding), "PEM")))
            _l_(623419)
            for ca in _n_(623420, "add_certs", lambda: add_certs):
                _l_(623430)

                _c_(623428, _a_(623422, _n_(623421, "pem_file", lambda: pem_file), "write"), _c_(623427, _a_(623424, _n_(623423, "ca", lambda: ca), "public_bytes"), _a_(623426, _n_(623425, "Encoding", lambda: Encoding), "PEM")))
                _l_(623429)
        yield _a_(623433, _n_(623432, "t_pem", lambda: t_pem), "name")
        _l_(623434)


def generate_nonce(length=15):
    _l_(623448)

    """Generate pseudorandom number."""
    aux = _c_(623446, _a_(623437, '', "join"), [_c_(623442, _n_(623438, "str", lambda: str), _c_(623441, _a_(623440, _n_(623439, "random", lambda: random), "randint"), 0, 9)) for i in _c_(623445, _n_(623443, "range", lambda: range), _n_(623444, "length", lambda: length))])
    _l_(623447)
    return aux


# CERTIFICATES PATHS

api_p12_key = _c_(623452, _a_(623451, _a_(623450, _n_(623449, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\API Outplan OSI TCC MOTE.p12')
_l_(623453)
api_certificate = _c_(623457, _a_(623456, _a_(623455, _n_(623454, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\OSITCC.crt')
_l_(623458)
api_pfx_key = _c_(623462, _a_(623461, _a_(623460, _n_(623459, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\API Outplan OSI TCC MOTE.pfx')
_l_(623463)

# SETUP
wsdl_file = _c_(623467, _a_(623466, _a_(623465, _n_(623464, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\Nodal.wsdl')
_l_(623468)

api_base_url = "https://testmisapi.ercot.com"
_l_(623469)
session = _c_(623472, _a_(623471, _n_(623470, "requests", lambda: requests), "Session"))
_l_(623473)
_c_(623480, _a_(623475, _n_(623474, "session", lambda: session), "mount"), _n_(623476, "api_base_url", lambda: api_base_url),
 _c_(623479, _n_(623477, "Pkcs12Adapter", lambda: Pkcs12Adapter), pkcs12_filename=_n_(623478, "api_p12_key", lambda: api_p12_key), pkcs12_password='AEP'))
_l_(623481)
_n_(623482, "session", lambda: session).verify = None
_l_(623483)

transport = _c_(623486, _n_(623484, "Transport", lambda: Transport), session=_n_(623485, "session", lambda: session))
_l_(623487)
settings = _c_(623489, _n_(623488, "Settings", lambda: Settings), forbid_entities=False)
_l_(623490)

# CREATE CLIENT
_c_(623492, _n_(623491, "print", lambda: print), "Creating client.")
_l_(623493)
with _c_(623496, _n_(623494, "pfx_to_pem", lambda: pfx_to_pem), pfx_path=_n_(623495, "api_pfx_key", lambda: api_pfx_key), pfx_password='hidden') as pem_fle:
    _l_(623507)

    client = _c_(623505, _n_(623497, "Client", lambda: Client), wsdl=_n_(623498, "wsdl_file", lambda: wsdl_file), settings=_n_(623499, "settings", lambda: settings), transport=_n_(623500, "transport", lambda: transport),
    wsse=_c_(623504, _n_(623501, "BinarySignatureTimestamp", lambda: BinarySignatureTimestamp), _n_(623502, "pem_fle", lambda: pem_fle), _n_(623503, "api_certificate", lambda: api_certificate), "AEP"))
    _l_(623506)

_c_(623509, _n_(623508, "print", lambda: print), "Making request.")
_l_(623510)
request_data = {
 "Header": {
 "Verb": "get",
 "Noun": "SystemStatus",
 "ReplayDetection": {
 "Nonce": _c_(623512, _n_(623511, "generate_nonce", lambda: generate_nonce)),
 "Created": "2022-11-10T15:34:00-06:00"},
 "Revision": "1",
 "Source": "API Outplan OSI TCC",
 "UserID": "API_OutplanOSITCC",
 }
 }
_l_(623513)

_c_(623515, _n_(623514, "print", lambda: print), "Call URL")
_l_(623516)
_c_(623523, _n_(623517, "print", lambda: print), _c_(623522, _a_(623520, _a_(623519, _n_(623518, "client", lambda: client), "service"), "MarketInfo"), **_n_(623521, "request_data", lambda: request_data)))
_l_(623524)