# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import settings
    _l_(670424)

except ImportError:
    pass
try:
    import dataAccquisition as da
    _l_(670426)

except ImportError:
    pass

data = []
_l_(670427)

def getData():
    _l_(670443)

    global data
    _l_(670428)
    _c_(670430, _n_(670429, "print", lambda: print), ' : [MSG] : Starting up...')
    _l_(670431)
    _c_(670434, _a_(670433, _n_(670432, "da", lambda: da), "getFile"))
    _l_(670435)
    data = _c_(670438, _a_(670437, _n_(670436, "da", lambda: da), "parseData"))
    _l_(670439)
    _c_(670441, _n_(670440, "print", lambda: print), ' : [MSG] : Start up done, ready to be used.')
    _l_(670442)

def getRate(currencyName):
    _l_(670447)

    aux = _n_(670444, "data", lambda: data)[_n_(670445, "currencyName", lambda: currencyName)]
    _l_(670446)
    return aux

def menu():
    _l_(670501)

    def text():
        _l_(670451)

        _c_(670449, _n_(670448, "print", lambda: print), '''\n----------------MENU----------------
-    0. Convert currency           -
-    1. Display all rates          -
-    2. Retry to download data     -
-    3. Quit                       -
------------------------------------''')
        _l_(670450)
    run = True
    _l_(670452)
    while _n_(670453, "run", lambda: run):
        _l_(670500)

        _c_(670455, _n_(670454, "text", lambda: text))
        _l_(670456)
        choice = _c_(670458, _n_(670457, "input", lambda: input), 's: ')
        _l_(670459)
        if _n_(670460, "choice", lambda: choice) == '0':
            _l_(670499)

            for currency, rates in _c_(670463, _a_(670462, _n_(670461, "data", lambda: data), "items")):
                _l_(670473)

                _c_(670471, _n_(670464, "print", lambda: print), "'"+_c_(670467, _n_(670465, "str", lambda: str), _n_(670466, "currency", lambda: currency))+"'",":","to"+_c_(670470, _n_(670468, "str", lambda: str), _n_(670469, "currency", lambda: currency))+",")
                _l_(670472)
        elif _n_(670474, "choice", lambda: choice) == '1':
            _l_(670498)

            for currency, rates in _c_(670477, _a_(670476, _n_(670475, "data", lambda: data), "items")):
                _l_(670483)

                _c_(670481, _n_(670478, "print", lambda: print), _n_(670479, "currency", lambda: currency),':', _n_(670480, "rates", lambda: rates))
                _l_(670482)
        elif _n_(670484, "choice", lambda: choice) == '2':
            _l_(670497)

            _c_(670486, _n_(670485, "getData", lambda: getData))
            _l_(670487)
        elif _n_(670488, "choice", lambda: choice) == '3':
            _l_(670496)

            run = False
            _l_(670489)
        else:
            _c_(670491, _n_(670490, "print", lambda: print), ' : [MSG] : No such choice!')
            _l_(670492)
            choice = _c_(670494, _n_(670493, "input", lambda: input), 's: ')
            _l_(670495)

def toUSD():
    _l_(670503)

    pass
    _l_(670502)

def toJPY():
    _l_(670505)

    pass
    _l_(670504)

def toBGN():
    _l_(670507)

    pass
    _l_(670506)

def toCZK():
    _l_(670509)

    pass
    _l_(670508)

def toDKK():
    _l_(670511)

    pass
    _l_(670510)

def toGBP():
    _l_(670513)

    pass
    _l_(670512)

def toHUF():
    _l_(670515)

    pass
    _l_(670514)

def toPLN():
    _l_(670517)

    pass
    _l_(670516)

def toRON():
    _l_(670519)

    pass
    _l_(670518)

def toSEK():
    _l_(670521)

    pass
    _l_(670520)

def toCHF():
    _l_(670523)

    pass
    _l_(670522)

def toISK():
    _l_(670525)

    pass
    _l_(670524)

def toNOK():
    _l_(670527)

    pass
    _l_(670526)

_c_(670529, _n_(670528, "getData", lambda: getData))
_l_(670530)
_c_(670532, _n_(670531, "menu", lambda: menu))
_l_(670533)