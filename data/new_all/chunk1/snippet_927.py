# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30679134/xlrd-throws-typeerror-embedded-nul-character-when-trying-to-open-an-xls-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from urllib.request import urlopen
    _l_(400670)

except ImportError:
    pass
try:
    import xlrd
    _l_(400672)

except ImportError:
    pass
DJIA_URL = 'http://www.djaverages.com/?go=export-components&symbol=DJI'
_l_(400673)
xlfile = _c_(400678, _a_(400677, _c_(400676, _n_(400674, "urlopen", lambda: urlopen), _n_(400675, "DJIA_URL", lambda: DJIA_URL)), "read"))
_l_(400679)
xlbook = _c_(400683, _a_(400681, _n_(400680, "xlrd", lambda: xlrd), "open_workbook"), _n_(400682, "xlfile", lambda: xlfile))
_l_(400684)