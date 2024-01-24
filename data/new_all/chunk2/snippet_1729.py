# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56377141/typeerror-f1-score-got-an-unexpected-keyword-argument-average
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Y_dev_pred = _c_(458514, _a_(458507, _a_(458506, _n_(458505, "self", lambda: self), "model"), "predict"), [_a_(458509, _n_(458508, "self", lambda: self), "dev")[0], _a_(458511, _n_(458510, "self", lambda: self), "dev")[1]], batch_size=_a_(458513, _n_(458512, "self", lambda: self), "BatchSize"), verbose=0)
_l_(458515)
Y_dev_pred = _c_(458519, _a_(458517, _n_(458516, "np", lambda: np), "argmax"), _n_(458518, "Y_dev_pred", lambda: Y_dev_pred), axis=1)
_l_(458520)
_n_(458521, "self", lambda: self).Y_dev = _c_(458526, _a_(458523, _n_(458522, "np", lambda: np), "argmax"), _a_(458525, _n_(458524, "self", lambda: self), "dev")[2], axis=1)
_l_(458527)
_c_(458534, _n_(458528, "print", lambda: print), '####### ', _a_(458531, _a_(458530, _n_(458529, "self", lambda: self), "Y_dev"), "shape"), ' ', _a_(458533, _n_(458532, "Y_dev_pred", lambda: Y_dev_pred), "shape"))
_l_(458535)
_c_(458540, _n_(458536, "print", lambda: print), _a_(458538, _n_(458537, "self", lambda: self), "Y_dev"), ' ### ', _n_(458539, "Y_dev_pred", lambda: Y_dev_pred))
_l_(458541)
_c_(458548, _n_(458542, "print", lambda: print), _c_(458547, _n_(458543, "f1_score", lambda: f1_score), _a_(458545, _n_(458544, "self", lambda: self), "Y_dev"), _n_(458546, "Y_dev_pred", lambda: Y_dev_pred), average='macro'))
_l_(458549)