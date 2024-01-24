# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59170064/tracer-runmain-report-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(563417)

except ImportError:
    pass
try:
    import trace
    _l_(563419)

except ImportError:
    pass

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = _c_(563426, _a_(563421, _n_(563420, "trace", lambda: trace), "Trace"), ignoredirs=[_a_(563423, _n_(563422, "sys", lambda: sys), "prefix"), _a_(563425, _n_(563424, "sys", lambda: sys), "exec_prefix")],
    trace=0,
    count=1)
_l_(563427)

# run the new command using the given tracer
_c_(563430, _a_(563429, _n_(563428, "tracer", lambda: tracer), "run"), 'main()')
_l_(563431)

# make a report, placing output in the current directory
r = _c_(563434, _a_(563433, _n_(563432, "tracer", lambda: tracer), "results"))
_l_(563435)
_c_(563438, _a_(563437, _n_(563436, "r", lambda: r), "write_results"), show_missing=True, coverdir=".")
_l_(563439)