# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74933471/type-error-and-got-an-unexpected-keyword-argument-when-passing-dict-to-python-z
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from zeep.wsse.signature import BinarySignature
    _l_(613845)

except ImportError:
    pass
try:
    from zeep.wsse import utils
    _l_(613847)

except ImportError:
    pass
try:
    from datetime import datetime, timedelta
    _l_(613849)

except ImportError:
    pass
try:
    import contextlib
    _l_(613851)

except ImportError:
    pass
try:
    import os
    _l_(613853)

except ImportError:
    pass
try:
    import requests
    _l_(613855)

except ImportError:
    pass
try:
    from requests_pkcs12 import Pkcs12Adapter
    _l_(613857)

except ImportError:
    pass
try:
    from zeep.transports import Transport
    _l_(613859)

except ImportError:
    pass
try:
    from zeep import Client, Settings
    _l_(613861)

except ImportError:
    pass
try:
    from pathlib import Path
    _l_(613863)

except ImportError:
    pass
try:
    from tempfile import NamedTemporaryFile
    _l_(613865)

except ImportError:
    pass
try:
    from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
    _l_(613867)

except ImportError:
    pass
try:
    from cryptography.hazmat.primitives.serialization.pkcs12 import load_key_and_certificates
    _l_(613869)

except ImportError:
    pass
try:
    import random
    _l_(613871)

except ImportError:
    pass
try:
    import logging.config
    _l_(613873)

except ImportError:
    pass

# USE THE MOST VERBOSE LOGGING LEVEL
_c_(613876, _a_(613875, _a_(613874, logging, "config"), "dictConfig"), {
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
_l_(613877)


class BinarySignatureTimestamp(_n_(613878, "BinarySignature", lambda: BinarySignature)):
    _l_(613938)

    def apply(self, envelope, headers):
        _l_(613934)

        security = _c_(613882, _a_(613880, _n_(613879, "utils", lambda: utils), "get_security_header"), _n_(613881, "envelope", lambda: envelope))
        _l_(613883)

        created = _c_(613886, _a_(613885, _n_(613884, "datetime", lambda: datetime), "utcnow"))
        _l_(613887)
        expired = _n_(613888, "created", lambda: created) + _c_(613890, _n_(613889, "timedelta", lambda: timedelta), seconds=1 * 60)
        _l_(613891)

        timestamp = _c_(613894, _a_(613893, _n_(613892, "utils", lambda: utils), "WSU"), 'Timestamp')
        _l_(613895)
        _c_(613906, _a_(613897, _n_(613896, "timestamp", lambda: timestamp), "append"), _c_(613905, _a_(613899, _n_(613898, "utils", lambda: utils), "WSU"), 'Created', _c_(613904, _a_(613903, _c_(613902, _a_(613901, _n_(613900, "created", lambda: created), "replace"), microsecond=0), "isoformat")) + 'Z'))
        _l_(613907)
        _c_(613918, _a_(613909, _n_(613908, "timestamp", lambda: timestamp), "append"), _c_(613917, _a_(613911, _n_(613910, "utils", lambda: utils), "WSU"), 'Expires', _c_(613916, _a_(613915, _c_(613914, _a_(613913, _n_(613912, "expired", lambda: expired), "replace"), microsecond=0), "isoformat")) + 'Z'))
        _l_(613919)

        _c_(613923, _a_(613921, _n_(613920, "security", lambda: security), "append"), _n_(613922, "timestamp", lambda: timestamp))
        _l_(613924)

        _c_(613929, _a_(613926, _n_(613925, "super", lambda: super)(), "apply"), _n_(613927, "envelope", lambda: envelope), _n_(613928, "headers", lambda: headers))
        _l_(613930)
        aux = _n_(613931, "envelope", lambda: envelope), _n_(613932, "headers", lambda: headers)
        _l_(613933)
        return aux

    def verify(self, envelope):
        _l_(613937)

        aux = _n_(613935, "envelope", lambda: envelope)
        _l_(613936)
        return aux


@_a_(613940, _n_(613939, "contextlib", lambda: contextlib), "contextmanager")
def pfx_to_pem(pfx_path, pfx_password):
    _l_(613999)

    ''' Decrypts the .pfx file to be used with requests. '''
    _l_(613941)
    pfx = _c_(613946, _a_(613945, _c_(613944, _n_(613942, "Path", lambda: Path), _n_(613943, "pfx_path", lambda: pfx_path)), "read_bytes"))
    _l_(613947)
    private_key, main_cert, add_certs = _c_(613953, _n_(613948, "load_key_and_certificates", lambda: load_key_and_certificates), _n_(613949, "pfx", lambda: pfx), _c_(613952, _a_(613951, _n_(613950, "pfx_password", lambda: pfx_password), "encode"), 'utf-8'), None)
    _l_(613954)

    with _c_(613956, _n_(613955, "NamedTemporaryFile", lambda: NamedTemporaryFile), suffix='.pem', delete=False) as t_pem:
        _l_(613998)

        with _c_(613960, _n_(613957, "open", lambda: open), _a_(613959, _n_(613958, "t_pem", lambda: t_pem), "name"), 'wb') as pem_file:
            _l_(613994)

            _c_(613972, _a_(613962, _n_(613961, "pem_file", lambda: pem_file), "write"), _c_(613971, _a_(613964, _n_(613963, "private_key", lambda: private_key), "private_bytes"), _a_(613966, _n_(613965, "Encoding", lambda: Encoding), "PEM"), _a_(613968, _n_(613967, "PrivateFormat", lambda: PrivateFormat), "PKCS8"), _c_(613970, _n_(613969, "NoEncryption", lambda: NoEncryption))))
            _l_(613973)
            _c_(613981, _a_(613975, _n_(613974, "pem_file", lambda: pem_file), "write"), _c_(613980, _a_(613977, _n_(613976, "main_cert", lambda: main_cert), "public_bytes"), _a_(613979, _n_(613978, "Encoding", lambda: Encoding), "PEM")))
            _l_(613982)
            for ca in _n_(613983, "add_certs", lambda: add_certs):
                _l_(613993)

                _c_(613991, _a_(613985, _n_(613984, "pem_file", lambda: pem_file), "write"), _c_(613990, _a_(613987, _n_(613986, "ca", lambda: ca), "public_bytes"), _a_(613989, _n_(613988, "Encoding", lambda: Encoding), "PEM")))
                _l_(613992)
        yield _a_(613996, _n_(613995, "t_pem", lambda: t_pem), "name")
        _l_(613997)


def generate_nonce(length=15):
    _l_(614011)

    """Generate pseudorandom number."""
    aux = _c_(614009, _a_(614000, '', "join"), [_c_(614005, _n_(614001, "str", lambda: str), _c_(614004, _a_(614003, _n_(614002, "random", lambda: random), "randint"), 0, 9)) for i in _c_(614008, _n_(614006, "range", lambda: range), _n_(614007, "length", lambda: length))])
    _l_(614010)
    return aux


# CERTIFICATES PATHS

api_p12_key = _c_(614015, _a_(614014, _a_(614013, _n_(614012, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\API Outplan OSI TCC MOTE.p12')
_l_(614016)
api_certificate = _c_(614020, _a_(614019, _a_(614018, _n_(614017, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\OSITCC.crt')
_l_(614021)
api_pfx_key = _c_(614025, _a_(614024, _a_(614023, _n_(614022, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\API Outplan OSI TCC MOTE.pfx')
_l_(614026)

# SETUP
wsdl_file = _c_(614030, _a_(614029, _a_(614028, _n_(614027, "os", lambda: os), "path"), "join"), 'C:\\Users\\SGUPTA\\ALL\\Projects\\AEPE2\\Nodal.wsdl')
_l_(614031)

api_base_url = "https://testmisapi.ercot.com"
_l_(614032)
session = _c_(614035, _a_(614034, _n_(614033, "requests", lambda: requests), "Session"))
_l_(614036)
_c_(614043, _a_(614038, _n_(614037, "session", lambda: session), "mount"), _n_(614039, "api_base_url", lambda: api_base_url),
              _c_(614042, _n_(614040, "Pkcs12Adapter", lambda: Pkcs12Adapter), pkcs12_filename=_n_(614041, "api_p12_key", lambda: api_p12_key), pkcs12_password='HIDDEN'))
_l_(614044)
_n_(614045, "session", lambda: session).verify = None
_l_(614046)

transport = _c_(614049, _n_(614047, "Transport", lambda: Transport), session=_n_(614048, "session", lambda: session))
_l_(614050)
settings = _c_(614052, _n_(614051, "Settings", lambda: Settings), forbid_entities=False)
_l_(614053)

# CREATE CLIENT
_c_(614055, _n_(614054, "print", lambda: print), "Creating client.")
_l_(614056)
with _c_(614059, _n_(614057, "pfx_to_pem", lambda: pfx_to_pem), pfx_path=_n_(614058, "api_pfx_key", lambda: api_pfx_key), pfx_password='AEP') as pem_fle:
    _l_(614070)

    client = _c_(614068, _n_(614060, "Client", lambda: Client), wsdl=_n_(614061, "wsdl_file", lambda: wsdl_file), settings=_n_(614062, "settings", lambda: settings), transport=_n_(614063, "transport", lambda: transport),
                    wsse=_c_(614067, _n_(614064, "BinarySignatureTimestamp", lambda: BinarySignatureTimestamp), _n_(614065, "pem_fle", lambda: pem_fle), _n_(614066, "api_certificate", lambda: api_certificate), "AEP"))
    _l_(614069)

_c_(614072, _n_(614071, "print", lambda: print), "Making request.")
_l_(614073)
request_data = {'http://www.ercot.com/schema/2007-06/nodal/ews/message:RequestMessage': {'http://www.ercot.com/schema/2007-06/nodal/ews/message:Header': {'http://www.ercot.com/schema/2007-06/nodal/ews/message:Verb': 'create', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Noun': 'OutageSet', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:ReplayDetection': {'http://www.ercot.com/schema/2007-06/nodal/ews/message:Nonce': '72465', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Created': '2022-12-27T00:40:00-07:00'}, 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Revision': '004', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Source': 'TAEPTC', 'http://www.ercot.com/schema/2007-06/nodal/ews/message:UserID': 'API_OutplanOSITCC'}, 'http://www.ercot.com/schema/2007-06/nodal/ews/message:Payload': {'http://www.ercot.com/schema/2007-06/nodal/ews:OutageSet': {'http://www.ercot.com/schema/2007-06/nodal/ews:Outage': {'http://www.ercot.com/schema/2007-06/nodal/ews:OutageInfo': {'http://www.ercot.com/schema/2007-06/nodal/ews:outageType': 'PL', 'http://www.ercot.com/schema/2007-06/nodal/ews:Requestor': {'http://www.ercot.com/schema/2007-06/nodal/ews:name': 'API_OutplanOSITCC', 'http://www.ercot.com/schema/2007-06/nodal/ews:userFullName': 'APIOutplanOSITCC'}, 'http://www.ercot.com/schema/2007-06/nodal/ews:Disclaimer': 'tempdisclaimer', 'http://www.ercot.com/schema/2007-06/nodal/ews:disclaimerAck': 'true'}, 'http://www.ercot.com/schema/2007-06/nodal/ews:TransmissionOutage': {'http://www.ercot.com/schema/2007-06/nodal/ews:operatingCompany': 'TAEPTC', 'http://www.ercot.com/schema/2007-06/nodal/ews:equipmentName': '1589', 'http://www.ercot.com/schema/2007-06/nodal/ews:equipmentIdentifier': '_{072D6FCA-D121-49E7-AC9D-CDF5D4DB3D70}', 'http://www.ercot.com/schema/2007-06/nodal/ews:transmissionType': 'DSC', 'http://www.ercot.com/schema/2007-06/nodal/ews:fromStation': 'AIRLINE', 'http://www.ercot.com/schema/2007-06/nodal/ews:outageState': 'O', 'http://www.ercot.com/schema/2007-06/nodal/ews:emergencyRestorationTime': '1', 'http://www.ercot.com/schema/2007-06/nodal/ews:natureOfWork': 'OE'}, 'http://www.ercot.com/schema/2007-06/nodal/ews:Schedule': {'http://www.ercot.com/schema/2007-06/nodal/ews:plannedStart': '2023-01-16T10:00:00', 'http://www.ercot.com/schema/2007-06/nodal/ews:plannedEnd': '2023-01-17T10:00:00', 'http://www.ercot.com/schema/2007-06/nodal/ews:earliestStart': '2023-01-16T10:00:00', 'http://www.ercot.com/schema/2007-06/nodal/ews:latestEnd': '2023-01-17T12:00:00'}}}}}}
_l_(614074)

_c_(614076, _n_(614075, "print", lambda: print), "Call URL")
_l_(614077)
_c_(614084, _n_(614078, "print", lambda: print), _c_(614083, _a_(614081, _a_(614080, _n_(614079, "client", lambda: client), "service"), "MarketTransactions"), **_n_(614082, "request_data", lambda: request_data)))
_l_(614085)