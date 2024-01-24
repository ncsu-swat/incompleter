# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69209908/tensorflow-typeerror-generator-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class BatchGenerator():
    _l_(448541)

    def __init__(self, X, batch_size):
        _l_(448511)

        _n_(448505, "self", lambda: self).X=_n_(448506, "X", lambda: X)
        _l_(448507)
        _n_(448508, "self", lambda: self).batch_size=_n_(448509, "batch_size", lambda: batch_size)
        _l_(448510)
    def __call__(self):
        _l_(448540)

        indices = _c_(448518, _a_(448513, _n_(448512, "np", lambda: np), "arange"), _c_(448517, _n_(448514, "len", lambda: len), _a_(448516, _n_(448515, "self", lambda: self), "X"))) 
        _l_(448519) 
        batch=[]
        _l_(448520)
        while True:
            _l_(448539)

            for i in _n_(448521, "indices", lambda: indices):
                _l_(448538)

                _c_(448525, _a_(448523, _n_(448522, "batch", lambda: batch), "append"), _n_(448524, "i", lambda: i))
                _l_(448526)
                if _c_(448529, _n_(448527, "len", lambda: len), _n_(448528, "batch", lambda: batch))==_a_(448531, _n_(448530, "self", lambda: self), "batch_size"):
                    _l_(448537)

                    yield _a_(448533, _n_(448532, "self", lambda: self), "X")[_n_(448534, "batch", lambda: batch)]
                    _l_(448535)
                    batch=[]       
                    _l_(448536)       

data=_c_(448544, _a_(448543, _n_(448542, "pd", lambda: pd), "read_csv"), './test_x_data_OOP3.csv', index_col=[0])
_l_(448545)
data=_c_(448549, _a_(448547, _n_(448546, "np", lambda: np), "array"), _n_(448548, "data", lambda: data))
_l_(448550)
data=_c_(448553, _n_(448551, "reshape_for_Lstm", lambda: reshape_for_Lstm), _n_(448552, "data", lambda: data))  
_l_(448554)  

batch_generator=_c_(448557, _n_(448555, "BatchGenerator", lambda: BatchGenerator), _n_(448556, "data", lambda: data), 2)   
_l_(448558)   

_n_(448559, "converter", lambda: converter).representative_dataset = _n_(448560, "batch_generator", lambda: batch_generator)
_l_(448561)