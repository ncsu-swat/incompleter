# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46080156/python-multiprocessing-typeerror-pickling-an-authenticationstring-object-is-d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing
    _l_(376579)

except ImportError:
    pass

class TestCrawler:
    _l_(376634)

    def __init__(self):
        _l_(376607)

        _n_(376580, "self", lambda: self).m = _c_(376583, _a_(376582, _n_(376581, "multiprocessing", lambda: multiprocessing), "Manager"))
        _l_(376584)
        _n_(376585, "self", lambda: self).queue = _c_(376589, _a_(376588, _a_(376587, _n_(376586, "self", lambda: self), "m"), "Queue"))
        _l_(376590)
        for i in _c_(376592, _n_(376591, "range", lambda: range), 50):
            _l_(376601)

            _c_(376599, _a_(376595, _a_(376594, _n_(376593, "self", lambda: self), "queue"), "put"), _c_(376598, _n_(376596, "str", lambda: str), _n_(376597, "i", lambda: i)))
            _l_(376600)
        _n_(376602, "self", lambda: self).pool = _c_(376605, _a_(376604, _n_(376603, "multiprocessing", lambda: multiprocessing), "Pool"), 6)
        _l_(376606)



    def mainloop(self):
        _l_(376624)

        _c_(376612, _a_(376609, _n_(376608, "self", lambda: self), "process_next_url"), _a_(376611, _n_(376610, "self", lambda: self), "queue"))
        _l_(376613)

        while True:
            _l_(376623)

            _c_(376621, _a_(376616, _a_(376615, _n_(376614, "self", lambda: self), "pool"), "map"), _a_(376618, _n_(376617, "self", lambda: self), "process_next_url"), (_a_(376620, _n_(376619, "self", lambda: self), "queue"),))                
            _l_(376622)                

    def process_next_url(self, queue):
        _l_(376633)

        url = _c_(376627, _a_(376626, _n_(376625, "queue", lambda: queue), "get"))
        _l_(376628)
        _c_(376631, _n_(376629, "print", lambda: print), _n_(376630, "url", lambda: url))
        _l_(376632)


c = _c_(376636, _n_(376635, "TestCrawler", lambda: TestCrawler))
_l_(376637)
_c_(376640, _a_(376639, _n_(376638, "c", lambda: c), "mainloop"))
_l_(376641)