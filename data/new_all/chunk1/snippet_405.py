# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71945399/python-3-8-multiprocessing-typeerror-cannot-pickle-weakref-object
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import multiprocessing as mp
    _l_(395791)

except ImportError:
    pass

ctx = _c_(395794, _a_(395793, _n_(395792, "mp", lambda: mp), "get_context"), "spawn")
_l_(395795)
(child, pipe) = _c_(395798, _a_(395797, _n_(395796, "ctx", lambda: ctx), "Pipe"), duplex=True)
_l_(395799)
job_process = _c_(395808, _a_(395801, _n_(395800, "ctx", lambda: ctx), "Process"), name="my_job",
    target=_n_(395802, "job_func", lambda: job_func),
    args=(
        _n_(395803, "child", lambda: child),
        _n_(395804, "server_info", lambda: server_info),
        _n_(395805, "manager", lambda: manager),
        _n_(395806, "job_config", lambda: job_config),
        _n_(395807, "config_file", lambda: config_file),
    ),
)
_l_(395809)
_c_(395812, _a_(395811, _n_(395810, "job_process", lambda: job_process), "start"))
_l_(395813)