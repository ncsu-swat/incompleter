# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/39112489/typeerror-unsupported-operand-types-for-str-and-str
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(614087)

except ImportError:
    pass

class Cashier:
    _l_(614111)


    def getDollars(self, x):
        _l_(614090)

        aux = _n_(614088, "x", lambda: x) / 100
        _l_(614089)
        return aux

    def getQuarters(self, x):
        _l_(614095)

        y = _n_(614091, "x", lambda: x) % 100
        _l_(614092)
        aux = _n_(614093, "y", lambda: y) / 25
        _l_(614094)
        return aux

    def getDimes(self, x):
        _l_(614100)

        y = _n_(614096, "x", lambda: x) % 100
        _l_(614097)
        aux = _n_(614098, "y", lambda: y) % 10
        _l_(614099)
        return aux

    def getNickels(self, x):
        _l_(614105)

        y = _n_(614101, "x", lambda: x) % 100
        _l_(614102)
        aux = _n_(614103, "y", lambda: y) % 5
        _l_(614104)
        return aux

    def getPennies(self, x):
        _l_(614110)

        y = _n_(614106, "x", lambda: x) * 1
        _l_(614107)
        aux = _n_(614108, "y", lambda: y)
        _l_(614109)
        return aux

while True:
    _l_(614170)


    thecashier = _c_(614113, _n_(614112, "Cashier", lambda: Cashier))
    _l_(614114)

    amountDue = _c_(614116, _n_(614115, "input", lambda: input), "Please enter amount due: ")
    _l_(614117)
    amountReceived = _c_(614119, _n_(614118, "input", lambda: input), "Please enter amount received: ")
    _l_(614120)

    changePennies = _c_(614124, _n_(614121, "int", lambda: int), (_n_(614122, "amountReceived", lambda: amountReceived) - _n_(614123, "amountDue", lambda: amountDue)) * 100)
    _l_(614125)

    _c_(614131, _n_(614126, "print", lambda: print), _c_(614130, _a_(614128, _n_(614127, "thecashier", lambda: thecashier), "getPennies"), _n_(614129, "changePennies", lambda: changePennies)))
    _l_(614132)
    _c_(614138, _n_(614133, "print", lambda: print), _c_(614137, _a_(614135, _n_(614134, "thecashier", lambda: thecashier), "getDollars"), _n_(614136, "changePennies", lambda: changePennies)))
    _l_(614139)
    _c_(614145, _n_(614140, "print", lambda: print), _c_(614144, _a_(614142, _n_(614141, "thecashier", lambda: thecashier), "getQuarters"), _n_(614143, "changePennies", lambda: changePennies)))
    _l_(614146)
    _c_(614152, _n_(614147, "print", lambda: print), _c_(614151, _a_(614149, _n_(614148, "thecashier", lambda: thecashier), "getDimes"), _n_(614150, "changePennies", lambda: changePennies)))
    _l_(614153)
    _c_(614159, _n_(614154, "print", lambda: print), _c_(614158, _a_(614156, _n_(614155, "thecashier", lambda: thecashier), "getNickels"), _n_(614157, "changePennies", lambda: changePennies)))
    _l_(614160)

    choice = _c_(614162, _n_(614161, "input", lambda: input), "Do you want to continue <yes> <no>? ")
    _l_(614163)
    if (_n_(614164, "choice", lambda: choice) == "no"):
        _l_(614169)

        _c_(614166, _n_(614165, "print", lambda: print), "Have a nice day. ")
        _l_(614167)
        break
        _l_(614168)