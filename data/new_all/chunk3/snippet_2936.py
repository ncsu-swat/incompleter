# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57854166/nameerror-name-lock-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def send_request(data):
    _l_(535036)

    global lock
    _l_(535023)
    _c_(535026, _a_(535025, _n_(535024, "lock", lambda: lock), "acquire"))
    _l_(535027)
    _c_(535030, _n_(535028, "print", lambda: print), _n_(535029, "data", lambda: data))
    _l_(535031)
    _c_(535034, _a_(535033, _n_(535032, "lock", lambda: lock), "release"))
    _l_(535035)

if _n_(535037, "__name__", lambda: __name__) == '__main__':
    _l_(535061)

    data_list = ['data1', 'data2', 'data3']
    _l_(535038)
    lock = _c_(535041, _a_(535040, _n_(535039, "multiprocessing", lambda: multiprocessing), "Lock"))
    _l_(535042)
    pool = _c_(535045, _a_(535044, _n_(535043, "multiprocessing", lambda: multiprocessing), "Pool"), 3)
    _l_(535046)

    _c_(535051, _a_(535048, _n_(535047, "pool", lambda: pool), "map"), _n_(535049, "send_request", lambda: send_request), _n_(535050, "data_list", lambda: data_list))
    _l_(535052)
    _c_(535055, _a_(535054, _n_(535053, "pool", lambda: pool), "close"))
    _l_(535056)
    _c_(535059, _a_(535058, _n_(535057, "pool", lambda: pool), "join"))
    _l_(535060)