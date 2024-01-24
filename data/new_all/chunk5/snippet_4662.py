# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
#Currency conversions - dataAccquisition.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import settings
    _l_(688435)

except ImportError:
    pass
try:
    import requests
    _l_(688437)

except ImportError:
    pass
try:
    from xml.etree import cElementTree as ET
    _l_(688439)

except ImportError:
    pass
try:
    import os
    _l_(688441)

except ImportError:
    pass
try:
    import time
    _l_(688443)

except ImportError:
    pass

def isDataOld():
    _l_(688475)

    if _c_(688449, _a_(688446, _a_(688445, _n_(688444, "os", lambda: os), "path"), "isfile"), _a_(688448, _n_(688447, "settings", lambda: settings), "FILE")):
        _l_(688470)

        fileTime = _c_(688455, _a_(688452, _a_(688451, _n_(688450, "os", lambda: os), "path"), "getmtime"), _a_(688454, _n_(688453, "settings", lambda: settings), "FILE"))
        _l_(688456)
        if (_c_(688459, _a_(688458, _n_(688457, "time", lambda: time), "time")) - _n_(688460, "fileTime", lambda: fileTime)) / 3600 > 24*1:
            _l_(688469)

            _c_(688462, _n_(688461, "print", lambda: print), ' : [MSG] : Data is old.')
            _l_(688463)
            aux = True
            _l_(688464)
            return aux
        else:
            _c_(688466, _n_(688465, "print", lambda: print), ' : [MSG] : Data is up to date.')
            _l_(688467)
            aux = False
            _l_(688468)
            return aux
    _c_(688472, _n_(688471, "print", lambda: print), ' : [MSG] : Data does not exist.')
    _l_(688473)
    aux = True
    _l_(688474)
    return aux

def getFile():
    _l_(688495)

    if _c_(688477, _n_(688476, "isDataOld", lambda: isDataOld)):
        _l_(688494)

        _c_(688479, _n_(688478, "print", lambda: print), ' : [MSG] : Finding and downloading data from URL.')
        _l_(688480)
        r = _c_(688485, _a_(688482, _n_(688481, "requests", lambda: requests), "get"), _a_(688484, _n_(688483, "settings", lambda: settings), "URL"), allow_redirects=True)
        _l_(688486)
        _c_(688492, _a_(688489, _c_(688488, _n_(688487, "open", lambda: open), 'exData.xml', 'wb'), "write"), _a_(688491, _n_(688490, "r", lambda: r), "content"))
        _l_(688493)

def parseData():
    _l_(688554)

    _c_(688497, _n_(688496, "print", lambda: print), ' : [MSG] : Starting to parse data...')
    _l_(688498)
    tree = _c_(688503, _a_(688500, _n_(688499, "ET", lambda: ET), "ElementTree"), file=_a_(688502, _n_(688501, "settings", lambda: settings), "FILE"))
    _l_(688504)
    root = _c_(688507, _a_(688506, _n_(688505, "tree", lambda: tree), "getroot"))
    _l_(688508)
    datalist_currency = []
    _l_(688509)
    datalist_rates    = []
    _l_(688510)
    _c_(688512, _n_(688511, "print", lambda: print), ' : [MSG] : Adding currency and rates to datalist=')
    _l_(688513)
    for child in _n_(688514, "root", lambda: root):
        _l_(688541)

        for subchild in _n_(688515, "child", lambda: child):
            _l_(688540)

            for subsubchild in _n_(688516, "subchild", lambda: subchild):
                _l_(688539)

                _c_(688520, _n_(688517, "print", lambda: print), ' : [MSG] : Adding currency',_a_(688519, _n_(688518, "subsubchild", lambda: subsubchild), "attrib")['currency'])
                _l_(688521)
                _c_(688526, _a_(688523, _n_(688522, "datalist_currency", lambda: datalist_currency), "append"), _a_(688525, _n_(688524, "subsubchild", lambda: subsubchild), "attrib")['currency'])
                _l_(688527)
                _c_(688531, _n_(688528, "print", lambda: print), ' : [MSG] : with rate',_a_(688530, _n_(688529, "subsubchild", lambda: subsubchild), "attrib")['rate'])
                _l_(688532)
                _c_(688537, _a_(688534, _n_(688533, "datalist_rates", lambda: datalist_rates), "append"), _a_(688536, _n_(688535, "subsubchild", lambda: subsubchild), "attrib")['rate'])
                _l_(688538)

    datalist_zip = _c_(688547, _n_(688542, "dict", lambda: dict), _c_(688546, _n_(688543, "zip", lambda: zip), _n_(688544, "datalist_currency", lambda: datalist_currency), _n_(688545, "datalist_rates", lambda: datalist_rates)))
    _l_(688548)
    _c_(688550, _n_(688549, "print", lambda: print), ' : [MSG] : Done parsing data!')
    _l_(688551)
    aux = _n_(688552, "datalist_zip", lambda: datalist_zip)
    _l_(688553)
    return aux