# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51712554/system-path-check-has-typeerror-argument-of-type-nonetype-is-not-iterable
#!/usr/bin/env python3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(688556)

except ImportError:
    pass
try:
    from dotenv import load_dotenv, find_dotenv
    _l_(688558)

except ImportError:
    pass
try:
    from os import environ
    _l_(688560)

except ImportError:
    pass

# Add python project root folder to python path
_c_(688564, _n_(688561, "load_dotenv", lambda: load_dotenv), _c_(688563, _n_(688562, "find_dotenv", lambda: find_dotenv)), override=True, verbose=False)
_l_(688565)
PYTHON_SCRIPTS_DIR = _c_(688568, _a_(688567, _n_(688566, "environ", lambda: environ), "get"), 'PYTHON_SCRIPTS_DIR')
_l_(688569)
PROJECT_DIR = _c_(688572, _a_(688571, _n_(688570, "environ", lambda: environ), "get"), 'PROJECT_DIR')
_l_(688573)
_c_(688578, _a_(688576, _a_(688575, _n_(688574, "sys", lambda: sys), "path"), "insert"), 0, _n_(688577, "PYTHON_SCRIPTS_DIR", lambda: PYTHON_SCRIPTS_DIR))
_l_(688579)
try:
    from evaluation.word_probability import WordFrequencyCounter
    _l_(688581)

except ImportError:
    pass