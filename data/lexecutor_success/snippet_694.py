# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import schedule
    _l_(1545352)

except ImportError:
    pass
try:
    import time
    _l_(1545354)

except ImportError:
    pass

def job():
    _l_(1545358)

    _c_(1545356, _n_(1545355, "print", lambda: print), "I'm working...")
    _l_(1545357)

_c_(1545365, _a_(1545363, _a_(1545362, _c_(1545361, _a_(1545360, _n_(1545359, "schedule", lambda: schedule), "every"), 10), "minutes"), "do"), _n_(1545364, "job", lambda: job))
_l_(1545366)
_c_(1545373, _a_(1545371, _a_(1545370, _c_(1545369, _a_(1545368, _n_(1545367, "schedule", lambda: schedule), "every")), "hour"), "do"), _n_(1545372, "job", lambda: job))
_l_(1545374)
_c_(1545383, _a_(1545381, _c_(1545380, _a_(1545379, _a_(1545378, _c_(1545377, _a_(1545376, _n_(1545375, "schedule", lambda: schedule), "every")), "day"), "at"), "10:30"), "do"), _n_(1545382, "job", lambda: job))
_l_(1545384)

while 1:
    _l_(1545393)

    _c_(1545387, _a_(1545386, _n_(1545385, "schedule", lambda: schedule), "run_pending"))
    _l_(1545388)
    _c_(1545391, _a_(1545390, _n_(1545389, "time", lambda: time), "sleep"), 1)
    _l_(1545392)

