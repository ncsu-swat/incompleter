# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31884175/multiprocessing-typeerror-int-object-is-not-iterable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def main(i):
    _l_(380920)

    global urlDepth
    _l_(380906)
    global row
    _l_(380907)
    global counter
    _l_(380908)
    urlDepth = []
    _l_(380909)
    row = 0
    _l_(380910)
    counter = 0
    _l_(380911)
    _c_(380914, _n_(380912, "login", lambda: login), _n_(380913, "i", lambda: i))
    _l_(380915)
    _c_(380918, _n_(380916, "crawler", lambda: crawler), _n_(380917, "MENU_URL", lambda: MENU_URL))
    _l_(380919)


if _n_(380921, "__name__", lambda: __name__) == '__main__':
    _l_(380948)

    workers = 2
    _l_(380922)
    processes = []
    _l_(380923)
    for p_number in _c_(380926, _n_(380924, "range", lambda: range), _n_(380925, "workers", lambda: workers)):
        _l_(380941)

        p = _c_(380930, _n_(380927, "Process", lambda: Process), target=_n_(380928, "main", lambda: main), args=_n_(380929, "p_number", lambda: p_number))
        _l_(380931)
        _c_(380934, _a_(380933, _n_(380932, "p", lambda: p), "start"))
        _l_(380935)
        _c_(380939, _a_(380937, _n_(380936, "processes", lambda: processes), "append"), _n_(380938, "p", lambda: p))
        _l_(380940)

    for p in _n_(380942, "processes", lambda: processes):
        _l_(380947)

        _c_(380945, _a_(380944, _n_(380943, "p", lambda: p), "join"))
        _l_(380946)