# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53284528/importing-file-with-constants-and-throwing-attributeerror-python-3
#Currency conversions - dataAccquisition.py

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import settings
    _l_(702383)

except ImportError:
    pass
try:
    import requests
    _l_(702385)

except ImportError:
    pass
try:
    from xml.etree import cElementTree as ET
    _l_(702387)

except ImportError:
    pass
try:
    import os
    _l_(702389)

except ImportError:
    pass
try:
    import time
    _l_(702391)

except ImportError:
    pass

def isDataOld():
    _l_(702423)

    if _c_(702397, _a_(702394, _a_(702393, _n_(702392, "os", lambda: os), "path"), "isfile"), _a_(702396, _n_(702395, "settings", lambda: settings), "FILE")):
        _l_(702418)

        fileTime = _c_(702403, _a_(702400, _a_(702399, _n_(702398, "os", lambda: os), "path"), "getmtime"), _a_(702402, _n_(702401, "settings", lambda: settings), "FILE"))
        _l_(702404)
        if (_c_(702407, _a_(702406, _n_(702405, "time", lambda: time), "time")) - _n_(702408, "fileTime", lambda: fileTime)) / 3600 > 24*1:
            _l_(702417)

            _c_(702410, _n_(702409, "print", lambda: print), ' : [MSG] : Data is old.')
            _l_(702411)
            aux = True
            _l_(702412)
            return aux
        else:
            _c_(702414, _n_(702413, "print", lambda: print), ' : [MSG] : Data is up to date.')
            _l_(702415)
            aux = False
            _l_(702416)
            return aux
    _c_(702420, _n_(702419, "print", lambda: print), ' : [MSG] : Data does not exist.')
    _l_(702421)
    aux = True
    _l_(702422)
    return aux

def getFile():
    _l_(702443)

    if _c_(702425, _n_(702424, "isDataOld", lambda: isDataOld)):
        _l_(702442)

        _c_(702427, _n_(702426, "print", lambda: print), ' : [MSG] : Finding and downloading data from URL.')
        _l_(702428)
        r = _c_(702433, _a_(702430, _n_(702429, "requests", lambda: requests), "get"), _a_(702432, _n_(702431, "settings", lambda: settings), "URL"), allow_redirects=True)
        _l_(702434)
        _c_(702440, _a_(702437, _c_(702436, _n_(702435, "open", lambda: open), 'exData.xml', 'wb'), "write"), _a_(702439, _n_(702438, "r", lambda: r), "content"))
        _l_(702441)

def parseData():
    _l_(702502)

    _c_(702445, _n_(702444, "print", lambda: print), ' : [MSG] : Starting to parse data...')
    _l_(702446)
    tree = _c_(702451, _a_(702448, _n_(702447, "ET", lambda: ET), "ElementTree"), file=_a_(702450, _n_(702449, "settings", lambda: settings), "FILE"))
    _l_(702452)
    root = _c_(702455, _a_(702454, _n_(702453, "tree", lambda: tree), "getroot"))
    _l_(702456)
    datalist_currency = []
    _l_(702457)
    datalist_rates    = []
    _l_(702458)
    _c_(702460, _n_(702459, "print", lambda: print), ' : [MSG] : Adding currency and rates to datalist=')
    _l_(702461)
    for child in _n_(702462, "root", lambda: root):
        _l_(702489)

        for subchild in _n_(702463, "child", lambda: child):
            _l_(702488)

            for subsubchild in _n_(702464, "subchild", lambda: subchild):
                _l_(702487)

                _c_(702468, _n_(702465, "print", lambda: print), ' : [MSG] : Adding currency',_a_(702467, _n_(702466, "subsubchild", lambda: subsubchild), "attrib")['currency'])
                _l_(702469)
                _c_(702474, _a_(702471, _n_(702470, "datalist_currency", lambda: datalist_currency), "append"), _a_(702473, _n_(702472, "subsubchild", lambda: subsubchild), "attrib")['currency'])
                _l_(702475)
                _c_(702479, _n_(702476, "print", lambda: print), ' : [MSG] : with rate',_a_(702478, _n_(702477, "subsubchild", lambda: subsubchild), "attrib")['rate'])
                _l_(702480)
                _c_(702485, _a_(702482, _n_(702481, "datalist_rates", lambda: datalist_rates), "append"), _a_(702484, _n_(702483, "subsubchild", lambda: subsubchild), "attrib")['rate'])
                _l_(702486)

    datalist_zip = _c_(702495, _n_(702490, "dict", lambda: dict), _c_(702494, _n_(702491, "zip", lambda: zip), _n_(702492, "datalist_currency", lambda: datalist_currency), _n_(702493, "datalist_rates", lambda: datalist_rates)))
    _l_(702496)
    _c_(702498, _n_(702497, "print", lambda: print), ' : [MSG] : Done parsing data!')
    _l_(702499)
    aux = _n_(702500, "datalist_zip", lambda: datalist_zip)
    _l_(702501)
    return aux