# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50384627/threading-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import schedule
    _l_(453433)

except ImportError:
    pass
try:
    import time
    _l_(453435)

except ImportError:
    pass
try:
    import psycopg2
    _l_(453437)

except ImportError:
    pass
try:
    import threading
    _l_(453439)

except ImportError:
    pass
try:
    import activity_url_collector
    _l_(453441)

except ImportError:
    pass
try:
    import storage_data_collector
    _l_(453443)

except ImportError:
    pass

def main():
    _l_(453488)



    def run_threaded(job_func):
        _l_(453453)

        job_thread = _c_(453447, _a_(453445, _n_(453444, "threading", lambda: threading), "Thread"), target=_n_(453446, "job_func", lambda: job_func))
        _l_(453448)
        _c_(453451, _a_(453450, _n_(453449, "job_thread", lambda: job_thread), "start"))
        _l_(453452)

    _c_(453461, _a_(453458, _a_(453457, _c_(453456, _a_(453455, _n_(453454, "schedule", lambda: schedule), "every"), 3), "minutes"), "do"), _n_(453459, "run_threaded", lambda: run_threaded), _n_(453460, "activity_url_collector", lambda: activity_url_collector))
    _l_(453462)
    _c_(453470, _a_(453467, _a_(453466, _c_(453465, _a_(453464, _n_(453463, "schedule", lambda: schedule), "every"), 3), "minutes"), "do"), _n_(453468, "run_threaded", lambda: run_threaded), _n_(453469, "storage_data_collector", lambda: storage_data_collector))
    _l_(453471)

    _c_(453474, _a_(453473, _n_(453472, "schedule", lambda: schedule), "run_all"))
    _l_(453475)

    _c_(453477, _n_(453476, "print", lambda: print), 'Post-Processing-Application is running')
    _l_(453478)

    while True:
        _l_(453487)

        _c_(453481, _a_(453480, _n_(453479, "schedule", lambda: schedule), "run_pending"))
        _l_(453482)
        _c_(453485, _a_(453484, _n_(453483, "time", lambda: time), "sleep"), 1)    
        _l_(453486)    

if _n_(453489, "__name__", lambda: __name__)=="__main__":
    _l_(453493)

    _c_(453491, _n_(453490, "main", lambda: main))
    _l_(453492)