# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75634860/problem-with-sdv-library-in-python-nameerror-name-load-tabular-demo-is-not-d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sdv.demo import get_available_demos
    _l_(409116)

except ImportError:
    pass
demos = _c_(409118, _n_(409117, "get_available_demos", lambda: get_available_demos))
_l_(409119)
data = _c_(409121, _n_(409120, "load_tabular_demo", lambda: load_tabular_demo), 'student_placements')
_l_(409122)