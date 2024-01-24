# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/44614397/typeerror-in-python-when-populating-data-in-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
test_size = 0.2
_l_(701251)
train_set = {2:[],4:[]}
_l_(701252)
test_set = {2:[],4:[]}
_l_(701253)
train_data = _n_(701254, "full_data", lambda: full_data)[:-_c_(701260, _n_(701255, "int", lambda: int), _n_(701256, "test_size", lambda: test_size)*_c_(701259, _n_(701257, "len", lambda: len), _n_(701258, "full_data", lambda: full_data)))]
_l_(701261)
test_data = _n_(701262, "full_data", lambda: full_data)[-_c_(701268, _n_(701263, "int", lambda: int), _n_(701264, "test_size", lambda: test_size)*_c_(701267, _n_(701265, "len", lambda: len), _n_(701266, "full_data", lambda: full_data))):]    
_l_(701269)    
_c_(701272, _n_(701270, "len", lambda: len), _n_(701271, "train_data", lambda: train_data)),_c_(701275, _n_(701273, "len", lambda: len), _n_(701274, "test_data", lambda: test_data))
_l_(701276)
for i in _n_(701277, "train_data", lambda: train_data):
    _l_(701284)

    _c_(701282, _a_(701280, _n_(701278, "train_set", lambda: train_set)[_n_(701279, "i", lambda: i)[-1]], "append"), _n_(701281, "i", lambda: i)[:-1])
    _l_(701283)

for i in _n_(701285, "test_data", lambda: test_data):
    _l_(701292)

    _c_(701290, _a_(701288, _n_(701286, "test_set", lambda: test_set)[_n_(701287, "i", lambda: i)[-1]], "append"), _n_(701289, "i", lambda: i)[:-1])
    _l_(701291)