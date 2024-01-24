# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/57847177/attributeerror-numpy-ndarray-object-has-no-attribute-predict
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pickle
    _l_(661214)

except ImportError:
    pass
model = _c_(661219, _a_(661216, _n_(661215, "pickle", lambda: pickle), "load"), _c_(661218, _n_(661217, "open", lambda: open), 'model3.pkl','rb'))
_l_(661220)
_c_(661225, _n_(661221, "print", lambda: print), _c_(661224, _a_(661223, _n_(661222, "model", lambda: model), "predict"), [['Finance and Control'], ['EMEA'], ['Professional Services']]))
_l_(661226)