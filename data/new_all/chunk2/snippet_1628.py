# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def batch_generator():
    _l_(455610)

    for X in _n_(455582, "data", lambda: data):
        _l_(455609)

        batch_size = 2
        _l_(455583)
        indices = _c_(455589, _a_(455585, _n_(455584, "np", lambda: np), "arange"), _c_(455588, _n_(455586, "len", lambda: len), _n_(455587, "X", lambda: X))) 
        _l_(455590) 
        batch=[]
        _l_(455591)
        while True:
            _l_(455608)

            for i in _n_(455592, "indices", lambda: indices):
                _l_(455607)

                _c_(455596, _a_(455594, _n_(455593, "batch", lambda: batch), "append"), _n_(455595, "i", lambda: i))
                _l_(455597)
                if _c_(455600, _n_(455598, "len", lambda: len), _n_(455599, "batch", lambda: batch))==_n_(455601, "batch_size", lambda: batch_size):
                    _l_(455606)

                    yield _n_(455602, "X", lambda: X)[_n_(455603, "batch", lambda: batch)]
                    _l_(455604)
                    batch=[]
                    _l_(455605)

data=_c_(455613, _a_(455612, _n_(455611, "pd", lambda: pd), "read_csv"), './test_x_data_OOP3.csv', index_col=[0])
_l_(455614)
data=_c_(455618, _a_(455616, _n_(455615, "np", lambda: np), "array"), _n_(455617, "data", lambda: data))
_l_(455619)
data=_c_(455622, _n_(455620, "reshape_for_Lstm", lambda: reshape_for_Lstm), _n_(455621, "data", lambda: data)) 
_l_(455623) 

_n_(455624, "converter", lambda: converter).representative_dataset = _n_(455625, "batch_generator", lambda: batch_generator)
_l_(455626)