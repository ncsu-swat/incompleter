# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import settings
    _l_(676441)

except ImportError:
    pass
try:
    import dataAccquisition as da
    _l_(676443)

except ImportError:
    pass

data = []
_l_(676444)

def getData():
    _l_(676460)

    global data
    _l_(676445)
    _c_(676447, _n_(676446, "print", lambda: print), ' : [MSG] : Starting up...')
    _l_(676448)
    _c_(676451, _a_(676450, _n_(676449, "da", lambda: da), "getFile"))
    _l_(676452)
    data = _c_(676455, _a_(676454, _n_(676453, "da", lambda: da), "parseData"))
    _l_(676456)
    _c_(676458, _n_(676457, "print", lambda: print), ' : [MSG] : Start up done, ready to be used.')
    _l_(676459)

def getRate(currencyName):
    _l_(676464)

    aux = _n_(676461, "data", lambda: data)[_n_(676462, "currencyName", lambda: currencyName)]
    _l_(676463)
    return aux

def menu():
    _l_(676518)

    def text():
        _l_(676468)

        _c_(676466, _n_(676465, "print", lambda: print), '''\n----------------MENU----------------
-    0. Convert currency           -
-    1. Display all rates          -
-    2. Retry to download data     -
-    3. Quit                       -
------------------------------------''')
        _l_(676467)
    run = True
    _l_(676469)
    while _n_(676470, "run", lambda: run):
        _l_(676517)

        _c_(676472, _n_(676471, "text", lambda: text))
        _l_(676473)
        choice = _c_(676475, _n_(676474, "input", lambda: input), 's: ')
        _l_(676476)
        if _n_(676477, "choice", lambda: choice) == '0':
            _l_(676516)

            for currency, rates in _c_(676480, _a_(676479, _n_(676478, "data", lambda: data), "items")):
                _l_(676490)

                _c_(676488, _n_(676481, "print", lambda: print), "'"+_c_(676484, _n_(676482, "str", lambda: str), _n_(676483, "currency", lambda: currency))+"'",":","to"+_c_(676487, _n_(676485, "str", lambda: str), _n_(676486, "currency", lambda: currency))+",")
                _l_(676489)
        elif _n_(676491, "choice", lambda: choice) == '1':
            _l_(676515)

            for currency, rates in _c_(676494, _a_(676493, _n_(676492, "data", lambda: data), "items")):
                _l_(676500)

                _c_(676498, _n_(676495, "print", lambda: print), _n_(676496, "currency", lambda: currency),':', _n_(676497, "rates", lambda: rates))
                _l_(676499)
        elif _n_(676501, "choice", lambda: choice) == '2':
            _l_(676514)

            _c_(676503, _n_(676502, "getData", lambda: getData))
            _l_(676504)
        elif _n_(676505, "choice", lambda: choice) == '3':
            _l_(676513)

            run = False
            _l_(676506)
        else:
            _c_(676508, _n_(676507, "print", lambda: print), ' : [MSG] : No such choice!')
            _l_(676509)
            choice = _c_(676511, _n_(676510, "input", lambda: input), 's: ')
            _l_(676512)

def toUSD():
    _l_(676520)

    pass
    _l_(676519)

def toJPY():
    _l_(676522)

    pass
    _l_(676521)

def toBGN():
    _l_(676524)

    pass
    _l_(676523)

def toCZK():
    _l_(676526)

    pass
    _l_(676525)

def toDKK():
    _l_(676528)

    pass
    _l_(676527)

def toGBP():
    _l_(676530)

    pass
    _l_(676529)

def toHUF():
    _l_(676532)

    pass
    _l_(676531)

def toPLN():
    _l_(676534)

    pass
    _l_(676533)

def toRON():
    _l_(676536)

    pass
    _l_(676535)

def toSEK():
    _l_(676538)

    pass
    _l_(676537)

def toCHF():
    _l_(676540)

    pass
    _l_(676539)

def toISK():
    _l_(676542)

    pass
    _l_(676541)

def toNOK():
    _l_(676544)

    pass
    _l_(676543)

_c_(676546, _n_(676545, "getData", lambda: getData))
_l_(676547)
_c_(676549, _n_(676548, "menu", lambda: menu))
_l_(676550)