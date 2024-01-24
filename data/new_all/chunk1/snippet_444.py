# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60699518/attributeerror-lifoqueue-object-has-no-attribute-put-selenium-webdriver
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import selenium
    _l_(394103)

except ImportError:
    pass
try:
    from selenium import webdriver
    _l_(394105)

except ImportError:
    pass

options = _c_(394110, _a_(394109, _a_(394108, _a_(394107, _n_(394106, "webdriver", lambda: webdriver), "chrome"), "options"), "Options"))
_l_(394111)

_c_(394114, _a_(394113, _n_(394112, "options", lambda: options), "add_argument"), '--no-sandbox') 
_l_(394115) 
_c_(394118, _a_(394117, _n_(394116, "options", lambda: options), "add_argument"), '--disable-dev-shm-usage')
_l_(394119)

chromedriver = '/usr/bin/chromedriver'
_l_(394120)

_c_(394122, _n_(394121, "print", lambda: print), 'test0') #is being printed
_l_(394123) #is being printed

driver = _c_(394127, _a_(394125, _n_(394124, "webdriver", lambda: webdriver), "Chrome"), '/usr/bin/chromedriver',options=_n_(394126, "options", lambda: options))
_l_(394128)

_c_(394130, _n_(394129, "print", lambda: print), 'test') #not being printed
_l_(394131) #not being printed

_c_(394134, _a_(394133, _n_(394132, "driver", lambda: driver), "get"), 'http:google.com')
_l_(394135)