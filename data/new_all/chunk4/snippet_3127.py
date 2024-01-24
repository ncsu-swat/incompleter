# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41175651/classes-in-python-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class FindByXPATH_1():
    _l_(621009)

    def __init__(self):
        _l_(621008)

        _n_(620994, "self", lambda: self).driver_location = '/usr/local/bin/chromedriver'
        _l_(620995)
        _n_(620996, "self", lambda: self).driver = _c_(621001, _a_(620998, _n_(620997, "webdriver", lambda: webdriver), "Chrome"), _a_(621000, _n_(620999, "self", lambda: self), "driver_location"))
        _l_(621002)
        _c_(621006, _a_(621005, _a_(621004, _n_(621003, "self", lambda: self), "driver"), "get"), 'https://letskodeit.teachable.com/p/practice')
        _l_(621007)
try:
    from basics.xpath_1 import FindByXPATH_1
    _l_(621011)

except ImportError:
    pass
try:
    import basics
    _l_(621013)

except ImportError:
    pass

class FindByXpath_2(_n_(621014, "FindByXPATH_1", lambda: FindByXPATH_1)):
    _l_(621035)

    def __init__(self):
        _l_(621020)

        _c_(621018, _a_(621016, _n_(621015, "FindByXPATH_1", lambda: FindByXPATH_1), "__init__"), _n_(621017, "self", lambda: self))
        _l_(621019)

    def find_by_starts_with(self):
        _l_(621034)

        starting_with = _c_(621026, _a_(621023, _a_(621022, _n_(621021, "FindByXPATH_1", lambda: FindByXPATH_1), "driver"), "find_elements"), _a_(621025, _n_(621024, "By", lambda: By), "XPATH"), 
        '//div[@class="view-school"]//h3[starts-with(@)class, "subtitle"]')
        _l_(621027)
        _c_(621032, _n_(621028, "print", lambda: print), _c_(621031, _n_(621029, "len", lambda: len), _n_(621030, "starting_with", lambda: starting_with)))
        _l_(621033)

test = _c_(621037, _n_(621036, "FindByXPATH_2", lambda: FindByXPATH_2))
_l_(621038)
_c_(621041, _a_(621040, _n_(621039, "test", lambda: test), "find_by_starts_with"))
_l_(621042)