# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51712554/system-path-check-has-typeerror-argument-of-type-nonetype-is-not-iterable
#!/usr/bin/env python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(693182)

except ImportError:
    pass
try:
    from dotenv import load_dotenv, find_dotenv
    _l_(693184)

except ImportError:
    pass
try:
    from os import environ
    _l_(693186)

except ImportError:
    pass

# Add python project root folder to python path
_c_(693190, _n_(693187, "load_dotenv", lambda: load_dotenv), _c_(693189, _n_(693188, "find_dotenv", lambda: find_dotenv)), override=True, verbose=False)
_l_(693191)
PYTHON_SCRIPTS_DIR = _c_(693194, _a_(693193, _n_(693192, "environ", lambda: environ), "get"), 'PYTHON_SCRIPTS_DIR')
_l_(693195)
PROJECT_DIR = _c_(693198, _a_(693197, _n_(693196, "environ", lambda: environ), "get"), 'PROJECT_DIR')
_l_(693199)
_c_(693204, _a_(693202, _a_(693201, _n_(693200, "sys", lambda: sys), "path"), "insert"), 0, _n_(693203, "PYTHON_SCRIPTS_DIR", lambda: PYTHON_SCRIPTS_DIR))
_l_(693205)
try:
    from evaluation.word_probability import WordFrequencyCounter
    _l_(693207)

except ImportError:
    pass