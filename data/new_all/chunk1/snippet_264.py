# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/20826430/start-method-on-thread-fails-with-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TimerQueue(_a_(383696, _n_(383695, "threading", lambda: threading), "Thread")):
    _l_(383757)


    def __init__(self, qyoo, kwargs):
        _l_(383721)

        _c_(383701, _a_(383699, _a_(383698, _n_(383697, "threading", lambda: threading), "Thread"), "__init__"), _n_(383700, "self", lambda: self))
        _l_(383702)
        _n_(383703, "self", lambda: self).queue = _n_(383704, "qyoo", lambda: qyoo)
        _l_(383705)
        _n_(383706, "self", lambda: self).work = _n_(383707, "kwargs", lambda: kwargs)
        _l_(383708)
        _n_(383709, "self", lambda: self).start = _c_(383714, _n_(383710, "ceiling", lambda: ceiling), _c_(383713, _a_(383712, _n_(383711, "time", lambda: time), "time")))
        _l_(383715)
        _n_(383716, "self", lambda: self).times = _c_(383719, _a_(383718, _n_(383717, "kwargs", lambda: kwargs), "keys"))
        _l_(383720)


    def run(self):
        _l_(383756)

        while True:
            _l_(383755)

            for t in _a_(383723, _n_(383722, "self", lambda: self), "times"):
                _l_(383750)

                if _c_(383728, _n_(383724, "ceiling", lambda: ceiling), _c_(383727, _a_(383726, _n_(383725, "time", lambda: time), "time"))) - _a_(383730, _n_(383729, "self", lambda: self), "start") == _n_(383731, "t", lambda: t):
                    _l_(383749)

                    _c_(383739, _a_(383733, _n_(383732, "logger", lambda: logger), "debug"), _c_(383738, _a_(383734, "adding {} to the queue", "format"), _a_(383736, _n_(383735, "self", lambda: self), "work")[_n_(383737, "t", lambda: t)]))
                    _l_(383740)
                    _c_(383747, _a_(383743, _a_(383742, _n_(383741, "self", lambda: self), "queue"), "put"), _a_(383745, _n_(383744, "self", lambda: self), "work")[_n_(383746, "t", lambda: t)])
                    _l_(383748)
            _c_(383753, _a_(383752, _n_(383751, "time", lambda: time), "sleep"), 1)
            _l_(383754)

if _n_(383758, "__name__", lambda: __name__) == "__main__":
    _l_(383772)

    input_queue = _c_(383761, _a_(383760, _n_(383759, "queue", lambda: queue), "Queue"))
    _l_(383762)
    tt = _c_(383766, _n_(383763, "TimerQueue", lambda: TimerQueue), _n_(383764, "input_queue", lambda: input_queue), _n_(383765, "time_url_dict", lambda: time_url_dict))
    _l_(383767)
    _c_(383770, _a_(383769, _n_(383768, "tt", lambda: tt), "start"))
    _l_(383771)