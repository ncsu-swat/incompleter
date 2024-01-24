# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50102728/tflearns-fit-method-with-numpy-ndarrays-causing-typeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tflearn.datasets.mnist as mnist
    _l_(678739)

except ImportError:
    pass
x,y,X,Y=_c_(678742, _a_(678741, _n_(678740, "mnist", lambda: mnist), "load_data"), one_hot=True)
_l_(678743)
x=_c_(678746, _a_(678745, _n_(678744, "x", lambda: x), "reshape"), [-1,28,28,1])
_l_(678747)
X=_c_(678750, _a_(678749, _n_(678748, "X", lambda: X), "reshape"), [-1,28,28,1])
_l_(678751)
try:
    import tflearn
    _l_(678753)

except ImportError:
    pass


class Neural_Network():
    _l_(678850)

    def __init__(self,x,y):
        _l_(678762)

        _n_(678754, "self", lambda: self).x=_n_(678755, "x", lambda: x)
        _l_(678756)
        _n_(678757, "self", lambda: self).y=_n_(678758, "y", lambda: y)
        _l_(678759)
        _n_(678760, "self", lambda: self).epochs=60000
        _l_(678761)

    def main(self):
        _l_(678849)

        cnn=_c_(678767, _a_(678766, _a_(678765, _a_(678764, _n_(678763, "tflearn", lambda: tflearn), "layers"), "core"), "input_data"), shape=[None,28,28,1],name="input_layer")
        _l_(678768)
        cnn=_c_(678774, _a_(678772, _a_(678771, _a_(678770, _n_(678769, "tflearn", lambda: tflearn), "layers"), "conv"), "conv_2d"), _n_(678773, "cnn", lambda: cnn),32,2, activation="relu")
        _l_(678775)
        cnn=_c_(678781, _a_(678779, _a_(678778, _a_(678777, _n_(678776, "tflearn", lambda: tflearn), "layers"), "conv"), "max_pool_2d"), _n_(678780, "cnn", lambda: cnn),2)
        _l_(678782)
        cnn=_c_(678788, _a_(678786, _a_(678785, _a_(678784, _n_(678783, "tflearn", lambda: tflearn), "layers"), "conv"), "conv_2d"), _n_(678787, "cnn", lambda: cnn),32,2, activation="relu")
        _l_(678789)
        cnn=_c_(678795, _a_(678793, _a_(678792, _a_(678791, _n_(678790, "tflearn", lambda: tflearn), "layers"), "conv"), "max_pool_2d"), _n_(678794, "cnn", lambda: cnn),2)
        _l_(678796)
        cnn=_c_(678802, _a_(678800, _a_(678799, _a_(678798, _n_(678797, "tflearn", lambda: tflearn), "layers"), "core"), "flatten"), _n_(678801, "cnn", lambda: cnn))
        _l_(678803)
        cnn=_c_(678809, _a_(678807, _a_(678806, _a_(678805, _n_(678804, "tflearn", lambda: tflearn), "layers"), "core"), "fully_connected"), _n_(678808, "cnn", lambda: cnn),1000,activation="relu")        
        _l_(678810)        
        cnn=_c_(678816, _a_(678814, _a_(678813, _a_(678812, _n_(678811, "tflearn", lambda: tflearn), "layers"), "core"), "dropout"), _n_(678815, "cnn", lambda: cnn),0.85)
        _l_(678817)
        cnn=_c_(678823, _a_(678821, _a_(678820, _a_(678819, _n_(678818, "tflearn", lambda: tflearn), "layers"), "core"), "fully_connected"), _n_(678822, "cnn", lambda: cnn),10,activation="softmax")
        _l_(678824)
        cnn=_c_(678830, _a_(678828, _a_(678827, _a_(678826, _n_(678825, "tflearn", lambda: tflearn), "layers"), "estimator"), "regression"), _n_(678829, "cnn", lambda: cnn),learning_rate=0.001)
        _l_(678831)
        modell=_c_(678835, _a_(678833, _n_(678832, "tflearn", lambda: tflearn), "DNN"), _n_(678834, "cnn", lambda: cnn))
        _l_(678836)
        _c_(678843, _a_(678838, _n_(678837, "modell", lambda: modell), "fit"), _a_(678840, _n_(678839, "self", lambda: self), "x"),_a_(678842, _n_(678841, "self", lambda: self), "y"))
        _l_(678844)
        _c_(678847, _a_(678846, _n_(678845, "modell", lambda: modell), "save"), "mnist.modell")
        _l_(678848)


nn=_c_(678854, _n_(678851, "Neural_Network", lambda: Neural_Network), _n_(678852, "x", lambda: x),_n_(678853, "y", lambda: y))    
_l_(678855)    
_c_(678858, _a_(678857, _n_(678856, "nn", lambda: nn), "main"))
_l_(678859)
_c_(678863, _a_(678861, _n_(678860, "nn", lambda: nn), "predict"), _n_(678862, "X", lambda: X)[1])
_l_(678864)
_c_(678867, _n_(678865, "print", lambda: print), "Label for prediction:",_n_(678866, "Y", lambda: Y)[1])
_l_(678868)