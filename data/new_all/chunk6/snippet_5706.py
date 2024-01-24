# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63009994/getting-filenotfounderror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import firebase_admin
    _l_(374985)

except ImportError:
    pass
try:
    from firebase_admin import credentials
    _l_(374987)

except ImportError:
    pass
try:
    from firebase_admin import firestore
    _l_(374989)

except ImportError:
    pass

cred = _c_(374992, _a_(374991, _n_(374990, "credentials", lambda: credentials), "Certificate"), 'json file')
_l_(374993)
_c_(374997, _a_(374995, _n_(374994, "firebase_admin", lambda: firebase_admin), "initialize_app"), _n_(374996, "cred", lambda: cred))
_l_(374998)

db = _c_(375001, _a_(375000, _n_(374999, "firestore", lambda: firestore), "client"))
_l_(375002)
doc_ref = _c_(375007, _a_(375006, _c_(375005, _a_(375004, _n_(375003, "db", lambda: db), "collection"), u'device-configs'), "document"), '5ed7ee5c31ed1b8166e1c2ee')
_l_(375008)

_c_(375011, _a_(375010, _n_(375009, "doc_ref", lambda: doc_ref), "update"), {
    u'value.on': True
})
_l_(375012)