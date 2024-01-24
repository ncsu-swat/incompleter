# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50102728/tflearns-fit-method-with-numpy-ndarrays-causing-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tflearn.datasets.mnist as mnist
    _l_(664000)

except ImportError:
    pass
x,y,X,Y=_c_(664003, _a_(664002, _n_(664001, "mnist", lambda: mnist), "load_data"), one_hot=True)
_l_(664004)
x=_c_(664007, _a_(664006, _n_(664005, "x", lambda: x), "reshape"), [-1,28,28,1])
_l_(664008)
X=_c_(664011, _a_(664010, _n_(664009, "X", lambda: X), "reshape"), [-1,28,28,1])
_l_(664012)
try:
    import tflearn
    _l_(664014)

except ImportError:
    pass


class Neural_Network():
    _l_(664111)

    def __init__(self,x,y):
        _l_(664023)

        _n_(664015, "self", lambda: self).x=_n_(664016, "x", lambda: x)
        _l_(664017)
        _n_(664018, "self", lambda: self).y=_n_(664019, "y", lambda: y)
        _l_(664020)
        _n_(664021, "self", lambda: self).epochs=60000
        _l_(664022)

    def main(self):
        _l_(664110)

        cnn=_c_(664028, _a_(664027, _a_(664026, _a_(664025, _n_(664024, "tflearn", lambda: tflearn), "layers"), "core"), "input_data"), shape=[None,28,28,1],name="input_layer")
        _l_(664029)
        cnn=_c_(664035, _a_(664033, _a_(664032, _a_(664031, _n_(664030, "tflearn", lambda: tflearn), "layers"), "conv"), "conv_2d"), _n_(664034, "cnn", lambda: cnn),32,2, activation="relu")
        _l_(664036)
        cnn=_c_(664042, _a_(664040, _a_(664039, _a_(664038, _n_(664037, "tflearn", lambda: tflearn), "layers"), "conv"), "max_pool_2d"), _n_(664041, "cnn", lambda: cnn),2)
        _l_(664043)
        cnn=_c_(664049, _a_(664047, _a_(664046, _a_(664045, _n_(664044, "tflearn", lambda: tflearn), "layers"), "conv"), "conv_2d"), _n_(664048, "cnn", lambda: cnn),32,2, activation="relu")
        _l_(664050)
        cnn=_c_(664056, _a_(664054, _a_(664053, _a_(664052, _n_(664051, "tflearn", lambda: tflearn), "layers"), "conv"), "max_pool_2d"), _n_(664055, "cnn", lambda: cnn),2)
        _l_(664057)
        cnn=_c_(664063, _a_(664061, _a_(664060, _a_(664059, _n_(664058, "tflearn", lambda: tflearn), "layers"), "core"), "flatten"), _n_(664062, "cnn", lambda: cnn))
        _l_(664064)
        cnn=_c_(664070, _a_(664068, _a_(664067, _a_(664066, _n_(664065, "tflearn", lambda: tflearn), "layers"), "core"), "fully_connected"), _n_(664069, "cnn", lambda: cnn),1000,activation="relu")        
        _l_(664071)        
        cnn=_c_(664077, _a_(664075, _a_(664074, _a_(664073, _n_(664072, "tflearn", lambda: tflearn), "layers"), "core"), "dropout"), _n_(664076, "cnn", lambda: cnn),0.85)
        _l_(664078)
        cnn=_c_(664084, _a_(664082, _a_(664081, _a_(664080, _n_(664079, "tflearn", lambda: tflearn), "layers"), "core"), "fully_connected"), _n_(664083, "cnn", lambda: cnn),10,activation="softmax")
        _l_(664085)
        cnn=_c_(664091, _a_(664089, _a_(664088, _a_(664087, _n_(664086, "tflearn", lambda: tflearn), "layers"), "estimator"), "regression"), _n_(664090, "cnn", lambda: cnn),learning_rate=0.001)
        _l_(664092)
        modell=_c_(664096, _a_(664094, _n_(664093, "tflearn", lambda: tflearn), "DNN"), _n_(664095, "cnn", lambda: cnn))
        _l_(664097)
        _c_(664104, _a_(664099, _n_(664098, "modell", lambda: modell), "fit"), _a_(664101, _n_(664100, "self", lambda: self), "x"),_a_(664103, _n_(664102, "self", lambda: self), "y"))
        _l_(664105)
        _c_(664108, _a_(664107, _n_(664106, "modell", lambda: modell), "save"), "mnist.modell")
        _l_(664109)


nn=_c_(664115, _n_(664112, "Neural_Network", lambda: Neural_Network), _n_(664113, "x", lambda: x),_n_(664114, "y", lambda: y))    
_l_(664116)    
_c_(664119, _a_(664118, _n_(664117, "nn", lambda: nn), "main"))
_l_(664120)
_c_(664124, _a_(664122, _n_(664121, "nn", lambda: nn), "predict"), _n_(664123, "X", lambda: X)[1])
_l_(664125)
_c_(664128, _n_(664126, "print", lambda: print), "Label for prediction:",_n_(664127, "Y", lambda: Y)[1])
_l_(664129)