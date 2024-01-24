# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45897118/attribute-error-python-from-a-new-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import runMain
    _l_(607023)

except ImportError:
    pass


def isUser(credentialsInput):
    _l_(607028)

    aux = _n_(607024, "credentialsInput", lambda: credentialsInput) in _a_(607026, _n_(607025, "runMain", lambda: runMain), "users")
    _l_(607027)
    return aux


def isReserved(names):
    _l_(607037)

    for strings in _a_(607030, _n_(607029, "runMain", lambda: runMain), "roomName"):
        _l_(607036)

        if _n_(607031, "names", lambda: names) in _n_(607032, "strings", lambda: strings):
            _l_(607035)

            aux = True
            _l_(607033)
            return aux
        else:
            aux = False
            _l_(607034)
            return aux


def getIndex(e, check):
    _l_(607043)

    aux = _c_(607041, _a_(607039, _n_(607038, "e", lambda: e), "index"), _n_(607040, "check", lambda: check))
    _l_(607042)
    return aux


def findInArray(e, searchName):
    _l_(607063)

    _n_(607044, "runMain", lambda: runMain).i = 0
    _l_(607045)
    while _a_(607047, _n_(607046, "runMain", lambda: runMain), "i") < _c_(607050, _n_(607048, "len", lambda: len), _n_(607049, "e", lambda: e)):
        _l_(607059)

        test = _n_(607051, "e", lambda: e)[_a_(607053, _n_(607052, "runMain", lambda: runMain), "i")]
        _l_(607054)
        if _n_(607055, "searchName", lambda: searchName) in _n_(607056, "test", lambda: test):
            _l_(607058)

            break
            _l_(607057)
    aux = _a_(607061, _n_(607060, "runMain", lambda: runMain), "i")
    _l_(607062)
    return aux


def registerUser(creds):
    _l_(607074)

    _c_(607072, _a_(607066, _a_(607065, _n_(607064, "runMain", lambda: runMain), "users"), "__add__"), _c_(607070, _n_(607067, "len", lambda: len), _a_(607069, _n_(607068, "runMain", lambda: runMain), "users")), _n_(607071, "creds", lambda: creds))
    _l_(607073)


def runCredentialCheck():
    _l_(607094)

    _n_(607075, "runMain", lambda: runMain).username = _c_(607077, _n_(607076, "input", lambda: input), "admin$ -u>>> ")
    _l_(607078)
    _n_(607079, "runMain", lambda: runMain).password = _c_(607081, _n_(607080, "input", lambda: input), "admin$ -p>>> ")
    _l_(607082)
    _n_(607083, "runMain", lambda: runMain).credentials = _a_(607085, _n_(607084, "runMain", lambda: runMain), "username") + ":" + _a_(607087, _n_(607086, "runMain", lambda: runMain), "password")
    _l_(607088)
    aux = _c_(607092, _n_(607089, "isUser", lambda: isUser), _a_(607091, _n_(607090, "runMain", lambda: runMain), "credentials"))
    _l_(607093)
    return aux