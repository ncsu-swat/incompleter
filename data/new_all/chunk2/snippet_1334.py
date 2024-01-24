# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/41297838/using-python-3-5-throwing-error-typeerror-a-bytes-like-object-is-required-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(452962)

except ImportError:
    pass

enron_data = _c_(452967, _a_(452964, _n_(452963, "pickle", lambda: pickle), "load"), _c_(452966, _n_(452965, "open", lambda: open), "../final_project/final_project_dataset.pkl", "r"))
_l_(452968)