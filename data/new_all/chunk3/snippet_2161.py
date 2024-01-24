# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60616722/typeerror-when-chunking-subtasks-in-grouped-tasks
#!/usr/bin/env python3

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import argparse
    _l_(523890)

except ImportError:
    pass
try:
    from tasks import generate_file_from_output
    _l_(523892)

except ImportError:
    pass
try:
    import time
    _l_(523894)

except ImportError:
    pass

if _n_(523895, "__name__", lambda: __name__) == '__main__':
    _l_(523926)

    # Arguments parsing :
    parser = _c_(523898, _a_(523897, _n_(523896, "argparse", lambda: argparse), "ArgumentParser"))
    _l_(523899)
    _c_(523903, _a_(523901, _n_(523900, "parser", lambda: parser), "add_argument"), "-e", "--entries",
        help="set entries number",
        type=_n_(523902, "int", lambda: int),
        default=100,
        metavar="e",
    )
    _l_(523904)
    # Multi process : one a worksheet?
    _c_(523907, _a_(523906, _n_(523905, "parser", lambda: parser), "add_argument"), "-m", "--multi", action="store_true")
    _l_(523908)
    # Chunks : optimize by chunk (mutually exclusive with "multi_thread")
    _c_(523912, _a_(523910, _n_(523909, "parser", lambda: parser), "add_argument"), "-c", "--chunks",
        help="perform the file generation by spliting the data to process into chunks",
        type=_n_(523911, "int", lambda: int),
        nargs="?",
        const=10,
        default=None,
        metavar="N",
    )
    _l_(523913)
    parsed_args = _c_(523916, _a_(523915, _n_(523914, "parser", lambda: parser), "parse_args"))
    _l_(523917)
    _c_(523920, _n_(523918, "print", lambda: print), _n_(523919, "parsed_args", lambda: parsed_args))
    _l_(523921)
    result = _c_(523924, _n_(523922, "generate_file_from_output", lambda: generate_file_from_output), _n_(523923, "parsed_args", lambda: parsed_args))
    _l_(523925)