# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44614397/typeerror-in-python-when-populating-data-in-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
test_size = 0.2
_l_(665612)
train_set = {2:[],4:[]}
_l_(665613)
test_set = {2:[],4:[]}
_l_(665614)
train_data = _n_(665615, "full_data", lambda: full_data)[:-_c_(665621, _n_(665616, "int", lambda: int), _n_(665617, "test_size", lambda: test_size)*_c_(665620, _n_(665618, "len", lambda: len), _n_(665619, "full_data", lambda: full_data)))]
_l_(665622)
test_data = _n_(665623, "full_data", lambda: full_data)[-_c_(665629, _n_(665624, "int", lambda: int), _n_(665625, "test_size", lambda: test_size)*_c_(665628, _n_(665626, "len", lambda: len), _n_(665627, "full_data", lambda: full_data))):]    
_l_(665630)    
_c_(665633, _n_(665631, "len", lambda: len), _n_(665632, "train_data", lambda: train_data)),_c_(665636, _n_(665634, "len", lambda: len), _n_(665635, "test_data", lambda: test_data))
_l_(665637)
for i in _n_(665638, "train_data", lambda: train_data):
    _l_(665645)

    _c_(665643, _a_(665641, _n_(665639, "train_set", lambda: train_set)[_n_(665640, "i", lambda: i)[-1]], "append"), _n_(665642, "i", lambda: i)[:-1])
    _l_(665644)

for i in _n_(665646, "test_data", lambda: test_data):
    _l_(665653)

    _c_(665651, _a_(665649, _n_(665647, "test_set", lambda: test_set)[_n_(665648, "i", lambda: i)[-1]], "append"), _n_(665650, "i", lambda: i)[:-1])
    _l_(665652)