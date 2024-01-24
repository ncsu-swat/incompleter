# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58163433/python-concurrent-futures-typeerror-zip-argument-1-must-support-iteration
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def documents_processing(skip):
    _l_(558397)

    conn = _c_(558374, _n_(558373, "get_connection", lambda: get_connection))
    _l_(558375)
    db = _n_(558376, "conn", lambda: conn)["db_name"]
    _l_(558377)

    _c_(558385, _n_(558378, "print", lambda: print), _c_(558384, _a_(558379, "Process::{} -- db.Transactions.find(no_cursor_timeout=True).skip({}).limit(10000)", "format"), _c_(558382, _a_(558381, _n_(558380, "os", lambda: os), "getpid")), _n_(558383, "skip", lambda: skip)))
    _l_(558386)
    documents = _c_(558395, _a_(558394, _c_(558393, _a_(558391, _c_(558390, _a_(558389, _a_(558388, _n_(558387, "db", lambda: db), "Transactions"), "find"), no_cursor_timeout=True), "skip"), _n_(558392, "skip", lambda: skip)), "limit"), 10000)
    _l_(558396)


max_workers = 20
_l_(558398)


def skip_list():
    _l_(558408)

    for i in _c_(558400, _n_(558399, "range", lambda: range), 0, 100000, 10000):
        _l_(558407)

        yield [_n_(558401, "j", lambda: j) for j in _c_(558405, _n_(558402, "range", lambda: range), _n_(558403, "i", lambda: i), _n_(558404, "i", lambda: i) + 10000, 1000)]
        _l_(558406)


def main_f():
    _l_(558430)

    try:
        _l_(558429)

        with _c_(558413, _a_(558411, _a_(558410, _n_(558409, "concurrent", lambda: concurrent), "futures"), "ProcessPoolExecutor"), max_workers=_n_(558412, "max_workers", lambda: max_workers)) as executor:
            _l_(558420)

            _c_(558418, _a_(558415, _n_(558414, "executor", lambda: executor), "map"), _n_(558416, "documents_processing", lambda: documents_processing), _n_(558417, "skip_list", lambda: skip_list))
            _l_(558419)
    except _n_(558421, "Exception", lambda: Exception):
        _l_(558428)

        _c_(558426, _n_(558422, "print", lambda: print), "exception:", _c_(558425, _a_(558424, _n_(558423, "traceback", lambda: traceback), "format_exc")))
        _l_(558427)

_c_(558432, _n_(558431, "main_f", lambda: main_f))
_l_(558433)