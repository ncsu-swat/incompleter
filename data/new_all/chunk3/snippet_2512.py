# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/74181540/typeerror-argument-should-be-a-bytes-like-object-or-ascii-string-not-buffered
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import PGL
    _l_(541908)

except ImportError:
    pass
try:
    from cryptography.fernet import Fernet as Fn
    _l_(541910)

except ImportError:
    pass
class APM():
    _l_(542034)

    class database():
        _l_(542020)

        def genkey():
            _l_(541923)

            keyfile = _c_(541912, _n_(541911, "open", lambda: open), "D:\\CODING\\Python\\APMKEY.APMKEY", "wb")
            _l_(541913)
            key = _c_(541916, _a_(541915, _n_(541914, "Fn", lambda: Fn), "generate_key"))
            _l_(541917)
            _c_(541921, _a_(541919, _n_(541918, "keyfile", lambda: keyfile), "write"), _n_(541920, "key", lambda: key))
            _l_(541922)
        def encrypt(self):
            _l_(541944)

            key = _c_(541925, _n_(541924, "open", lambda: open), "D:\\CODING\\Python\\APMKEY.APMKEY", "rb")
            _l_(541926)
            database = _c_(541928, _n_(541927, "open", lambda: open), "D:\\CODING\\Python\\APMDatabase.APMDATA", "w")
            _l_(541929)

            newdata = _c_(541937, _a_(541933, _c_(541932, _n_(541930, "Fn", lambda: Fn), _n_(541931, "key", lambda: key)), "encrypt"), _c_(541936, _a_(541935, _n_(541934, "database", lambda: database), "encode")))
            _l_(541938)
            _c_(541942, _a_(541940, _n_(541939, "database", lambda: database), "write"), _n_(541941, "newdata", lambda: newdata))
            _l_(541943)
        def decrypt(self):
            _l_(541963)

            key = _c_(541946, _n_(541945, "open", lambda: open), "D:\\CODING\\Python\\APMKEY.APMKEY", "rb")
            _l_(541947)
            database = _c_(541949, _n_(541948, "open", lambda: open), "D:\\CODING\\Python\\APMDatabase.APMDATA", "w")
            _l_(541950)

            newdata = _c_(541956, _a_(541954, _c_(541953, _n_(541951, "Fn", lambda: Fn), _n_(541952, "key", lambda: key)), "decrypt"), _n_(541955, "database", lambda: database))
            _l_(541957)
            _c_(541961, _a_(541959, _n_(541958, "database", lambda: database), "write"), _n_(541960, "newdata", lambda: newdata))
            _l_(541962)
        def access(self):
            _l_(541975)

            database = _c_(541965, _n_(541964, "open", lambda: open), "D:\\CODING\\Python\\APMDatabase.APMDATA", "r")
            _l_(541966)
            content = _c_(541969, _a_(541968, _n_(541967, "database", lambda: database), "readlines"))
            _l_(541970)
            _c_(541973, _n_(541971, "print", lambda: print), _n_(541972, "content", lambda: content))
            _l_(541974)
        def write(self):
            _l_(541983)

            database = _c_(541977, _n_(541976, "open", lambda: open), "D:\\CODING\\Python\\APMDatabase.APMDATA", "a")
            _l_(541978)
            _c_(541981, _a_(541980, _n_(541979, "database", lambda: database), "write"), "\"NAME OF SITE\", \"WEBSITE URL\", \"USERNAME\", \"PASSWORD\", \"XTRA INFO\"\n")
            _l_(541982)
        def reencrypt():
            _l_(542019)

            key = _c_(541986, _a_(541985, _n_(541984, "Fn", lambda: Fn), "generate_key"))
            _l_(541987)
            keyfile = _c_(541989, _n_(541988, "open", lambda: open), "D:\\CODING\\Python\\APMKEY.APMKEY", "r")
            _l_(541990)
            oldkey = _c_(541993, _a_(541992, _n_(541991, "keyfile", lambda: keyfile), "read"))
            _l_(541994)
            _c_(541997, _a_(541996, _n_(541995, "keyfile", lambda: keyfile), "close"))
            _l_(541998)
            keyfile = _c_(542000, _n_(541999, "open", lambda: open), "D:\\CODING\\Python\\APMKEY.APMKEY", "w")
            _l_(542001)
            _c_(542005, _a_(542003, _n_(542002, "keyfile", lambda: keyfile), "write"), _n_(542004, "key", lambda: key))
            _l_(542006)
            _c_(542011, _a_(542009, _a_(542008, _n_(542007, "APM", lambda: APM), "database"), "decrypt"), _n_(542010, "oldkey", lambda: oldkey))
            _l_(542012)
            _c_(542017, _a_(542015, _a_(542014, _n_(542013, "APM", lambda: APM), "database"), "encrypt"), _n_(542016, "key", lambda: key))
            _l_(542018)



    class gen():
        _l_(542033)

        def password():
            _l_(542026)

            _c_(542024, _a_(542023, _a_(542022, _n_(542021, "PGL", lambda: PGL), "gen"), "password"))
            _l_(542025)
        def username():
            _l_(542032)

            _c_(542030, _a_(542029, _a_(542028, _n_(542027, "PGL", lambda: PGL), "gen"), "username"))
            _l_(542031)

_c_(542038, _a_(542037, _a_(542036, _n_(542035, "APM", lambda: APM), "database"), "encrypt"), "a")
_l_(542039)