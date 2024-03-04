# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/33759623/how-to-save-restore-a-model-after-training
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from keras.models import load_model
    _l_(63038)

except ImportError:
    pass

_c_(63041, _a_(63040, _n_(63039, "my_model", lambda: my_model), "save"), 'my_model.h5')  # creates a HDF5 file 'my_model.h5'
_l_(63042)  # creates a HDF5 file 'my_model.h5'

del my_model  # deletes the existing model
_l_(63043)  # deletes the existing model


my_model = _c_(63045, _n_(63044, "load_model", lambda: load_model), 'my_model.h5') # returns a compiled model identical to the previous one
_l_(63046) # returns a compiled model identical to the previous one

